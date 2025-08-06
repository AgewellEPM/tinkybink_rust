use regex::Regex;
use tracing::debug;

use crate::core::events::{SuggestionTile, TileCategory};

/// Eliza-style conversational response generator for AAC suggestions
pub struct ElizaEngine {
    response_patterns: Vec<ResponsePattern>,
}

struct ResponsePattern {
    pattern: Regex,
    responses: Vec<ResponseTemplate>,
    category: TileCategory,
    priority: u8, // Higher number = higher priority
}

struct ResponseTemplate {
    emoji: String,
    text: String,
    confidence: f32,
}

impl Default for ElizaEngine {
    fn default() -> Self {
        Self::new()
    }
}

impl ElizaEngine {
    pub fn new() -> Self {
        let mut engine = Self {
            response_patterns: Vec::new(),
        };

        engine.initialize_patterns();
        engine
    }

    /// Generate contextual response suggestions based on input text
    pub fn generate_response(&self, text: &str) -> Option<Vec<SuggestionTile>> {
        debug!("Generating Eliza response for: '{}'", text);

        // Find the highest priority matching pattern
        let mut best_match: Option<&ResponsePattern> = None;
        let mut best_priority = 0;

        for pattern in &self.response_patterns {
            if pattern.pattern.is_match(text) && pattern.priority > best_priority {
                best_match = Some(pattern);
                best_priority = pattern.priority;
            }
        }

        if let Some(pattern) = best_match {
            debug!("Found matching pattern with priority {}", pattern.priority);
            Some(self.create_suggestions_from_pattern(pattern))
        } else {
            None
        }
    }

    fn create_suggestions_from_pattern(&self, pattern: &ResponsePattern) -> Vec<SuggestionTile> {
        pattern
            .responses
            .iter()
            .take(3)
            .map(|template| SuggestionTile {
                emoji: template.emoji.clone(),
                text: template.text.clone(),
                category: pattern.category.clone(),
                confidence: template.confidence,
            })
            .collect()
    }

    fn initialize_patterns(&mut self) {
        // YES/NO Questions (highest priority for clear responses)
        self.add_pattern(
            r"^(do|does|did|are|is|was|were|will|would|could|should|can|may|have|has)\s+you",
            vec![
                ("✅", "Yes!", 0.95),
                ("❌", "No", 0.95),
                ("🤔", "I'm not sure", 0.8),
            ],
            TileCategory::BasicResponse,
            10,
        );

        // Feeling Questions
        self.add_pattern(
            r"how\s+(are|do)\s+you|feel(ing)?",
            vec![
                ("😊", "I'm doing great!", 0.9),
                ("🙂", "I'm okay", 0.85),
                ("😔", "Not so good", 0.7),
            ],
            TileCategory::Emotion,
            9,
        );

        // Want/Like Questions
        self.add_pattern(
            r"what.*(want|like|prefer|enjoy)",
            vec![
                ("🍕", "I want food", 0.8),
                ("💧", "I want water", 0.8),
                ("🎮", "I want to play", 0.75),
            ],
            TileCategory::Action,
            8,
        );

        // Location Questions
        self.add_pattern(
            r"where",
            vec![
                ("🏠", "At home", 0.85),
                ("📍", "Right here", 0.8),
                ("🤷", "I don't know", 0.7),
            ],
            TileCategory::Place,
            8,
        );

        // Time Questions
        self.add_pattern(
            r"when",
            vec![
                ("⏰", "Right now", 0.85),
                ("⏳", "Later", 0.8),
                ("🌅", "Tomorrow", 0.75),
            ],
            TileCategory::Time,
            8,
        );

        // Food Related
        self.add_pattern(
            r"eat|hungry|food|meal|breakfast|lunch|dinner|snack",
            vec![
                ("🍕", "I want pizza", 0.8),
                ("🥗", "Something healthy", 0.75),
                ("❌", "I'm not hungry", 0.7),
            ],
            TileCategory::Food,
            7,
        );

        // Drink Related
        self.add_pattern(
            r"drink|thirsty|water|juice|milk",
            vec![
                ("💧", "I want water", 0.9),
                ("🧃", "I want juice", 0.8),
                ("❌", "I'm not thirsty", 0.7),
            ],
            TileCategory::Food,
            7,
        );

        // Help Requests
        self.add_pattern(
            r"help|assist|support",
            vec![
                ("✅", "Yes, please help me", 0.9),
                ("❌", "No, I'm okay", 0.8),
                ("🤝", "I need help with this", 0.85),
            ],
            TileCategory::Action,
            7,
        );

        // Activity Questions
        self.add_pattern(
            r"play|game|fun|activity|do",
            vec![
                ("🎮", "Let's play a game", 0.8),
                ("📚", "I want to read", 0.75),
                ("🎵", "I want music", 0.75),
            ],
            TileCategory::Action,
            6,
        );

        // Pain/Discomfort
        self.add_pattern(
            r"hurt|pain|sick|ow|ouch",
            vec![
                ("🤒", "I don't feel well", 0.9),
                ("🆘", "I need help", 0.85),
                ("💊", "I need medicine", 0.8),
            ],
            TileCategory::Emotion,
            9, // High priority for medical concerns
        );

        // Bathroom Needs
        self.add_pattern(
            r"bathroom|toilet|potty|pee|restroom",
            vec![
                ("🚽", "I need the bathroom", 0.95),
                ("🏃", "It's urgent", 0.9),
                ("📍", "Where is it?", 0.8),
            ],
            TileCategory::Action,
            9, // High priority for urgent needs
        );

        // Tired/Sleep
        self.add_pattern(
            r"tired|sleepy|sleep|nap|rest",
            vec![
                ("😴", "I'm tired", 0.9),
                ("🛏️", "I want to sleep", 0.85),
                ("⏰", "What time is it?", 0.7),
            ],
            TileCategory::Emotion,
            7,
        );

        // Happy/Excited
        self.add_pattern(
            r"happy|excited|great|awesome|wonderful",
            vec![
                ("😊", "I'm so happy!", 0.9),
                ("🎉", "This is great!", 0.85),
                ("❤️", "I love this", 0.8),
            ],
            TileCategory::Emotion,
            6,
        );

        // Confused/Don't Understand
        self.add_pattern(
            r"confused|understand|know|huh|what",
            vec![
                ("🤔", "I don't understand", 0.9),
                ("❓", "Can you explain?", 0.85),
                ("🔄", "Say that again", 0.8),
            ],
            TileCategory::Question,
            7,
        );

        // Greetings
        self.add_pattern(
            r"hello|hi|hey|good morning|good afternoon|good evening",
            vec![
                ("👋", "Hello!", 0.9),
                ("😊", "Hi there!", 0.85),
                ("🌅", "Good morning!", 0.8),
            ],
            TileCategory::BasicResponse,
            6,
        );

        // Goodbye
        self.add_pattern(
            r"bye|goodbye|see you|farewell",
            vec![
                ("👋", "Goodbye!", 0.9),
                ("❤️", "See you later!", 0.85),
                ("😊", "Have a good day!", 0.8),
            ],
            TileCategory::BasicResponse,
            6,
        );

        // Default conversational responses (lowest priority)
        self.add_pattern(
            r".*", // Matches anything
            vec![
                ("💬", "Tell me more", 0.6),
                ("🤔", "I understand", 0.5),
                ("👍", "That's interesting", 0.5),
            ],
            TileCategory::Default,
            1, // Lowest priority
        );
    }

