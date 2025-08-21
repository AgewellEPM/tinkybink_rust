use anyhow::Result;
use tracing::{debug, info};

pub mod child_ai_engine;
pub mod choice_detector;
pub mod eliza_engine;
pub mod emoji_mapper;
pub mod simple_tiles;

use crate::ai::{AiContext, AiEngine, AiEngineFactory, ResponseStyle};
use crate::core::events::{SuggestionTile, TileCategory};
use crate::core::user_profile::UserProfile;
use crate::memory::TinkyMemoryCore;
use child_ai_engine::ChildAiEngine;
use choice_detector::ChoiceDetector;
use eliza_engine::ElizaEngine;
use emoji_mapper::EmojiMapper;

/// Advanced suggestion engine with emotional intelligence and memory
pub struct SuggestionEngine {
    choice_detector: ChoiceDetector,
    emoji_mapper: EmojiMapper,
    eliza_engine: ElizaEngine,
    child_ai_engine: std::cell::RefCell<ChildAiEngine>,
    memory_core: std::cell::RefCell<TinkyMemoryCore>,
    ai_engine: Option<Box<dyn AiEngine>>,
    user_profile: Option<UserProfile>,
}

impl Default for SuggestionEngine {
    fn default() -> Self {
        Self::new()
    }
}

impl SuggestionEngine {
    pub fn new() -> Self {
        info!("Initializing Suggestion Engine");

        // Try to load AI engine
        let ai_engine = match tokio::runtime::Handle::try_current() {
            Ok(_) => {
                // We're in an async context, can use async
                match tokio::task::block_in_place(|| {
                    tokio::runtime::Handle::current().block_on(AiEngineFactory::create_best_available())
                }) {
                    Ok(engine) => {
                        info!("✅ AI engine loaded successfully!");
                        Some(engine)
                    }
                    Err(e) => {
                        info!("ℹ️ AI engine not available: {}, using pattern matching", e);
                        None
                    }
                }
            }
            Err(_) => {
                info!("ℹ️ Not in async context, AI engine disabled");
                None
            }
        };

        Self {
            choice_detector: ChoiceDetector::new(),
            emoji_mapper: EmojiMapper::new(),
            eliza_engine: ElizaEngine::new(),
            child_ai_engine: std::cell::RefCell::new(ChildAiEngine::new()),
            memory_core: std::cell::RefCell::new(TinkyMemoryCore::new()),
            ai_engine,
            user_profile: None,
        }
    }

    /// Set user profile for adaptive responses
    pub fn set_user_profile(&mut self, profile: UserProfile) {
        info!("👤 Setting user profile: {} ({:?})", profile.name, profile.user_type);
        self.user_profile = Some(profile);
    }

    /// Generate 4 emotionally intelligent suggestions based on input text and memory
    pub async fn generate_suggestions(&self, text: &str) -> Result<Vec<SuggestionTile>> {
        info!("🧠 Generating emotionally intelligent suggestions for: '{}'", text);

        let text_lower = text.to_lowercase();

        // Check if we should avoid this topic based on memory
        {
            let memory = self.memory_core.borrow();
            if memory.should_avoid_topic(&text_lower) {
                debug!("🚫 Topic flagged for avoidance, generating gentle alternatives");
                return Ok(self.get_gentle_alternatives());
            }
        }

        // Check if we have a user profile for adaptive responses
        if let Some(ref profile) = self.user_profile {
            debug!("👤 Using adaptive responses for user type: {:?}", profile.user_type);
            let contextual_responses = profile.get_contextual_responses(&text_lower);
            if !contextual_responses.is_empty() {
                let adaptive_suggestions: Vec<SuggestionTile> = contextual_responses
                    .into_iter()
                    .take(4)
                    .map(|response| {
                        let emoji = self.emoji_mapper.get_emoji(&response);
                        SuggestionTile { emoji, text: response, category: TileCategory::Default, confidence: 0.9 }
                    })
                    .collect();
                info!("✅ Generated {} adaptive suggestions for user type", adaptive_suggestions.len());
                return Ok(adaptive_suggestions);
            }
        }

        // 1. First try real AI engine if available
        let mut suggestions = if let Some(ref ai_engine) = self.ai_engine {
            debug!("🤖 Using real AI engine for generation");

            // Build AI context from memory
            let context = {
                let memory = self.memory_core.borrow();
                let _emotional_state = &memory.get_emotional_insights().current_mood_summary;

                AiContext {
                    emotional_state: crate::ai::EmotionalContext {
                        happiness: 0.6, // TODO: Get from actual memory state
                        energy: 0.5,
                        anxiety: 0.3,
                        confidence: 0.5,
                    },
                    history: vec![], // TODO: Add conversation history
                    style: ResponseStyle::Expressive,
                    max_length: 50,
                }
            };

            match ai_engine.generate_response(&text_lower, &context).await {
                Ok(ai_responses) => {
                    debug!("✅ AI generated {} responses", ai_responses.len());
                    ai_responses
                        .into_iter()
                        .map(|resp| SuggestionTile {
                            emoji: resp.emoji,
                            text: resp.text,
                            category: TileCategory::Default,
                            confidence: resp.confidence,
                        })
                        .collect()
                }
                Err(e) => {
                    debug!("❌ AI generation failed: {}, falling back", e);
                    vec![]
                }
            }
        } else {
            vec![]
        };

        // 2. If AI didn't generate enough, try choice detection
        if suggestions.len() < 2 {
            if let Some(choice_suggestions) = self.choice_detector.detect_choices(&text_lower) {
                debug!("Found choice pattern, adding choice-based suggestions");
                suggestions.extend(choice_suggestions);
            }
        }

        // 3. Try child AI engine for more responses
        if suggestions.len() < 4 {
            if let Ok(child_suggestions) = {
                let mut engine = self.child_ai_engine.borrow_mut();
                engine.add_question(&text_lower);
                engine.generate_child_responses(&text_lower)
            } {
                debug!("Adding child AI suggestions");
                suggestions.extend(child_suggestions);
            }
        }

        // 4. Fallback to Eliza if still need more
        if suggestions.len() < 4 {
            if let Some(eliza_suggestions) = self.eliza_engine.generate_response(&text_lower) {
                debug!("Adding Eliza-style suggestions");
                suggestions.extend(eliza_suggestions);
            }
        }

        // 5. Final fallback to defaults
        if suggestions.is_empty() {
            debug!("Using default suggestions");
            suggestions = self.get_default_suggestions();
        }

        // 🧠 APPLY EMOTIONAL INTELLIGENCE: Adapt responses based on mood and memory
        {
            let memory = self.memory_core.borrow();
            suggestions = memory.adapt_responses_to_mood(suggestions);
            debug!("🎭 Applied emotional adaptation to responses");
        }

        // Ensure all suggestions have appropriate emojis
        for suggestion in &mut suggestions {
            if suggestion.emoji.is_empty() || suggestion.emoji == "💭" {
                suggestion.emoji = self.emoji_mapper.get_emoji(&suggestion.text);
            }
        }

        // TinkyAsk uses 4 suggestions, so let's match that
        suggestions.truncate(4);
        while suggestions.len() < 4 {
            suggestions.push(self.get_fallback_suggestion(suggestions.len()));
        }

        info!("🧠 Generated {} emotionally intelligent suggestions", suggestions.len());
        Ok(suggestions)
    }

