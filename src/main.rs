#[cfg(feature = "clap")]
use anyhow::Result;
#[cfg(feature = "clap")]
use clap::{Parser, Subcommand};
#[cfg(feature = "tracing")]
use tracing::info;

#[cfg(not(feature = "wasm"))]
mod ai;
#[cfg(not(feature = "wasm"))]
mod core;
#[cfg(not(feature = "wasm"))]
mod memory;
#[cfg(not(feature = "wasm"))]
mod speech;
#[cfg(not(feature = "wasm"))]
mod storage;
#[cfg(not(feature = "wasm"))]
mod suggestions;
#[cfg(not(feature = "wasm"))]
mod ui;
#[cfg(not(feature = "wasm"))]
mod utils;

#[cfg(not(feature = "wasm"))]
use crate::core::TinkyBinkSystem;

#[cfg(feature = "clap")]
#[derive(Parser)]
#[command(name = "tinkybink")]
#[command(about = "TinkyBink AAC - Advanced Communication Assistant")]
struct Cli {
    #[command(subcommand)]
    command: Option<Commands>,
}

#[cfg(feature = "clap")]
#[derive(Subcommand)]
enum Commands {
    /// Start the AAC system
    Start {
        #[arg(short, long, default_value = "false")]
        headless: bool,
    },
    /// Test speech recognition
    TestSpeech,
    /// Test suggestion engine
    TestSuggestions,
    /// Interactive demo mode
    Demo,
}

#[cfg(all(feature = "tokio", feature = "clap", feature = "tracing-subscriber"))]
#[tokio::main]
async fn main() -> Result<()> {
    // Initialize tracing
    tracing_subscriber::fmt::init();

    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Start { headless }) => {
            info!("Starting TinkyBink AAC System (headless: {})", headless);
            let mut system = TinkyBinkSystem::new().await?;
            system.run(*headless).await?;
        }
        Some(Commands::TestSpeech) => {
            info!("Testing speech recognition...");
            // TODO: Implement speech test
        }
        Some(Commands::TestSuggestions) => {
            info!("Testing suggestion engine...");
            test_suggestions().await?;
        }
        Some(Commands::Demo) => {
            info!("Starting interactive demo...");
            interactive_demo().await?;
        }
        None => {
            info!("Starting TinkyBink AAC System in GUI mode...");
            let mut system = TinkyBinkSystem::new().await?;
            system.run(false).await?;
        }
    }

    Ok(())
}

async fn test_suggestions() -> Result<()> {
    use crate::suggestions::SuggestionEngine;

    let engine = SuggestionEngine::new();

    let test_cases = [
        "Do you want pizza or pasta?",
        "How are you feeling today?",
        "Are you hungry?",
        "I need help with this",
        "What do you want to eat?",
        "Where are you going?",
        "I'm feeling sad",
        "Can you help me?",
        "This is just random text",
    ];

    println!("\n🧠 TinkyBink AAC Suggestion Engine Test\n");
    println!("{}", "=".repeat(50));

    for (i, input) in test_cases.iter().enumerate() {
        println!("\n{}. Input: \"{}\"", i + 1, input);

        match engine.generate_suggestions(input).await {
            Ok(suggestions) => {
                println!("   Suggestions:");
                for (j, suggestion) in suggestions.iter().enumerate() {
                    println!(
                        "   {}. {} {} (confidence: {:.2})",
                        j + 1,
                        suggestion.emoji,
                        suggestion.text,
                        suggestion.confidence
                    );
                }
            }
            Err(e) => {
                println!("   Error: {e}");
            }
        }
    }

    println!("\n{}", "=".repeat(50));
    println!("✅ Suggestion engine test completed!");

    Ok(())
}

