//! 🧠🌐 TinkyBink AAC - Revolutionary WASM-Powered Communication System
//! 
//! World's first emotionally intelligent AAC system that runs in browsers
//! with full speech synthesis, recognition, and adaptive learning capabilities.

#[cfg(feature = "wasm")]
use wasm_bindgen::prelude::*;

pub mod core;
pub mod speech;
pub mod suggestions;
pub mod ui;
pub mod storage;
pub mod utils;
pub mod memory;
pub mod ai;

#[cfg(feature = "wasm")]
pub mod wasm;

// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

// Export the main entry point for non-WASM builds
#[cfg(not(feature = "wasm"))]
pub fn main() {
    println!("🧠 TinkyBink AAC - Use 'cargo run demo' for interactive mode");
    println!("📦 Or build with --features wasm for browser deployment");
}