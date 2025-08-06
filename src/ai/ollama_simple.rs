//! Simple Ollama integration that works without reqwest

use super::{AiContext, AiEngine, AiEngineInfo, AiResponse};
use anyhow::Result;
use std::process::Command;

#[cfg(feature = "tracing")]
use tracing::{debug, info, warn};

pub struct SimpleOllamaEngine {
    model_name: String,
}

impl SimpleOllamaEngine {
    pub async fn new() -> Result<Self> {
        // Check if ollama is installed
        let output = Command::new("ollama").arg("list").output();

        match output {
            Ok(output) => {
                let models = String::from_utf8_lossy(&output.stdout);
                info!("🦙 Available Ollama models:\n{}", models);

                // Check for preferred models
                // Check for our custom TinkyBink model first!
                let model_name = if models.contains("tinkybink") {
                    info!("🎉 Found custom TinkyBink AAC model!");
                    "tinkybink".to_string()
                } else if models.contains("tinyllama") {
                    "tinyllama".to_string()
                } else if models.contains("phi3") {
                    "phi3".to_string()
                } else if models.contains("llama3.2") {
                    "llama3.2".to_string()
                } else {
                    warn!("No suitable model found. Using pattern matching.");
                    return Err(anyhow::anyhow!("No suitable Ollama model"));
                };

                Ok(Self { model_name })
            }
            Err(_) => {
                warn!(
                    "Ollama not found. Install with: curl -fsSL https://ollama.ai/install.sh | sh"
                );
                Err(anyhow::anyhow!("Ollama not installed"))
            }
        }
    }

    async fn generate_with_ollama(
        &self,
        input: &str,
        _context: &AiContext,
    ) -> Result<Vec<AiResponse>> {
        let prompt = if self.model_name == "tinkybink" {
            // Our custom model expects this format
            input.to_string()
        } else {
            // Generic models need more instruction
            format!(
                "You are a nonverbal child. The parent said: '{input}'. Give 4 short responses the child might want to say, separated by commas. Be emotional and child-like."
            )
        };

        // Run ollama command
        let output = Command::new("ollama")
            .arg("run")
            .arg(&self.model_name)
            .arg(&prompt)
            .output()?;

        let response = String::from_utf8_lossy(&output.stdout);
        debug!("Ollama response: {}", response);

        // Parse responses
        let responses: Vec<AiResponse> = response
            .split(',')
            .filter_map(|s| {
                let text = s.trim();
                if text.is_empty() {
                    return None;
                }

                let (emoji, emotion) = self.infer_emoji_and_emotion(text);
                Some(AiResponse {
                    text: text.to_string(),
                    emoji,
                    confidence: 0.9,
                    emotion,
                })
            })
            .take(4)
            .collect();

        if responses.is_empty() {
            // Fallback responses
            Ok(self.get_fallback_responses(input))
        } else {
            Ok(responses)
        }
    }

    fn get_fallback_responses(&self, input: &str) -> Vec<AiResponse> {
        let input_lower = input.to_lowercase();

        if input_lower.contains("park") || input_lower.contains("outside") {
            vec![
                AiResponse {
                    text: "Yes! Park!".to_string(),
                    emoji: "🏞️".to_string(),
                    confidence: 0.9,
                    emotion: "excited".to_string(),
                },
                AiResponse {
                    text: "Stay home".to_string(),
                    emoji: "🏠".to_string(),
                    confidence: 0.8,
                    emotion: "reluctant".to_string(),
                },
                AiResponse {
                    text: "Too cold".to_string(),
                    emoji: "🥶".to_string(),
                    confidence: 0.7,
                    emotion: "concerned".to_string(),
                },
                AiResponse {
                    text: "Play inside?".to_string(),
                    emoji: "🎮".to_string(),
                    confidence: 0.7,
                    emotion: "suggesting".to_string(),
                },
            ]
        } else {
            vec![
                AiResponse {
                    text: "Yes".to_string(),
                    emoji: "✅".to_string(),
                    confidence: 0.8,
                    emotion: "positive".to_string(),
                },
                AiResponse {
                    text: "No".to_string(),
                    emoji: "❌".to_string(),
                    confidence: 0.8,
                    emotion: "negative".to_string(),
                },
                AiResponse {
                    text: "Maybe".to_string(),
                    emoji: "🤔".to_string(),
                    confidence: 0.7,
                    emotion: "unsure".to_string(),
                },
                AiResponse {
                    text: "I don't know".to_string(),
                    emoji: "🤷".to_string(),
                    confidence: 0.6,
                    emotion: "confused".to_string(),
                },
            ]
        }
    }

    fn infer_emoji_and_emotion(&self, text: &str) -> (String, String) {
        let text_lower = text.to_lowercase();

        match text_lower {
            s if s.contains("yes") || s.contains("okay") => {
                ("✅".to_string(), "positive".to_string())
            }
            s if s.contains("no") || s.contains("don't") => {
                ("❌".to_string(), "negative".to_string())
            }
            s if s.contains("happy") || s.contains("yay") => {
                ("😊".to_string(), "happy".to_string())
            }
            s if s.contains("sad") => ("😢".to_string(), "sad".to_string()),
            s if s.contains("hungry") || s.contains("eat") => {
                ("🍽️".to_string(), "hungry".to_string())
            }
            s if s.contains("tired") || s.contains("sleep") => {
                ("😴".to_string(), "tired".to_string())
            }
            s if s.contains("play") => ("🎮".to_string(), "playful".to_string()),
            s if s.contains("love") => ("❤️".to_string(), "loving".to_string()),
            _ => ("💭".to_string(), "neutral".to_string()),
        }
    }
}

#[async_trait::async_trait]
impl AiEngine for SimpleOllamaEngine {
    async fn generate_response(&self, input: &str, context: &AiContext) -> Result<Vec<AiResponse>> {
        self.generate_with_ollama(input, context).await
    }

    fn is_ready(&self) -> bool {
        true
    }

    fn get_info(&self) -> AiEngineInfo {
        AiEngineInfo {
            name: "Simple Ollama".to_string(),
            model: self.model_name.clone(),
            parameters: "Local LLM".to_string(),
            memory_usage: "Varies".to_string(),
        }
    }
}