async fn interactive_demo() -> Result<()> {
    use crate::core::user_profile::{UserProfile, UserType};
    use crate::speech::SpeechManager;
    use std::io::{self, Write};
    use tokio::sync::mpsc;

    // Initialize speech system for TTS
    let (tx, mut _rx) = mpsc::unbounded_channel();
    let mut speech_manager = SpeechManager::new(tx).await?;
    let has_tts = speech_manager.can_speak();

    println!("\n👶🗣️  TinkyBink AAC - Adaptive Communication System");
    println!("==================================================");

    // User type selection
    println!("\n👥 Choose user type:");
    println!("  1. Child (ages 2-12)");
    println!("  2. Adult");
    println!("  3. Stroke survivor");
    println!("  4. Medical patient");

    print!("\nSelect (1-4): ");
    io::stdout().flush()?;

    let mut choice = String::new();
    io::stdin().read_line(&mut choice)?;
    let choice = choice.trim();

    let user_profile = match choice {
        "1" => {
            println!("\n👶 Selected: Child user");
            UserProfile::child("Demo Child".to_string(), 6)
        }
        "2" => {
            println!("\n👨 Selected: Adult user");
            UserProfile::adult("Demo Adult".to_string(), None)
        }
        "3" => {
            println!("\n🏥 Selected: Stroke survivor");
            UserProfile::stroke_survivor("Demo Patient".to_string(), Some(6))
        }
        "4" => {
            println!("\n🏥 Selected: Medical patient");
            UserProfile::adult("Demo Patient".to_string(), None) // Could add medical-specific profile
        }
        _ => {
            println!("\n👶 Default: Child user");
            UserProfile::child("Demo Child".to_string(), 6)
        }
    };

    println!(
        "\n{:?} asks questions → {:?} taps to respond",
        if matches!(user_profile.user_type, UserType::Child { .. }) { "Parent" } else { "Caregiver" },
        user_profile.name
    );

    if has_tts {
        println!("\n🔊 VOICE: ON - Child's response will be spoken");
    } else {
        println!("\n🔇 Voice not available");
    }

    println!("\n📝 Examples:");
    println!("  • 'cookie or milk?' → Shows: 🍪 I want cookie | 🥛 I want milk");
    println!("  • 'are you tired?' → Shows: ✅ Yes | ❌ No | 😴 I'm tired");
    println!("  • 'juice or water or milk?' → Shows all 3 options");
    println!("\nType 'quit' to exit.\n");

    let mut iteration_count = 0;
    const MAX_ITERATIONS: usize = 100; // Safety limit

    loop {
        iteration_count += 1;
        if iteration_count > MAX_ITERATIONS {
            println!("\n⚠️  Demo reached maximum iterations limit. Exiting for safety.");
            break;
        }

        print!("💬 You: ");
        if let Err(e) = io::stdout().flush() {
            println!("\n❌ Error flushing output: {e}. Exiting demo.");
            break;
        }

        let mut input = String::new();
        match io::stdin().read_line(&mut input) {
            Ok(0) => {
                println!("\n📄 End of input reached. Exiting demo.");
                break;
            }
            Ok(_) => {
                let input = input.trim();

                if input.is_empty() {
                    continue;
                }

                if input.to_lowercase() == "quit" {
                    println!("\n👋 Goodbye! Thanks for trying TinkyBink AAC!");
                    break;
                }

                println!("\n{} can tap these to communicate:", user_profile.name);

                // Create suggestion engine with user profile
                let mut engine = crate::suggestions::SuggestionEngine::new();
                engine.set_user_profile(user_profile.clone());

                // Try AI-powered suggestions first, fallback to simple tiles
                let tiles = match tokio::task::block_in_place(|| {
                    tokio::runtime::Handle::current().block_on(engine.generate_suggestions(input))
                }) {
                    Ok(ai_tiles) if !ai_tiles.is_empty() => {
                        println!("🤖 Using adaptive AI suggestions for {:?}", user_profile.user_type);
                        ai_tiles
                    }
                    _ => {
                        println!("📝 Using default responses for {:?}", user_profile.user_type);
                        user_profile
                            .get_contextual_responses(input)
                            .into_iter()
                            .enumerate()
                            .map(|(i, response)| {
                                let emoji = match i {
                                    0 => "✅",
                                    1 => "❌",
                                    2 => "🤔",
                                    3 => "💭",
                                    _ => "💬",
                                }
                                .to_string();
                                crate::core::events::SuggestionTile {
                                    emoji,
                                    text: response,
                                    category: crate::core::events::TileCategory::Default,
                                    confidence: 0.9,
                                }
                            })
                            .collect()
                    }
                };

                // Display tiles for child to tap
                for (i, tile) in tiles.iter().enumerate() {
                    println!("   {}. {} {}", i + 1, tile.emoji, tile.text);
                }

                println!("\n💬 {} taps number (1-{}) to speak:", user_profile.name, tiles.len());

                // Let user select a response to build conversation history
                print!("👆 Your choice (or new question): ");
                if io::stdout().flush().is_err() {
                    break;
                }

                let mut choice_input = String::new();
                match io::stdin().read_line(&mut choice_input) {
                    Ok(_) => {
                        let choice_input = choice_input.trim();
                        if let Ok(choice_num) = choice_input.parse::<usize>() {
                            if choice_num > 0 && choice_num <= tiles.len() {
                                let selected = &tiles[choice_num - 1];
                                println!("\n👶🗣️ CHILD SAYS: \"{}\"", selected.text);

                                // Speak the selected response if TTS is available
                                if has_tts {
                                    println!("🔊 Speaking with child-like voice...");
                                    if let Err(e) = speech_manager.speak(&selected.text).await {
                                        println!("🔇 Could not speak: {e}");
                                    } else {
                                        println!("✨ Voice output complete!");
                                    }
                                }
                            }
                        } else if !choice_input.is_empty() && choice_input.to_lowercase() != "quit" {
                            // New parent question - continue loop
                            continue;
                        }
                    }
                    Err(_) => break,
                }

                println!("{}", "-".repeat(50));
            }
            Err(e) => {
                println!("\n❌ Error reading input: {e}. Exiting demo.");
                break;
            }
        }
    }

    Ok(())
}

#[cfg(not(all(feature = "tokio", feature = "clap", feature = "tracing-subscriber")))]
fn main() {
    println!("🧠 TinkyBink AAC - Use 'cargo run --features default demo' for interactive mode");
    println!("📦 Or build with --features wasm for browser deployment");
}
