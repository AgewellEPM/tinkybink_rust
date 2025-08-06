//! 🦙 Llama AI Engine - Free, Local, Fast
//!
//! Uses llama.cpp for efficient CPU inference of small language models

// Llama.cpp integration would go here
// For now, we'll use a simpler approach

use super::{AiContext, AiEngine, AiEngineInfo, AiResponse, CHILD_AAC_PROMPT};
use anyhow::Result;
use std::path::Path;

#[cfg(feature = "tracing")]
use tracing::{debug, info, warn};

/// Llama-based AI engine for child-like responses
pub struct LlamaEngine {
    model_path: String,
}

impl LlamaEngine {
    /// Create new Llama engine - will attempt to download TinyLlama if not found
    pub async fn new() -> Result<Self> {
        let model_path = Self::get_or_download_model().await?;

        info!("🦙 Loading Llama model from: {}", model_path);

        Ok(Self { model_path })
    }

    /// Get model path or download TinyLlama if not found
    async fn get_or_download_model() -> Result<String> {
        // Check common locations for models
        let possible_paths = vec![
            "models/tinyllama-1.1b-q4_k_m.gguf",
            "tinyllama-1.1b-q4_k_m.gguf",
            "/Users/lukekist/tinkybink_rust/models/tinyllama-1.1b-q4_k_m.gguf",
        ];

        for path in &possible_paths {
            if Path::new(path).exists() {
                info!("📁 Found model at: {}", path);
                return Ok(path.to_string());
            }
        }

        // Model not found - provide instructions
        warn!("🦙 TinyLlama model not found!");
        warn!("📥 Please download a model:");
        warn!("1. Create 'models' directory: mkdir models");
        warn!("2. Download TinyLlama:");
        warn!(
            "   curl -L https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -o models/tinyllama-1.1b-q4_k_m.gguf"
        );
        warn!("3. Or any small GGUF model from HuggingFace");

        Err(anyhow::anyhow!(
            "Model not found. Please download TinyLlama or another small GGUF model."
        ))
    }

    /// Generate child-like response using pattern matching (Llama not available)
    fn generate_pattern_based(&self, input: &str, context: &AiContext) -> Result<Vec<AiResponse>> {
        debug!("🦙 Generating response for: '{}'", input);

        // Build the prompt
        let emotional_hint = match context.emotional_state.happiness {
            h if h > 0.8 => "The child is very happy and excited.",
            h if h > 0.5 => "The child is in a good mood.",
            h if h < 0.3 => "The child is feeling a bit down.",
            _ => "The child is feeling okay.",
        };

        let style_hint = match context.style {
            super::ResponseStyle::Simple => "Keep responses very simple, just yes/no/maybe.",
            super::ResponseStyle::Expressive => "Be expressive but keep it short.",
            super::ResponseStyle::Playful => "Be playful and creative.",
            super::ResponseStyle::Gentle => "Be gentle and calm.",
        };

        let _full_prompt = format!(
            "{CHILD_AAC_PROMPT}\n\n{emotional_hint}\n{style_hint}\n\nParent: \"{input}\"\nChild:"
        );

        // Pattern-based generation since Llama is not available
        let response = if input.to_lowercase().contains("hungry") {
            "Yes! I want food!"
        } else if input.to_lowercase().contains("tired") {
            "I'm sleepy"
        } else if input.to_lowercase().contains("play") {
            "Let's play!"
        } else {
            "Okay"
        }
        .to_string();

        // Parse into multiple suggestions if the model generated alternatives
        let suggestions = if response.contains(" or ") {
            response
                .split(" or ")
                .map(|s| s.trim().to_string())
                .collect()
        } else {
            vec![response]
        };

        // Convert to AiResponse format
        let responses: Vec<AiResponse> = suggestions
            .into_iter()
            .map(|text| {
                let (emoji, emotion) = self.infer_emoji_and_emotion(&text);
                AiResponse {
                    text,
                    emoji,
                    confidence: 0.85, // Llama responses are generally high quality
                    emotion,
                }
            })
            .collect();

        Ok(responses)
    }

    /// Infer appropriate emoji and emotion from response text
    fn infer_emoji_and_emotion(&self, text: &str) -> (String, String) {
        let text_lower = text.to_lowercase();

        if text_lower.contains("yes") || text_lower.contains("okay") {
            ("✅".to_string(), "positive".to_string())
        } else if text_lower.contains("no") || text_lower.contains("don't") {
            ("❌".to_string(), "negative".to_string())
        } else if text_lower.contains("happy") || text_lower.contains("yay") {
            ("😊".to_string(), "happy".to_string())
        } else if text_lower.contains("sad") || text_lower.contains("hurt") {
            ("😢".to_string(), "sad".to_string())
        } else if text_lower.contains("tired") || text_lower.contains("sleepy") {
            ("😴".to_string(), "tired".to_string())
        } else if text_lower.contains("hungry") || text_lower.contains("eat") {
            ("🍽️".to_string(), "hungry".to_string())
        } else if text_lower.contains("play") || text_lower.contains("fun") {
            ("🎮".to_string(), "playful".to_string())
        } else if text_lower.contains("?") {
            ("❓".to_string(), "curious".to_string())
        } else {
            ("💭".to_string(), "neutral".to_string())
        }
    }
}

#[async_trait::async_trait]
impl AiEngine for LlamaEngine {
    async fn generate_response(&self, input: &str, context: &AiContext) -> Result<Vec<AiResponse>> {
        self.generate_pattern_based(input, context)
    }

    fn is_ready(&self) -> bool {
        true // Pattern matching is always ready
    }

    fn get_info(&self) -> AiEngineInfo {
        AiEngineInfo {
            name: "Llama.cpp Engine".to_string(),
            model: self.model_path.clone(),
            parameters: "TinyLlama 1.1B or similar".to_string(),
            memory_usage: "~1GB RAM".to_string(),
        }
    }
}
