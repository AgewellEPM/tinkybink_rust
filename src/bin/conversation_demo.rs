use std::io::{self, Write};
use std::path::Path;
use tinkybink_rust::TinkyBinkAAC;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("🧠 TinkyBink Conversation Demo");
    println!("🔄 Demonstrating drill-down conversation logic");
    println!("{}", "=".repeat(50));

    // Create AAC system
    let mut aac = TinkyBinkAAC::new();

    // Load training data
    let training_file = Path::new("training/tinkybink_ultimate_conversational_master.jsonl");
    if training_file.exists() {
        let loaded = aac.load_training_data(training_file)?;
        println!("✅ Loaded {loaded} conversation nodes");
    } else {
        println!("⚠️  Training file not found, using demo data");
        // In real use, we'd load the actual training data
        return demo_without_file();
    }

    // Start conversation
    println!("\n🗣️ Starting conversation...\n");

    // Get starters and convert to owned data
    let starters = aac.get_starters(None);

    if starters.is_empty() {
        println!("No conversation starters found!");
        return Ok(());
    }

    // Store responses as owned data to avoid borrow issues
    let mut current_response = starters[0].clone();
    let mut current_node_id = "node_0"; // In real implementation, track this

    loop {
        // Display current prompt
        println!("💬 {}", current_response.input);
        println!();

        // Display tiles
        for (i, tile) in current_response.tiles.iter().enumerate() {
            println!("  {}. {} {}", i + 1, tile.emoji, tile.words);
        }
        println!();

        // Get user input
        print!("Select tile (1-4) or 'q' to quit: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;
        let input = input.trim();

        if input == "q" {
            break;
        }

        // Parse selection
        if let Ok(selection) = input.parse::<usize>() {
            if selection > 0 && selection <= current_response.tiles.len() {
                let selected_tile = &current_response.tiles[selection - 1];

                println!("\nYou selected: {} {}\n", selected_tile.emoji, selected_tile.words);

                // Get follow-up responses and clone to own them
                let follow_ups = aac.process_selection(current_node_id, &selected_tile.words);

                if follow_ups.is_empty() {
                    println!("No follow-up responses available. Starting over...\n");
                    let starters = aac.get_starters(None);
                    if !starters.is_empty() {
                        current_response = starters[0].clone();
                        current_node_id = "node_0";
                    }
                } else {
                    current_response = follow_ups[0].clone();
                    // In real implementation, track the node ID properly
                    current_node_id = "node_next";
                }
            } else {
                println!("Invalid selection. Please choose 1-4.\n");
            }
        } else {
            println!("Invalid input. Please enter a number 1-4 or 'q'.\n");
        }
    }

    println!("\n👋 Thanks for using TinkyBink!");
    Ok(())
}

fn demo_without_file() -> Result<(), Box<dyn std::error::Error>> {
    println!("\n🎮 Running hardcoded demo...\n");

    // Pizza ordering demo
    let conversations = vec![
        ("What would you like to eat?", vec![("🍕", "Pizza"), ("🍔", "Burger"), ("🥗", "Salad"), ("🍝", "Pasta")]),
        (
            "Pizza chosen! What toppings?",
            vec![("🍄", "Mushrooms"), ("🥓", "Bacon"), ("🧄", "Pepperoni"), ("🧀", "Extra cheese")],
        ),
        (
            "Mushroom pizza! What size?",
            vec![("🍕", "Small"), ("🍕🍕", "Medium"), ("🍕🍕🍕", "Large"), ("🍕🍕🍕🍕", "Extra large")],
        ),
        (
            "Large pizza! Crust type?",
            vec![("🥖", "Thin crust"), ("🍞", "Thick crust"), ("🧄", "Garlic crust"), ("🧀", "Stuffed crust")],
        ),
    ];

    for (prompt, tiles) in conversations {
        println!("💬 {prompt}");
        println!();

        for (i, (emoji, words)) in tiles.iter().enumerate() {
            println!("  {}. {} {}", i + 1, emoji, words);
        }
        println!();

        // Simulate selection
        println!("Demo: Auto-selecting option 1...\n");
        std::thread::sleep(std::time::Duration::from_secs(1));
    }

    println!("🎊 Order complete: Large thin crust mushroom pizza!");
    Ok(())
}
