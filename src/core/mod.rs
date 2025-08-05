use anyhow::Result;
use std::sync::Arc;
use tokio::sync::{mpsc, RwLock};
use tracing::{debug, info, warn};
use uuid::Uuid;

pub mod events;
pub mod state;

use crate::speech::SpeechManager;
use crate::suggestions::SuggestionEngine;
use crate::ui::UIManager;
use crate::storage::StorageManager;

pub use events::*;
pub use state::*;

/// Main system orchestrating all AAC components
pub struct TinkyBinkSystem {
    state: Arc<RwLock<SystemState>>,
    speech_manager: SpeechManager,
    suggestion_engine: SuggestionEngine,
    ui_manager: UIManager,
    storage_manager: StorageManager,
    event_tx: mpsc::UnboundedSender<SystemEvent>,
    event_rx: mpsc::UnboundedReceiver<SystemEvent>,
}

impl TinkyBinkSystem {
    pub async fn new() -> Result<Self> {
        info!("Initializing TinkyBink AAC System...");
        
        let (event_tx, event_rx) = mpsc::unbounded_channel();
        let state = Arc::new(RwLock::new(SystemState::default()));
        
        // Initialize subsystems
        let storage_manager = StorageManager::new("tinkybink_data").await?;
        let suggestion_engine = SuggestionEngine::new();
        let speech_manager = SpeechManager::new(event_tx.clone()).await?;
        let ui_manager = UIManager::new(event_tx.clone()).await?;
        
        info!("All subsystems initialized successfully");
        
        Ok(Self {
            state,
            speech_manager,
            suggestion_engine,
            ui_manager,
            storage_manager,
            event_tx,
            event_rx,
        })
    }
    
    pub async fn run(&mut self, headless: bool) -> Result<()> {
        info!("Starting TinkyBink AAC System (headless: {})", headless);
        
        // Load saved state
        if let Ok(saved_state) = self.storage_manager.load_state().await {
            *self.state.write().await = saved_state;
            info!("Loaded saved state");
        }
        
        // Start subsystems
        self.speech_manager.start().await?;
        
        if !headless {
            self.ui_manager.start().await?;
        }
        
        // Main event loop
        self.event_loop().await?;
        
        Ok(())
    }
    
    async fn event_loop(&mut self) -> Result<()> {
        info!("Starting main event loop");
        
        while let Some(event) = self.event_rx.recv().await {
            debug!("Processing event: {:?}", event);
            
            match event {
                SystemEvent::SpeechRecognized { text, confidence } => {
                    self.handle_speech_input(text, confidence).await?;
                },
                SystemEvent::SpeechStarted { text } => {
                    debug!("Speech started: '{}'", text);
                    // Update UI to show speaking state if needed
                },
                SystemEvent::SpeechFinished { text } => {
                    debug!("Speech finished: '{}'", text);
                    // Update UI to show speech completed if needed
                },
                SystemEvent::TileSelected { tile } => {
                    self.handle_tile_selection(tile).await?;
                },
                SystemEvent::SpeechBufferAction { action } => {
                    self.handle_speech_buffer_action(action).await?;
                },
                SystemEvent::UIAction { action } => {
                    self.handle_ui_action(action).await?;
                },
                SystemEvent::Shutdown => {
                    info!("Received shutdown event");
                    break;
                },
            }
            
            // Save state periodically
            if let Err(e) = self.storage_manager.save_state(&*self.state.read().await).await {
                warn!("Failed to save state: {}", e);
            }
        }
        
        Ok(())
    }
    
    async fn handle_speech_input(&mut self, text: String, confidence: f32) -> Result<()> {
        info!("Processing speech input: '{}' (confidence: {:.2})", text, confidence);
        
        // Add to conversation history
        {
            let mut state = self.state.write().await;
            let message = ChatMessage {
                id: Uuid::new_v4(),
                content: text.clone(),
                message_type: MessageType::Heard,
                timestamp: chrono::Utc::now(),
                confidence: Some(confidence),
            };
            state.conversation_history.push(message);
        }
        
        // Generate suggestions
        let suggestions = self.suggestion_engine.generate_suggestions(&text).await?;
        
        // Update UI with suggestions
        self.ui_manager.update_suggestions(suggestions).await?;
        
        Ok(())
    }
    
    async fn handle_tile_selection(&mut self, tile: SuggestionTile) -> Result<()> {
        info!("Tile selected: {} {}", tile.emoji, tile.text);
        
        // Add to speech buffer
        {
            let mut state = self.state.write().await;
            state.speech_buffer.push(tile.text.clone());
        }
        
        // Add to conversation as spoken
        {
            let mut state = self.state.write().await;
            let message = ChatMessage {
                id: Uuid::new_v4(),
                content: format!("{} {}", tile.emoji, tile.text),
                message_type: MessageType::Spoken,
                timestamp: chrono::Utc::now(),
                confidence: None,
            };
            state.conversation_history.push(message);
        }
        
        // Speak the text
        self.speech_manager.speak(&tile.text).await?;
        
        // Update UI
        self.ui_manager.update_chat_history(&*self.state.read().await).await?;
        self.ui_manager.update_speech_buffer(&*self.state.read().await).await?;
        
        Ok(())
    }
    
    async fn handle_speech_buffer_action(&mut self, action: SpeechBufferAction) -> Result<()> {
        match action {
            SpeechBufferAction::Clear => {
                self.state.write().await.speech_buffer.clear();
                info!("Speech buffer cleared");
            },
            SpeechBufferAction::Speak => {
                let buffer = self.state.read().await.speech_buffer.join(" ");
                if !buffer.is_empty() {
                    self.speech_manager.speak(&buffer).await?;
                    info!("Speaking buffer contents: {}", buffer);
                }
            },
            SpeechBufferAction::Save => {
                let buffer = self.state.read().await.speech_buffer.join(" ");
                if !buffer.is_empty() {
                    self.storage_manager.save_phrase(&buffer).await?;
                    info!("Saved phrase: {}", buffer);
                }
            },
        }
        
        self.ui_manager.update_speech_buffer(&*self.state.read().await).await?;
        Ok(())
    }
    
    async fn handle_ui_action(&mut self, _action: UIAction) -> Result<()> {
        // Handle UI-specific actions
        Ok(())
    }
}