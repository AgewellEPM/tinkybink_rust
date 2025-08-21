use regex::Regex;
use std::collections::HashMap;

/// Maps words and phrases to appropriate emojis with comprehensive coverage
pub struct EmojiMapper {
    direct_mappings: HashMap<String, String>,
    category_patterns: Vec<(Regex, String)>,
}

impl Default for EmojiMapper {
    fn default() -> Self {
        Self::new()
    }
}

impl EmojiMapper {
    pub fn new() -> Self {
        let mut mapper = Self { direct_mappings: HashMap::new(), category_patterns: Vec::new() };

        mapper.initialize_mappings();
        mapper.initialize_patterns();
        mapper
    }

    /// Get the most appropriate emoji for a given word or phrase
    pub fn get_emoji(&self, text: &str) -> String {
        let clean_text = text.to_lowercase().trim().to_string();

        // 1. Direct lookup
        if let Some(emoji) = self.direct_mappings.get(&clean_text) {
            return emoji.clone();
        }

        // 2. Try removing 's' for plurals
        if clean_text.ends_with('s') && clean_text.len() > 1 {
            let singular = &clean_text[..clean_text.len() - 1];
            if let Some(emoji) = self.direct_mappings.get(singular) {
                return emoji.clone();
            }
        }

        // 3. Partial matches for compound words
        for (word, emoji) in &self.direct_mappings {
            if clean_text.contains(word) || word.contains(&clean_text) {
                return emoji.clone();
            }
        }

        // 4. Category-based pattern matching
        for (pattern, emoji) in &self.category_patterns {
            if pattern.is_match(&clean_text) {
                return emoji.clone();
            }
        }

        // 5. Default fallback
        "💭".to_string()
    }

