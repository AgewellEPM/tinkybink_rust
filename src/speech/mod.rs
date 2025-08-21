use anyhow::Result;
#[cfg(feature = "whisper-rs")]
use std::sync::Arc;
use tokio::sync::mpsc;
use tracing::{debug, error, info, warn};
use tts::Tts;
#[cfg(feature = "whisper-rs")]
use whisper_rs::{WhisperContext, WhisperContextParameters};

use crate::core::events::SystemEvent;

/// Speech recognition and synthesis manager with TTS capabilities
pub struct SpeechManager {
    event_sender: mpsc::UnboundedSender<SystemEvent>,
    is_listening: bool,
    tts: Option<Tts>,
    #[cfg(feature = "whisper-rs")]
    whisper_context: Option<Arc<WhisperContext>>,
}

impl SpeechManager {
    pub async fn new(event_sender: mpsc::UnboundedSender<SystemEvent>) -> Result<Self> {
        info!("Initializing Speech Manager with TTS");

        // Initialize TTS engine
        let tts = match Tts::default() {
            Ok(mut tts_engine) => {
                info!("🔊 TTS engine initialized successfully");

                // Configure TTS settings for child-like speech
                // Note: Rate setting may not be available on all platforms
                // if let Err(e) = tts_engine.set_rate(0.9) {
                //     warn!("Failed to set TTS rate: {}", e);
                // }

                // Try to set a friendly voice
                if let Ok(voices) = tts_engine.voices() {
                    let preferred_voices = ["child", "young", "female", "girl", "boy", "alex", "samantha"];
                    for voice in voices {
                        let voice_name = voice.name().to_lowercase();
                        if preferred_voices.iter().any(|pv| voice_name.contains(pv)) {
                            if let Ok(()) = tts_engine.set_voice(&voice) {
                                info!("🎵 Set child-friendly voice: {}", voice.name());
                                break;
                            }
                        }
                    }
                }

                Some(tts_engine)
            }
            Err(e) => {
                error!("Failed to initialize TTS engine: {}", e);
                warn!("🔇 Speech output will not be available");
                None
            }
        };

        // Initialize Whisper for speech recognition
        #[cfg(feature = "whisper-rs")]
        let whisper_context = {
            info!("🎤 Initializing Whisper speech recognition...");
            match WhisperContext::new_with_params("models/whisper-base.bin", WhisperContextParameters::default()) {
                Ok(ctx) => {
                    info!("✅ Whisper context initialized successfully!");
                    Some(Arc::new(ctx))
                }
                Err(e) => {
                    error!("❌ Failed to initialize Whisper context: {}", e);
                    warn!("🔇 Speech recognition will not be available");
                    None
                }
            }
        };

        #[cfg(not(feature = "whisper-rs"))]
        info!("🎤 Whisper speech recognition: Feature disabled");

        Ok(Self {
            event_sender,
            is_listening: false,
            tts,
            #[cfg(feature = "whisper-rs")]
            whisper_context,
        })
    }

    pub async fn start(&mut self) -> Result<()> {
        info!("Starting speech recognition services");
        // TODO: Initialize speech recognition
        // For now, this would integrate with system speech services
        // or web-based speech recognition APIs
        Ok(())
    }

    pub async fn start_listening(&mut self) -> Result<()> {
        if !self.is_listening {
            info!("Starting speech recognition");
            self.is_listening = true;
            // TODO: Start actual speech recognition
        }
        Ok(())
    }

    pub async fn stop_listening(&mut self) -> Result<()> {
        if self.is_listening {
            info!("Stopping speech recognition");
            self.is_listening = false;
            // TODO: Stop actual speech recognition
        }
        Ok(())
    }

