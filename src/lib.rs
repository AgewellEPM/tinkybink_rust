#![allow(clippy::needless_borrow)]
#![allow(clippy::needless_range_loop)]
#![allow(clippy::let_and_return)]
#![allow(clippy::uninlined_format_args)]

//! 🧠🌐 TinkyBink AAC - Revolutionary WASM-Powered Communication System
//!
//! World's first emotionally intelligent AAC system that runs in browsers
//! with full speech synthesis, recognition, and adaptive learning capabilities.

#![allow(dead_code)]

pub mod ai;
pub mod comprehensive_brain_loader;
pub mod conversation_logic;
pub mod core;
pub mod memory;
pub mod speech;
pub mod storage;
pub mod suggestions;
pub mod training_loader;
pub mod ui;
pub mod utils;

#[cfg(feature = "wasm")]
pub mod wasm;

use conversation_logic::ConversationLogicSystem;
use std::path::Path;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
// #[cfg(feature = "wee_alloc")]
// #[global_allocator]
// static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

/// Main TinkyBink AAC system
pub struct TinkyBinkAAC {
    conversation_system: ConversationLogicSystem,
}

impl Default for TinkyBinkAAC {
    fn default() -> Self {
        Self::new()
    }
}

impl TinkyBinkAAC {
    /// Create a new TinkyBink AAC system
    pub fn new() -> Self {
        Self { conversation_system: ConversationLogicSystem::new() }
    }

    /// Load training data from JSONL file
    pub fn load_training_data(&mut self, file_path: &Path) -> Result<usize, Box<dyn std::error::Error>> {
        let loaded = training_loader::load_training_data(&mut self.conversation_system, file_path)?;

        // Build connections after loading
        training_loader::build_conversation_connections(&mut self.conversation_system);

        Ok(loaded)
    }

    /// Get conversation starters
    pub fn get_starters(&self, category: Option<&str>) -> Vec<ConversationResponse> {
        self.conversation_system
            .get_starters(category)
            .into_iter()
            .map(|node| ConversationResponse {
                input: node.input.clone(),
                tiles: node.tiles.iter().map(|t| Tile { emoji: t.emoji.clone(), words: t.words.clone() }).collect(),
            })
            .collect()
    }

    /// Process user selection and get follow-up responses
    pub fn process_selection(&self, current_node_id: &str, selected_tile: &str) -> Vec<ConversationResponse> {
        self.conversation_system
            .get_follow_ups(current_node_id, selected_tile)
            .into_iter()
            .map(|node| ConversationResponse {
                input: node.input.clone(),
                tiles: node.tiles.iter().map(|t| Tile { emoji: t.emoji.clone(), words: t.words.clone() }).collect(),
            })
            .collect()
    }
}

/// Response structure for the UI
#[derive(Debug, Clone)]
pub struct ConversationResponse {
    pub input: String,
    pub tiles: Vec<Tile>,
}

#[derive(Debug, Clone)]
pub struct Tile {
    pub emoji: String,
    pub words: String,
}

// Export the main entry point for non-WASM builds
#[cfg(not(feature = "wasm"))]
pub fn main() {
    println!("🧠 TinkyBink AAC - Use 'cargo run demo' for interactive mode");
    println!("📦 Or build with --features wasm for browser deployment");
}
