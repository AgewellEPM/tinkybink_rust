#![allow(clippy::needless_range_loop)]
#![allow(clippy::uninlined_format_args)]
//! 🧠💥 GPT-Infused Small Model Core
//!
//! Give ANY small model GPT-like intelligence through:
//! - Causal attention flow
//! - Token prediction
//! - Context windows
//! - Emotional mapping

#![allow(dead_code)]

// use anyhow::Result;
use std::collections::VecDeque;

/// 🧠 GPT-Like Core for Small Models
pub struct GPTCore {
    /// Conversation memory buffer
    conversation_buffer: VecDeque<String>,
    /// Maximum context window (in turns)
    max_context: usize,
    /// Current emotional state
    emotional_state: EmotionalState,
    /// Token prediction engine
    predictor: TokenPredictor,
    /// Attention mechanism
    attention: MultiHeadAttention,
}

impl Default for GPTCore {
    fn default() -> Self {
        Self::new()
    }
}

impl GPTCore {
    pub fn new() -> Self {
        Self {
            conversation_buffer: VecDeque::with_capacity(10),
            max_context: 4, // Keep last 4 conversation turns
            emotional_state: EmotionalState::default(),
            predictor: TokenPredictor::new(),
            attention: MultiHeadAttention::new(4), // 4 attention heads even for small model
        }
    }

    /// 🔮 GPT-like prediction with causal attention
    pub fn gpt_like_predict(&mut self, input: &str) -> String {
        // 1. Tokenize input
        let tokens = self.tokenize(input);

        // 2. Add positional encoding
        let positioned = self.add_positional_encoding(&tokens);

        // 3. Apply multi-head attention (causal mask)
        let attended = self.attention.apply_causal(&positioned);

        // 4. Predict next tokens
        let predicted = self.predictor.predict_next(&attended);

        // 5. Decode back to text
        self.decode(&predicted)
    }

    /// 💾 Inject GPT memory behavior
    pub fn update_memory(&mut self, user_input: &str, bot_response: &str) {
        // Add to conversation buffer
        self.conversation_buffer.push_back(format!("User: {user_input}"));
        self.conversation_buffer.push_back(format!("TinkyBink: {bot_response}"));

        // Maintain rolling window
        while self.conversation_buffer.len() > self.max_context * 2 {
            self.conversation_buffer.pop_front();
        }
    }

    /// 🎭 Get context-aware prompt
    pub fn build_gpt_prompt(&self, new_input: &str) -> String {
        let mut prompt = String::new();

        // Add conversation history
        for turn in &self.conversation_buffer {
            prompt.push_str(turn);
            prompt.push('\n');
        }

        // Add emotional context
        prompt.push_str(&format!("[Emotional State: {}]\n", self.emotional_state));

        // Add new input
        prompt.push_str(&format!("User: {new_input}\nTinkyBink:"));

        prompt
    }

    /// 🧬 Inject emotional GPT logic
    pub fn apply_emotional_intelligence(&mut self, input: &str) -> Vec<EmotionalResponse> {
        let emotion = self.detect_emotion(input);
        self.emotional_state = emotion.clone();

        match emotion {
            EmotionalState::Sad => vec![
                EmotionalResponse::new("I'm sorry you're feeling that way 💙", 0.9),
                EmotionalResponse::new("Want to talk about it? 🤗", 0.8),
                EmotionalResponse::new("That must be really hard 😔", 0.7),
                EmotionalResponse::new("I'm here for you 🫂", 0.6),
            ],
            EmotionalState::Happy => vec![
                EmotionalResponse::new("That's wonderful! 🎉", 0.9),
                EmotionalResponse::new("Yay! So happy for you! 😊", 0.8),
                EmotionalResponse::new("Amazing news! ⭐", 0.7),
                EmotionalResponse::new("Let's celebrate! 🎊", 0.6),
            ],
            EmotionalState::Anxious => vec![
                EmotionalResponse::new("Take a deep breath 🌊", 0.9),
                EmotionalResponse::new("You're safe here 🏠", 0.8),
                EmotionalResponse::new("One step at a time 👣", 0.7),
                EmotionalResponse::new("It's okay to feel this way 💚", 0.6),
            ],
            EmotionalState::Angry => vec![
                EmotionalResponse::new("I understand you're upset 🫶", 0.9),
                EmotionalResponse::new("That sounds frustrating 😤", 0.8),
                EmotionalResponse::new("Your feelings are valid ✨", 0.7),
                EmotionalResponse::new("Let's work through this 🤝", 0.6),
            ],
            _ => vec![
                EmotionalResponse::new("I hear you 👂", 0.7),
                EmotionalResponse::new("Tell me more 💭", 0.6),
                EmotionalResponse::new("I'm listening 🎧", 0.5),
                EmotionalResponse::new("Go on... 💬", 0.4),
            ],
        }
    }

