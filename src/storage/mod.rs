use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::path::PathBuf;
use tokio::fs;
use tracing::{info, warn};

use crate::core::state::SystemState;

/// Storage manager for persistence of state, phrases, and settings
pub struct StorageManager {
    data_dir: PathBuf,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SavedPhrase {
    pub id: String,
    pub text: String,
    pub timestamp: DateTime<Utc>,
    pub usage_count: u32,
}

impl StorageManager {
    pub async fn new(data_dir_name: &str) -> Result<Self> {
        let data_dir = Self::get_data_directory(data_dir_name)?;

        // Ensure data directory exists
        fs::create_dir_all(&data_dir).await?;

        info!(
            "Storage manager initialized with data directory: {:?}",
            data_dir
        );

        Ok(Self { data_dir })
    }

    pub async fn save_state(&self, state: &SystemState) -> Result<()> {
        let state_file = self.data_dir.join("state.json");
        let json = serde_json::to_string_pretty(state)?;
        fs::write(state_file, json).await?;
        Ok(())
    }

    pub async fn load_state(&self) -> Result<SystemState> {
        let state_file = self.data_dir.join("state.json");

        if !state_file.exists() {
            return Ok(SystemState::default());
        }

        let json = fs::read_to_string(state_file).await?;
        let state = serde_json::from_str(&json)?;
        Ok(state)
    }

    pub async fn save_phrase(&self, text: &str) -> Result<()> {
        let phrases_file = self.data_dir.join("saved_phrases.json");

        // Load existing phrases
        let mut phrases = self.load_phrases().await.unwrap_or_default();

        // Add new phrase
        let phrase = SavedPhrase {
            id: uuid::Uuid::new_v4().to_string(),
            text: text.to_string(),
            timestamp: Utc::now(),
            usage_count: 1,
        };

        phrases.push(phrase);

        // Keep only last 100 phrases
        if phrases.len() > 100 {
            phrases.drain(0..phrases.len() - 100);
        }

        // Save back to file
        let json = serde_json::to_string_pretty(&phrases)?;
        fs::write(phrases_file, json).await?;

        info!("Saved phrase: '{}'", text);
        Ok(())
    }

    pub async fn load_phrases(&self) -> Result<Vec<SavedPhrase>> {
        let phrases_file = self.data_dir.join("saved_phrases.json");

        if !phrases_file.exists() {
            return Ok(Vec::new());
        }

        let json = fs::read_to_string(phrases_file).await?;
        let phrases = serde_json::from_str(&json)?;
        Ok(phrases)
    }

    pub async fn export_conversation_history(
        &self,
        state: &SystemState,
        format: ExportFormat,
    ) -> Result<String> {
        let timestamp = Utc::now().format("%Y%m%d_%H%M%S");
        let filename = match format {
            ExportFormat::Json => format!("conversation_history_{timestamp}.json"),
            ExportFormat::Csv => format!("conversation_history_{timestamp}.csv"),
            ExportFormat::Txt => format!("conversation_history_{timestamp}.txt"),
        };

        let export_file = self.data_dir.join(&filename);

        match format {
            ExportFormat::Json => {
                let json = serde_json::to_string_pretty(&state.conversation_history)?;
                fs::write(&export_file, json).await?;
            }
            ExportFormat::Csv => {
                // TODO: Implement CSV export
                warn!("CSV export not yet implemented");
            }
            ExportFormat::Txt => {
                let mut content = String::new();
                for message in &state.conversation_history {
                    content.push_str(&format!(
                        "[{}] {}: {}\n",
                        message.timestamp.format("%Y-%m-%d %H:%M:%S"),
                        match message.message_type {
                            crate::core::state::MessageType::Heard => "HEARD",
                            crate::core::state::MessageType::Spoken => "SPOKEN",
                            crate::core::state::MessageType::System => "SYSTEM",
                        },
                        message.content
                    ));
                }
                fs::write(&export_file, content).await?;
            }
        }

        info!("Exported conversation history to: {:?}", export_file);
        Ok(filename)
    }

    fn get_data_directory(name: &str) -> Result<PathBuf> {
        let home = std::env::var("HOME")
            .ok()
            .map(std::path::PathBuf::from)
            .ok_or_else(|| anyhow::anyhow!("Could not find home directory"))?;
        Ok(home.join(".local").join("share").join(name))
    }
}

#[derive(Debug, Clone)]
pub enum ExportFormat {
    Json,
    Csv,
    Txt,
}