    /// Speak text aloud using TTS with child-like voice
    pub async fn speak(&mut self, text: &str) -> Result<()> {
        if let Some(ref mut tts) = self.tts {
            info!("🗣️ Speaking: '{}'", text);

            // Clean the text for TTS (remove emojis that might confuse the engine)
            let clean_text = Self::clean_text_for_tts_static(text);
            debug!("Cleaned text for TTS: '{}'", clean_text);

            if let Err(e) = tts.speak(&clean_text, true) {
                error!("Failed to speak text '{}': {}", clean_text, e);
                return Err(anyhow::anyhow!("TTS error: {}", e));
            }

            // Send event that speech started
            let event = SystemEvent::SpeechStarted { text: text.to_string() };
            if let Err(e) = self.event_sender.send(event) {
                error!("Failed to send speech started event: {}", e);
            }
        } else {
            warn!("🔇 TTS not available, cannot speak: '{}'", text);
            return Err(anyhow::anyhow!("TTS engine not initialized"));
        }

        Ok(())
    }

    /// Check if TTS is available
    pub fn can_speak(&self) -> bool {
        self.tts.is_some()
    }

    /// Stop any current speech
    pub async fn stop_speaking(&mut self) -> Result<()> {
        if let Some(ref mut tts) = self.tts {
            if let Err(e) = tts.stop() {
                error!("Failed to stop TTS: {}", e);
                return Err(anyhow::anyhow!("Failed to stop TTS: {}", e));
            }
            info!("🔇 Stopped speaking");
        }
        Ok(())
    }

    /// Clean text for TTS by removing emojis and formatting that might confuse the engine
    fn clean_text_for_tts_static(text: &str) -> String {
        // Remove common emojis and symbols that might confuse TTS
        let binding = text
            .replace("✅", "")
            .replace("🚫", "")
            .replace("🤔", "")
            .replace("❓", "")
            .replace("💭", "")
            .replace("🆘", "")
            .replace("🍕", "")
            .replace("🧃", "")
            .replace("💧", "")
            .replace("🎮", "")
            .replace("📚", "")
            .replace("🎵", "")
            .replace("🤒", "")
            .replace("💊", "")
            .replace("🚽", "")
            .replace("🏃", "")
            .replace("📍", "")
            .replace("😴", "")
            .replace("🛏️", "")
            .replace("⏰", "")
            .replace("😊", "")
            .replace("🎉", "")
            .replace("❤️", "")
            .replace("👋", "")
            .replace("🌅", "")
            .replace("🧢", "")
            .replace("➕", "")
            .replace("🔄", "")
            .replace("🤷", "")
            .replace("❌", "");
        let cleaned = binding.trim();

        // If the cleaned text is empty, return a default phrase
        if cleaned.is_empty() { "hmm".to_string() } else { cleaned.to_string() }
    }

    /// Check if speech recognition is available
    pub fn can_recognize_speech(&self) -> bool {
        #[cfg(feature = "whisper-rs")]
        return self.whisper_context.is_some();

        #[cfg(not(feature = "whisper-rs"))]
        false
    }

    /// Simulate audio capture and recognition (for demo purposes)
    pub async fn simulate_speech_recognition(&mut self, simulated_text: &str) -> Result<()> {
        info!("🎤 Simulating speech recognition: '{}'", simulated_text);

        // Send simulated speech recognition event
        let event = SystemEvent::SpeechRecognized { text: simulated_text.to_string(), confidence: 0.95 };

        if let Err(e) = self.event_sender.send(event) {
            error!("Failed to send simulated speech event: {}", e);
            return Err(anyhow::anyhow!("Failed to send speech event: {}", e));
        }

        Ok(())
    }

    pub fn is_listening(&self) -> bool {
        self.is_listening
    }

    // This would be called by the actual speech recognition implementation
    async fn on_speech_recognized(&self, text: String, confidence: f32) -> Result<()> {
        let event = SystemEvent::SpeechRecognized { text, confidence };
        if let Err(e) = self.event_sender.send(event) {
            warn!("Failed to send speech recognition event: {}", e);
        }
        Ok(())
    }
}