    fn tokenize(&self, text: &str) -> Vec<Token> {
        // Simple word-based tokenization for now
        text.split_whitespace().map(|word| Token::new(word.to_string())).collect()
    }

    fn add_positional_encoding(&self, tokens: &[Token]) -> Vec<PositionedToken> {
        tokens
            .iter()
            .enumerate()
            .map(|(pos, token)| PositionedToken {
                token: token.clone(),
                position: pos,
                encoding: self.calculate_position_encoding(pos),
            })
            .collect()
    }

    fn calculate_position_encoding(&self, position: usize) -> f32 {
        // Simplified sinusoidal encoding
        (position as f32 / 10000.0).sin()
    }

    fn decode(&self, tokens: &[Token]) -> String {
        tokens.iter().map(|t| t.text.clone()).collect::<Vec<_>>().join(" ")
    }

    fn detect_emotion(&self, text: &str) -> EmotionalState {
        let lower = text.to_lowercase();

        if lower.contains("sad") || lower.contains("cry") || lower.contains("hurt") {
            EmotionalState::Sad
        } else if lower.contains("happy") || lower.contains("joy") || lower.contains("excited") {
            EmotionalState::Happy
        } else if lower.contains("angry") || lower.contains("mad") || lower.contains("furious") {
            EmotionalState::Angry
        } else if lower.contains("worried") || lower.contains("anxious") || lower.contains("scared") {
            EmotionalState::Anxious
        } else {
            EmotionalState::Neutral
        }
    }
}

/// 🎯 Multi-Head Attention mechanism
pub struct MultiHeadAttention {
    #[allow(dead_code)]
    num_heads: usize,
}

impl MultiHeadAttention {
    pub fn new(num_heads: usize) -> Self {
        Self { num_heads }
    }

    pub fn apply_causal(&self, tokens: &[PositionedToken]) -> Vec<Token> {
        // Simplified causal attention (masks future tokens)
        let mut attended = Vec::new();

        for i in 0..tokens.len() {
            // Only attend to previous tokens (causal mask)
            let context = &tokens[..=i];

            // Compute attention weights (simplified)
            let weights = self.compute_attention_weights(context);

            // Apply attention
            let attended_token = self.apply_attention(&tokens[i].token, &weights);
            attended.push(attended_token);
        }

        attended
    }

    fn compute_attention_weights(&self, context: &[PositionedToken]) -> Vec<f32> {
        // Simplified attention weights
        context.iter().map(|_t| 1.0 / context.len() as f32).collect()
    }

    fn apply_attention(&self, token: &Token, _weights: &[f32]) -> Token {
        // For now, just return the token
        // In a real implementation, this would transform based on attention
        token.clone()
    }
}

/// 🔮 Token Predictor
pub struct TokenPredictor {
    #[allow(dead_code)]
    vocabulary: Vec<String>,
}

impl Default for TokenPredictor {
    fn default() -> Self {
        Self::new()
    }
}

impl TokenPredictor {
    pub fn new() -> Self {
        Self {
            vocabulary: vec![
                "yes".to_string(),
                "no".to_string(),
                "maybe".to_string(),
                "happy".to_string(),
                "sad".to_string(),
                "hungry".to_string(),
                "tired".to_string(),
                "play".to_string(),
                "help".to_string(),
                "love".to_string(),
            ],
        }
    }

    pub fn predict_next(&self, context: &[Token]) -> Vec<Token> {
        // Simplified next-token prediction
        // In reality, this would use the model's learned weights

        if context.is_empty() {
            return vec![Token::new("hello".to_string())];
        }

        let last_token = &context[context.len() - 1];

        // Simple pattern matching for demonstration
        match last_token.text.as_str() {
            "are" => vec![Token::new("you".to_string())],
            "you" => vec![Token::new("okay".to_string())],
            "feel" => vec![Token::new("happy".to_string())],
            _ => vec![Token::new("yes".to_string())],
        }
    }
}

/// Token representation
#[derive(Clone, Debug)]
pub struct Token {
    pub text: String,
    #[allow(dead_code)]
    pub id: usize,
}

impl Token {
    pub fn new(text: String) -> Self {
        Self {
            id: text.len(), // Simplified token ID
            text,
        }
    }
}

