//! 🧠 Free AI Model Integration for TinkyBink AAC
//! 
//! Supports multiple free, local AI models:
//! - Llama (via llama.cpp) - Lightweight, fast inference
//! - TinyLlama - 1.1B parameter model perfect for child responses
//! - Phi-3 Mini - Microsoft's small but powerful model

use anyhow::Result;
use std::sync::Arc;
use tokio::sync::Mutex;

#[cfg(feature = "tracing")]
use tracing::{info, warn, error};

pub mod online_engine;
pub mod ollama_engine;
pub mod ollama_simple;
pub mod llama_engine;
pub mod candle_engine;

/// Trait for AI engines that can generate child-like responses
#[async_trait::async_trait]
pub trait AiEngine: Send + Sync {
    /// Generate a child-like response to the given input
    async fn generate_response(&self, input: &str, context: &AiContext) -> Result<Vec<AiResponse>>;
    
    /// Check if the AI engine is ready
    fn is_ready(&self) -> bool;
    
    /// Get engine information
    fn get_info(&self) -> AiEngineInfo;
}

/// Context for AI generation
#[derive(Debug, Clone)]
pub struct AiContext {
    /// Child's current emotional state
    pub emotional_state: EmotionalContext,
    /// Recent conversation history
    pub history: Vec<String>,
    /// Preferred response style
    pub style: ResponseStyle,
    /// Maximum response length
    pub max_length: usize,
}

#[derive(Debug, Clone)]
pub struct EmotionalContext {
    pub happiness: f32,
    pub energy: f32,
    pub anxiety: f32,
    pub confidence: f32,
}

#[derive(Debug, Clone)]
pub enum ResponseStyle {
    /// Simple yes/no responses
    Simple,
    /// More expressive responses
    Expressive,
    /// Playful, creative responses
    Playful,
    /// Calm, gentle responses
    Gentle,
}

/// AI-generated response with metadata
#[derive(Debug, Clone)]
pub struct AiResponse {
    pub text: String,
    pub emoji: String,
    pub confidence: f32,
    pub emotion: String,
}

#[derive(Debug, Clone)]
pub struct AiEngineInfo {
    pub name: String,
    pub model: String,
    pub parameters: String,
    pub memory_usage: String,
}

/// Factory for creating AI engines based on available features
pub struct AiEngineFactory;

impl AiEngineFactory {
    /// Create the best available AI engine
    pub async fn create_best_available() -> Result<Box<dyn AiEngine>> {
        // First try online AI (requires internet)
        info!("🌐 Checking for internet connection...");
        if let Ok(engine) = online_engine::OnlineEngine::new().await {
            info!("✅ Online AI engine loaded - using cloud AI!");
            return Ok(Box::new(engine));
        }
        
        // Then try Ollama (offline, local)
        info!("🦙 Attempting to load Ollama AI engine...");
        // Try simple Ollama first (no reqwest needed)
        if let Ok(engine) = ollama_simple::SimpleOllamaEngine::new().await {
            info!("✅ Simple Ollama AI engine loaded - using local AI!");
            return Ok(Box::new(engine));
        }
        
        // Try full Ollama if reqwest is available
        #[cfg(feature = "reqwest")]
        if let Ok(engine) = ollama_engine::OllamaEngine::new().await {
            info!("✅ Ollama AI engine loaded - using local AI!");
            return Ok(Box::new(engine));
        }
        
        #[cfg(feature = "ai-llama")]
        {
            info!("🦙 Attempting to load Llama AI engine...");
            if let Ok(engine) = llama_engine::LlamaEngine::new().await {
                info!("✅ Llama AI engine loaded successfully!");
                return Ok(Box::new(engine));
            }
        }
        
        #[cfg(feature = "ai-candle")]
        {
            info!("🕯️ Attempting to load Candle AI engine...");
            if let Ok(engine) = candle_engine::CandleEngine::new().await {
                info!("✅ Candle AI engine loaded successfully!");
                return Ok(Box::new(engine));
            }
        }
        
        warn!("⚠️ No AI engine available, falling back to pattern matching");
        warn!("💡 To enable AI:");
        warn!("   1. Install Ollama: curl -fsSL https://ollama.ai/install.sh | sh");
        warn!("   2. Start Ollama: ollama serve");
        warn!("   3. Pull a model: ollama pull tinyllama");
        Err(anyhow::anyhow!("No AI engine available"))
    }
    
    /// Check which AI engines are available
    pub fn available_engines() -> Vec<String> {
        let mut engines = Vec::new();
        
        #[cfg(feature = "ai-llama")]
        engines.push("llama-cpp".to_string());
        
        #[cfg(feature = "ai-candle")]
        engines.push("candle".to_string());
        
        engines
    }
}

impl Default for AiContext {
    fn default() -> Self {
        Self {
            emotional_state: EmotionalContext {
                happiness: 0.6,
                energy: 0.5,
                anxiety: 0.3,
                confidence: 0.5,
            },
            history: Vec::new(),
            style: ResponseStyle::Expressive,
            max_length: 50,
        }
    }
}

/// System prompt for child-like AAC responses
pub const CHILD_AAC_PROMPT: &str = r#"You are TinkyBink, an AI assistant helping a nonverbal child communicate. 

Your responses should be:
- Short and simple (max 10 words)
- Child-like and natural
- Emotionally appropriate
- Using simple vocabulary
- Sometimes playful or creative

Examples:
Parent: "Are you hungry?"
You: "Yes! I want pizza!" or "Not right now" or "Maybe a little bit"

Parent: "How are you feeling?"
You: "I'm happy today!" or "Feeling sleepy" or "My tummy hurts"

Parent: "Do you want to play?"
You: "Yes! Let's play blocks!" or "Can we go outside?" or "I'm too tired"

Remember: You're speaking AS the child, not TO the child. Keep it natural and authentic."#;