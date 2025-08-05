#!/usr/bin/env python3
"""
Ultimate AAC Logic Tree Trainer
Processes all 49 JSON tile files to create comprehensive logic trees and decision patterns
"""
import json
import os
import re
from typing import Dict, List, Set, Tuple
from collections import defaultdict, Counter
import random

class UltimateAACTrainer:
    def __init__(self):
        self.tile_categories = {}
        self.context_mappings = {}
        self.logic_trees = {}
        self.training_examples = []
        
    def discover_json_files(self) -> List[str]:
        """Discover all TinkyBink JSON tile files"""
        json_files = []
        for file in os.listdir('.'):
            if file.startswith('tinkybink_') and file.endswith('.json'):
                json_files.append(file)
        
        print(f"🔍 Discovered {len(json_files)} TinkyBink JSON files")
        return sorted(json_files)
    
    def load_all_tile_data(self, json_files: List[str]) -> Dict:
        """Load and categorize all tile data"""
        all_data = {}
        categories = defaultdict(list)
        
        for file in json_files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    
                # Extract category from filename
                category = file.replace('tinkybink_', '').replace('_tiles.json', '').replace('.json', '')
                all_data[category] = data
                
                # Count tiles in each category
                if isinstance(data, dict):
                    if 'tiles' in data:
                        categories[category] = len(data['tiles'])
                    elif 'categories' in data:
                        total = sum(len(cat.get('tiles', [])) for cat in data['categories'].values())
                        categories[category] = total
                    else:
                        categories[category] = len(data)
                elif isinstance(data, list):
                    categories[category] = len(data)
                
            except Exception as e:
                print(f"⚠️ Error loading {file}: {e}")
        
        print(f"📊 Loaded data from {len(all_data)} categories")
        for cat, count in sorted(categories.items()):
            print(f"  - {cat}: {count} tiles")
        
        return all_data
    
    def analyze_tile_patterns(self, all_data: Dict) -> Dict:
        """Analyze patterns across all tile categories"""
        patterns = {
            'communication_types': defaultdict(list),
            'context_triggers': defaultdict(set),
            'response_categories': defaultdict(list),
            'user_scenarios': defaultdict(list),
            'tile_relationships': defaultdict(list)
        }
        
        for category, data in all_data.items():
            tiles = self.extract_tiles_from_data(data)
            
            for tile in tiles:
                # Analyze communication types
                comm_type = self.classify_communication_type(tile, category)
                patterns['communication_types'][comm_type].append(tile)
                
                # Extract context triggers
                triggers = self.extract_context_triggers(tile, category)
                for trigger in triggers:
                    patterns['context_triggers'][trigger].add(category)
                
                # Categorize response types
                response_cat = self.categorize_response_types(tile)
                patterns['response_categories'][response_cat].append(tile)
                
                # Generate user scenarios
                scenarios = self.generate_user_scenarios(tile, category)
                patterns['user_scenarios'][category].extend(scenarios)
        
        return patterns
    
    def extract_tiles_from_data(self, data) -> List[Dict]:
        """Extract individual tiles from various data structures"""
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
    
    def classify_communication_type(self, tile: Dict, category: str) -> str:
        """Classify the type of communication this tile represents"""
        text = str(tile.get('text', '')).lower()
        
        # Question types
        if any(word in text for word in ['what', 'how', 'why', 'when', 'where', 'who']):
            return 'question'
        
        # Request types
        if any(word in text for word in ['please', 'help', 'need', 'want', 'like']):
            return 'request'
        
        # Emotion types
        if any(word in text for word in ['happy', 'sad', 'angry', 'excited', 'scared', 'tired']):
            return 'emotion'
        
        # Action types
        if any(word in text for word in ['go', 'play', 'eat', 'sleep', 'stop', 'start']):
            return 'action'
        
        # Response types
        if any(word in text for word in ['yes', 'no', 'okay', 'maybe', 'sure']):
            return 'response'
        
        # Category-based classification
        if 'medical' in category or 'health' in category:
            return 'medical'
        elif 'social' in category or 'friend' in category:
            return 'social'
        elif 'emergency' in category or 'safety' in category:
            return 'emergency'
        elif 'school' in category or 'classroom' in category:
            return 'educational'
        
        return 'general'
    
    def extract_context_triggers(self, tile: Dict, category: str) -> List[str]:
        """Extract words/phrases that should trigger this tile"""
        triggers = []
        text = str(tile.get('text', '')).lower()
        
        # Add important words from the tile text
        important_words = re.findall(r'\b\w{3,}\b', text)
        triggers.extend(important_words[:3])  # Top 3 words
        
        # Add category-based triggers
        category_words = category.replace('_', ' ').split()
        triggers.extend(category_words)
        
        # Add semantic triggers based on category
        semantic_map = {
            'medical': ['doctor', 'hospital', 'pain', 'medicine', 'sick'],
            'food': ['hungry', 'eat', 'drink', 'meal', 'snack'],
            'emotion': ['feel', 'mood', 'happy', 'sad', 'angry'],
            'school': ['learn', 'teacher', 'homework', 'class'],
            'home': ['house', 'family', 'room', 'bed'],
            'play': ['game', 'toy', 'fun', 'friend'],
            'help': ['assist', 'support', 'need', 'please']
        }
        
        for key, words in semantic_map.items():
            if key in category:
                triggers.extend(words)
        
        return list(set(triggers))  # Remove duplicates
    
    def categorize_response_types(self, tile: Dict) -> str:
        """Categorize the type of response this tile provides"""
        text = str(tile.get('text', '')).lower()
        
        if any(word in text for word in ['yes', 'okay', 'sure', 'good']):
            return 'positive'
        elif any(word in text for word in ['no', 'not', 'stop', 'don\'t']):
            return 'negative'
        elif any(word in text for word in ['help', 'please', 'need']):
            return 'request'
        elif any(word in text for word in ['happy', 'sad', 'angry', 'excited']):
            return 'emotional'
        elif '?' in text:
            return 'question'
        else:
            return 'statement'
    
    def generate_user_scenarios(self, tile: Dict, category: str) -> List[Dict]:
        """Generate realistic user scenarios for this tile"""
        scenarios = []
        text = str(tile.get('text', ''))
        
        # Generate different scenario types
        scenario_templates = {
            'direct_request': f"I want {text}",
            'question_about': f"Can I have {text}?",
            'feeling_about': f"I feel {text}",
            'need_help_with': f"Help me with {text}",
            'want_to_do': f"Let's {text}",
            'time_for': f"Time for {text}",
            'where_is': f"Where is {text}?",
            'how_to': f"How do I {text}?",
        }
        
        # Select appropriate templates based on category and tile
        if 'emotion' in category:
            scenarios.append({'input': f"How are you feeling?", 'expected_tile': text})
        elif 'food' in category or 'cooking' in category:
            scenarios.append({'input': f"What would you like to eat?", 'expected_tile': text})
        elif 'medical' in category:
            scenarios.append({'input': f"How can I help you?", 'expected_tile': text})
        elif 'school' in category:
            scenarios.append({'input': f"What do you want to do at school?", 'expected_tile': text})
        else:
            scenarios.append({'input': f"What do you need?", 'expected_tile': text})
        
        return scenarios
    
    def build_comprehensive_logic_trees(self, patterns: Dict) -> Dict:
        """Build comprehensive logic trees from all patterns"""
        logic_trees = {}
        
        # Communication type trees
        for comm_type, tiles in patterns['communication_types'].items():
            logic_trees[f"communication_{comm_type}"] = {
                'type': 'communication_classifier',
                'classification': comm_type,
                'tile_options': [str(tile.get('text', '')) for tile in tiles[:8]],
                'triggers': list(patterns['context_triggers'].keys())[:5]
            }
        
        # Context-based trees
        for trigger, categories in patterns['context_triggers'].items():
            if len(categories) > 1:  # Only create trees for multi-category triggers
                logic_trees[f"context_{trigger}"] = {
                    'type': 'context_responder',
                    'trigger_word': trigger,
                    'relevant_categories': list(categories),
                    'response_strategy': 'context_aware'
                }
        
        # Scenario-based trees
        for category, scenarios in patterns['user_scenarios'].items():
            if scenarios:
                logic_trees[f"scenario_{category}"] = {
                    'type': 'scenario_handler',
                    'category': category,
                    'common_inputs': [s['input'] for s in scenarios[:5]],
                    'expected_responses': [s['expected_tile'] for s in scenarios[:5]]
                }
        
        return logic_trees
    
    def generate_comprehensive_training_data(self, logic_trees: Dict, patterns: Dict) -> List[Dict]:
        """Generate comprehensive training data from logic trees and patterns"""
        training_examples = []
        
        # Generate examples for each logic tree
        for tree_name, tree in logic_trees.items():
            examples = self.generate_tree_training_examples(tree_name, tree, patterns)
            training_examples.extend(examples)
        
        # Generate cross-category examples
        cross_examples = self.generate_cross_category_examples(patterns)
        training_examples.extend(cross_examples)
        
        # Generate user adaptation examples
        adaptation_examples = self.generate_user_adaptation_examples(patterns)
        training_examples.extend(adaptation_examples)
        
        return training_examples
    
    def generate_tree_training_examples(self, tree_name: str, tree: Dict, patterns: Dict) -> List[Dict]:
        """Generate training examples for a specific logic tree"""
        examples = []
        
        if tree['type'] == 'communication_classifier':
            classification = tree['classification']
            tile_options = tree['tile_options']
            
            # Create examples that teach the model to recognize this communication type
            input_examples = [
                f"I need help with {classification}",
                f"Can you help me {classification}?",
                f"What about {classification}?",
                f"Show me {classification} options"
            ]
            
            for input_text in input_examples:
                example = {
                    'instruction': f'AAC Logic: Provide {classification} communication options',
                    'input': input_text,
                    'output': ', '.join(tile_options[:4]),
                    'logic_tree': {
                        'type': 'communication_classification',
                        'category': classification,
                        'reasoning': f'User is asking for {classification} communication'
                    }
                }
                examples.append(example)
        
        elif tree['type'] == 'context_responder':
            trigger = tree['trigger_word']
            categories = tree['relevant_categories']
            
            # Create context-aware examples
            context_inputs = [
                f"I want to talk about {trigger}",
                f"Help me with {trigger}",
                f"What can I do with {trigger}?",
                f"Tell me about {trigger}"
            ]
            
            for input_text in context_inputs:
                # Get relevant tiles from the categories
                relevant_tiles = []
                for category in categories[:3]:  # Limit to 3 categories
                    if category in patterns['user_scenarios']:
                        scenarios = patterns['user_scenarios'][category][:2]
                        relevant_tiles.extend([s['expected_tile'] for s in scenarios])
                
                if relevant_tiles:
                    example = {
                        'instruction': f'AAC Logic: Context-aware responses for "{trigger}"',
                        'input': input_text,
                        'output': ', '.join(relevant_tiles[:4]),
                        'logic_tree': {
                            'type': 'context_triggered',
                            'trigger': trigger,
                            'categories': list(categories)
                        }
                    }
                    examples.append(example)
        
        elif tree['type'] == 'scenario_handler':
            category = tree['category']
            inputs = tree['common_inputs']
            responses = tree['expected_responses']
            
            # Create scenario-based examples
            for input_text, expected_response in zip(inputs, responses):
                example = {
                    'instruction': f'AAC Logic: Handle {category} scenario',
                    'input': input_text,
                    'output': expected_response,
                    'logic_tree': {
                        'type': 'scenario_based',
                        'category': category,
                        'scenario': 'direct_match'
                    }
                }
                examples.append(example)
        
        return examples
    
    def generate_cross_category_examples(self, patterns: Dict) -> List[Dict]:
        """Generate examples that require reasoning across multiple categories"""
        examples = []
        
        # Create complex scenarios that need multiple categories
        complex_scenarios = [
            {
                'input': "I'm not feeling well and need to go to the doctor",
                'categories': ['medical', 'health', 'emotions'],
                'expected_logic': 'Combine medical help with emotional support'
            },
            {
                'input': "Can we play a game after we eat dinner?",
                'categories': ['games', 'food', 'time'],
                'expected_logic': 'Sequence activities: food first, then play'
            },
            {
                'input': "I need help getting dressed for school",
                'categories': ['clothing', 'school', 'self_care'],
                'expected_logic': 'Morning routine assistance'
            },
            {
                'input': "My friend is coming over to cook with me",
                'categories': ['friendship', 'cooking', 'social'],
                'expected_logic': 'Social cooking activity'
            }
        ]
        
        for scenario in complex_scenarios:
            # Generate appropriate responses by combining category knowledge
            combined_responses = []
            for category in scenario['categories']:
                if category in patterns['user_scenarios']:
                    scenarios = patterns['user_scenarios'][category][:2]
                    combined_responses.extend([s['expected_tile'] for s in scenarios])
            
            if combined_responses:
                example = {
                    'instruction': 'AAC Logic: Multi-category reasoning',
                    'input': scenario['input'], 
                    'output': ', '.join(combined_responses[:4]),
                    'logic_tree': {
                        'type': 'cross_category',
                        'categories': scenario['categories'],
                        'reasoning': scenario['expected_logic']
                    }
                }
                examples.append(example)
        
        return examples
    
    def generate_user_adaptation_examples(self, patterns: Dict) -> List[Dict]:
        """Generate examples for different user types and contexts"""
        examples = []
        
        user_types = ['child', 'adult', 'elderly', 'stroke_survivor', 'medical_patient']
        adaptation_scenarios = [
            "How are you feeling today?",
            "What would you like to do?",
            "Do you need any help?",
            "Are you ready to go?",
            "What's your favorite activity?"
        ]
        
        for user_type in user_types:
            for scenario in adaptation_scenarios:
                # Adapt responses based on user type
                adapted_responses = self.adapt_responses_for_user_type(scenario, user_type, patterns)
                
                example = {
                    'instruction': f'AAC Logic: Adapt for {user_type} user',
                    'input': scenario,
                    'output': ', '.join(adapted_responses),
                    'logic_tree': {
                        'type': 'user_adaptation',
                        'user_type': user_type,
                        'adaptation_strategy': self.get_adaptation_strategy(user_type)
                    }
                }
                examples.append(example)
        
        return examples
    
    def adapt_responses_for_user_type(self, scenario: str, user_type: str, patterns: Dict) -> List[str]:
        """Adapt responses based on specific user type"""
        base_responses = ['Yes', 'No', 'Maybe', 'Help']
        
        if user_type == 'child':
            return ['Yes please!', 'No thank you', 'Maybe later', "I don't know"]
        elif user_type == 'adult':
            return ['Certainly', 'Not at this time', 'Let me consider', 'I need assistance']  
        elif user_type == 'elderly':
            return ['Yes dear', 'No thanks', 'Perhaps', 'Can you help me?']
        elif user_type == 'stroke_survivor':
            return ['Yes', 'No', 'Hard to say', 'Need help']
        elif user_type == 'medical_patient':
            return ['Feeling better', 'Not well', 'About the same', 'Call nurse']
        
        return base_responses
    
    def get_adaptation_strategy(self, user_type: str) -> str:
        """Get the adaptation strategy for a user type"""
        strategies = {
            'child': 'Use simple, enthusiastic language with emotional expressions',
            'adult': 'Use complete, respectful language with professional tone',
            'elderly': 'Use gentle, patient language with familiar terms',
            'stroke_survivor': 'Use short, clear phrases focused on immediate needs',
            'medical_patient': 'Use health-focused language with status indicators'
        }
        return strategies.get(user_type, 'Use clear, neutral language')
    
    def save_ultimate_training_data(self, examples: List[Dict], patterns: Dict, trees: Dict):
        """Save all training data and metadata"""
        
        # Save main training data
        with open('tinkybink_ultimate_logic_train.jsonl', 'w') as f:
            for example in examples:
                f.write(json.dumps(example) + '\n')
        
        # Save logic trees
        with open('aac_ultimate_logic_trees.json', 'w') as f:
            json.dump(trees, f, indent=2)
        
        # Save patterns analysis
        with open('aac_pattern_analysis.json', 'w') as f:
            # Convert sets to lists for JSON serialization
            serializable_patterns = {}
            for key, value in patterns.items():
                if key == 'context_triggers':
                    serializable_patterns[key] = {k: list(v) for k, v in value.items()}
                else:
                    serializable_patterns[key] = dict(value)
            json.dump(serializable_patterns, f, indent=2)
        
        print(f"💾 Saved {len(examples)} ultimate training examples")
        print(f"🌳 Saved {len(trees)} comprehensive logic trees") 
        print(f"📊 Saved pattern analysis covering {len(patterns)} pattern types")

