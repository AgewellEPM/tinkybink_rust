use crate::conversation_logic::{AACTile, ConversationNode};
use serde_json::Value;
use std::collections::HashMap;
use std::fs;
use std::path::Path;

pub struct ComprehensiveBrainLoader {
    pub total_tiles: usize,
    pub categories_loaded: Vec<String>,
}

impl Default for ComprehensiveBrainLoader {
    fn default() -> Self {
        Self::new()
    }
}

impl ComprehensiveBrainLoader {
    pub fn new() -> Self {
        Self { total_tiles: 0, categories_loaded: Vec::new() }
    }

    pub fn load_all_tile_categories(
        &mut self,
        training_dir: &Path,
    ) -> Result<Vec<ConversationNode>, Box<dyn std::error::Error>> {
        let mut all_nodes = Vec::new();

        // List of all 49 tile categories
        let tile_files = vec![
            // Speech & Language Therapy
            "tinkybink_articulation_phonology_tiles.json",
            "tinkybink_cognitive_communication_tiles.json",
            "tinkybink_communication_language_tiles.json",
            "tinkybink_fluency_stuttering_tiles.json",
            "tinkybink_functional_communication_tiles.json",
            "tinkybink_voice_resonance_tiles.json",
            // Daily Living & Life Skills
            "tinkybink_adaptive_skills_tiles.json",
            "tinkybink_life_skills_independence_tiles.json",
            "tinkybink_self_care_hygiene_tiles.json",
            "tinkybink_household_chores_tiles.json",
            "tinkybink_cooking_kitchen_tiles.json",
            "tinkybink_money_shopping_tiles.json",
            // Social & Emotional
            "tinkybink_behavioral_social_tiles.json",
            "tinkybink_emotions_feelings_tiles.json",
            "tinkybink_friendship_relationships_tiles.json",
            "tinkybink_social_emotional_learning_tiles.json",
            // Education & Learning
            "tinkybink_classroom_tiles.json",
            "tinkybink_school_tiles.json",
            "tinkybink_finemotor_academic_tiles.json",
            "tinkybink_science_exploration_tiles.json",
            "tinkybink_early_intervention_tiles.json",
            // Health & Medical
            "tinkybink_body_parts_health_tiles.json",
            "tinkybink_health_tiles.json",
            "tinkybink_medical_healthcare_tiles.json",
            "tinkybink_sensory_feeding_tiles.json",
            "tinkybink_swallowing_dysphagia_tiles.json",
            // Activities & Recreation
            "tinkybink_animals_pets_tiles.json",
            "tinkybink_arts_creativity_tiles.json",
            "tinkybink_community_recreation_tiles.json",
            "tinkybink_games_toys_tiles.json",
            "tinkybink_hobbies_crafts_tiles.json",
            "tinkybink_music_instruments_tiles.json",
            "tinkybink_reallife_activities_tiles.json",
            "tinkybink_sports_tiles.json",
            // Environment & Context
            "tinkybink_nature_environment_tiles.json",
            "tinkybink_seasonal_holidays_tiles.json",
            "tinkybink_weather_seasons_tiles.json",
            "tinkybink_clothing_fashion_tiles.json",
            // Transportation & Travel
            "tinkybink_transportation_travel_tiles.json",
            "tinkybink_transportation_vehicles_tiles.json",
            "tinkybink_pets_trips_tiles.json",
            // Safety & Work
            "tinkybink_emergency_safety_tiles.json",
            "tinkybink_safety_emergency_tiles.json",
            "tinkybink_work_vocational_tiles.json",
            // Technology & Organization
            "tinkybink_technology_devices_tiles.json",
            "tinkybink_transitions_routines_tiles.json",
            "tinkybink_personal_information_tiles.json",
        ];

        println!("🧠 Loading Comprehensive TinkyBink Brain...");
        println!("📁 Processing {} specialized tile categories", tile_files.len());

        for tile_file in tile_files {
            let file_path = training_dir.join(tile_file);

            if file_path.exists() {
                match self.load_tile_category(&file_path) {
                    Ok(mut nodes) => {
                        let category_name = tile_file
                            .strip_prefix("tinkybink_")
                            .unwrap_or(tile_file)
                            .strip_suffix("_tiles.json")
                            .unwrap_or(tile_file)
                            .replace("_", " ");

                        // Add category context to each node
                        for node in &mut nodes {
                            node.category = category_name.clone();
                        }

                        let node_count = nodes.len();
                        all_nodes.extend(nodes);
                        self.categories_loaded.push(category_name.clone());

                        println!("✅ Loaded {category_name} - {node_count} conversation nodes");
                    }
                    Err(e) => {
                        println!("⚠️  Failed to load {tile_file}: {e}");
                    }
                }
            } else {
                println!("❌ File not found: {tile_file}");
            }
        }

        println!("\n🎯 Comprehensive Brain Summary:");
        println!("   📊 Total Categories: {}", self.categories_loaded.len());
        println!("   🔢 Total Nodes: {}", all_nodes.len());
        println!("   🎪 Total Tiles: {}", self.total_tiles);

        Ok(all_nodes)
    }

