use regex::Regex;
use std::collections::HashSet;
use tracing::debug;

use crate::core::events::{SuggestionTile, TileCategory};
use crate::suggestions::emoji_mapper::EmojiMapper;

/// Detects choice patterns in user input and generates appropriate response tiles
pub struct ChoiceDetector {
    or_pattern: Regex,
    extended_or_patterns: Vec<Regex>,
    choice_indicators: HashSet<String>,
    emoji_mapper: EmojiMapper,
}

impl ChoiceDetector {
    pub fn new() -> Self {
        let or_pattern = Regex::new(r"\b(\w+)\s+or\s+(\w+)\b").unwrap();
        
        let extended_or_patterns = vec![
            // "apple, banana, or orange"
            Regex::new(r"\b(\w+)\s*,\s*(\w+)\s*,?\s*or\s+(\w+)\b").unwrap(),
            // "apple or banana or orange"
            Regex::new(r"\b(\w+)\s+or\s+(\w+)\s+or\s+(\w+)\b").unwrap(),
            // "apple/banana"
            Regex::new(r"\b(\w+)\s*/\s*(\w+)\b").unwrap(),
        ];
        
        let choice_indicators = [
            "which", "what", "prefer", "rather", "want", "like", 
            "choose", "pick", "select", "decide"
        ].iter().map(|s| s.to_string()).collect();
        
        Self {
            or_pattern,
            extended_or_patterns,
            choice_indicators,
            emoji_mapper: EmojiMapper::new(),
        }
    }
    
    /// Detect if input contains choice patterns and generate suggestions
    pub fn detect_choices(&self, text: &str) -> Option<Vec<SuggestionTile>> {
        let choices = self.extract_choices(text);
        let has_choice_indicator = self.has_choice_indicator(text);
        
        if !choices.is_empty() || has_choice_indicator {
            debug!("Detected choices: {:?}, has indicator: {}", choices, has_choice_indicator);
            Some(self.generate_choice_suggestions(choices))
        } else {
            None
        }
    }
    
    /// Extract choice options from text using various patterns
    fn extract_choices(&self, text: &str) -> Vec<String> {
        let mut choices = Vec::new();
        
        // Check basic OR pattern
        for captures in self.or_pattern.captures_iter(text) {
            if let (Some(choice1), Some(choice2)) = (captures.get(1), captures.get(2)) {
                choices.push(choice1.as_str().to_string());
                choices.push(choice2.as_str().to_string());
            }
        }
        
        // Check extended patterns
        for pattern in &self.extended_or_patterns {
            for captures in pattern.captures_iter(text) {
                for i in 1..captures.len() {
                    if let Some(choice) = captures.get(i) {
                        let choice_str = choice.as_str().trim();
                        if !choice_str.is_empty() {
                            choices.push(choice_str.to_string());
                        }
                    }
                }
            }
        }
        
        // Remove duplicates while preserving order
        let mut unique_choices = Vec::new();
        let mut seen = HashSet::new();
        for choice in choices {
            let clean_choice = choice.trim().to_lowercase();
            if !clean_choice.is_empty() && seen.insert(clean_choice.clone()) {
                unique_choices.push(clean_choice);
            }
        }
        
        unique_choices
    }
    
    /// Check if text contains choice indicator words
    fn has_choice_indicator(&self, text: &str) -> bool {
        let words: HashSet<String> = text
            .split_whitespace()
            .map(|w| w.to_lowercase().trim_matches(|c: char| !c.is_alphabetic()).to_string())
            .collect();
        
        self.choice_indicators.intersection(&words).next().is_some()
    }
    
    /// Generate suggestions based on detected choices
    fn generate_choice_suggestions(&self, choices: Vec<String>) -> Vec<SuggestionTile> {
        let mut suggestions = Vec::new();
        
        // Add each choice as a suggestion (limit to first 3)
        for (index, choice) in choices.iter().enumerate() {
            if index >= 3 {
                break;
            }
            
            let emoji = self.emoji_mapper.get_emoji(choice);
            suggestions.push(SuggestionTile {
                emoji,
                text: format!("I want {}", choice),
                category: TileCategory::Choice,
                confidence: 0.9,
            });
        }
        
        // Fill remaining slots with contextual options
        while suggestions.len() < 3 {
            match suggestions.len() {
                1 => {
                    // If we have 1 choice, add "something else" option
                    suggestions.push(SuggestionTile {
                        emoji: "🔄".to_string(),
                        text: "Something else".to_string(),
                        category: TileCategory::Choice,
                        confidence: 0.7,
                    });
                },
                2 => {
                    if choices.len() == 2 {
                        // If exactly 2 choices, offer "both" option
                        suggestions.push(SuggestionTile {
                            emoji: "🤝".to_string(),
                            text: format!("Both {} and {}", choices[0], choices[1]),
                            category: TileCategory::Choice,
                            confidence: 0.8,
                        });
                    } else {
                        // Otherwise offer "either one"
                        suggestions.push(SuggestionTile {
                            emoji: "🤷".to_string(),
                            text: "Either one is fine".to_string(),
                            category: TileCategory::Choice,
                            confidence: 0.6,
                        });
                    }
                },
                _ => {
                    // Fallback option
                    suggestions.push(SuggestionTile {
                        emoji: "❌".to_string(),
                        text: "Neither, thank you".to_string(),
                        category: TileCategory::Choice,
                        confidence: 0.5,
                    });
                }
            }
        }
        
        suggestions.truncate(3);
        suggestions
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_basic_or_pattern() {
        let detector = ChoiceDetector::new();
        let choices = detector.extract_choices("do you want pizza or pasta");
        assert_eq!(choices, vec!["pizza", "pasta"]);
    }
    
    #[test]
    fn test_extended_patterns() {
        let detector = ChoiceDetector::new();
        let choices = detector.extract_choices("choose apple, banana, or orange");
        assert_eq!(choices, vec!["apple", "banana", "orange"]);
    }
    
    #[test]
    fn test_choice_indicators() {
        let detector = ChoiceDetector::new();
        assert!(detector.has_choice_indicator("which one do you prefer"));
        assert!(detector.has_choice_indicator("what would you like"));
        assert!(!detector.has_choice_indicator("how are you doing"));
    }
    
    #[test]
    fn test_generate_suggestions() {
        let detector = ChoiceDetector::new();
        let suggestions = detector.generate_choice_suggestions(vec!["pizza".to_string(), "pasta".to_string()]);
        assert_eq!(suggestions.len(), 3);
        assert!(suggestions[0].text.contains("pizza"));
        assert!(suggestions[1].text.contains("pasta"));
        assert!(suggestions[2].text.contains("Both"));
    }
}