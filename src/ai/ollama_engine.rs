//! 🦙 Ollama Integration - Run Any Local LLM Free!
//!
//! Ollama is the easiest way to run LLMs locally

use super::{AiContext, AiEngine, AiEngineInfo, AiResponse, CHILD_AAC_PROMPT};
use anyhow::Result;
use serde::{Deserialize, Serialize};

#[cfg(feature = "tracing")]
use tracing::{debug, info, warn};

/// Ollama API client for local LLM inference
pub struct OllamaEngine {
    model_name: String,
    api_url: String,
    #[cfg(feature = "reqwest")]
    client: reqwest::Client,
}

#[derive(Serialize)]
struct OllamaRequest {
    model: String,
    prompt: String,
    system: Option<String>,
    stream: bool,
    options: OllamaOptions,
}

#[derive(Serialize)]
struct OllamaOptions {
    temperature: f32,
    top_p: f32,
    max_tokens: u32,
}

#[derive(Deserialize)]
struct OllamaResponse {
    response: String,
}

impl OllamaEngine {
    /// Create new Ollama engine
    pub async fn new() -> Result<Self> {
        let api_url = "http://localhost:11434".to_string();

        #[cfg(feature = "reqwest")]
        {
            let client = reqwest::Client::new();

            // Check if Ollama is running
            match client.get(format!("{api_url}/api/tags")).send().await {
                Ok(_) => {
                    info!("✅ Ollama is running at {}", api_url);
                }
                Err(_) => {
                    warn!("⚠️ Ollama not running. Please install and start Ollama:");
                    warn!("1. Install: curl -fsSL https://ollama.ai/install.sh | sh");
                    warn!("2. Start: ollama serve");
                    warn!("3. Pull a model: ollama pull tinyllama");
                    return Err(anyhow::anyhow!("Ollama not running"));
                }
            }

            // Try to find best available model
            let model_name = Self::find_best_model(&client, &api_url).await?;
            info!("🦙 Using Ollama model: {}", model_name);

            Ok(Self {
                model_name,
                api_url,
                client,
            })
        }

        #[cfg(not(feature = "reqwest"))]
        {
            warn!("Ollama engine requires 'reqwest' feature");
            Err(anyhow::anyhow!("Ollama requires reqwest feature"))
        }
    }

    /// Find the best available model for child-like responses
    #[cfg(feature = "reqwest")]
    async fn find_best_model(client: &reqwest::Client, api_url: &str) -> Result<String> {
        // Preferred models for child-like responses
        let preferred = ["tinyllama", "phi3", "llama3.2", "gemma2:2b", "qwen2.5:0.5b"];

        // Get list of available models
        let response = client.get(format!("{api_url}/api/tags")).send().await?;
        let text = response.text().await?;

        // Check which preferred models are available
        for model in &preferred {
            if text.contains(model) {
                return Ok(model.to_string());
            }
        }

        // If no preferred model, suggest downloading one
        warn!("📥 No suitable model found. Please run:");
        warn!("   ollama pull tinyllama");

        Err(anyhow::anyhow!("No suitable Ollama model found"))
    }

    /// Generate response using Ollama
    async fn generate_with_ollama(
        &self,
        input: &str,
        context: &AiContext,
    ) -> Result<Vec<AiResponse>> {
        debug!("🦙 Generating with Ollama model: {}", self.model_name);

        let emotional_hint = match context.emotional_state.happiness {
            h if h > 0.8 => "The child is very happy and excited.",
            h if h > 0.5 => "The child is in a good mood.",
            h if h < 0.3 => "The child is feeling a bit down.",
            _ => "The child is feeling okay.",
        };

        let prompt = format!(
            "{CHILD_AAC_PROMPT}\n\n{emotional_hint}\n\nParent: \"{input}\"\nChild:"
        );

        let request = OllamaRequest {
            model: self.model_name.clone(),
            prompt,
            system: Some(
                "You are a nonverbal child using an AAC device. Respond in 1-10 words max."
                    .to_string(),
            ),
            stream: false,
            options: OllamaOptions {
                temperature: 0.7,
                top_p: 0.9,
                max_tokens: 30,
            },
        };

        #[cfg(feature = "reqwest")]
        let response = self
            .client
            .post(format!("{}/api/generate", self.api_url))
            .json(&request)
            .send()
            .await?;

        #[cfg(not(feature = "reqwest"))]
        return Err(anyhow::anyhow!("Ollama requires reqwest feature"));

        let ollama_response: OllamaResponse = response.json().await?;
        let text = ollama_response.response.trim().to_string();

        // Generate multiple variations
        let responses = vec![
            self.create_response(&text, 0.9),
            self.create_response(&self.make_variation(&text, "positive"), 0.8),
            self.create_response(&self.make_variation(&text, "negative"), 0.7),
            self.create_response("Maybe later", 0.6),
        ];

        Ok(responses)
    }

    fn create_response(&self, text: &str, confidence: f32) -> AiResponse {
        let (emoji, emotion) = self.infer_emoji_and_emotion(text);
        AiResponse {
            text: text.to_string(),
            emoji,
            confidence,
            emotion,
        }
    }

    fn make_variation(&self, text: &str, style: &str) -> String {
        match style {
            "positive" => {
                if text.contains("no") {
                    "Maybe yes!".to_string()
                } else {
                    format!("{text} please!")
                }
            }
            "negative" => {
                if text.contains("yes") {
                    "Not right now".to_string()
                } else {
                    "No thanks".to_string()
                }
            }
            _ => text.to_string(),
        }
    }

    fn infer_emoji_and_emotion(&self, text: &str) -> (String, String) {
        let text_lower = text.to_lowercase();

        if text_lower.contains("yes") || text_lower.contains("okay") {
            ("✅".to_string(), "positive".to_string())
        } else if text_lower.contains("no") || text_lower.contains("don't") {
            ("❌".to_string(), "negative".to_string())
        } else if text_lower.contains("happy") || text_lower.contains("yay") {
            ("😊".to_string(), "happy".to_string())
        } else if text_lower.contains("hungry") || text_lower.contains("eat") {
            ("🍽️".to_string(), "hungry".to_string())
        } else if text_lower.contains("play") {
            ("🎮".to_string(), "playful".to_string())
        } else {
            ("💭".to_string(), "neutral".to_string())
        }
    }
}

#[async_trait::async_trait]
impl AiEngine for OllamaEngine {
    async fn generate_response(&self, input: &str, context: &AiContext) -> Result<Vec<AiResponse>> {
        self.generate_with_ollama(input, context).await
    }

    fn is_ready(&self) -> bool {
        true
    }

    fn get_info(&self) -> AiEngineInfo {
        AiEngineInfo {
            name: "Ollama Engine".to_string(),
            model: self.model_name.clone(),
            parameters: "Local LLM via Ollama".to_string(),
            memory_usage: "Varies by model".to_string(),
        }
    }
}
