use anyhow::Result;
use serde::{Deserialize, Serialize};
use tracing::{debug, info};

use crate::core::events::{SuggestionTile, TileCategory};

/// Child-like AI conversation engine inspired by TinkyAsk
/// Generates emotionally varied, personality-rich responses that feel authentic to a child
pub struct ChildAiEngine {
    conversation_history: Vec<ConversationEntry>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct ConversationEntry {
    text: String,
    is_question: bool,
    timestamp: chrono::DateTime<chrono::Utc>,
}

impl ChildAiEngine {
    pub fn new() -> Self {
        info!("Initializing Child AI Engine");
        Self {
            conversation_history: Vec::new(),
        }
    }
    
    /// Add a question to the conversation history
    pub fn add_question(&mut self, question: &str) {
        self.conversation_history.push(ConversationEntry {
            text: question.to_string(),
            is_question: true,
            timestamp: chrono::Utc::now(),
        });
        
        // Keep only last 8 entries for context
        if self.conversation_history.len() > 8 {
            self.conversation_history.remove(0);
        }
    }
    
    /// Add a response to the conversation history
    pub fn add_response(&mut self, response: &str) {
        self.conversation_history.push(ConversationEntry {
            text: response.to_string(),
            is_question: false,
            timestamp: chrono::Utc::now(),
        });
        
        // Keep only last 8 entries for context
        if self.conversation_history.len() > 8 {
            self.conversation_history.remove(0);
        }
    }
    
    /// Generate child-like suggestions based on the question and conversation context
    pub fn generate_child_responses(&self, question: &str) -> Result<Vec<SuggestionTile>> {
        debug!("Generating child-like responses for: '{}'", question);
        
        // Build context from recent conversation
        let context_history = self.build_context_string();
        
        // Generate responses using the child personality patterns
        let responses = self.generate_contextual_responses(question, &context_history);
        
        // Convert to suggestion tiles with sentiment analysis
        let tiles: Vec<SuggestionTile> = responses.into_iter()
            .map(|response| self.create_suggestion_tile(response))
            .collect();
        
        info!("Generated {} child-like suggestion tiles", tiles.len());
        Ok(tiles)
    }
    
    fn build_context_string(&self) -> String {
        self.conversation_history
            .iter()
            .take(4) // Last 4 entries for context
            .map(|entry| {
                if entry.is_question {
                    format!("Parent asked: {}", entry.text)
                } else {
                    format!("Child replied: {}", entry.text)
                }
            })
            .collect::<Vec<_>>()
            .join("\n")
    }
    
    fn generate_contextual_responses(&self, question: &str, _context: &str) -> Vec<String> {
        let question_lower = question.to_lowercase();
        
        // Pattern-based child responses (like the Android app but simpler)
        if self.is_yes_no_question(&question_lower) {
            self.get_yes_no_responses(&question_lower)
        } else if self.is_feeling_question(&question_lower) {
            self.get_feeling_responses()
        } else if self.is_food_question(&question_lower) {
            self.get_food_responses()
        } else if self.is_want_question(&question_lower) {
            self.get_want_responses()
        } else if self.is_play_question(&question_lower) {
            self.get_play_responses()
        } else if self.is_help_question(&question_lower) {
            self.get_help_responses()
        } else {
            self.get_general_responses()
        }
    }
    
    fn is_yes_no_question(&self, question: &str) -> bool {
        let patterns = [
            "do you", "does you", "did you", "are you", "is you", "was you", "were you",
            "will you", "would you", "could you", "should you", "can you", "may you", "have you"
        ];
        patterns.iter().any(|pattern| question.contains(pattern))
    }
    
    fn is_feeling_question(&self, question: &str) -> bool {
        question.contains("how") && (question.contains("feel") || question.contains("doing"))
    }
    
    fn is_food_question(&self, question: &str) -> bool {
        let food_words = ["eat", "hungry", "food", "meal", "breakfast", "lunch", "dinner", "snack"];
        food_words.iter().any(|word| question.contains(word))
    }
    
    fn is_want_question(&self, question: &str) -> bool {
        question.contains("want") || question.contains("like") || question.contains("prefer")
    }
    
    fn is_play_question(&self, question: &str) -> bool {
        let play_words = ["play", "game", "fun", "activity"];
        play_words.iter().any(|word| question.contains(word))
    }
    
    fn is_help_question(&self, question: &str) -> bool {
        question.contains("help") || question.contains("assist")
    }
    
    fn get_yes_no_responses(&self, question: &str) -> Vec<String> {
        let mut responses = vec!["Yes please!".to_string(), "No way".to_string()];
        
        // Add context-specific third and fourth options
        if question.contains("hungry") {
            responses.push("Maybe a little".to_string());
            responses.push("I'm starving!".to_string());
        } else if question.contains("tired") {
            responses.push("Kinda sleepy".to_string());
            responses.push("I'm wide awake!".to_string());
        } else {
            responses.push("I'm not sure".to_string());
            responses.push("Can I think about it?".to_string());
        }
        
        responses
    }
    
