use std::path::Path;
use tinkybink_rust::comprehensive_brain_loader::ComprehensiveBrainLoader;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("🚀 Building TinkyBink Super Brain");
    println!("🎯 Combining all 49 specialized AAC categories");
    println!("{}", "=".repeat(60));

    let training_dir = Path::new("training");
    let output_path = Path::new("training/tinkybink_super_brain_complete.jsonl");

    if !training_dir.exists() {
        return Err("Training directory not found".into());
    }

    let mut loader = ComprehensiveBrainLoader::new();

    // Load all 49 tile categories
    let all_nodes = loader.load_all_tile_categories(training_dir)?;

    if all_nodes.is_empty() {
        return Err("No conversation nodes loaded".into());
    }

    // Save the comprehensive brain
    loader.save_comprehensive_brain(&all_nodes, output_path)?;

    println!("\n🎉 Super Brain Creation Complete!");
    println!("📊 Final Statistics:");
    println!("   🗂️  Categories: {}", loader.categories_loaded.len());
    println!("   🧠 Conversation Nodes: {}", all_nodes.len());
    println!("   🎪 Total Tiles: {}", loader.total_tiles);
    println!("   💾 Output File: {}", output_path.display());

    println!("\n📋 Categories Loaded:");
    for (i, category) in loader.categories_loaded.iter().enumerate() {
        println!("   {}. {}", i + 1, category);
    }

    // Compare with existing conversational master
    let existing_path = Path::new("training/tinkybink_ultimate_conversational_master.jsonl");
    if existing_path.exists() {
        let existing_content = std::fs::read_to_string(existing_path)?;
        let existing_lines = existing_content.lines().count();

        println!("\n📈 Comparison:");
        println!(
            "   🔄 Original Conversational Master: {existing_lines} nodes"
        );
        println!("   🆕 New Super Brain: {} nodes", all_nodes.len());
        println!(
            "   📊 Growth: {}x larger",
            all_nodes.len() as f64 / existing_lines as f64
        );
    }

    println!("\n🎯 Next Steps:");
    println!(
        "   1. Copy to iOS: cp {} path/to/ios/Resources/",
        output_path.display()
    );
    println!(
        "   2. Copy to Android: cp {} path/to/android/assets/",
        output_path.display()
    );
    println!("   3. Use in HTML5: Include in web app bundle");

    Ok(())
}