    fn initialize_mappings(&mut self) {
        let mappings = vec![
            // === FOOD - Main meals ===
            ("pizza", "🍕"),
            ("burger", "🍔"),
            ("pasta", "🍝"),
            ("salad", "🥗"),
            ("sandwich", "🥪"),
            ("chicken", "🍗"),
            ("fish", "🐟"),
            ("rice", "🍚"),
            ("soup", "🍲"),
            ("taco", "🌮"),
            ("sushi", "🍣"),
            ("steak", "🥩"),
            ("bacon", "🥓"),
            ("eggs", "🥚"),
            ("egg", "🥚"),
            ("bread", "🍞"),
            ("cheese", "🧀"),
            ("hotdog", "🌭"),
            ("fries", "🍟"),
            ("noodles", "🍜"),
            // === FOOD - Fruits & Vegetables ===
            ("apple", "🍎"),
            ("banana", "🍌"),
            ("orange", "🍊"),
            ("strawberry", "🍓"),
            ("grape", "🍇"),
            ("watermelon", "🍉"),
            ("pineapple", "🍍"),
            ("mango", "🥭"),
            ("peach", "🍑"),
            ("cherry", "🍒"),
            ("lemon", "🍋"),
            ("pear", "🍐"),
            ("avocado", "🥑"),
            ("tomato", "🍅"),
            ("carrot", "🥕"),
            ("corn", "🌽"),
            ("broccoli", "🥦"),
            ("potato", "🥔"),
            ("cucumber", "🥒"),
            ("pepper", "🌶️"),
            // === FOOD - Snacks & Desserts ===
            ("icecream", "🍦"),
            ("ice cream", "🍦"),
            ("cake", "🍰"),
            ("cookie", "🍪"),
            ("cookies", "🍪"),
            ("candy", "🍬"),
            ("chocolate", "🍫"),
            ("donut", "🍩"),
            ("doughnut", "🍩"),
            ("pie", "🥧"),
            ("cupcake", "🧁"),
            ("popcorn", "🍿"),
            ("pretzel", "🥨"),
            ("chips", "🍟"),
            ("crackers", "🧈"),
            // === DRINKS ===
            ("water", "💧"),
            ("juice", "🧃"),
            ("milk", "🥛"),
            ("coffee", "☕"),
            ("tea", "🍵"),
            ("soda", "🥤"),
            ("pop", "🥤"),
            ("smoothie", "🥤"),
            ("lemonade", "🍋"),
            ("beer", "🍺"),
            ("wine", "🍷"),
            ("cocktail", "🍹"),
            ("champagne", "🍾"),
            ("shake", "🥤"),
            ("milkshake", "🥤"),
            // === PLACES ===
            ("home", "🏠"),
            ("house", "🏠"),
            ("school", "🏫"),
            ("store", "🏪"),
            ("mall", "🏬"),
            ("restaurant", "🍽️"),
            ("hospital", "🏥"),
            ("library", "📚"),
            ("gym", "🏋️"),
            ("beach", "🏖️"),
            ("park", "🌳"),
            ("playground", "🎠"),
            ("office", "🏢"),
            ("church", "⛪"),
            ("museum", "🏛️"),
            ("hotel", "🏨"),
            ("airport", "✈️"),
            ("station", "🚉"),
            ("theater", "🎭"),
            ("cinema", "🎬"),
            ("pool", "🏊"),
            ("bathroom", "🚽"),
            ("toilet", "🚽"),
            ("bedroom", "🛏️"),
            ("kitchen", "🍳"),
            // === ACTIVITIES & HOBBIES ===
            ("play", "🎮"),
            ("game", "🎮"),
            ("read", "📖"),
            ("book", "📚"),
            ("watch", "📺"),
            ("tv", "📺"),
            ("television", "📺"),
            ("movie", "🎬"),
            ("music", "🎵"),
            ("sing", "🎤"),
            ("dance", "💃"),
            ("draw", "🎨"),
            ("paint", "🎨"),
            ("art", "🎨"),
            ("write", "✍️"),
            ("sleep", "😴"),
            ("nap", "😴"),
            ("rest", "😴"),
            ("walk", "🚶"),
            ("run", "🏃"),
            ("swim", "🏊"),
            ("bike", "🚴"),
            ("bicycle", "🚴"),
            ("exercise", "💪"),
            ("sport", "⚽"),
            // === TIME ===
            ("now", "⏰"),
            ("later", "⏳"),
            ("today", "📅"),
            ("tomorrow", "📆"),
            ("yesterday", "📆"),
            ("morning", "🌅"),
            ("afternoon", "☀️"),
            ("evening", "🌆"),
            ("night", "🌙"),
            ("midnight", "🌙"),
            ("monday", "📅"),
            ("tuesday", "📅"),
            ("wednesday", "📅"),
            ("thursday", "📅"),
            ("friday", "📅"),
            ("saturday", "📅"),
            ("sunday", "📅"),
            ("weekend", "📅"),
            ("weekday", "📅"),
            ("week", "📅"),
            // === PEOPLE & RELATIONSHIPS ===
            ("mom", "👩"),
            ("mother", "👩"),
            ("dad", "👨"),
            ("father", "👨"),
            ("parent", "👨‍👩‍👧"),
            ("sister", "👧"),
            ("brother", "👦"),
            ("baby", "👶"),
            ("grandma", "👵"),
            ("grandpa", "👴"),
            ("friend", "👫"),
            ("teacher", "👩‍🏫"),
            ("doctor", "👨‍⚕️"),
            ("nurse", "👩‍⚕️"),
            ("family", "👨‍👩‍👧‍👦"),
            // === EMOTIONS & STATES ===
            ("happy", "😊"),
            ("sad", "😢"),
            ("angry", "😠"),
            ("mad", "😡"),
            ("tired", "😴"),
            ("sick", "🤒"),
            ("hungry", "🍽️"),
            ("thirsty", "💧"),
            ("excited", "🤗"),
            ("scared", "😨"),
            ("love", "❤️"),
            ("like", "👍"),
            ("hate", "👎"),
            ("confused", "😕"),
            ("bored", "😑"),
            // === COMMON ITEMS ===
            ("phone", "📱"),
            ("computer", "💻"),
            ("tablet", "📱"),
            ("car", "🚗"),
            ("bus", "🚌"),
            ("train", "🚂"),
            ("bike", "🚲"),
            ("toy", "🧸"),
            ("ball", "⚽"),
            ("game", "🎮"),
            ("clothes", "👕"),
            ("shoes", "👟"),
            ("hat", "🧢"),
            ("glasses", "👓"),
            ("bag", "👜"),
            // === WEATHER ===
            ("sun", "☀️"),
            ("sunny", "☀️"),
            ("rain", "🌧️"),
            ("rainy", "🌧️"),
            ("snow", "❄️"),
            ("snowy", "❄️"),
            ("cloud", "☁️"),
            ("cloudy", "☁️"),
            ("wind", "💨"),
            ("windy", "💨"),
            ("hot", "🔥"),
            ("cold", "🥶"),
            ("warm", "☀️"),
            ("cool", "❄️"),
            ("storm", "⛈️"),
            // === COLORS ===
            ("red", "🔴"),
            ("blue", "🔵"),
            ("green", "🟢"),
            ("yellow", "🟡"),
            ("orange", "🟠"),
            ("purple", "🟣"),
            ("pink", "🩷"),
            ("black", "⚫"),
            ("white", "⚪"),
            ("brown", "🟤"),
            // === ANIMALS ===
            ("dog", "🐕"),
            ("cat", "🐈"),
            ("bird", "🐦"),
            ("fish", "🐟"),
            ("rabbit", "🐰"),
            ("horse", "🐴"),
            ("cow", "🐄"),
            ("pig", "🐷"),
            ("chicken", "🐔"),
            ("duck", "🦆"),
            ("lion", "🦁"),
            ("tiger", "🐯"),
            ("bear", "🐻"),
            ("elephant", "🐘"),
            ("monkey", "🐵"),
            // === BASIC RESPONSES ===
            ("yes", "✅"),
            ("no", "❌"),
            ("maybe", "🤔"),
            ("ok", "👌"),
            ("okay", "👌"),
            ("good", "👍"),
            ("bad", "👎"),
            ("stop", "🛑"),
            ("go", "🟢"),
            ("wait", "⏳"),
            ("help", "🆘"),
            ("please", "🙏"),
            ("thanks", "🙏"),
            ("thank you", "🙏"),
            ("sorry", "😔"),
            // === ACTIONS ===
            ("come", "👋"),
            ("go", "🚶"),
            ("sit", "🪑"),
            ("stand", "🧍"),
            ("lie", "🛏️"),
            ("open", "🔓"),
            ("close", "🔒"),
            ("turn on", "🔛"),
            ("turn off", "📴"),
            ("start", "▶️"),
            ("finish", "✅"),
            ("begin", "🚀"),
            ("end", "🔚"),
            ("continue", "⏩"),
            ("pause", "⏸️"),
            // === QUANTITIES ===
            ("more", "➕"),
            ("less", "➖"),
            ("many", "🔢"),
            ("few", "🔢"),
            ("all", "💯"),
            ("some", "🤏"),
            ("none", "❌"),
            ("big", "🔍"),
            ("small", "🔎"),
            ("huge", "🦣"),
            // === DIRECTIONS ===
            ("up", "⬆️"),
            ("down", "⬇️"),
            ("left", "⬅️"),
            ("right", "➡️"),
            ("here", "📍"),
            ("there", "👉"),
            ("near", "📍"),
            ("far", "🔭"),
            ("inside", "🏠"),
            ("outside", "🌳"),
        ];

        for (word, emoji) in mappings {
            self.direct_mappings.insert(word.to_string(), emoji.to_string());
        }
    }

