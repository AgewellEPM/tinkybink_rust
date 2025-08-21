use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use tracing::{debug, info};

use crate::core::events::SuggestionTile;

/// 🧠 TinkyMemoryCore™ - Emotional Context & Learning Engine
///
/// This revolutionary system learns from every interaction to create
/// more personalized, contextually aware responses that adapt to the
/// child's emotional patterns and preferences over time.
pub struct TinkyMemoryCore {
    emotional_profile: EmotionalProfile,
    interaction_history: Vec<InteractionMemory>,
    mood_patterns: HashMap<String, MoodPattern>,
    preference_weights: HashMap<String, f32>,
    avoidance_topics: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EmotionalProfile {
    /// Current emotional state (updated in real-time)
    pub current_mood: EmotionalState,
    /// Baseline emotional tendencies
    pub baseline_mood: EmotionalState,
    /// Last 10 emotional states for pattern detection
    pub recent_moods: Vec<(DateTime<Utc>, EmotionalState)>,
    /// Emotional volatility (how quickly mood changes)
    pub volatility: f32,
    /// Preferred response tone (gentle, energetic, calm, etc.)
    pub preferred_tone: ResponseTone,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct EmotionalState {
    pub happiness: f32,  // 0.0 to 1.0
    pub energy: f32,     // 0.0 to 1.0
    pub anxiety: f32,    // 0.0 to 1.0
    pub confidence: f32, // 0.0 to 1.0
    pub curiosity: f32,  // 0.0 to 1.0
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum ResponseTone {
    Gentle,
    Energetic,
    Calm,
    Playful,
    Serious,
    Adaptive, // Changes based on context
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct InteractionMemory {
    pub timestamp: DateTime<Utc>,
    pub parent_question: String,
    pub child_response: String,
    pub emotional_context: EmotionalState,
    pub success_rating: f32, // How "successful" was this interaction
    pub topic_category: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MoodPattern {
    pub triggers: Vec<String>, // What topics/words trigger this mood
    pub typical_responses: Vec<String>,
    pub frequency: u32,
    pub last_seen: DateTime<Utc>,
}

impl Default for TinkyMemoryCore {
    fn default() -> Self {
        Self::new()
    }
}

impl TinkyMemoryCore {
    pub fn new() -> Self {
        info!("🧠 Initializing TinkyMemoryCore™ - Advanced Emotional Intelligence System");

        Self {
            emotional_profile: EmotionalProfile::default(),
            interaction_history: Vec::new(),
            mood_patterns: HashMap::new(),
            preference_weights: HashMap::new(),
            avoidance_topics: Vec::new(),
        }
    }

    /// 🎯 Learn from each interaction to improve future responses
    pub fn learn_from_interaction(&mut self, question: &str, selected_response: &str, success_rating: f32) {
        debug!(
            "🧠 Learning from interaction: '{}' → '{}' (success: {:.2})",
            question, selected_response, success_rating
        );

        // Create interaction memory
        let memory = InteractionMemory {
            timestamp: Utc::now(),
            parent_question: question.to_string(),
            child_response: selected_response.to_string(),
            emotional_context: self.emotional_profile.current_mood.clone(),
            success_rating,
            topic_category: self.categorize_topic(question),
        };

        // Store interaction
        self.interaction_history.push(memory.clone());

        // Update emotional state based on success
        self.update_mood_from_interaction(&memory);

        // Update preferences
        self.update_preferences(question, selected_response, success_rating);

        // Detect patterns
        self.detect_mood_patterns(&memory);

        // Keep only recent history (last 100 interactions)
        if self.interaction_history.len() > 100 {
            self.interaction_history.remove(0);
        }

        info!("🧠 Learned new interaction pattern. Total memories: {}", self.interaction_history.len());
    }

    /// 🎭 Adapt responses based on current emotional context
    pub fn adapt_responses_to_mood(&self, base_responses: Vec<SuggestionTile>) -> Vec<SuggestionTile> {
        let mood = &self.emotional_profile.current_mood;

        debug!(
            "🎭 Adapting responses for mood: happiness={:.2}, energy={:.2}, anxiety={:.2}",
            mood.happiness, mood.energy, mood.anxiety
        );

        base_responses
            .into_iter()
            .map(|mut tile| {
                // Modify responses based on emotional state
                if mood.anxiety > 0.7 {
                    // High anxiety - make responses gentler and more reassuring
                    tile.text = self.make_response_gentler(&tile.text);
                    tile.confidence *= 0.9; // Slightly less confident when anxious
                } else if mood.energy > 0.8 && mood.happiness > 0.7 {
                    // High energy + happiness - make responses more enthusiastic
                    tile.text = self.make_response_energetic(&tile.text);
                    tile.confidence *= 1.1; // More confident when happy and energetic
                } else if mood.happiness < 0.3 {
                    // Low happiness - avoid overly cheerful responses
                    tile.text = self.make_response_subdued(&tile.text);
                }

                // Apply preference weights
                if let Some(weight) = self.preference_weights.get(&tile.text.to_lowercase()) {
                    tile.confidence *= weight;
                }

                tile
            })
            .collect()
    }

    /// 🚫 Filter out topics the child consistently avoids
    pub fn should_avoid_topic(&self, question: &str) -> bool {
        let question_lower = question.to_lowercase();
        self.avoidance_topics.iter().any(|topic| question_lower.contains(topic))
    }

    /// 📊 Get current emotional intelligence insights
    pub fn get_emotional_insights(&self) -> EmotionalInsights {
        let _mood = &self.emotional_profile.current_mood;
        let recent_success = self.calculate_recent_success_rate();

        EmotionalInsights {
            current_mood_summary: self.describe_current_mood(),
            suggested_approach: self.suggest_interaction_approach(),
            recent_success_rate: recent_success,
            preferred_topics: self.get_preferred_topics(),
            topics_to_avoid: self.avoidance_topics.clone(),
            interaction_count: self.interaction_history.len(),
        }
    }

    // Private helper methods

    fn update_mood_from_interaction(&mut self, memory: &InteractionMemory) {
        let mood = &mut self.emotional_profile.current_mood;

        // Positive interactions boost happiness and confidence
        if memory.success_rating > 0.7 {
            mood.happiness = (mood.happiness + 0.1).min(1.0);
            mood.confidence = (mood.confidence + 0.05).min(1.0);
            mood.anxiety = (mood.anxiety - 0.05).max(0.0);
        }
        // Negative interactions reduce happiness and confidence
        else if memory.success_rating < 0.3 {
            mood.happiness = (mood.happiness - 0.05).max(0.0);
            mood.confidence = (mood.confidence - 0.03).max(0.0);
            mood.anxiety = (mood.anxiety + 0.03).min(1.0);
        }

        // Store mood history
        self.emotional_profile.recent_moods.push((Utc::now(), mood.clone()));
        if self.emotional_profile.recent_moods.len() > 10 {
            self.emotional_profile.recent_moods.remove(0);
        }
    }

    fn update_preferences(&mut self, question: &str, response: &str, success_rating: f32) {
        let response_key = response.to_lowercase();
        let current_weight = self.preference_weights.get(&response_key).unwrap_or(&0.5);

        // Increase preference for successful responses
        let new_weight = if success_rating > 0.7 {
            (current_weight + 0.1).min(2.0)
        } else if success_rating < 0.3 {
            (current_weight - 0.05).max(0.1)
        } else {
            *current_weight
        };

        self.preference_weights.insert(response_key, new_weight);

        // Track avoidance patterns
        if success_rating < 0.2 {
            let topic = self.categorize_topic(question);
            if !self.avoidance_topics.contains(&topic) {
                self.avoidance_topics.push(topic);
            }
        }
    }

    fn detect_mood_patterns(&mut self, memory: &InteractionMemory) {
        let topic = &memory.topic_category;

        let pattern = self.mood_patterns.entry(topic.clone()).or_insert(MoodPattern {
            triggers: Vec::new(),
            typical_responses: Vec::new(),
            frequency: 0,
            last_seen: Utc::now(),
        });

        pattern.frequency += 1;
        pattern.last_seen = Utc::now();

        if !pattern.typical_responses.contains(&memory.child_response) {
            pattern.typical_responses.push(memory.child_response.clone());
        }
    }

    fn categorize_topic(&self, question: &str) -> String {
        let question_lower = question.to_lowercase();

        if question_lower.contains("hungry") || question_lower.contains("eat") || question_lower.contains("food") {
            "food".to_string()
        } else if question_lower.contains("feel")
            || question_lower.contains("mood")
            || question_lower.contains("emotion")
        {
            "emotions".to_string()
        } else if question_lower.contains("play") || question_lower.contains("game") || question_lower.contains("fun") {
            "play".to_string()
        } else if question_lower.contains("help") || question_lower.contains("need") {
            "help".to_string()
        } else if question_lower.contains("tired") || question_lower.contains("sleep") {
            "rest".to_string()
        } else {
            "general".to_string()
        }
    }

    fn make_response_gentler(&self, response: &str) -> String {
        if response.ends_with('!') {
            response.trim_end_matches('!').to_string() + "."
        } else if response.contains("No way") {
            "Not right now".to_string()
        } else {
            response.to_string()
        }
    }

    fn make_response_energetic(&self, response: &str) -> String {
        if !response.ends_with('!') && !response.ends_with('?') {
            response.to_string() + "!"
        } else {
            response.to_string()
        }
    }

    fn make_response_subdued(&self, response: &str) -> String {
        response.replace("!", ".").replace("Yay", "Okay")
    }

    fn describe_current_mood(&self) -> String {
        let mood = &self.emotional_profile.current_mood;

        if mood.happiness > 0.8 && mood.energy > 0.7 {
            "Happy and energetic! 😊⚡".to_string()
        } else if mood.anxiety > 0.7 {
            "Feeling a bit anxious 😰".to_string()
        } else if mood.confidence > 0.8 {
            "Confident and ready! 💪".to_string()
        } else if mood.happiness < 0.3 {
            "Feeling subdued 😔".to_string()
        } else {
            "Balanced and calm 😌".to_string()
        }
    }

    fn suggest_interaction_approach(&self) -> String {
        let mood = &self.emotional_profile.current_mood;

        if mood.anxiety > 0.7 {
            "Use gentle, reassuring questions. Avoid complex choices.".to_string()
        } else if mood.energy > 0.8 {
            "Great time for active, engaging questions!".to_string()
        } else if mood.happiness < 0.3 {
            "Keep interactions simple and supportive.".to_string()
        } else {
            "Normal interaction approach works well.".to_string()
        }
    }

    fn calculate_recent_success_rate(&self) -> f32 {
        let recent_interactions: Vec<_> = self.interaction_history.iter().rev().take(20).collect();

        if recent_interactions.is_empty() {
            return 0.5;
        }

        let total_success: f32 = recent_interactions.iter().map(|i| i.success_rating).sum();

        total_success / recent_interactions.len() as f32
    }

    fn get_preferred_topics(&self) -> Vec<String> {
        let mut topic_scores: HashMap<String, f32> = HashMap::new();

        for interaction in &self.interaction_history {
            if interaction.success_rating > 0.7 {
                let entry = topic_scores.entry(interaction.topic_category.clone()).or_insert(0.0);
                *entry += interaction.success_rating;
            }
        }

        let mut topics: Vec<_> = topic_scores.into_iter().collect();
        topics.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());

        topics.into_iter().take(5).map(|(topic, _)| topic).collect()
    }
}

impl Default for EmotionalProfile {
    fn default() -> Self {
        Self {
            current_mood: EmotionalState { happiness: 0.6, energy: 0.5, anxiety: 0.3, confidence: 0.5, curiosity: 0.7 },
            baseline_mood: EmotionalState {
                happiness: 0.6,
                energy: 0.5,
                anxiety: 0.3,
                confidence: 0.5,
                curiosity: 0.7,
            },
            recent_moods: Vec::new(),
            volatility: 0.3,
            preferred_tone: ResponseTone::Adaptive,
        }
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub struct EmotionalInsights {
    pub current_mood_summary: String,
    pub suggested_approach: String,
    pub recent_success_rate: f32,
    pub preferred_topics: Vec<String>,
    pub topics_to_avoid: Vec<String>,
    pub interaction_count: usize,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_mood_adaptation() {
        let mut memory = TinkyMemoryCore::new();

        // Simulate successful interaction
        memory.learn_from_interaction("Are you hungry?", "Yes please!", 0.9);

        assert!(memory.emotional_profile.current_mood.happiness > 0.6);
        assert_eq!(memory.interaction_history.len(), 1);
    }

    #[test]
    fn test_topic_categorization() {
        let memory = TinkyMemoryCore::new();

        assert_eq!(memory.categorize_topic("Are you hungry?"), "food");
        assert_eq!(memory.categorize_topic("How are you feeling?"), "emotions");
        assert_eq!(memory.categorize_topic("Do you want to play?"), "play");
    }
}