    /// Record when a user selects a response (for conversation history and learning)
    pub fn record_response(&self, question: &str, response: &str, success_rating: f32) {
        // Update child AI engine
        {
            let mut engine = self.child_ai_engine.borrow_mut();
            engine.add_response(response);
        }

        // Update memory core with learning
        {
            let mut memory = self.memory_core.borrow_mut();
            memory.learn_from_interaction(question, response, success_rating);
        }

        info!(
            "🧠 Recorded and learned from interaction: '{}' → '{}' (success: {:.2})",
            question, response, success_rating
        );
    }

    /// Get emotional insights about the current interaction patterns
    pub fn get_emotional_insights(&self) -> serde_json::Value {
        let memory = self.memory_core.borrow();
        let insights = memory.get_emotional_insights();
        serde_json::to_value(insights).unwrap_or(serde_json::Value::Null)
    }

    fn get_default_suggestions(&self) -> Vec<SuggestionTile> {
        // Use user profile defaults if available
        if let Some(ref profile) = self.user_profile {
            let default_responses = profile.get_default_responses();
            return default_responses
                .into_iter()
                .map(|response| {
                    let emoji = self.emoji_mapper.get_emoji(&response);
                    SuggestionTile { emoji, text: response, category: TileCategory::BasicResponse, confidence: 1.0 }
                })
                .collect();
        }

        // Fallback to generic defaults
        vec![
            SuggestionTile {
                emoji: "👋".to_string(),
                text: "Hello".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            },
            SuggestionTile {
                emoji: "✅".to_string(),
                text: "Yes".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            },
            SuggestionTile {
                emoji: "❌".to_string(),
                text: "No".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            },
        ]
    }

    fn get_fallback_suggestion(&self, index: usize) -> SuggestionTile {
        let fallbacks = [("🤔", "I'm thinking"), ("👍", "Okay"), ("❓", "I have a question")];

        let (emoji, text) = fallbacks.get(index).unwrap_or(&("💭", "..."));

        SuggestionTile {
            emoji: emoji.to_string(),
            text: text.to_string(),
            category: TileCategory::Default,
            confidence: 0.5,
        }
    }

    /// Generate gentle alternatives when topics should be avoided
    fn get_gentle_alternatives(&self) -> Vec<SuggestionTile> {
        vec![
            SuggestionTile {
                emoji: "🤗".to_string(),
                text: "Let's talk about something else".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 0.9,
            },
            SuggestionTile {
                emoji: "😌".to_string(),
                text: "I'm okay".to_string(),
                category: TileCategory::Emotion,
                confidence: 0.8,
            },
            SuggestionTile {
                emoji: "🎈".to_string(),
                text: "What else is new?".to_string(),
                category: TileCategory::Question,
                confidence: 0.7,
            },
            SuggestionTile {
                emoji: "💫".to_string(),
                text: "Tell me something fun".to_string(),
                category: TileCategory::Default,
                confidence: 0.6,
            },
        ]
    }
}
