//! 🌐 WASM-specific implementation of TinkyBink AAC
//! 
//! This module provides browser-compatible implementations without tokio dependencies

#[cfg(feature = "wasm")]
use wasm_bindgen::prelude::*;

#[cfg(feature = "wasm")]
use web_sys::{console, window, SpeechSynthesis, SpeechSynthesisUtterance};

#[cfg(feature = "wasm")]
use crate::suggestions::SuggestionEngine;
#[cfg(feature = "wasm")]
use crate::memory::TinkyMemoryCore;

/// 🧠 WASM-Exposed TinkyBink Engine for browser integration
#[cfg(feature = "wasm")]
#[wasm_bindgen]
pub struct TinkyBinkWasm {
    engine: SuggestionEngine,
    memory_core: TinkyMemoryCore,
    speech_synthesis: Option<SpeechSynthesis>,
}

#[cfg(feature = "wasm")]
#[wasm_bindgen]
impl TinkyBinkWasm {
    /// 🚀 Create new TinkyBink instance for browser
    #[wasm_bindgen(constructor)]
    pub fn new() -> Result<TinkyBinkWasm, JsValue> {
        console::log_1(&"🧠 Initializing TinkyBink AAC Engine...".into());
        
        let engine = SuggestionEngine::new();
        let memory_core = TinkyMemoryCore::new();
        
        // Initialize browser speech synthesis
        let speech_synthesis = window()
            .and_then(|w| w.speech_synthesis().ok());
            
        if speech_synthesis.is_some() {
            console::log_1(&"🔊 Browser speech synthesis available!".into());
        } else {
            console::log_1(&"🔇 Speech synthesis not available in this browser".into());
        }
        
        console::log_1(&"✅ TinkyBink AAC Engine ready for revolutionary communication!".into());
        
        Ok(TinkyBinkWasm {
            engine,
            memory_core,
            speech_synthesis,
        })
    }
    
    /// 🗣️ Speak text using browser speech synthesis
    #[wasm_bindgen]
    pub fn speak(&self, text: &str) -> Result<(), JsValue> {
        if let Some(ref speech_synth) = self.speech_synthesis {
            console::log_1(&format!("🗣️ Speaking: '{}'", text).into());
            
            let utterance = SpeechSynthesisUtterance::new_with_text(text)?;
            
            // Configure for child-like voice
            utterance.set_rate(0.9);
            utterance.set_pitch(1.2);
            utterance.set_volume(1.0);
            
            speech_synth.speak(&utterance);
            Ok(())
        } else {
            Err(JsValue::from_str("Speech synthesis not available"))
        }
    }
    
    /// 🧠 Record interaction for emotional learning
    #[wasm_bindgen]
    pub fn record_interaction(&mut self, question: &str, response: &str, success_rating: f32) {
        console::log_1(&format!("🧠 Learning from: '{}' → '{}' ({})", question, response, success_rating).into());
        self.memory_core.learn_from_interaction(question, response, success_rating);
    }
    
    /// 📊 Get emotional intelligence insights as JSON string
    #[wasm_bindgen]
    pub fn get_insights(&self) -> String {
        let insights = self.memory_core.get_emotional_insights();
        serde_json::to_string(&insights).unwrap_or_else(|_| "{}".to_string())
    }
    
    /// 🎯 Check if topic should be avoided
    #[wasm_bindgen]
    pub fn should_avoid_topic(&self, question: &str) -> bool {
        self.memory_core.should_avoid_topic(question)
    }
    
    /// 🔊 Check if speech synthesis is available
    #[wasm_bindgen]
    pub fn can_speak(&self) -> bool {
        self.speech_synthesis.is_some()
    }
}

/// 🌐 Create HTML interface for TinkyBink AAC
#[cfg(feature = "wasm")]
#[wasm_bindgen]
pub fn create_tinky_interface() -> Result<(), JsValue> {
    let window = window().ok_or("No global `window` exists")?;
    let document = window.document().ok_or("Should have a document on window")?;
    let body = document.body().ok_or("Document should have a body")?;
    
    // Create revolutionary TinkyBink interface
    let html = r#"
    <div id="tinky-container" style="
        font-family: 'Comic Sans MS', cursive;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        color: white;
        text-align: center;
    ">
        <h1 style="font-size: 2.5em; margin-bottom: 10px;">
            🧠🗣️ TinkyBink AAC
        </h1>
        <p style="font-size: 1.2em; margin-bottom: 30px;">
            Revolutionary Emotionally Intelligent Communication System
        </p>
        
        <div id="input-section" style="margin-bottom: 30px;">
            <input type="text" id="user-input" placeholder="Type your question here..." style="
                width: 70%;
                padding: 15px;
                font-size: 1.1em;
                border: none;
                border-radius: 25px;
                margin-right: 10px;
                font-family: inherit;
            ">
            <button id="ask-btn" style="
                padding: 15px 25px;
                font-size: 1.1em;
                background: #ff6b6b;
                color: white;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                font-family: inherit;
                font-weight: bold;
            ">Ask! 🚀</button>
        </div>
        
        <div id="suggestions-container" style="
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        "></div>
        
        <div id="insights-panel" style="
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            text-align: left;
            display: none;
        ">
            <h3>🧠 Emotional Intelligence Insights</h3>
            <div id="insights-content"></div>
        </div>
        
        <div style="margin-top: 20px;">
            <button id="insights-btn" style="
                padding: 10px 20px;
                background: rgba(255,255,255,0.2);
                color: white;
                border: 1px solid rgba(255,255,255,0.3);
                border-radius: 20px;
                cursor: pointer;
                font-family: inherit;
                margin-right: 10px;
            ">📊 Show Insights</button>
            
            <button id="voice-toggle" style="
                padding: 10px 20px;
                background: rgba(255,255,255,0.2);
                color: white;
                border: 1px solid rgba(255,255,255,0.3);
                border-radius: 20px;
                cursor: pointer;
                font-family: inherit;
            ">🔊 Voice: ON</button>
        </div>
        
        <div style="margin-top: 30px; font-size: 0.9em; opacity: 0.8;">
            🌟 Features: Emotional Learning • Voice Synthesis • Adaptive Intelligence • Child-Friendly Responses
        </div>
    </div>
    "#;
    
    body.set_inner_html(html);
    
    console::log_1(&"🎨 Revolutionary TinkyBink AAC interface created!".into());
    Ok(())
}