    fn get_feeling_responses(&self) -> Vec<String> {
        vec![
            "I'm doing great!".to_string(),
            "Pretty good today".to_string(),
            "Not so good".to_string(),
            "I feel silly".to_string(),
        ]
    }
    
    fn get_food_responses(&self) -> Vec<String> {
        vec![
            "I want pizza!".to_string(),
            "Something yummy".to_string(),
            "I'm not hungry".to_string(),
            "Can we have cookies?".to_string(),
        ]
    }
    
    fn get_want_responses(&self) -> Vec<String> {
        vec![
            "That sounds fun!".to_string(),
            "Not right now".to_string(),
            "Maybe later?".to_string(),
            "Ooh yes please!".to_string(),
        ]
    }
    
    fn get_play_responses(&self) -> Vec<String> {
        vec![
            "Let's play!".to_string(),
            "I'm too tired".to_string(),
            "What game?".to_string(),
            "That's boring".to_string(),
        ]
    }
    
    fn get_help_responses(&self) -> Vec<String> {
        vec![
            "Yes please help me".to_string(),
            "I can do it myself".to_string(),
            "I need help with this".to_string(),
            "Show me how".to_string(),
        ]
    }
    
    fn get_general_responses(&self) -> Vec<String> {
        vec![
            "Tell me more".to_string(),
            "I don't understand".to_string(),
            "That's interesting".to_string(),
            "What do you mean?".to_string(),
        ]
    }
    
    fn create_suggestion_tile(&self, response: String) -> SuggestionTile {
        let response_lower = response.to_lowercase();
        
        // Sentiment analysis like the Android app
        let (emoji, category, confidence) = if self.is_negative_sentiment(&response_lower) {
            ("🚫", TileCategory::Emotion, 0.9)
        } else if self.is_positive_sentiment(&response_lower) {
            ("✅", TileCategory::BasicResponse, 0.9)
        } else if response_lower.contains("?") {
            ("❓", TileCategory::Question, 0.8)
        } else if self.is_thinking_sentiment(&response_lower) {
            ("🤔", TileCategory::Default, 0.7)
        } else {
            ("💭", TileCategory::Default, 0.6)
        };
        
        SuggestionTile {
            emoji: emoji.to_string(),
            text: response,
            category,
            confidence,
        }
    }
    
    fn is_negative_sentiment(&self, text: &str) -> bool {
        let negative_words = ["no", "not", "don't", "stop", "sad", "angry", "boring", "tired", "way"];
        negative_words.iter().any(|word| text.contains(word))
    }
    
    fn is_positive_sentiment(&self, text: &str) -> bool {
        let positive_words = ["yes", "love", "like", "go", "want", "sure", "fun", "happy", "ok", "play", "good", "great", "yay", "please"];
        positive_words.iter().any(|word| text.contains(word))
    }
    
    fn is_thinking_sentiment(&self, text: &str) -> bool {
        let thinking_words = ["think", "maybe", "not sure", "kinda", "little", "understand"];
        thinking_words.iter().any(|word| text.contains(word))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_yes_no_question_detection() {
        let engine = ChildAiEngine::new();
        assert!(engine.is_yes_no_question("are you hungry"));
        assert!(engine.is_yes_no_question("do you want to play"));
        assert!(!engine.is_yes_no_question("what do you want"));
    }
    
    #[test]
    fn test_feeling_question_detection() {
        let engine = ChildAiEngine::new();
        assert!(engine.is_feeling_question("how are you feeling"));
        assert!(engine.is_feeling_question("how are you doing"));
        assert!(!engine.is_feeling_question("what are you doing"));
    }
    
    #[test]
    fn test_sentiment_analysis() {
        let engine = ChildAiEngine::new();
        let tile = engine.create_suggestion_tile("Yes please!".to_string());
        assert_eq!(tile.emoji, "✅");
        assert_eq!(tile.category, TileCategory::BasicResponse);
        
        let tile = engine.create_suggestion_tile("No way".to_string());
        assert_eq!(tile.emoji, "🚫");
        assert_eq!(tile.category, TileCategory::Emotion);
    }
    
    #[test]
    fn test_conversation_history() {
        let mut engine = ChildAiEngine::new();
        engine.add_question("Are you hungry?");
        engine.add_response("Yes please!");
        
        assert_eq!(engine.conversation_history.len(), 2);
        assert!(engine.conversation_history[0].is_question);
        assert!(!engine.conversation_history[1].is_question);
    }
}