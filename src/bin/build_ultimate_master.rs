use serde_json::Value;
use std::collections::{HashMap, HashSet};
use std::fs;
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("🚀 Building Ultimate TinkyBink Master Brain");
    println!("🎯 Combining Conversational Master + 49 Specialized Categories");
    println!("🔄 Preserving 3-tier drill-down structure");
    println!("{}", "=".repeat(70));

    let training_dir = Path::new("training");
    let conversational_master_path = training_dir.join("tinkybink_ultimate_conversational_master.jsonl");
    let specialized_brain_path = training_dir.join("tinkybink_super_brain_complete.jsonl");
    let output_path = training_dir.join("tinkybink_ultimate_master_brain.jsonl");

    // Load original conversational master
    println!("📖 Loading Original Conversational Master...");
    let conversational_content = fs::read_to_string(&conversational_master_path)?;
    let conversational_lines: Vec<&str> = conversational_content.lines().collect();
    println!("✅ Loaded {} conversational nodes", conversational_lines.len());

    // Load specialized categories brain
    println!("📖 Loading Specialized Categories Brain...");
    let specialized_content = fs::read_to_string(&specialized_brain_path)?;
    let specialized_lines: Vec<&str> = specialized_content.lines().collect();
    println!("✅ Loaded {} specialized nodes", specialized_lines.len());

    // Combine and deduplicate
    println!("🔄 Merging datasets...");
    let mut all_entries: Vec<Value> = Vec::new();
    let mut seen_inputs: HashSet<String> = HashSet::new();
    let mut duplicates = 0;

    // Add conversational master entries first (priority)
    for line in &conversational_lines {
        if line.trim().is_empty() {
            continue;
        }

        match serde_json::from_str::<Value>(line) {
            Ok(entry) => {
                if let Some(input) = entry.get("input").and_then(|v| v.as_str()) {
                    let normalized_input = input.to_lowercase().trim().to_string();
                    if !seen_inputs.contains(&normalized_input) {
                        seen_inputs.insert(normalized_input);
                        all_entries.push(entry);
                    } else {
                        duplicates += 1;
                    }
                }
            }
            Err(e) => println!("⚠️  Skipped invalid JSON in conversational master: {e}"),
        }
    }

    let conversational_count = all_entries.len();

    // Add specialized entries (only if not duplicate)
    for line in &specialized_lines {
        if line.trim().is_empty() {
            continue;
        }

        match serde_json::from_str::<Value>(line) {
            Ok(entry) => {
                if let Some(input) = entry.get("input").and_then(|v| v.as_str()) {
                    let normalized_input = input.to_lowercase().trim().to_string();
                    if !seen_inputs.contains(&normalized_input) {
                        seen_inputs.insert(normalized_input);

                        // Enhance specialized entries with conversational structure
                        let enhanced_entry = enhance_specialized_entry(entry)?;
                        all_entries.push(enhanced_entry);
                    } else {
                        duplicates += 1;
                    }
                }
            }
            Err(e) => println!("⚠️  Skipped invalid JSON in specialized brain: {e}"),
        }
    }

    let specialized_added = all_entries.len() - conversational_count;

    // Create drill-down connections
    println!("🔗 Creating 3-tier drill-down connections...");
    let connected_entries = create_drill_down_structure(all_entries)?;

    // Save ultimate brain
    let output_content = connected_entries.iter().map(serde_json::to_string).collect::<Result<Vec<_>, _>>()?.join("\n");

    fs::write(&output_path, output_content)?;

    println!("\n🎉 Ultimate Master Brain Creation Complete!");
    println!("📊 Final Statistics:");
    println!("   🧠 Original Conversational Master: {conversational_count} nodes");
    println!("   ➕ Specialized Categories Added: {specialized_added} nodes");
    println!("   🗑️  Duplicates Removed: {duplicates}");
    println!("   🎯 Total Ultimate Brain: {} nodes", connected_entries.len());
    println!("   💾 Output File: {}", output_path.display());

    // Calculate growth
    let total_input = conversational_lines.len() + specialized_lines.len();
    let growth_factor = connected_entries.len() as f64 / 4436.0; // Original conversational master size

    println!("\n📈 Growth Analysis:");
    println!("   📥 Total Input Entries: {total_input}");
    println!("   📤 Final Output Entries: {}", connected_entries.len());
    println!("   📊 Growth Factor: {growth_factor:.2}x larger than original");
    println!("   🎪 Estimated Total Tiles: {}", connected_entries.len() * 4);

    // Analyze categories
    analyze_categories(&connected_entries)?;

    println!("\n🎯 Next Steps:");
    println!("   1. Copy to iOS: cp {} path/to/ios/Resources/conversation_brain.jsonl", output_path.display());
    println!("   2. Copy to Android: cp {} path/to/android/assets/conversation_brain.jsonl", output_path.display());
    println!("   3. Use in HTML5: Include in web app bundle");
    println!("   4. Test with conversation_demo: cargo run --bin conversation_demo");

    Ok(())
}