    fn load_tile_category(&mut self, file_path: &Path) -> Result<Vec<ConversationNode>, Box<dyn std::error::Error>> {
        let content = fs::read_to_string(file_path)?;
        let json: Value = serde_json::from_str(&content)?;

        let mut nodes = Vec::new();

        // Handle different JSON structures
        match &json {
            Value::Array(tiles_array) => {
                // Direct array of tiles
                nodes.extend(self.convert_tiles_to_nodes(tiles_array.clone())?);
            }
            Value::Object(obj) => {
                // Look for common tile array keys
                let possible_keys = vec!["tiles", "aac_tiles", "vocabulary", "words", "items"];

                for key in possible_keys {
                    if let Some(Value::Array(tiles_array)) = obj.get(key) {
                        nodes.extend(self.convert_tiles_to_nodes(tiles_array.clone())?);
                        break;
                    }
                }

                // If no array found, try to convert object directly
                if nodes.is_empty() {
                    nodes.push(self.convert_object_to_node(json)?);
                }
            }
            _ => {
                return Err("Unsupported JSON structure".into());
            }
        }

        Ok(nodes)
    }

    fn convert_tiles_to_nodes(
        &mut self,
        tiles: Vec<Value>,
    ) -> Result<Vec<ConversationNode>, Box<dyn std::error::Error>> {
        let mut nodes = Vec::new();

        // Group tiles into sets of 4 for conversation nodes
        for chunk in tiles.chunks(4) {
            let mut aac_tiles = Vec::new();
            let mut spoken_words = Vec::new();

            for tile_value in chunk {
                if let Some(tile) = self.parse_tile(tile_value)? {
                    spoken_words.push(format!("{} {}", tile.emoji, tile.words));
                    aac_tiles.push(tile);
                    self.total_tiles += 1;
                }
            }

            if !aac_tiles.is_empty() {
                // Create conversation prompt based on first tile's context
                let prompt = self.generate_contextual_prompt(&aac_tiles);
                let _spoken_sentence = spoken_words.join(", ");

                let node = ConversationNode {
                    id: format!("node_{}", self.total_tiles),
                    input: prompt,
                    tiles: aac_tiles,
                    category: "general".to_string(), // Will be updated by caller
                    emotion_level: "neutral".to_string(),
                    conversation_layer: self.calculate_complexity(chunk.len()) as u8,
                    follow_ups: HashMap::new(),
                };

                nodes.push(node);
            }
        }

        Ok(nodes)
    }

    fn parse_tile(&self, tile_value: &Value) -> Result<Option<AACTile>, Box<dyn std::error::Error>> {
        let tile = match tile_value {
            Value::Object(obj) => {
                let words = obj
                    .get("word")
                    .or_else(|| obj.get("words"))
                    .or_else(|| obj.get("text"))
                    .or_else(|| obj.get("label"))
                    .and_then(|v| v.as_str())
                    .unwrap_or("Unknown");

                let emoji = obj
                    .get("emoji")
                    .or_else(|| obj.get("symbol"))
                    .or_else(|| obj.get("icon"))
                    .and_then(|v| v.as_str())
                    .unwrap_or("🔘");

                let default_id = format!("tile_{}", self.total_tiles);
                let id = obj.get("id").or_else(|| obj.get("tile_id")).and_then(|v| v.as_str()).unwrap_or(&default_id);

                Some(AACTile { emoji: emoji.to_string(), words: words.to_string(), tile_id: id.to_string() })
            }
            Value::String(s) => {
                // Simple string tile
                Some(AACTile {
                    emoji: "💬".to_string(),
                    words: s.clone(),
                    tile_id: format!("tile_{}", self.total_tiles),
                })
            }
            _ => None,
        };

        Ok(tile)
    }