/// Token with positional encoding
#[derive(Clone, Debug)]
pub struct PositionedToken {
    pub token: Token,
    #[allow(dead_code)]
    pub position: usize,
    #[allow(dead_code)]
    pub encoding: f32,
}

/// Emotional states
#[derive(Clone, Debug, Default)]
pub enum EmotionalState {
    Happy,
    Sad,
    Angry,
    Anxious,
    Excited,
    #[default]
    Neutral,
}

impl std::fmt::Display for EmotionalState {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            EmotionalState::Happy => write!(f, "😊 Happy"),
            EmotionalState::Sad => write!(f, "😢 Sad"),
            EmotionalState::Angry => write!(f, "😠 Angry"),
            EmotionalState::Anxious => write!(f, "😰 Anxious"),
            EmotionalState::Excited => write!(f, "🎉 Excited"),
            EmotionalState::Neutral => write!(f, "😐 Neutral"),
        }
    }
}

/// Emotional response with confidence
pub struct EmotionalResponse {
    pub text: String,
    pub confidence: f32,
}

impl EmotionalResponse {
    pub fn new(text: &str, confidence: f32) -> Self {
        Self { text: text.to_string(), confidence }
    }
}

/// 🚀 Build an offline GPT-like system
pub struct OfflineGPT {
    core: GPTCore,
    tile_decoder: TileBasedDecoder,
}

impl Default for OfflineGPT {
    fn default() -> Self {
        Self::new()
    }
}

impl OfflineGPT {
    pub fn new() -> Self {
        Self { core: GPTCore::new(), tile_decoder: TileBasedDecoder::new() }
    }

    /// Generate GPT-like response for AAC
    pub fn generate_aac_response(&mut self, input: &str) -> Vec<AACTile> {
        // 1. Build GPT-style prompt with context
        let prompt = self.core.build_gpt_prompt(input);

        // 2. Apply emotional intelligence
        let emotional_responses = self.core.apply_emotional_intelligence(input);

        // 3. Generate prediction
        let prediction = self.core.gpt_like_predict(&prompt);

        // 4. Update memory
        self.core.update_memory(input, &prediction);

        // 5. Convert to AAC tiles
        self.tile_decoder.decode_to_tiles(&prediction, emotional_responses)
    }
}

/// Tile-based decoder for AAC
pub struct TileBasedDecoder;

impl Default for TileBasedDecoder {
    fn default() -> Self {
        Self::new()
    }
}

impl TileBasedDecoder {
    pub fn new() -> Self {
        Self
    }

    pub fn decode_to_tiles(&self, _text: &str, emotions: Vec<EmotionalResponse>) -> Vec<AACTile> {
        emotions
            .into_iter()
            .map(|emotion| AACTile {
                emoji: self.get_emoji_for_text(&emotion.text),
                text: emotion.text,
                confidence: emotion.confidence,
            })
            .collect()
    }

    fn get_emoji_for_text(&self, text: &str) -> String {
        let lower = text.to_lowercase();

        if lower.contains("happy") || lower.contains("yay") {
            "😊".to_string()
        } else if lower.contains("sad") || lower.contains("sorry") {
            "😢".to_string()
        } else if lower.contains("love") || lower.contains("heart") {
            "❤️".to_string()
        } else if lower.contains("help") {
            "🆘".to_string()
        } else if lower.contains("yes") || lower.contains("okay") {
            "✅".to_string()
        } else if lower.contains("no") {
            "❌".to_string()
        } else {
            "💭".to_string()
        }
    }
}

#[derive(Debug)]
pub struct AACTile {
    pub emoji: String,
    pub text: String,
    pub confidence: f32,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gpt_core() {
        let mut gpt = GPTCore::new();

        // Test prediction
        let response = gpt.gpt_like_predict("How are you");
        assert!(!response.is_empty());

        // Test memory
        gpt.update_memory("How are you?", "I'm doing well!");
        let prompt = gpt.build_gpt_prompt("What about you?");
        assert!(prompt.contains("How are you?"));
        assert!(prompt.contains("I'm doing well!"));
    }

    #[test]
    fn test_emotional_intelligence() {
        let mut gpt = GPTCore::new();

        let responses = gpt.apply_emotional_intelligence("I feel so sad today");
        assert!(!responses.is_empty());
        assert!(responses[0].text.contains("sorry") || responses[0].text.contains("hard"));
    }

    #[test]
    fn test_offline_gpt() {
        let mut offline_gpt = OfflineGPT::new();

        let tiles = offline_gpt.generate_aac_response("Are you hungry?");
        assert_eq!(tiles.len(), 4); // Should generate 4 tile options
        assert!(!tiles[0].emoji.is_empty());
    }
}
