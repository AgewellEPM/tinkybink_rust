use serde::{Deserialize, Serialize};

/// System-wide events that flow through the event bus
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum SystemEvent {
    /// Speech was recognized from user input
    SpeechRecognized { text: String, confidence: f32 },

    /// TTS started speaking text
    SpeechStarted { text: String },

    /// TTS finished speaking
    SpeechFinished { text: String },

    /// User selected a suggestion tile
    TileSelected { tile: SuggestionTile },

    /// Action on the speech buffer
    SpeechBufferAction { action: SpeechBufferAction },

    /// UI-related action
    UIAction { action: UIAction },

    /// System shutdown requested
    Shutdown,
}

/// Actions that can be performed on the speech buffer
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum SpeechBufferAction {
    Clear,
    Speak,
    Save,
}

/// UI-related actions
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum UIAction {
    ToggleListening,
    BackToDefault,
    ShowSettings,
}

/// Represents a suggestion tile with emoji and text
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SuggestionTile {
    pub emoji: String,
    pub text: String,
    pub category: TileCategory,
    pub confidence: f32,
}

/// Categories for suggestion tiles
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
#[derive(Default)]
pub enum TileCategory {
    BasicResponse,
    Choice,
    Emotion,
    Action,
    Object,
    Place,
    Time,
    Food,
    Person,
    Question,
    #[default]
    Default,
}

