#!/usr/bin/env python3
"""
Emoji Logic Integrator
Hooks up emoji mapping with all JSON tile data and logic trees
"""
import json
import re
from typing import Dict, List, Set
from collections import defaultdict

class EmojiLogicIntegrator:
    def __init__(self):
        self.emoji_mappings = {}
        self.contextual_emojis = {}
        self.category_emojis = {}
        self.load_emoji_mappings()
    
    def load_emoji_mappings(self):
        """Load comprehensive emoji mappings for AAC tiles"""
        
        # Core emotion emojis
        self.emoji_mappings.update({
            # Basic emotions
            'happy': '😊', 'sad': '😢', 'angry': '😠', 'excited': '🤩',
            'scared': '😨', 'tired': '😴', 'sick': '🤒', 'hurt': '🤕',
            'love': '❤️', 'laugh': '😂', 'cry': '😭', 'worry': '😰',
            
            # Basic responses
            'yes': '✅', 'no': '❌', 'maybe': '🤔', 'help': '🆘',
            'please': '🙏', 'thank you': '🙏', 'sorry': '😔', 'okay': '👍',
            
            # Actions
            'eat': '🍽️', 'drink': '🥤', 'sleep': '😴', 'play': '🎮',
            'walk': '🚶', 'run': '🏃', 'sit': '🪑', 'stand': '🧍',
            'go': '➡️', 'stop': '🛑', 'wait': '⏰', 'come': '👋',
            
            # Places
            'home': '🏠', 'school': '🏫', 'hospital': '🏥', 'park': '🏞️',
            'store': '🏪', 'bathroom': '🚽', 'kitchen': '🍳', 'bedroom': '🛏️',
            
            # People
            'mom': '👩', 'dad': '👨', 'teacher': '👩‍🏫', 'doctor': '👩‍⚕️',
            'friend': '👫', 'family': '👨‍👩‍👧‍👦', 'baby': '👶', 'child': '👧',
            
            # Body parts
            'head': '🗣️', 'eyes': '👀', 'mouth': '👄', 'hands': '🙌',
            'feet': '🦶', 'stomach': '🤰', 'back': '🔙', 'heart': '❤️',
            
            # Food & drinks
            'food': '🍽️', 'water': '💧', 'milk': '🥛', 'juice': '🧃',
            'apple': '🍎', 'banana': '🍌', 'cookie': '🍪', 'bread': '🍞',
            
            # Activities
            'read': '📖', 'write': '✏️', 'draw': '🎨', 'music': '🎵',
            'dance': '💃', 'sing': '🎤', 'watch': '👁️', 'listen': '👂',
            
            # Medical/therapy
            'medicine': '💊', 'therapy': '🏥', 'exercise': '🏃‍♀️', 'rest': '😴',
            'pain': '🤕', 'better': '😌', 'worse': '😣', 'same': '🔄',
            
            # Emergency/safety
            'emergency': '🚨', 'danger': '⚠️', 'safe': '🛡️', 'call': '📞',
            'fire': '🔥', 'police': '👮', 'ambulance': '🚑', 'exit': '🚪',
            
            # Weather/time
            'sunny': '☀️', 'rainy': '🌧️', 'cold': '🥶', 'hot': '🥵',
            'morning': '🌅', 'night': '🌙', 'today': '📅', 'tomorrow': '📆',
            
            # Transportation
            'car': '🚗', 'bus': '🚌', 'train': '🚂', 'bike': '🚴',
            'walk': '🚶', 'wheelchair': '♿', 'taxi': '🚕', 'plane': '✈️',
            
            # Technology
            'phone': '📱', 'computer': '💻', 'tv': '📺', 'tablet': '📱',
            'camera': '📷', 'music': '🎵', 'video': '📹', 'game': '🎮',
            
            # Clothing
            'shirt': '👕', 'pants': '👖', 'shoes': '👟', 'hat': '🧢',
            'coat': '🧥', 'dress': '👗', 'socks': '🧦', 'glasses': '👓',
        })
        
        # Category-specific emoji mappings
        self.category_emojis = {
            'medical_healthcare': '🏥',
            'emotions_feelings': '😊',
            'food_nutrition': '🍽️',
            'transportation_travel': '🚗',
            'school': '🏫',
            'home': '🏠',
            'family': '👨‍👩‍👧‍👦',
            'friends': '👫',
            'play': '🎮',
            'work': '💼',
            'safety': '🛡️',
            'emergency': '🚨',
            'body_parts': '🗣️',
            'clothing': '👕',
            'weather': '☀️',
            'time': '⏰',
            'animals': '🐶',
            'nature': '🌳',
            'sports': '⚽',
            'music': '🎵',
            'art': '🎨',
            'technology': '💻',
            'cooking': '🍳',
            'cleaning': '🧹',
            'shopping': '🛒',
            'money': '💰'
        }
    
    def extract_emoji_patterns_from_tiles(self, json_files: List[str]) -> Dict:
        """Extract emoji patterns from all tile JSON files"""
        emoji_patterns = defaultdict(list)
        
        for file in json_files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                
                category = file.replace('tinkybink_', '').replace('_tiles.json', '').replace('.json', '')
                tiles = self.extract_tiles_from_data(data)
                
                for tile in tiles:
                    text = str(tile.get('text', ''))
                    emoji = tile.get('emoji', '')
                    
                    if emoji:
                        # Direct emoji mapping from tile
                        emoji_patterns[text.lower()].append(emoji)
                    else:
                        # Generate emoji based on text content
                        generated_emoji = self.generate_contextual_emoji(text, category)
                        if generated_emoji:
                            emoji_patterns[text.lower()].append(generated_emoji)
                            
            except Exception as e:
                print(f"⚠️ Error processing {file}: {e}")
        
        return emoji_patterns
    
    def extract_tiles_from_data(self, data) -> List[Dict]:
        """Extract tiles from various JSON structures"""
        tiles = []
        
        if isinstance(data, list):
            tiles = data
        elif isinstance(data, dict):
            if 'tiles' in data:
                tiles = data['tiles']
            elif 'categories' in data:
                for cat_data in data['categories'].values():
                    if isinstance(cat_data, dict) and 'tiles' in cat_data:
                        tiles.extend(cat_data['tiles'])
            else:
                # Treat each key-value as a tile
                for key, value in data.items():
                    if isinstance(value, (str, dict)):
                        tiles.append({'text': key, 'data': value})
        
        return tiles
    
    def generate_contextual_emoji(self, text: str, category: str) -> str:
        """Generate contextually appropriate emoji for text"""
        text_lower = text.lower()
        
        # First check direct mappings
        for word, emoji in self.emoji_mappings.items():
            if word in text_lower:
                return emoji
        
        # Then check category-based mappings
        for cat_key, emoji in self.category_emojis.items():
            if cat_key in category:
                return emoji
        
        # Context-specific logic
        if 'medical' in category or 'health' in category:
            if any(word in text_lower for word in ['pain', 'hurt', 'sick']):
                return '🤕'
            elif any(word in text_lower for word in ['better', 'good', 'fine']):
                return '😌'
            elif any(word in text_lower for word in ['medicine', 'pill', 'medication']):
                return '💊'
            else:
                return '🏥'
        
        elif 'emotion' in category or 'feeling' in category:
            if any(word in text_lower for word in ['happy', 'joy', 'glad']):
                return '😊'
            elif any(word in text_lower for word in ['sad', 'upset', 'cry']):
                return '😢'
            elif any(word in text_lower for word in ['angry', 'mad', 'frustrated']):
                return '😠'
            else:
                return '💭'
        
        elif 'food' in category or 'cooking' in category:
            if any(word in text_lower for word in ['hungry', 'eat', 'meal']):
                return '🍽️'
            elif any(word in text_lower for word in ['drink', 'thirsty', 'water']):
                return '🥤'
            else:
                return '🍎'
        
        elif 'school' in category or 'classroom' in category:
            if any(word in text_lower for word in ['read', 'book', 'study']):
                return '📖'
            elif any(word in text_lower for word in ['write', 'pencil', 'pen']):
                return '✏️'
            else:
                return '🏫'
        
        elif 'play' in category or 'game' in category:
            if any(word in text_lower for word in ['toy', 'doll', 'block']):
                return '🧸'
            elif any(word in text_lower for word in ['ball', 'sport']):
                return '⚽'
            else:
                return '🎮'
        
        elif 'transportation' in category or 'travel' in category:
            if any(word in text_lower for word in ['car', 'drive']):
                return '🚗'
            elif any(word in text_lower for word in ['bus', 'public']):
                return '🚌'
            elif any(word in text_lower for word in ['walk', 'foot']):
                return '🚶'
            else:
                return '🚗'
        
        # Default fallback emojis
        if any(word in text_lower for word in ['i', 'me', 'my', 'want', 'need']):
            return '👤'
        elif any(word in text_lower for word in ['you', 'help', 'please']):
            return '🤝'
        elif '?' in text:
            return '❓'
        elif '!' in text:
            return '❗'
        else:
            return '💬'
    
    def create_emoji_enhanced_training_data(self, base_training_file: str) -> List[Dict]:
        """Enhance existing training data with proper emoji mappings"""
        enhanced_examples = []
        
        # Load existing training data
        try:
            with open(base_training_file, 'r') as f:
                for line in f:
                    if line.strip():
                        example = json.loads(line)
                        enhanced_example = self.enhance_example_with_emojis(example)
                        enhanced_examples.append(enhanced_example)
        except FileNotFoundError:
            print(f"⚠️ Training file {base_training_file} not found")
        
        return enhanced_examples
    
    def enhance_example_with_emojis(self, example: Dict) -> Dict:
        """Add proper emoji mappings to a training example"""
        enhanced = example.copy()
        
        # Extract responses and add emojis
        output = example.get('output', '')
        responses = [r.strip() for r in output.split(',') if r.strip()]
        
        enhanced_responses = []
        for response in responses:
            emoji = self.get_best_emoji_for_response(response, example)
            enhanced_responses.append(f"{emoji} {response}")
        
        enhanced['output'] = ', '.join(enhanced_responses)
        
        # Add emoji logic to the instruction
        if 'logic_tree' in enhanced:
            enhanced['logic_tree']['emoji_mapping'] = {
                'strategy': 'contextual_semantic',
                'fallback': '💬'
            }
        
        return enhanced
    
    def get_best_emoji_for_response(self, response: str, context: Dict) -> str:
        """Get the best emoji for a specific response in context"""
        response_lower = response.lower()
        
        # Check direct mappings first
        for word, emoji in self.emoji_mappings.items():
            if word in response_lower:
                return emoji
        
        # Context-aware mapping
        input_text = context.get('input', '').lower()
        
        # Medical context
        if any(word in input_text for word in ['pain', 'therapy', 'doctor', 'medicine']):
            if 'yes' in response_lower or 'better' in response_lower:
                return '✅'
            elif 'no' in response_lower or 'worse' in response_lower:
                return '❌'
            elif 'help' in response_lower:
                return '🆘'
            elif 'thank' in response_lower:
                return '🙏'
        
        # Emotion context
        elif any(word in input_text for word in ['feel', 'mood', 'emotion']):
            if any(word in response_lower for word in ['good', 'great', 'happy', 'fine']):
                return '😊'
            elif any(word in response_lower for word in ['bad', 'sad', 'upset']):
                return '😢'
            elif 'tired' in response_lower:
                return '😴'
            elif 'okay' in response_lower:
                return '😐'
        
        # Activity context
        elif any(word in input_text for word in ['play', 'go', 'do', 'want']):
            if 'yes' in response_lower:
                return '✅'
            elif 'no' in response_lower:
                return '❌'
            elif 'maybe' in response_lower:
                return '🤔'
            elif 'later' in response_lower:
                return '⏰'
        
        # Food context
        elif any(word in input_text for word in ['eat', 'drink', 'hungry', 'food']):
            if any(word in response_lower for word in ['yes', 'want', 'hungry']):
                return '🍽️'
            elif 'water' in response_lower:
                return '💧'
            elif 'not' in response_lower:
                return '❌'
        
        # Default response emojis
        if 'yes' in response_lower:
            return '✅'
        elif 'no' in response_lower:
            return '❌'
        elif 'maybe' in response_lower:
            return '🤔'
        elif 'help' in response_lower:
            return '🆘'
        elif 'please' in response_lower or 'thank' in response_lower:
            return '🙏'
        elif 'sorry' in response_lower:
            return '😔'
        elif response_lower.startswith('i '):
            return '👤'
        else:
            return '💬'
    
    def generate_emoji_training_examples(self) -> List[Dict]:
        """Generate specific training examples for emoji logic"""
        emoji_examples = []
        
        # Emoji selection training
        emoji_scenarios = [
            {
                'input': 'I am feeling happy today',
                'expected_emojis': ['😊', '😄', '🤗', '✨'],
                'context': 'emotion_positive'
            },
            {
                'input': 'My stomach hurts',
                'expected_emojis': ['🤕', '😣', '🆘', '💊'],
                'context': 'medical_pain'
            },
            {
                'input': 'Can we go to the park?',
                'expected_emojis': ['🏞️', '✅', '❌', '🤔'],
                'context': 'activity_request'
            },
            {
                'input': 'I want some water',
                'expected_emojis': ['💧', '🥤', '🙏', '✅'],
                'context': 'need_drink'
            },
            {
                'input': 'Help me please',
                'expected_emojis': ['🆘', '🤝', '🙏', '👤'],
                'context': 'request_help'
            }
        ]
        
        for scenario in emoji_scenarios:
            example = {
                'instruction': 'AAC Emoji Logic: Select contextually appropriate emojis',
                'input': scenario['input'],
                'output': ', '.join([f"{emoji} {word}" for emoji, word in 
                                   zip(scenario['expected_emojis'], 
                                       ['Yes', 'Help needed', 'Maybe', 'Thank you'])]),
                'emoji_logic': {
                    'context': scenario['context'],
                    'emoji_strategy': 'semantic_contextual',
                    'mappings': dict(zip(['Yes', 'Help needed', 'Maybe', 'Thank you'], 
                                        scenario['expected_emojis']))
                }
            }
            emoji_examples.append(example)
        
        return emoji_examples
    
    def save_emoji_enhanced_dataset(self, json_files: List[str]):
        """Create and save the ultimate emoji-enhanced dataset"""
        print("🎨 Creating Emoji-Enhanced AAC Training Dataset")
        print("=" * 50)
        
        # Step 1: Extract emoji patterns from tiles
        print("🔍 Extracting emoji patterns from tile data...")
        emoji_patterns = self.extract_emoji_patterns_from_tiles(json_files)
        print(f"   Found emoji patterns for {len(emoji_patterns)} concepts")
        
        # Step 2: Enhance existing training data
        print("✨ Enhancing training data with emojis...")
        enhanced_examples = self.create_emoji_enhanced_training_data('tinkybink_master_train.jsonl')
        print(f"   Enhanced {len(enhanced_examples)} training examples")
        
        # Step 3: Generate emoji-specific training
        print("🎯 Generating emoji logic training examples...")
        emoji_examples = self.generate_emoji_training_examples()
        print(f"   Generated {len(emoji_examples)} emoji logic examples")
        
        # Step 4: Combine everything
        all_examples = enhanced_examples + emoji_examples
        
        # Step 5: Save the dataset
        with open('tinkybink_emoji_master_train.jsonl', 'w') as f:
            for example in all_examples:
                f.write(json.dumps(example) + '\n')
        
        # Save emoji mappings
        with open('aac_emoji_mappings.json', 'w') as f:
            json.dump({
                'direct_mappings': self.emoji_mappings,
                'category_mappings': self.category_emojis,
                'contextual_patterns': dict(emoji_patterns)
            }, f, indent=2)
        
        print(f"\n💾 Saved {len(all_examples)} emoji-enhanced examples")
        print(f"🎨 Saved comprehensive emoji mappings")
        print(f"🎯 Ready for emoji-aware AAC model training!")
        
        return len(all_examples)

def main():
    print("🎨 AAC Emoji Logic Integration")
    print("=" * 40)
    
    integrator = EmojiLogicIntegrator()
    
    # Discover JSON files
    import os
    json_files = [f for f in os.listdir('.') if f.startswith('tinkybink_') and f.endswith('.json')]
    print(f"🔍 Found {len(json_files)} JSON tile files")
    
    # Create emoji-enhanced dataset
    total_examples = integrator.save_emoji_enhanced_dataset(json_files)
    
    print(f"\n🎉 Emoji Integration Complete!")
    print(f"📊 Total examples: {total_examples}")
    print(f"🎨 Emoji mappings: {len(integrator.emoji_mappings)}")
    print(f"🏷️ Category emojis: {len(integrator.category_emojis)}")

if __name__ == "__main__":
    main()