    fn convert_object_to_node(&mut self, _obj: Value) -> Result<ConversationNode, Box<dyn std::error::Error>> {
        // Convert single object to node (fallback)
        let default_tiles = vec![
            AACTile {
                emoji: "💬".to_string(),
                words: "Yes".to_string(),
                tile_id: format!("default_{}", self.total_tiles),
            },
            AACTile {
                emoji: "❌".to_string(),
                words: "No".to_string(),
                tile_id: format!("default_{}", self.total_tiles + 1),
            },
        ];

        self.total_tiles += 2;

        Ok(ConversationNode {
            id: format!("default_{}", self.total_tiles),
            input: "What would you like to say?".to_string(),
            tiles: default_tiles,
            category: "general".to_string(),
            emotion_level: "neutral".to_string(),
            conversation_layer: 2,
            follow_ups: HashMap::new(),
        })
    }

    fn generate_contextual_prompt(&self, tiles: &[AACTile]) -> String {
        if tiles.is_empty() {
            return "What would you like to say?".to_string();
        }

        let first_word = &tiles[0].words.to_lowercase();

        // Generate context-aware prompts
        match first_word.as_str() {
            w if w.contains("feel") || w.contains("emotion") => "How are you feeling?",
            w if w.contains("want") || w.contains("need") => "What do you want?",
            w if w.contains("go") || w.contains("place") => "Where would you like to go?",
            w if w.contains("eat") || w.contains("food") => "What would you like to eat?",
            w if w.contains("play") || w.contains("game") => "What would you like to play?",
            w if w.contains("help") => "Do you need help?",
            w if w.contains("stop") => "Should we stop?",
            w if w.contains("more") => "Do you want more?",
            _ => "What would you like to say?",
        }
        .to_string()
    }

    fn calculate_complexity(&self, tile_count: usize) -> i32 {
        match tile_count {
            1 => 1,
            2 => 2,
            3 => 3,
            _ => 4,
        }
    }

    pub fn save_comprehensive_brain(
        &self,
        nodes: &[ConversationNode],
        output_path: &Path,
    ) -> Result<(), Box<dyn std::error::Error>> {
        let mut jsonl_lines = Vec::new();

        for node in nodes {
            let spoken_sentence =
                node.tiles.iter().map(|t| format!("{} {}", t.emoji, t.words)).collect::<Vec<_>>().join(", ");

            let json_node = serde_json::json!({
                "instruction": format!("AAC {}: {}",
                    node.category,
                    node.input
                ),
                "input": node.input,
                "aac_response": {
                    "tiles": node.tiles.iter().map(|tile| serde_json::json!({
                        "emoji": tile.emoji,
                        "words": tile.words,
                        "tile_id": tile.tile_id
                    })).collect::<Vec<_>>(),
                    "spoken_sentence": spoken_sentence,
                    "usage_data": {
                        "category": node.category.to_lowercase(),
                        "emotion_level": node.emotion_level,
                        "complexity": node.conversation_layer,
                        "frequency_weight": 1.0
                    }
                },
                "raw_output": node.tiles.iter()
                    .map(|t| format!("{} {}", t.emoji, t.words))
                    .collect::<Vec<_>>()
                    .join(", ")
            });

            jsonl_lines.push(serde_json::to_string(&json_node)?);
        }

        fs::write(output_path, jsonl_lines.join("\n"))?;

        println!("💾 Saved comprehensive brain to: {}", output_path.display());
        println!("📊 Total entries: {}", jsonl_lines.len());

        Ok(())
    }
}
