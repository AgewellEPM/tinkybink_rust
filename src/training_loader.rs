use crate::conversation_logic::{ConversationLogicSystem, ConversationNodeBuilder};
use serde::{Deserialize, Serialize};
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

/// Represents the training data format from our JSONL files
#[derive(Debug, Deserialize, Serialize)]
pub struct TrainingExample {
    pub instruction: String,
    pub input: String,
    pub output: Option<String>,
    pub raw_output: Option<String>,
    pub aac_response: Option<AACResponse>,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct AACResponse {
    pub tiles: Vec<TileData>,
    pub spoken_sentence: String,
    pub usage_data: UsageData,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct TileData {
    pub emoji: String,
    pub words: String,
    pub tile_id: String,
}

#[derive(Debug, Deserialize, Serialize)]
pub struct UsageData {
    pub category: String,
    pub emotion_level: String,
    pub complexity: u8,
    pub frequency_weight: f32,
    pub conversation_layer: Option<u8>,
    pub drill_down_context: Option<String>,
}

/// Loads training data from JSONL file into the conversation system
pub fn load_training_data(
    system: &mut ConversationLogicSystem,
    file_path: &Path,
) -> Result<usize, Box<dyn std::error::Error>> {
    let file = File::open(file_path)?;
    let reader = BufReader::new(file);
    let mut loaded_count = 0;

    for (index, line) in reader.lines().enumerate() {
        let line = line?;
        if line.trim().is_empty() {
            continue;
        }

        match serde_json::from_str::<TrainingExample>(&line) {
            Ok(example) => {
                if let Some(node) = convert_to_conversation_node(example, index) {
                    system.add_node(node);
                    loaded_count += 1;
                }
            }
            Err(e) => {
                eprintln!("Error parsing line {}: {}", index + 1, e);
            }
        }
    }

    Ok(loaded_count)
}

/// Convert training example to conversation node
fn convert_to_conversation_node(
    example: TrainingExample,
    index: usize,
) -> Option<crate::conversation_logic::ConversationNode> {
    let node_id = format!("node_{index}");

    // Get output text
    let output_text = example.raw_output.or(example.output).unwrap_or_default();

    // Start building the node
    let mut builder = ConversationNodeBuilder::new(node_id).input(&example.input);

    // Add tiles
    if let Some(aac_response) = &example.aac_response {
        // Use tiles from aac_response if available
        for tile in &aac_response.tiles {
            builder = builder.add_tile(&tile.emoji, &tile.words);
        }

        // Set category and emotion
        builder =
            builder.category(&aac_response.usage_data.category).emotion_level(&aac_response.usage_data.emotion_level);

        // Set conversation layer if available
        if let Some(layer) = aac_response.usage_data.conversation_layer {
            builder = builder.conversation_layer(layer);
        }
    } else {
        // Parse tiles from output text
        let tiles = parse_tiles_from_output(&output_text);
        for (emoji, words) in tiles {
            builder = builder.add_tile(&emoji, &words);
        }
    }

    Some(builder.build())
}

/// Parse tiles from output text format
fn parse_tiles_from_output(output: &str) -> Vec<(String, String)> {
    let mut tiles = Vec::new();

    // Split by comma
    for part in output.split(',') {
        let part = part.trim();
        if part.is_empty() {
            continue;
        }

        // Find emoji and extract words
        let mut emoji = String::new();
        let mut words = String::new();
        let mut found_emoji = false;

        for ch in part.chars() {
            if ch as u32 > 127 && !found_emoji {
                // This is likely an emoji
                emoji.push(ch);
                found_emoji = true;
            } else if found_emoji {
                words.push(ch);
            }
        }

        // Clean up words
        words = words.trim().to_string();

        // If no emoji found, use a default
        if emoji.is_empty() {
            emoji = "💬".to_string();
            words = part.to_string();
        }

        tiles.push((emoji, words));
    }

    // Ensure we have exactly 4 tiles
    while tiles.len() < 4 {
        tiles.push(("❓".to_string(), "Option".to_string()));
    }

    tiles.truncate(4);
    tiles
}

/// Build conversation connections based on content analysis
pub fn build_conversation_connections(system: &mut ConversationLogicSystem) {
    // This would analyze all nodes and create connections
    // For now, we'll implement a simple version

    // Get all node IDs
    let node_ids: Vec<String> = system.get_all_node_ids();

    // Collect connections to add later (to avoid borrowing issues)
    let mut connections_to_add = Vec::new();

    for i in 0..node_ids.len() {
        let current_id = &node_ids[i];

        if let Some(current_node) = system.get_node(current_id) {
            // Clone tiles to avoid borrowing issues
            let tiles: Vec<_> = current_node.tiles.clone();

            // For each tile in the current node
            for tile in tiles {
                let tile_word = tile.words.to_lowercase();

                // Find nodes that could follow this selection
                for (j, _) in node_ids.iter().enumerate() {
                    if i == j {
                        continue;
                    }

                    let other_id = &node_ids[j];
                    if let Some(other_node) = system.get_node(other_id) {
                        // Check if the other node's input relates to this tile
                        if other_node.input.to_lowercase().contains(&tile_word) {
                            connections_to_add.push((current_id.clone(), tile.words.clone(), other_id.clone()));
                        }
                    }
                }
            }
        }
    }

    // Add all connections
    for (from, tile_word, to) in connections_to_add {
        system.add_connection(&from, &tile_word, &to);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Write;
    use tempfile::NamedTempFile;

    #[test]
    fn test_parse_tiles_from_output() {
        let output = "🍕 Pizza is great, 🍔 Burger tasty too, 🌮 Tacos are spicy, 🥗 Salad is healthy";
        let tiles = parse_tiles_from_output(output);

        assert_eq!(tiles.len(), 4);
        assert_eq!(tiles[0], ("🍕".to_string(), "Pizza is great".to_string()));
        assert_eq!(tiles[1], ("🍔".to_string(), "Burger tasty too".to_string()));
    }

    #[test]
    fn test_load_training_data() {
        let mut system = ConversationLogicSystem::new();

        // Create a temporary file with test data
        let mut temp_file = NamedTempFile::new().unwrap();
        writeln!(
            temp_file,
            r#"{{"instruction":"Test","input":"Hello","output":"😊 Happy, 😢 Sad, 😴 Tired, 🤔 Confused"}}"#
        )
        .unwrap();

        let loaded = load_training_data(&mut system, temp_file.path()).unwrap();
        assert_eq!(loaded, 1);
    }
}
