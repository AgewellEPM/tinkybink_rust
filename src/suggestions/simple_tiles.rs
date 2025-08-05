//! Simple AAC tiles for child to communicate with parent

use crate::core::events::{SuggestionTile, TileCategory};

/// Get basic communication tiles that are ALWAYS available
pub fn get_basic_tiles() -> Vec<SuggestionTile> {
    vec![
        // Basic needs
        SuggestionTile {
            emoji: "🍽️".to_string(),
            text: "I'm hungry".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "💧".to_string(),
            text: "I'm thirsty".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "🚽".to_string(),
            text: "Bathroom".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "😴".to_string(),
            text: "I'm tired".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
        
        // Emotions
        SuggestionTile {
            emoji: "😊".to_string(),
            text: "I'm happy".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "😢".to_string(),
            text: "I'm sad".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "🤕".to_string(),
            text: "It hurts".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "😡".to_string(),
            text: "I'm angry".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
        
        // Responses
        SuggestionTile {
            emoji: "✅".to_string(),
            text: "Yes".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "❌".to_string(),
            text: "No".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "🤷".to_string(),
            text: "I don't know".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "➕".to_string(),
            text: "More".to_string(),
            category: TileCategory::BasicResponse,
            confidence: 1.0,
        },
        
        // Activities
        SuggestionTile {
            emoji: "🎮".to_string(),
            text: "I want to play".to_string(),
            category: TileCategory::Action,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "📺".to_string(),
            text: "Watch TV".to_string(),
            category: TileCategory::Action,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "🏃".to_string(),
            text: "Go outside".to_string(),
            category: TileCategory::Action,
            confidence: 1.0,
        },
        SuggestionTile {
            emoji: "🤗".to_string(),
            text: "I need a hug".to_string(),
            category: TileCategory::Emotion,
            confidence: 1.0,
        },
    ]
}

/// Smart emoji mapping for any word
fn get_smart_emoji(word: &str) -> &'static str {
    let word_lower = word.to_lowercase();
    match word_lower.as_str() {
        // Places
        "park" => "🏞️",
        "home" | "house" => "🏠",
        "school" => "🏫",
        "store" | "shop" => "🏪",
        "playground" => "🎠",
        "beach" => "🏖️",
        "pool" => "🏊",
        "library" => "📚",
        "restaurant" => "🍽️",
        "car" => "🚗",
        "bus" => "🚌",
        "outside" => "🌳",
        "inside" => "🏠",
        "bed" | "bedroom" => "🛏️",
        "bathroom" => "🚽",
        "kitchen" => "🍳",
        
        // Food & Drink
        "eat" | "food" | "hungry" => "🍽️",
        "drink" | "thirsty" => "💧",
        "water" => "💧",
        "juice" => "🧃",
        "milk" => "🥛",
        "cookie" | "cookies" => "🍪",
        "apple" => "🍎",
        "banana" => "🍌",
        "pizza" => "🍕",
        "sandwich" => "🥪",
        "snack" => "🍿",
        "breakfast" => "🥞",
        "lunch" => "🥗",
        "dinner" => "🍝",
        "ice cream" => "🍦",
        "candy" => "🍬",
        "fruit" => "🍓",
        "vegetable" | "veggies" => "🥦",
        
        // Activities
        "play" => "🎮",
        "game" | "games" => "🎯",
        "tv" | "television" | "watch" => "📺",
        "movie" | "movies" => "🎬",
        "read" | "book" | "books" => "📚",
        "draw" | "drawing" | "art" => "🎨",
        "music" | "song" | "sing" => "🎵",
        "dance" | "dancing" => "💃",
        "swim" | "swimming" => "🏊",
        "run" | "running" => "🏃",
        "walk" | "walking" => "🚶",
        "sleep" | "nap" | "tired" => "😴",
        "bath" | "shower" => "🛁",
        "brush" => "🪥",
        "homework" => "📝",
        "computer" => "💻",
        "tablet" | "ipad" => "📱",
        
        // People
        "mom" | "mommy" | "mother" => "👩",
        "dad" | "daddy" | "father" => "👨",
        "grandma" | "grandmother" => "👵",
        "grandpa" | "grandfather" => "👴",
        "sister" => "👧",
        "brother" => "👦",
        "baby" => "👶",
        "friend" | "friends" => "👫",
        "teacher" => "👩‍🏫",
        
        // Emotions/States
        "happy" => "😊",
        "sad" => "😢",
        "angry" | "mad" => "😡",
        "scared" | "afraid" => "😨",
        "sick" | "hurt" => "🤒",
        "love" => "❤️",
        "hug" => "🤗",
        "kiss" => "😘",
        "hot" => "🥵",
        "cold" => "🥶",
        
        // Objects
        "toy" | "toys" => "🧸",
        "ball" => "⚽",
        "doll" => "🪆",
        "blocks" => "🧱",
        "puzzle" => "🧩",
        "clothes" => "👕",
        "shoes" => "👟",
        "jacket" | "coat" => "🧥",
        
        // Time
        "now" => "⏰",
        "later" => "⏳",
        "tomorrow" => "📅",
        "today" => "📆",
        "morning" => "🌅",
        "night" => "🌙",
        
        // Actions
        "go" => "👉",
        "stop" => "🛑",
        "wait" => "⏸️",
        "help" => "🆘",
        "share" => "🤝",
        "give" => "🤲",
        "take" => "✋",
        
        // Default
        _ => "💭"
    }
}

/// Extract key words from parent input
fn extract_key_words(text: &str) -> Vec<String> {
    let stop_words = vec!["the", "a", "an", "to", "do", "you", "want", "would", "like", 
                          "let's", "can", "we", "i", "me", "my", "your", "our", "go",
                          "is", "are", "was", "were", "be", "been", "have", "has"];
    
    text.to_lowercase()
        .split_whitespace()
        .map(|w| w.trim_matches(|c: char| !c.is_alphanumeric()))
        .filter(|w| !w.is_empty() && !stop_words.contains(&w))
        .map(|w| w.to_string())
        .collect()
}

/// Parse parent's input and create contextual response tiles
pub fn get_contextual_tiles(parent_input: &str) -> Vec<SuggestionTile> {
    let input_lower = parent_input.to_lowercase();
    let mut tiles = Vec::new();
    
    // Extract key words from parent input
    let key_words = extract_key_words(parent_input);
    
    // Look for specific patterns
    if input_lower.contains(" or ") {
        // Handle "X or Y" choices
        let parts: Vec<&str> = input_lower.split(" or ").collect();
        for part in parts {
            let choice_words = extract_key_words(part);
            if let Some(main_word) = choice_words.first() {
                let emoji = get_smart_emoji(main_word);
                tiles.push(SuggestionTile {
                    emoji: emoji.to_string(),
                    text: format!("Yes! {}", main_word.chars().next().unwrap().to_uppercase().collect::<String>() + &main_word[1..]),
                    category: TileCategory::Choice,
                    confidence: 1.0,
                });
            }
        }
    } else if !key_words.is_empty() {
        // For statements/questions, predict child responses based on key words
        let main_topic = key_words.first().unwrap();
        let emoji = get_smart_emoji(main_topic);
        
        // Generate contextual responses
        if input_lower.contains("let's") || input_lower.contains("let us") {
            // Responding to suggestions
            tiles.push(SuggestionTile {
                emoji: emoji.to_string(),
                text: format!("Yes! {}", main_topic),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            });
            tiles.push(SuggestionTile {
                emoji: "🚫".to_string(),
                text: format!("No {}", main_topic),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            });
            tiles.push(SuggestionTile {
                emoji: "⏳".to_string(),
                text: format!("{} later", main_topic.chars().next().unwrap().to_uppercase().collect::<String>() + &main_topic[1..]),
                category: TileCategory::BasicResponse,
                confidence: 0.8,
            });
        } else if input_lower.contains("?") {
            // Questions
            tiles.push(SuggestionTile {
                emoji: "✅".to_string(),
                text: "Yes".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            });
            tiles.push(SuggestionTile {
                emoji: "❌".to_string(),
                text: "No".to_string(),
                category: TileCategory::BasicResponse,
                confidence: 1.0,
            });
            if !key_words.is_empty() {
                tiles.push(SuggestionTile {
                    emoji: emoji.to_string(),
                    text: format!("I want {}", main_topic),
                    category: TileCategory::Choice,
                    confidence: 0.9,
                });
            }
        } else {
            // Statements - predict child's likely responses
            
            // Check all key words for better context
            let has_bed_context = key_words.iter().any(|w| matches!(w.as_str(), "bed" | "sleep" | "nap" | "tired" | "bedtime"));
            let has_food_context = key_words.iter().any(|w| matches!(w.as_str(), "eat" | "food" | "hungry" | "lunch" | "dinner" | "breakfast" | "snack"));
            let has_outside_context = key_words.iter().any(|w| matches!(w.as_str(), "park" | "outside" | "playground" | "walk" | "play"));
            
            if has_bed_context {
                tiles.push(SuggestionTile {
                    emoji: "😴".to_string(),
                    text: "I'm tired".to_string(),
                    category: TileCategory::Emotion,
                    confidence: 1.0,
                });
                tiles.push(SuggestionTile {
                    emoji: "⚡".to_string(),
                    text: "Not tired!".to_string(),
                    category: TileCategory::Emotion,
                    confidence: 0.9,
                });
                tiles.push(SuggestionTile {
                    emoji: "🧸".to_string(),
                    text: "Want teddy".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.8,
                });
                tiles.push(SuggestionTile {
                    emoji: "📚".to_string(),
                    text: "Story first".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.7,
                });
            } else if has_food_context {
                tiles.push(SuggestionTile {
                    emoji: "🍽️".to_string(),
                    text: "I'm hungry!".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 1.0,
                });
                tiles.push(SuggestionTile {
                    emoji: "🚫".to_string(),
                    text: "Not hungry".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.8,
                });
                tiles.push(SuggestionTile {
                    emoji: "💧".to_string(),
                    text: "Just thirsty".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.7,
                });
            } else if has_outside_context {
                tiles.push(SuggestionTile {
                    emoji: "🏞️".to_string(),
                    text: "Yes! Outside!".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 1.0,
                });
                tiles.push(SuggestionTile {
                    emoji: "🏠".to_string(),
                    text: "Stay home".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.8,
                });
                tiles.push(SuggestionTile {
                    emoji: "🧥".to_string(),
                    text: "Need jacket".to_string(),
                    category: TileCategory::BasicResponse,
                    confidence: 0.7,
                });
            } else {
                // Generic responses with topic emoji
                tiles.push(SuggestionTile {
                    emoji: emoji.to_string(),
                    text: format!("Yes {}", main_topic),
                    category: TileCategory::BasicResponse,
                    confidence: 0.9,
                });
                tiles.push(SuggestionTile {
                    emoji: "🚫".to_string(),
                    text: format!("No {}", main_topic),
                    category: TileCategory::BasicResponse,
                    confidence: 0.9,
                });
            }
        }
    }
    
    // Always add some fallback options
    tiles.push(SuggestionTile {
        emoji: "❓".to_string(),
        text: "I don't understand".to_string(),
        category: TileCategory::BasicResponse,
        confidence: 0.7,
    });
    
    tiles.push(SuggestionTile {
        emoji: "💭".to_string(),
        text: "Something else".to_string(),
        category: TileCategory::BasicResponse,
        confidence: 0.6,
    });
    
    tiles
}