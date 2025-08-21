// TinkyBink Friend Mode - Compassionate Guided Discovery System
// Helps patients figure out what they want to say through gentle questioning
// Like having a supportive friend who helps you find the right words

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FriendMode {
    pub discovery_phase: DiscoveryPhase,
    pub patient_mood: EmotionalState,
    pub discovered_needs: Vec<DiscoveredNeed>,
    pub gentle_questions: Vec<GentleQuestion>,
    pub helper_suggestions: Vec<HelperSuggestion>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum DiscoveryPhase {
    InitialCheck,      // "How are you feeling?"
    ExploringFeelings, // "Tell me more about that feeling"
    NarrowingDown,     // "Is it more like X or Y?"
    GettingSpecific,   // "What exactly would help?"
    Confirming,        // "So you want X, right?"
    Ready,             // Patient knows what they want
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EmotionalState {
    pub frustration_level: f32,  // 0.0 = calm, 1.0 = very frustrated
    pub confusion_level: f32,    // 0.0 = clear, 1.0 = very confused
    pub energy_level: f32,       // 0.0 = exhausted, 1.0 = energetic
    pub comfort_level: f32,      // 0.0 = uncomfortable, 1.0 = comfortable
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiscoveredNeed {
    pub category: String,
    pub specifics: Vec<String>,
    pub confidence: f32,
    pub urgency: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GentleQuestion {
    pub question_text: String,
    pub response_options: Vec<GuidedResponse>,
    pub helps_discover: String,
    pub patience_level: PatienceLevel,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GuidedResponse {
    pub emoji: String,
    pub simple_text: String,
    pub meaning: String,
    pub leads_to: NextDiscovery,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum NextDiscovery {
    Physical,    // Body needs (pain, bathroom, position)
    Emotional,   // Feelings (scared, lonely, happy)
    Social,      // Want company, call someone
    Comfort,     // Temperature, pillows, blankets
    Practical,   // Food, water, medicine
    Unclear,     // Still figuring it out
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum PatienceLevel {
    VeryPatient,    // Take all the time you need
    Gentle,         // No rush, we'll figure it out
    Encouraging,    // You're doing great
    Supportive,     // I'm here to help
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelperSuggestion {
    pub suggestion: String,
    pub why_suggested: String,
    pub based_on: Vec<String>,
}

// Friend Mode Discovery Engine
pub struct FriendDiscoveryEngine;

impl FriendDiscoveryEngine {
    
    // Start friend mode - gentle opening
    pub fn start_friend_mode() -> Vec<(String, String, String)> {
        vec![
            ("🤔".to_string(), "Something's up".to_string(), 
             "Something's bothering me but I'm not sure what.".to_string()),
            ("😕".to_string(), "Feel off".to_string(), 
             "I don't feel right.".to_string()),
            ("💭".to_string(), "Need something".to_string(), 
             "I need something but can't figure out what.".to_string()),
            ("🤷".to_string(), "Don't know".to_string(), 
             "I don't know what I want.".to_string()),
            ("😔".to_string(), "Frustrated".to_string(), 
             "I'm frustrated, help me figure this out.".to_string()),
            ("🆘".to_string(), "Help me say".to_string(), 
             "Help me figure out what I'm trying to say.".to_string()),
        ]
    }
    
    // First discovery question - broad categories
    pub fn discovery_level_1() -> GentleQuestion {
        GentleQuestion {
            question_text: "Let's figure this out together. What kind of feeling is it?".to_string(),
            response_options: vec![
                GuidedResponse {
                    emoji: "🤕".to_string(),
                    simple_text: "Body feeling".to_string(),
                    meaning: "Something with my body doesn't feel right.".to_string(),
                    leads_to: NextDiscovery::Physical,
                },
                GuidedResponse {
                    emoji: "😢".to_string(),
                    simple_text: "Emotion".to_string(),
                    meaning: "I'm having feelings I can't express.".to_string(),
                    leads_to: NextDiscovery::Emotional,
                },
                GuidedResponse {
                    emoji: "🍽️".to_string(),
                    simple_text: "Basic need".to_string(),
                    meaning: "I need something basic like food or water.".to_string(),
                    leads_to: NextDiscovery::Practical,
                },
                GuidedResponse {
                    emoji: "👥".to_string(),
                    simple_text: "People".to_string(),
                    meaning: "It's about people or being alone.".to_string(),
                    leads_to: NextDiscovery::Social,
                },
                GuidedResponse {
                    emoji: "🛏️".to_string(),
                    simple_text: "Comfort".to_string(),
                    meaning: "I'm not comfortable.".to_string(),
                    leads_to: NextDiscovery::Comfort,
                },
                GuidedResponse {
                    emoji: "❓".to_string(),
                    simple_text: "Still unsure".to_string(),
                    meaning: "I still don't know.".to_string(),
                    leads_to: NextDiscovery::Unclear,
                },
            ],
            helps_discover: "general_category".to_string(),
            patience_level: PatienceLevel::VeryPatient,
        }
    }
    
    // Physical discovery - what's wrong with body
    pub fn discover_physical() -> GentleQuestion {
        GentleQuestion {
            question_text: "OK, something physical. Let me help you narrow it down...".to_string(),
            response_options: vec![
                GuidedResponse {
                    emoji: "😣".to_string(),
                    simple_text: "Pain".to_string(),
                    meaning: "Something hurts.".to_string(),
                    leads_to: NextDiscovery::Physical,
                },
                GuidedResponse {
                    emoji: "🚻".to_string(),
                    simple_text: "Bathroom".to_string(),
                    meaning: "I need the bathroom.".to_string(),
                    leads_to: NextDiscovery::Practical,
                },
                GuidedResponse {
                    emoji: "🔄".to_string(),
                    simple_text: "Position".to_string(),
                    meaning: "I need to move or be repositioned.".to_string(),
                    leads_to: NextDiscovery::Comfort,
                },
                GuidedResponse {
                    emoji: "🤒".to_string(),
                    simple_text: "Feel sick".to_string(),
                    meaning: "I feel sick or nauseous.".to_string(),
                    leads_to: NextDiscovery::Physical,
                },
                GuidedResponse {
                    emoji: "😴".to_string(),
                    simple_text: "Tired".to_string(),
                    meaning: "I'm very tired.".to_string(),
                    leads_to: NextDiscovery::Comfort,
                },
                GuidedResponse {
                    emoji: "🤔".to_string(),
                    simple_text: "Something else".to_string(),
                    meaning: "It's something else physical.".to_string(),
                    leads_to: NextDiscovery::Unclear,
                },
            ],
            helps_discover: "physical_need".to_string(),
            patience_level: PatienceLevel::Gentle,
        }
    }
    
    // Emotional discovery - what feelings
    pub fn discover_emotional() -> GentleQuestion {
        GentleQuestion {
            question_text: "It's OK to have feelings. Which one feels closest?".to_string(),
            response_options: vec![
                GuidedResponse {
                    emoji: "😰".to_string(),
                    simple_text: "Scared".to_string(),
                    meaning: "I'm scared or anxious.".to_string(),
                    leads_to: NextDiscovery::Emotional,
                },
                GuidedResponse {
                    emoji: "😢".to_string(),
                    simple_text: "Sad".to_string(),
                    meaning: "I feel sad or want to cry.".to_string(),
                    leads_to: NextDiscovery::Emotional,
                },
                GuidedResponse {
                    emoji: "😔".to_string(),
                    simple_text: "Lonely".to_string(),
                    meaning: "I feel lonely.".to_string(),
                    leads_to: NextDiscovery::Social,
                },
                GuidedResponse {
                    emoji: "😤".to_string(),
                    simple_text: "Frustrated".to_string(),
                    meaning: "I'm frustrated or angry.".to_string(),
                    leads_to: NextDiscovery::Emotional,
                },
                GuidedResponse {
                    emoji: "😕".to_string(),
                    simple_text: "Confused".to_string(),
                    meaning: "I'm confused and need help understanding.".to_string(),
                    leads_to: NextDiscovery::Unclear,
                },
                GuidedResponse {
                    emoji: "🤗".to_string(),
                    simple_text: "Need comfort".to_string(),
                    meaning: "I just need some comfort.".to_string(),
                    leads_to: NextDiscovery::Social,
                },
            ],
            helps_discover: "emotional_need".to_string(),
            patience_level: PatienceLevel::Supportive,
        }
    }
    
    // When still unclear - more gentle probing
    pub fn discover_unclear() -> GentleQuestion {
        GentleQuestion {
            question_text: "That's OK, sometimes it's hard to know. Let's try this way...".to_string(),
            response_options: vec![
                GuidedResponse {
                    emoji: "⏰".to_string(),
                    simple_text: "Been a while".to_string(),
                    meaning: "It's been a while since something.".to_string(),
                    leads_to: NextDiscovery::Practical,
                },
                GuidedResponse {
                    emoji: "🔄".to_string(),
                    simple_text: "Something changed".to_string(),
                    meaning: "Something changed and feels wrong.".to_string(),
                    leads_to: NextDiscovery::Comfort,
                },
                GuidedResponse {
                    emoji: "📞".to_string(),
                    simple_text: "Missing something".to_string(),
                    meaning: "I'm missing something or someone.".to_string(),
                    leads_to: NextDiscovery::Social,
                },
                GuidedResponse {
                    emoji: "🎯".to_string(),
                    simple_text: "Specific thing".to_string(),
                    meaning: "There's a specific thing but I can't name it.".to_string(),
                    leads_to: NextDiscovery::Practical,
                },
                GuidedResponse {
                    emoji: "😴".to_string(),
                    simple_text: "Too tired".to_string(),
                    meaning: "I'm too tired to figure it out.".to_string(),
                    leads_to: NextDiscovery::Comfort,
                },
                GuidedResponse {
                    emoji: "🛑".to_string(),
                    simple_text: "Give up".to_string(),
                    meaning: "Never mind, I give up.".to_string(),
                    leads_to: NextDiscovery::Emotional,
                },
            ],
            helps_discover: "unclear_need".to_string(),
            patience_level: PatienceLevel::VeryPatient,
        }
    }
    
    // Helper suggestions based on time of day, patterns, context
    pub fn generate_helpful_suggestions(time_of_day: &str, recent_activities: Vec<String>) -> Vec<HelperSuggestion> {
        let mut suggestions = Vec::new();
        
        // Time-based suggestions
        match time_of_day {
            "morning" => {
                suggestions.push(HelperSuggestion {
                    suggestion: "Maybe you're hungry for breakfast?".to_string(),
                    why_suggested: "It's morning and you haven't eaten yet.".to_string(),
                    based_on: vec!["time_of_day".to_string(), "meal_schedule".to_string()],
                });
                suggestions.push(HelperSuggestion {
                    suggestion: "Do you need help getting ready for the day?".to_string(),
                    why_suggested: "Morning routine assistance.".to_string(),
                    based_on: vec!["daily_routine".to_string()],
                });
            },
            "evening" => {
                suggestions.push(HelperSuggestion {
                    suggestion: "Are you getting tired? Maybe ready for bed?".to_string(),
                    why_suggested: "It's getting late.".to_string(),
                    based_on: vec!["time_of_day".to_string(), "sleep_schedule".to_string()],
                });
                suggestions.push(HelperSuggestion {
                    suggestion: "Would you like to call family before bed?".to_string(),
                    why_suggested: "Evening family connection time.".to_string(),
                    based_on: vec!["social_pattern".to_string()],
                });
            },
            _ => {}
        }
        
        // Activity-based suggestions
        if recent_activities.iter().any(|a| a.contains("long_time_in_position")) {
            suggestions.push(HelperSuggestion {
                suggestion: "You've been in the same position for a while. Need to move?".to_string(),
                why_suggested: "Preventing discomfort from staying still too long.".to_string(),
                based_on: vec!["position_tracking".to_string()],
            });
        }
        
        suggestions
    }
    
    // Generate friend mode response based on patient state
    pub fn generate_friend_response(patient_state: &EmotionalState) -> Vec<(String, String, String)> {
        if patient_state.frustration_level > 0.7 {
            // High frustration - simplify
            vec![
                ("😌".to_string(), "Take time".to_string(), 
                 "It's OK, take your time.".to_string()),
                ("🫂".to_string(), "I'm here".to_string(), 
                 "I'm here to help you.".to_string()),
                ("🔄".to_string(), "Try again".to_string(), 
                 "Let's try a different way.".to_string()),
                ("✋".to_string(), "Take break".to_string(), 
                 "Let's take a break.".to_string()),
            ]
        } else if patient_state.confusion_level > 0.7 {
            // High confusion - guide more
            vec![
                ("👍".to_string(), "Yes/No?".to_string(), 
                 "Can you answer yes or no?".to_string()),
                ("☝️".to_string(), "One thing".to_string(), 
                 "Let's focus on one thing.".to_string()),
                ("🎯".to_string(), "Main thing".to_string(), 
                 "What's the main thing?".to_string()),
                ("💭".to_string(), "Show me".to_string(), 
                 "Can you show me?".to_string()),
            ]
        } else {
            // Normal friend mode
            Self::start_friend_mode()
        }
    }
}

// Memory and pattern learning
pub struct PatientMemory {
    pub common_needs: HashMap<String, Vec<String>>,  // time -> needs
    pub frustration_triggers: Vec<String>,
    pub successful_discoveries: Vec<DiscoveredNeed>,
    pub preferred_communication_style: CommunicationStyle,
}

#[derive(Debug, Clone)]
pub enum CommunicationStyle {
    Direct,      // Knows what they want
    NeedsHelp,   // Often needs discovery
    Visual,      // Responds better to pictures
    Emotional,   // Expresses through feelings
}

impl PatientMemory {
    pub fn learn_from_session(&mut self, discovered: DiscoveredNeed) {
        self.successful_discoveries.push(discovered.clone());
        
        // Learn patterns
        let time = get_current_time_period();
        self.common_needs
            .entry(time)
            .or_insert_with(Vec::new)
            .push(discovered.category);
    }
    
    pub fn predict_likely_need(&self, time: &str) -> Option<String> {
        self.common_needs
            .get(time)
            .and_then(|needs| {
                // Find most common need at this time
                let mut counts = HashMap::new();
                for need in needs {
                    *counts.entry(need.clone()).or_insert(0) += 1;
                }
                counts.into_iter()
                    .max_by_key(|(_, count)| *count)
                    .map(|(need, _)| need)
            })
    }
}

fn get_current_time_period() -> String {
    // This would get actual time
    "afternoon".to_string()
}

// Main function for testing
fn main() {
    println!("🤝 TinkyBink Friend Mode");
    println!("💝 Compassionate Guided Discovery System");
    println!("🗣️ Helping patients find their words");
    
    println!("\n🌟 FRIEND MODE START:");
    println!("Patient seems to need something but can't express it...\n");
    
    let start_tiles = FriendDiscoveryEngine::start_friend_mode();
    println!("Friend: 'Having trouble finding the words? That's OK, let me help...'\n");
    for (i, (emoji, text, sentence)) in start_tiles.iter().enumerate() {
        println!("  {}. {} {} → \"{}\"", i+1, emoji, text, sentence);
    }
    
    println!("\n🔍 DISCOVERY PHASE 1:");
    let question1 = FriendDiscoveryEngine::discovery_level_1();
    println!("Friend: '{}'", question1.question_text);
    for (i, response) in question1.response_options.iter().enumerate() {
        println!("  {}. {} {} → \"{}\"", 
                i+1, response.emoji, response.simple_text, response.meaning);
    }
    
    println!("\n💭 If patient chooses 'Body feeling':");
    let physical = FriendDiscoveryEngine::discover_physical();
    println!("Friend: '{}'", physical.question_text);
    for (i, response) in physical.response_options.iter().take(3).enumerate() {
        println!("  {}. {} {} → \"{}\"", 
                i+1, response.emoji, response.simple_text, response.meaning);
    }
    
    println!("\n❤️ If patient chooses 'Emotion':");
    let emotional = FriendDiscoveryEngine::discover_emotional();
    println!("Friend: '{}'", emotional.question_text);
    for (i, response) in emotional.response_options.iter().take(3).enumerate() {
        println!("  {}. {} {} → \"{}\"", 
                i+1, response.emoji, response.simple_text, response.meaning);
    }
    
    println!("\n🎯 HELPFUL SUGGESTIONS:");
    let suggestions = FriendDiscoveryEngine::generate_helpful_suggestions(
        "morning", 
        vec!["long_time_in_position".to_string()]
    );
    for suggestion in suggestions {
        println!("💡 {}", suggestion.suggestion);
        println!("   ({})", suggestion.why_suggested);
    }
    
    println!("\n✅ Friend Mode: Compassionate guided discovery ready!");
    println!("🏆 Helping patients find their voice through gentle questioning!");
}