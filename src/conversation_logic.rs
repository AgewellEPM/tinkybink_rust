use serde::{Deserialize, Serialize};
use std::collections::{HashMap, HashSet};

/// Represents a single AAC tile with emoji and words
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AACTile {
    pub emoji: String,
    pub words: String,
    pub tile_id: String,
}

/// Represents a conversation node in the logic tree
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ConversationNode {
    pub id: String,
    pub input: String,
    pub tiles: Vec<AACTile>,
    pub category: String,
    pub emotion_level: String,
    pub conversation_layer: u8,
    pub follow_ups: HashMap<String, Vec<String>>, // tile_word -> next_node_ids
}

/// Represents a complete conversation path
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ConversationPath {
    pub path_id: String,
    pub nodes: Vec<String>, // node IDs in order
    pub context: HashMap<String, String>,
}

/// Main conversation logic system
pub struct ConversationLogicSystem {
    nodes: HashMap<String, ConversationNode>,
    categories: HashMap<String, Vec<String>>, // category -> node_ids
    #[allow(dead_code)]
    conversation_paths: Vec<ConversationPath>,
    tile_connections: HashMap<String, Vec<String>>, // tile_word -> node_ids
}

impl Default for ConversationLogicSystem {
    fn default() -> Self {
        Self::new()
    }
}

impl ConversationLogicSystem {
    /// Create a new conversation logic system
    pub fn new() -> Self {
        Self {
            nodes: HashMap::new(),
            categories: HashMap::new(),
            conversation_paths: Vec::new(),
            tile_connections: HashMap::new(),
        }
    }

    /// Load conversation data from JSON
    pub fn load_from_json(&mut self, _json_data: &str) -> Result<(), String> {
        // Parse JSON data and populate the system
        // This would load from our training data
        Ok(())
    }

    /// Add a conversation node
    pub fn add_node(&mut self, node: ConversationNode) {
        // Index by category
        self.categories
            .entry(node.category.clone())
            .or_default()
            .push(node.id.clone());

        // Index by tile words for quick lookup
        for tile in &node.tiles {
            let tile_word = tile.words.to_lowercase();
            self.tile_connections
                .entry(tile_word)
                .or_default()
                .push(node.id.clone());
        }

        // Store the node
        self.nodes.insert(node.id.clone(), node);
    }

    /// Get conversation starters for a category
    pub fn get_starters(&self, category: Option<&str>) -> Vec<&ConversationNode> {
        match category {
            Some(cat) => self
                .categories
                .get(cat)
                .map(|node_ids| {
                    node_ids
                        .iter()
                        .filter_map(|id| self.nodes.get(id))
                        .filter(|n| n.conversation_layer == 1)
                        .collect()
                })
                .unwrap_or_default(),
            None => {
                // Return starters from all categories
                self.nodes
                    .values()
                    .filter(|n| n.conversation_layer == 1)
                    .take(20)
                    .collect()
            }
        }
    }

    /// Get follow-up responses based on tile selection
    pub fn get_follow_ups(&self, node_id: &str, tile_word: &str) -> Vec<&ConversationNode> {
        if let Some(node) = self.nodes.get(node_id) {
            if let Some(follow_up_ids) = node.follow_ups.get(tile_word) {
                return follow_up_ids
                    .iter()
                    .filter_map(|id| self.nodes.get(id))
                    .collect();
            }
        }

        // If no specific follow-ups, find contextually relevant responses
        self.find_contextual_responses(tile_word, node_id)
    }

    /// Find contextually relevant responses
    fn find_contextual_responses(
        &self,
        tile_word: &str,
        current_node_id: &str,
    ) -> Vec<&ConversationNode> {
        let current_node = match self.nodes.get(current_node_id) {
            Some(node) => node,
            None => return Vec::new(),
        };

        let tile_word_lower = tile_word.to_lowercase();
        let mut candidates: Vec<(&ConversationNode, f32)> = Vec::new();

        // Search through all nodes for relevant responses
        for (id, node) in &self.nodes {
            if id == current_node_id {
                continue;
            }

            let mut relevance_score = 0.0;

            // Check if input contains the tile word
            if node.input.to_lowercase().contains(&tile_word_lower) {
                relevance_score += 1.0;
            }

            // Check category match
            if node.category == current_node.category {
                relevance_score += 0.5;
            }

            // Check emotion continuity
            if node.emotion_level == current_node.emotion_level {
                relevance_score += 0.3;
            }

            // Check conversation layer progression
            if node.conversation_layer == current_node.conversation_layer + 1 {
                relevance_score += 0.4;
            }

            if relevance_score > 0.0 {
                candidates.push((node, relevance_score));
            }
        }

        // Sort by relevance and return top matches
        candidates.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
        candidates
            .into_iter()
            .take(4)
            .map(|(node, _)| node)
            .collect()
    }

