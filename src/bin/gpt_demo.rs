//! 🚀 GPT-Infused TinkyBink Demo
//!
//! Demonstrates the complete GPT architecture with:
//! - Causal attention flow
//! - Emotional intelligence
//! - Conversation memory
//! - 4,000+ pattern matching

use tinkybink_rust::ai::gpt_core::{GPTCore, OfflineGPT};
use tinkybink_rust::ai::nano_gpt::{ModelSize, NanoGPT, TinkyGPT};
use tinkybink_rust::ai::{AiContext, AiEngine};

#[tokio::main]
async fn main() {
    println!("🧠💥 TinkyBink GPT-Infused AAC Demo");
    println!("=====================================\n");

    // Demo 1: GPT Core with Emotional Intelligence
    println!("📍 Demo 1: GPT Core Emotional Intelligence");
    println!("------------------------------------------");
    demo_gpt_core().await;

    println!("\n📍 Demo 2: NanoGPT Pattern Matching");
    println!("------------------------------------");
    demo_nano_gpt().await;

    println!("\n📍 Demo 3: Complete TinkyGPT System");
    println!("------------------------------------");
    demo_tinky_gpt().await;

    println!("\n📍 Demo 4: Medical Emergency Response");
    println!("--------------------------------------");
    demo_emergency().await;
}

async fn demo_gpt_core() {
    let mut gpt = GPTCore::new();

    // Test emotional responses
    let inputs = vec!["I feel so sad today", "I'm really excited!", "I'm scared", "This makes me angry"];

    for input in inputs {
        println!("\n👤 Input: \"{input}\"");
        let responses = gpt.apply_emotional_intelligence(input);
        println!("🤖 Emotional Responses:");
        for (i, resp) in responses.iter().take(2).enumerate() {
            println!("   {}. {} (confidence: {:.1})", i + 1, resp.text, resp.confidence);
        }
    }
}

async fn demo_nano_gpt() {
    let nano = NanoGPT::new(ModelSize::Nano);
    let context = AiContext::default();

    let questions = vec!["Are you hungry?", "How are you feeling?", "Do you want to play?", "What's wrong?"];

    for question in questions {
        println!("\n👤 Question: \"{question}\"");
        if let Ok(responses) = nano.generate_response(question, &context).await {
            println!("🎯 Generated Tiles:");
            for (i, resp) in responses.iter().enumerate() {
                println!("   [{}] {} {} (confidence: {:.1})", i + 1, resp.emoji, resp.text, resp.confidence);
            }
        }
    }
}

async fn demo_tinky_gpt() {
    let mut tinky = TinkyGPT::new();

    println!("\n🌟 Full Conversation Flow:");
    println!("Parent: \"Are you feeling okay?\"");

    if let Ok(responses) = tinky.generate("Are you feeling okay?").await {
        println!("💬 TinkyBink Options:");
        for resp in &responses {
            println!("   {} {} (from: {:?})", resp.emoji, resp.text, resp.source);
        }

        // Simulate selection and follow-up
        println!("\nChild selects: \"{}\"", responses[0].text);
        println!("Parent: \"What would help?\"");

        if let Ok(followup) = tinky.generate("What would help?").await {
            println!("💬 Follow-up Options:");
            for resp in &followup {
                println!("   {} {}", resp.emoji, resp.text);
            }
        }
    }
}

async fn demo_emergency() {
    let mut gpt = OfflineGPT::new();

    println!("\n🚨 Emergency Scenarios:");

    let emergencies = vec!["I can't breathe", "My chest hurts", "I fell down", "Help me"];

    for emergency in emergencies {
        println!("\n⚠️ Emergency: \"{emergency}\"");
        let tiles = gpt.generate_aac_response(emergency);
        println!("🆘 Quick Response Tiles:");
        for tile in tiles.iter().take(4) {
            println!("   {} {} (urgency: {:.1})", tile.emoji, tile.text, tile.confidence);
        }
    }
}