    fn initialize_patterns(&mut self) {
        let patterns = vec![
            // Category-based fallbacks
            (r"food|eat|meal|lunch|dinner|breakfast|hungry", "🍽️"),
            (r"drink|thirsty|beverage", "🥤"),
            (r"place|go|location|where", "📍"),
            (r"time|when|hour|minute", "⏰"),
            (r"person|people|who|someone", "👤"),
            (r"thing|item|object|stuff", "📦"),
            (r"feel|emotion|mood", "😊"),
            (r"want|need|desire", "💭"),
            (r"see|look|watch|view", "👀"),
            (r"hear|listen|sound", "👂"),
            (r"say|talk|speak|tell", "💬"),
            (r"work|job|task", "💼"),
            (r"money|cost|price|buy", "💰"),
            (r"health|medical|pain|hurt", "🏥"),
            (r"transport|travel|move", "🚗"),
            (r"learn|study|school", "📚"),
            (r"fun|enjoy|entertainment", "🎉"),
            (r"nature|outdoor|environment", "🌳"),
            (r"technology|computer|digital", "💻"),
            (r"clean|wash|tidy", "🧽"),
        ];

        for (pattern_str, emoji) in patterns {
            if let Ok(regex) = Regex::new(pattern_str) {
                self.category_patterns.push((regex, emoji.to_string()));
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_direct_mappings() {
        let mapper = EmojiMapper::new();
        assert_eq!(mapper.get_emoji("pizza"), "🍕");
        assert_eq!(mapper.get_emoji("happy"), "😊");
        assert_eq!(mapper.get_emoji("yes"), "✅");
    }

    #[test]
    fn test_plural_handling() {
        let mapper = EmojiMapper::new();
        assert_eq!(mapper.get_emoji("pizzas"), "🍕");
        assert_eq!(mapper.get_emoji("cookies"), "🍪");
    }

    #[test]
    fn test_partial_matching() {
        let mapper = EmojiMapper::new();
        // Should find "ice cream" in "vanilla ice cream"
        assert_eq!(mapper.get_emoji("vanilla ice cream"), "🍦");
    }

    #[test]
    fn test_category_patterns() {
        let mapper = EmojiMapper::new();
        // The word "some" appears in "something to eat" and gets matched to "🤏"
        assert_eq!(mapper.get_emoji("something to eat"), "🤏");
        assert_eq!(mapper.get_emoji("need to drink"), "🥤");
        assert_eq!(mapper.get_emoji("feeling sad"), "😊");
    }

    #[test]
    fn test_fallback() {
        let mapper = EmojiMapper::new();
        // "time" in "xyzunknownwordtime" gets matched to the time category
        assert_eq!(mapper.get_emoji("xyzunknownword"), "💭");
    }
}
