use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use uuid::Uuid;

/// System-wide state
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SystemState {
    pub conversation_history: Vec<ChatMessage>,
    pub speech_buffer: Vec<String>,
    pub current_suggestions: Vec<crate::core::events::SuggestionTile>,
    pub is_listening: bool,
    pub settings: UserSettings,
    pub session_id: Uuid,
    pub created_at: DateTime<Utc>,
}

impl Default for SystemState {
    fn default() -> Self {
        Self {
            conversation_history: Vec::new(),
            speech_buffer: Vec::new(),
            current_suggestions: Vec::new(),
            is_listening: false,
            settings: UserSettings::default(),
            session_id: Uuid::new_v4(),
            created_at: Utc::now(),
        }
    }
}

/// Chat message in conversation history
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ChatMessage {
    pub id: Uuid,
    pub content: String,
    pub message_type: MessageType,
    pub timestamp: DateTime<Utc>,
    pub confidence: Option<f32>,
}

/// Type of chat message
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum MessageType {
    Heard,   // Input from speech recognition
    Spoken,  // Output from AAC tiles
    System,  // System messages
}

/// User preferences and settings
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UserSettings {
    pub font_scale: f32,
    pub tile_scale: f32,
    pub emoji_scale: f32,
    pub speech_rate: f32,
    pub speech_pitch: f32,
    pub speech_volume: f32,
    pub language: String,
    pub auto_save_phrases: bool,
    pub suggestion_mode: SuggestionMode,
    pub theme: UITheme,
}

impl Default for UserSettings {
    fn default() -> Self {
        Self {
            font_scale: 1.0,
            tile_scale: 1.0,
            emoji_scale: 1.0,
            speech_rate: 1.0,
            speech_pitch: 1.0,
            speech_volume: 1.0,
            language: "en-US".to_string(),
            auto_save_phrases: true,
            suggestion_mode: SuggestionMode::Contextual,
            theme: UITheme::Dark,
        }
    }
}

/// How suggestions are generated
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum SuggestionMode {
    Static,      // Fixed set of tiles
    Contextual,  // Context-aware Eliza-like suggestions
    Learning,    // Adaptive based on usage patterns
}

/// UI theme options
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum UITheme {
    Dark,
    Light,
    HighContrast,
}