    fn add_pattern(
        &mut self,
        pattern_str: &str,
        responses: Vec<(&str, &str, f32)>,
        category: TileCategory,
        priority: u8,
    ) {
        if let Ok(regex) = Regex::new(pattern_str) {
            let templates = responses
                .into_iter()
                .map(|(emoji, text, confidence)| ResponseTemplate {
                    emoji: emoji.to_string(),
                    text: text.to_string(),
                    confidence,
                })
                .collect();

            self.response_patterns.push(ResponsePattern {
                pattern: regex,
                responses: templates,
                category,
                priority,
            });
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_yes_no_questions() {
        let engine = ElizaEngine::new();
        let suggestions = engine.generate_response("are you happy").unwrap();
        assert_eq!(suggestions.len(), 3);
        assert!(suggestions[0].text.contains("Yes"));
        assert!(suggestions[1].text.contains("No"));
    }

    #[test]
    fn test_feeling_questions() {
        let engine = ElizaEngine::new();
        let suggestions = engine.generate_response("how are you feeling").unwrap();
        assert_eq!(suggestions.len(), 3);
        assert!(suggestions[0].emoji == "😊");
    }

    #[test]
    fn test_food_related() {
        let engine = ElizaEngine::new();
        let suggestions = engine.generate_response("i am hungry").unwrap();
        assert_eq!(suggestions.len(), 3);
        assert!(suggestions.iter().any(|s| s.text.contains("pizza")));
    }

    #[test]
    fn test_priority_matching() {
        let engine = ElizaEngine::new();
        // "are you hungry" should match yes/no pattern (priority 10) over food pattern (priority 7)
        let suggestions = engine.generate_response("are you hungry").unwrap();
        assert!(suggestions[0].text.contains("Yes"));
    }

    #[test]
    fn test_default_response() {
        let engine = ElizaEngine::new();
        let suggestions = engine.generate_response("xyz random text qwerty").unwrap();
        assert_eq!(suggestions.len(), 3);
        assert!(suggestions.iter().any(|s| s.text.contains("Tell me more")));
    }
}
