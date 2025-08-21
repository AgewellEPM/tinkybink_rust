//! User Profile System for AAC
//! Supports children, adults, stroke survivors, and all AAC users

use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum UserType {
    /// Child user (ages 2-12)
    Child { age: u8 },
    /// Teenager (ages 13-17)
    Teen { age: u8 },
    /// Adult user (18+)
    Adult { age: Option<u8> },
    /// Stroke survivor or aphasia patient
    StrokeSurvivor { months_since_event: Option<u16>, therapy_stage: TherapyStage },
    /// Other medical conditions affecting speech
    Medical { condition: String, communication_level: CommunicationLevel },
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum TherapyStage {
    Acute,          // Just after stroke
    Rehabilitation, // Active therapy
    Maintenance,    // Long-term support
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum CommunicationLevel {
    Beginner,     // Just starting AAC
    Intermediate, // Some AAC experience
    Advanced,     // Fluent AAC user
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UserProfile {
    pub name: String,
    pub user_type: UserType,
    pub preferences: UserPreferences,
    pub vocabulary_level: VocabularyLevel,
    pub response_style: ResponseStyle,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UserPreferences {
    /// Number of tiles to show (2-8)
    pub tile_count: u8,
    /// Complexity of responses
    pub response_complexity: ResponseComplexity,
    /// Include medical/therapy vocabulary
    pub include_medical_terms: bool,
    /// Use age-appropriate language
    pub age_appropriate: bool,
    /// Show emotions in responses
    pub show_emotions: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum VocabularyLevel {
    Basic,          // Yes/no, basic needs
    Functional,     // Daily activities, simple requests
    Conversational, // Full conversations
    Advanced,       // Complex thoughts and feelings
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum ResponseComplexity {
    SingleWord,   // "Yes", "No", "Help"
    ShortPhrase,  // "I want water", "Need help"
    FullSentence, // "I would like some water please"
    Paragraph,    // Complex multi-sentence responses
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum ResponseStyle {
    /// Child-like responses with simple words
    Childlike,
    /// Professional adult communication
    Professional,
    /// Casual adult conversation
    Casual,
    /// Medical/therapy focused
    Therapeutic,
    /// Adaptive based on context
    Adaptive,
}

impl UserProfile {
    /// Create profile for a child user
    pub fn child(name: String, age: u8) -> Self {
        Self {
            name,
            user_type: UserType::Child { age },
            preferences: UserPreferences {
                tile_count: 4,
                response_complexity: ResponseComplexity::ShortPhrase,
                include_medical_terms: false,
                age_appropriate: true,
                show_emotions: true,
            },
            vocabulary_level: VocabularyLevel::Functional,
            response_style: ResponseStyle::Childlike,
        }
    }

    /// Create profile for an adult stroke survivor
    pub fn stroke_survivor(name: String, months_since: Option<u16>) -> Self {
        Self {
            name,
            user_type: UserType::StrokeSurvivor {
                months_since_event: months_since,
                therapy_stage: TherapyStage::Rehabilitation,
            },
            preferences: UserPreferences {
                tile_count: 6,
                response_complexity: ResponseComplexity::ShortPhrase,
                include_medical_terms: true,
                age_appropriate: true,
                show_emotions: true,
            },
            vocabulary_level: VocabularyLevel::Functional,
            response_style: ResponseStyle::Therapeutic,
        }
    }

    /// Create profile for an adult user
    pub fn adult(name: String, age: Option<u8>) -> Self {
        Self {
            name,
            user_type: UserType::Adult { age },
            preferences: UserPreferences {
                tile_count: 6,
                response_complexity: ResponseComplexity::FullSentence,
                include_medical_terms: false,
                age_appropriate: true,
                show_emotions: false,
            },
            vocabulary_level: VocabularyLevel::Conversational,
            response_style: ResponseStyle::Casual,
        }
    }

    /// Get appropriate greetings based on user type
    pub fn get_greetings(&self) -> Vec<&'static str> {
        match &self.user_type {
            UserType::Child { age } if *age < 6 => {
                vec!["Hi!", "Hello!", "Good morning!", "Bye bye!"]
            }
            UserType::Child { .. } | UserType::Teen { .. } => {
                vec!["Hey!", "Hi there!", "What's up?", "See you later!"]
            }
            UserType::Adult { .. } => {
                vec!["Hello", "Good morning", "Good evening", "Goodbye"]
            }
            UserType::StrokeSurvivor { .. } => {
                vec!["Hello", "Yes", "No", "Thank you"]
            }
            UserType::Medical { .. } => {
                vec!["Hello", "I need help", "Thank you", "Goodbye"]
            }
        }
    }

    /// Get appropriate responses for common situations
    pub fn get_contextual_responses(&self, context: &str) -> Vec<String> {
        let context_lower = context.to_lowercase();

        match &self.user_type {
            UserType::StrokeSurvivor { therapy_stage, .. } => {
                if context_lower.contains("therapy") || context_lower.contains("exercise") {
                    match therapy_stage {
                        TherapyStage::Acute => vec![
                            "Too tired".to_string(),
                            "Try later".to_string(),
                            "Need rest".to_string(),
                            "Hurts".to_string(),
                        ],
                        TherapyStage::Rehabilitation => vec![
                            "I'll try".to_string(),
                            "Need help".to_string(),
                            "Show me again".to_string(),
                            "Making progress".to_string(),
                        ],
                        TherapyStage::Maintenance => vec![
                            "Let's practice".to_string(),
                            "Getting better".to_string(),
                            "Still difficult".to_string(),
                            "Thank you".to_string(),
                        ],
                    }
                } else {
                    self.get_default_responses()
                }
            }
            UserType::Adult { .. } => {
                if context_lower.contains("work") || context_lower.contains("meeting") {
                    vec![
                        "I agree".to_string(),
                        "Need clarification".to_string(),
                        "Give me a moment".to_string(),
                        "Let's discuss".to_string(),
                    ]
                } else {
                    self.get_default_responses()
                }
            }
            _ => self.get_default_responses(),
        }
    }

    pub fn get_default_responses(&self) -> Vec<String> {
        match self.response_style {
            ResponseStyle::Childlike => {
                vec!["Yes!".to_string(), "No thanks".to_string(), "Maybe".to_string(), "I don't know".to_string()]
            }
            ResponseStyle::Professional => vec![
                "I agree".to_string(),
                "I disagree".to_string(),
                "Please clarify".to_string(),
                "I understand".to_string(),
            ],
            ResponseStyle::Casual => {
                vec!["Sure".to_string(), "Not really".to_string(), "Let me think".to_string(), "Got it".to_string()]
            }
            ResponseStyle::Therapeutic => {
                vec!["Yes".to_string(), "No".to_string(), "Help".to_string(), "Thank you".to_string()]
            }
            ResponseStyle::Adaptive => {
                vec!["Yes".to_string(), "No".to_string(), "Maybe".to_string(), "Help please".to_string()]
            }
        }
    }
}