def main():
    print("🚀 Ultimate AAC Logic Tree Trainer")
    print("=" * 50)
    print("Processing ALL 49 TinkyBink JSON tile files to create")
    print("the most comprehensive AAC training dataset ever!")
    print()
    
    trainer = UltimateAACTrainer()
    
    # Step 1: Discover all JSON files
    print("🔍 Step 1: Discovering TinkyBink JSON files...")
    json_files = trainer.discover_json_files()
    
    # Step 2: Load all tile data
    print(f"\n📥 Step 2: Loading data from {len(json_files)} files...")
    all_data = trainer.load_all_tile_data(json_files)
    
    # Step 3: Analyze patterns across all data
    print(f"\n🧠 Step 3: Analyzing patterns across all categories...")
    patterns = trainer.analyze_tile_patterns(all_data)
    
    print(f"   Communication types: {len(patterns['communication_types'])}")
    print(f"   Context triggers: {len(patterns['context_triggers'])}")
    print(f"   Response categories: {len(patterns['response_categories'])}")
    print(f"   User scenarios: {sum(len(v) for v in patterns['user_scenarios'].values())}")
    
    # Step 4: Build comprehensive logic trees
    print(f"\n🌳 Step 4: Building comprehensive logic trees...")
    logic_trees = trainer.build_comprehensive_logic_trees(patterns)
    print(f"   Created {len(logic_trees)} logic trees")
    
    # Step 5: Generate ultimate training data
    print(f"\n⚡ Step 5: Generating ultimate training dataset...")
    training_examples = trainer.generate_comprehensive_training_data(logic_trees, patterns)
    print(f"   Generated {len(training_examples)} training examples")
    
    # Step 6: Save everything
    print(f"\n💾 Step 6: Saving ultimate training data...")
    trainer.save_ultimate_training_data(training_examples, patterns, logic_trees)
    
    print(f"\n🎉 Ultimate AAC Training Complete!")
    print(f"📊 Processed {len(json_files)} JSON files")
    print(f"🌳 Created {len(logic_trees)} decision trees") 
    print(f"📚 Generated {len(training_examples)} training examples")
    print(f"🎯 Ready to train the ultimate AAC logic model!")

if __name__ == "__main__":
    main()