    /// Generate a complete conversation path
    pub fn generate_conversation_path(
        &self,
        start_node_id: &str,
        max_depth: usize,
    ) -> ConversationPath {
        let mut path = ConversationPath {
            path_id: format!("path_{}", uuid::Uuid::new_v4()),
            nodes: vec![start_node_id.to_string()],
            context: HashMap::new(),
        };

        let mut current_id = start_node_id;
        let mut visited = HashSet::new();
        visited.insert(current_id);

        for depth in 1..max_depth {
            if let Some(current_node) = self.nodes.get(current_id) {
                // Pick the first tile as the selection (in real usage, user would select)
                if let Some(first_tile) = current_node.tiles.first() {
                    let tile_word = &first_tile.words;

                    // Get follow-ups
                    let follow_ups = self.get_follow_ups(current_id, tile_word);

                    // Pick the best follow-up that hasn't been visited
                    if let Some(next_node) =
                        follow_ups.iter().find(|n| !visited.contains(n.id.as_str()))
                    {
                        path.nodes.push(next_node.id.clone());
                        path.context
                            .insert(format!("depth_{depth}_selection"), tile_word.clone());

                        visited.insert(&next_node.id);
                        current_id = &next_node.id;
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            } else {
                break;
            }
        }

        path
    }

    /// Get all node IDs
    pub fn get_all_node_ids(&self) -> Vec<String> {
        self.nodes.keys().cloned().collect()
    }

    /// Get a node by ID
    pub fn get_node(&self, node_id: &str) -> Option<&ConversationNode> {
        self.nodes.get(node_id)
    }

    /// Add a connection between nodes
    pub fn add_connection(&mut self, from_node: &str, tile_word: &str, to_node: &str) {
        if let Some(node) = self.nodes.get_mut(from_node) {
            node.follow_ups
                .entry(tile_word.to_string())
                .or_insert_with(Vec::new)
                .push(to_node.to_string());
        }
    }
}

/// Builder for creating conversation nodes
pub struct ConversationNodeBuilder {
    node: ConversationNode,
}

impl ConversationNodeBuilder {
    pub fn new(id: String) -> Self {
        Self {
            node: ConversationNode {
                id,
                input: String::new(),
                tiles: Vec::new(),
                category: "general".to_string(),
                emotion_level: "medium".to_string(),
                conversation_layer: 1,
                follow_ups: HashMap::new(),
            },
        }
    }

    pub fn input(mut self, input: &str) -> Self {
        self.node.input = input.to_string();
        self
    }

    pub fn add_tile(mut self, emoji: &str, words: &str) -> Self {
        self.node.tiles.push(AACTile {
            emoji: emoji.to_string(),
            words: words.to_string(),
            tile_id: format!("tile_{}", self.node.tiles.len() + 1),
        });
        self
    }

    pub fn category(mut self, category: &str) -> Self {
        self.node.category = category.to_string();
        self
    }

    pub fn emotion_level(mut self, level: &str) -> Self {
        self.node.emotion_level = level.to_string();
        self
    }

    pub fn conversation_layer(mut self, layer: u8) -> Self {
        self.node.conversation_layer = layer;
        self
    }

    pub fn add_follow_up(mut self, tile_word: &str, node_id: &str) -> Self {
        self.node
            .follow_ups
            .entry(tile_word.to_string())
            .or_default()
            .push(node_id.to_string());
        self
    }

    pub fn build(self) -> ConversationNode {
        self.node
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_conversation_flow() {
        let mut system = ConversationLogicSystem::new();

        // Create greeting node
        let greeting = ConversationNodeBuilder::new("greeting_1".to_string())
            .input("Hello! How are you?")
            .add_tile("😊", "Happy")
            .add_tile("😢", "Sad")
            .add_tile("😴", "Tired")
            .add_tile("🤔", "Confused")
            .category("greetings")
            .conversation_layer(1)
            .add_follow_up("Happy", "happy_response_1")
            .add_follow_up("Sad", "sad_response_1")
            .build();

        // Create follow-up for happy
        let happy_response = ConversationNodeBuilder::new("happy_response_1".to_string())
            .input("That's great! What would you like to do?")
            .add_tile("🎮", "Play games")
            .add_tile("📚", "Read book")
            .add_tile("🎵", "Listen music")
            .add_tile("🏃", "Go outside")
            .category("activities")
            .emotion_level("happy")
            .conversation_layer(2)
            .build();

        // Add nodes to system
        system.add_node(greeting);
        system.add_node(happy_response);

        // Test getting starters
        let starters = system.get_starters(Some("greetings"));
        assert_eq!(starters.len(), 1);

        // Test getting follow-ups
        let follow_ups = system.get_follow_ups("greeting_1", "Happy");
        assert_eq!(follow_ups.len(), 1);
        assert_eq!(follow_ups[0].id, "happy_response_1");
    }

    #[test]
    fn test_conversation_path_generation() {
        let mut system = ConversationLogicSystem::new();

        // Build a simple conversation tree
        let nodes = vec![
            ConversationNodeBuilder::new("start".to_string())
                .input("What would you like to eat?")
                .add_tile("🍕", "Pizza")
                .add_tile("🍔", "Burger")
                .add_tile("🥗", "Salad")
                .add_tile("🍝", "Pasta")
                .category("food")
                .add_follow_up("Pizza", "pizza_toppings")
                .build(),
            ConversationNodeBuilder::new("pizza_toppings".to_string())
                .input("What toppings would you like?")
                .add_tile("🧀", "Cheese")
                .add_tile("🍄", "Mushrooms")
                .add_tile("🥓", "Bacon")
                .add_tile("🌶️", "Peppers")
                .category("food")
                .conversation_layer(2)
                .build(),
        ];

        for node in nodes {
            system.add_node(node);
        }

        // Generate a path
        let path = system.generate_conversation_path("start", 3);
        assert_eq!(path.nodes.len(), 2);
        assert_eq!(path.nodes[0], "start");
        assert_eq!(path.nodes[1], "pizza_toppings");
    }
}