fn enhance_specialized_entry(mut entry: Value) -> Result<Value, Box<dyn std::error::Error>> {
    // Ensure specialized entries have conversational structure
    if let Some(obj) = entry.as_object_mut() {
        // Add instruction if missing
        if !obj.contains_key("instruction") {
            if let Some(input) = obj.get("input").and_then(|v| v.as_str()) {
                let category = obj
                    .get("aac_response")
                    .and_then(|r| r.get("usage_data"))
                    .and_then(|u| u.get("category"))
                    .and_then(|c| c.as_str())
                    .unwrap_or("specialized");

                obj.insert(
                    "instruction".to_string(),
                    Value::String(format!("AAC {}: {}", category.replace("_", " ").to_uppercase(), input)),
                );
            }
        }

        // Ensure raw_output exists
        if !obj.contains_key("raw_output") {
            if let Some(aac_response) = obj.get("aac_response") {
                if let Some(tiles) = aac_response.get("tiles").and_then(|t| t.as_array()) {
                    let raw_output = tiles
                        .iter()
                        .filter_map(|tile| {
                            let emoji = tile.get("emoji").and_then(|e| e.as_str()).unwrap_or("");
                            let words = tile.get("words").and_then(|w| w.as_str()).unwrap_or("");
                            if !emoji.is_empty() && !words.is_empty() { Some(format!("{emoji} {words}")) } else { None }
                        })
                        .collect::<Vec<_>>()
                        .join(", ");

                    obj.insert("raw_output".to_string(), Value::String(raw_output));
                }
            }
        }
    }

    Ok(entry)
}

fn create_drill_down_structure(mut entries: Vec<Value>) -> Result<Vec<Value>, Box<dyn std::error::Error>> {
    // Create category-based connections for drill-downs
    let mut category_groups: HashMap<String, Vec<usize>> = HashMap::new();

    // Group entries by category
    for (index, entry) in entries.iter().enumerate() {
        if let Some(category) = extract_category(entry) {
            category_groups.entry(category).or_default().push(index);
        }
    }

    println!("🔗 Creating connections across {} categories", category_groups.len());

    // Collect drill-down data first to avoid borrowing conflicts
    let mut drill_down_data: Vec<(usize, Vec<String>, String, usize)> = Vec::new();

    for (category, indices) in category_groups.iter() {
        if indices.len() > 1 {
            // Create connections within category
            for (i, &entry_idx) in indices.iter().enumerate() {
                // Collect follow-up inputs
                let mut follow_ups = Vec::new();
                for j in 1..=3 {
                    // Up to 3 follow-ups
                    let next_idx = (i + j) % indices.len();
                    if let Some(next_entry) = entries.get(indices[next_idx]) {
                        if let Some(input) = next_entry.get("input").and_then(|v| v.as_str()) {
                            follow_ups.push(input.to_string());
                        }
                    }
                }

                if !follow_ups.is_empty() {
                    drill_down_data.push((entry_idx, follow_ups, category.clone(), indices.len()));
                }
            }
        }
    }

    // Apply drill-down data to entries
    for (entry_idx, follow_ups, category, category_size) in drill_down_data {
        if let Some(entry_obj) = entries[entry_idx].as_object_mut() {
            entry_obj.insert(
                "drill_down_options".to_string(),
                Value::Array(follow_ups.into_iter().map(Value::String).collect()),
            );
            entry_obj.insert("category_group".to_string(), Value::String(category));
            entry_obj.insert("category_size".to_string(), Value::Number(serde_json::Number::from(category_size)));
        }
    }

    Ok(entries)
}

fn extract_category(entry: &Value) -> Option<String> {
    // Try multiple ways to extract category
    entry
        .get("aac_response")
        .and_then(|r| r.get("usage_data"))
        .and_then(|u| u.get("category"))
        .and_then(|c| c.as_str())
        .map(|s| s.to_string())
        .or_else(|| {
            // Extract from instruction
            entry.get("instruction").and_then(|i| i.as_str()).and_then(|s| {
                if s.starts_with("AAC ") {
                    s.split(":").next().map(|part| part.replace("AAC ", "").trim().to_lowercase())
                } else {
                    None
                }
            })
        })
        .or_else(|| Some("general".to_string()))
}

fn analyze_categories(entries: &[Value]) -> Result<(), Box<dyn std::error::Error>> {
    let mut category_counts: HashMap<String, usize> = HashMap::new();

    for entry in entries {
        if let Some(category) = extract_category(entry) {
            *category_counts.entry(category).or_insert(0) += 1;
        }
    }

    println!("\n📊 Category Distribution (Top 15):");
    let mut sorted_categories: Vec<_> = category_counts.iter().collect();
    sorted_categories.sort_by(|a, b| b.1.cmp(a.1));

    for (i, (category, count)) in sorted_categories.iter().take(15).enumerate() {
        println!("   {}. {}: {} nodes", i + 1, category, count);
    }

    if sorted_categories.len() > 15 {
        let remaining: usize = sorted_categories.iter().skip(15).map(|(_, count)| *count).sum();
        println!("   ... and {} more categories with {} nodes", sorted_categories.len() - 15, remaining);
    }

    Ok(())
}
