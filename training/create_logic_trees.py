#!/usr/bin/env python3
"""
Advanced AAC Logic Tree Training System
Uses all JSON data to create proper decision trees and contextual patterns
"""
import json
import re
from typing import Dict, List, Tuple, Set
from collections import defaultdict
import random

class AACLogicTreeBuilder:
    def __init__(self):
        self.patterns = defaultdict(list)
        self.context_trees = {}
        self.user_type_patterns = {}
        self.decision_nodes = {}
        
    def analyze_existing_data(self):
        """Analyze all existing JSON training data"""
        datasets = [
            'tinkybink_training.jsonl',
            'tinkybink_adult_train.jsonl'
        ]
        
        all_examples = []
        for dataset in datasets:
            try:
                with open(dataset, 'r') as f:
                    for line in f:
                        if line.strip():
                            all_examples.append(json.loads(line))
            except FileNotFoundError:
                print(f"⚠️ Dataset {dataset} not found, skipping...")
        
        print(f"📊 Analyzing {len(all_examples)} existing examples...")
        return all_examples
    
    def extract_logic_patterns(self, examples: List[Dict]) -> Dict:
        """Extract logical decision patterns from training data"""
        patterns = {
            'question_types': defaultdict(list),
            'response_categories': defaultdict(list),
            'context_triggers': defaultdict(list),
            'user_adaptations': defaultdict(list)
        }
        
        for example in examples:
            input_text = example.get('input', '').lower()
            output_text = example.get('output', '')
            metadata = example.get('metadata', {})
            
            # Extract question types
            if '?' in input_text:
                question_type = self.classify_question_type(input_text)
                patterns['question_types'][question_type].append({
                    'input': input_text,
                    'responses': output_text.split(', ')
                })
            
            # Extract context triggers
            context_words = self.extract_context_words(input_text)
            for word in context_words:
                patterns['context_triggers'][word].append(output_text.split(', '))
            
            # Extract user type adaptations
            if metadata:
                user_type = metadata.get('user_type', 'general')
                patterns['user_adaptations'][user_type].append({
                    'input': input_text,
                    'responses': output_text.split(', ')
                })
        
        return patterns
    
    def classify_question_type(self, text: str) -> str:
        """Classify the type of question for decision tree logic"""
        text = text.lower()
        
        # Yes/No questions
        if any(starter in text for starter in ['do you', 'are you', 'will you', 'can you', 'would you']):
            return 'yes_no_question'
        
        # Choice questions  
        if ' or ' in text and text.count(' or ') <= 3:
            return 'choice_question'
        
        # Feeling/emotion questions
        if any(word in text for word in ['feel', 'feeling', 'mood', 'emotion', 'happy', 'sad']):
            return 'emotion_question'
        
        # Need/want questions
        if any(word in text for word in ['need', 'want', 'like', 'prefer']):
            return 'preference_question'
        
        # Medical/health questions
        if any(word in text for word in ['pain', 'hurt', 'sick', 'medicine', 'doctor', 'therapy']):
            return 'medical_question'
        
        # Activity questions
        if any(word in text for word in ['go', 'play', 'do', 'watch', 'eat', 'sleep']):
            return 'activity_question'
        
        # Time-related questions
        if any(word in text for word in ['time', 'when', 'now', 'later', 'ready']):
            return 'timing_question'
        
        return 'general_question'
    
    def extract_context_words(self, text: str) -> List[str]:
        """Extract important context words that should trigger specific responses"""
        important_words = []
        
        # Medical contexts
        medical_words = ['pain', 'hurt', 'medicine', 'doctor', 'therapy', 'hospital', 'nurse']
        # Activity contexts  
        activity_words = ['park', 'play', 'eat', 'sleep', 'bath', 'bed', 'food', 'drink']
        # Emotion contexts
        emotion_words = ['happy', 'sad', 'angry', 'tired', 'scared', 'excited']
        # Social contexts
        social_words = ['friend', 'family', 'mom', 'dad', 'teacher', 'school']
        
        all_context_words = medical_words + activity_words + emotion_words + social_words
        
        for word in all_context_words:
            if word in text.lower():
                important_words.append(word)
        
        return important_words
    
    def build_decision_trees(self, patterns: Dict) -> Dict:
        """Build decision trees for different AAC scenarios"""
        decision_trees = {}
        
        # Build question type decision trees
        for q_type, examples in patterns['question_types'].items():
            decision_trees[q_type] = self.create_question_decision_tree(q_type, examples)
        
        # Build context-based decision trees
        for context, response_sets in patterns['context_triggers'].items():
            decision_trees[f"context_{context}"] = self.create_context_decision_tree(context, response_sets)
        
        # Build user-type decision trees
        for user_type, examples in patterns['user_adaptations'].items():
            decision_trees[f"user_{user_type}"] = self.create_user_type_decision_tree(user_type, examples)
        
        return decision_trees
    
    def create_question_decision_tree(self, q_type: str, examples: List[Dict]) -> Dict:
        """Create decision tree for specific question types"""
        tree = {
            'type': 'question_classifier',
            'question_type': q_type,
            'decision_logic': {},
            'fallback_responses': []
        }
        
        # Analyze common response patterns
        all_responses = []
        for example in examples:
            all_responses.extend(example['responses'])
        
        # Group similar responses
        response_groups = self.group_similar_responses(all_responses)
        
        if q_type == 'yes_no_question':
            tree['decision_logic'] = {
                'primary_responses': ['Yes', 'No'],
                'elaboration_responses': response_groups.get('elaborative', []),
                'emotional_responses': response_groups.get('emotional', [])
            }
        elif q_type == 'choice_question':
            tree['decision_logic'] = {
                'extract_choices': True,
                'add_maybe_option': True,
                'add_none_option': True
            }
        elif q_type == 'emotion_question':
            tree['decision_logic'] = {
                'emotion_scale': ['Great', 'Good', 'Okay', 'Not good', 'Bad'],
                'specific_emotions': response_groups.get('emotional', [])
            }
        
        return tree
    
    def create_context_decision_tree(self, context: str, response_sets: List[List[str]]) -> Dict:
        """Create decision tree for specific contexts"""
        tree = {
            'type': 'context_responder',
            'context_word': context,
            'response_patterns': []
        }
        
        # Analyze response patterns for this context
        common_responses = []
        for response_set in response_sets:
            common_responses.extend(response_set)
        
        # Find most common responses
        response_counts = defaultdict(int)
        for response in common_responses:
            response_counts[response.strip()] += 1
        
        # Top responses for this context
        top_responses = sorted(response_counts.items(), key=lambda x: x[1], reverse=True)[:4]
        tree['response_patterns'] = [resp[0] for resp in top_responses]
        
        return tree
    
    def create_user_type_decision_tree(self, user_type: str, examples: List[Dict]) -> Dict:
        """Create decision tree adapted for specific user types"""
        tree = {
            'type': 'user_adaptation',
            'user_type': user_type,
            'complexity_level': 'medium',
            'vocabulary_style': 'neutral',
            'response_length': 'short'
        }
        
        # Analyze user-specific patterns
        if user_type == 'adult':
            tree['complexity_level'] = 'high'
            tree['vocabulary_style'] = 'professional'
            tree['response_length'] = 'medium'
        elif 'child' in user_type.lower():
            tree['complexity_level'] = 'low'
            tree['vocabulary_style'] = 'simple'
            tree['response_length'] = 'short'
        elif 'medical' in user_type.lower() or 'stroke' in user_type.lower():
            tree['complexity_level'] = 'medium'
            tree['vocabulary_style'] = 'medical'
            tree['response_length'] = 'short'
        
        return tree
    
    def group_similar_responses(self, responses: List[str]) -> Dict[str, List[str]]:
        """Group responses by similarity and type"""
        groups = {
            'positive': [],
            'negative': [],
            'neutral': [],
            'emotional': [],
            'elaborative': []
        }
        
        for response in responses:
            response = response.strip()
            if not response:
                continue
                
            response_lower = response.lower()
            
            # Positive responses
            if any(word in response_lower for word in ['yes', 'okay', 'good', 'great', 'sure', 'fine']):
                groups['positive'].append(response)
            # Negative responses
            elif any(word in response_lower for word in ['no', 'not', 'dont', "don't", 'never', 'bad']):
                groups['negative'].append(response)
            # Emotional responses
            elif any(word in response_lower for word in ['happy', 'sad', 'angry', 'excited', 'scared', 'tired']):
                groups['emotional'].append(response)
            # Elaborative responses
            elif len(response.split()) > 3:
                groups['elaborative'].append(response)
            else:
                groups['neutral'].append(response)
        
        return groups
    
    def generate_advanced_training_data(self, decision_trees: Dict) -> List[Dict]:
        """Generate advanced training data based on decision trees"""
        advanced_examples = []
        
        # Generate examples for each decision tree
        for tree_name, tree in decision_trees.items():
            examples = self.generate_tree_examples(tree_name, tree)
            advanced_examples.extend(examples)
        
        return advanced_examples
    
    def generate_tree_examples(self, tree_name: str, tree: Dict) -> List[Dict]:
        """Generate training examples for a specific decision tree"""
        examples = []
        
        if tree['type'] == 'question_classifier':
            examples.extend(self.generate_question_examples(tree))
        elif tree['type'] == 'context_responder':
            examples.extend(self.generate_context_examples(tree))
        elif tree['type'] == 'user_adaptation':
            examples.extend(self.generate_user_adaptation_examples(tree))
        
        return examples
    
    def generate_question_examples(self, tree: Dict) -> List[Dict]:
        """Generate examples for question classification logic"""
        examples = []
        q_type = tree['question_type']
        
        # Create logic-based training examples
        if q_type == 'yes_no_question':
            base_questions = [
                "Do you want to go outside?",
                "Are you feeling tired?", 
                "Would you like some water?",
                "Can you help me?"
            ]
            
            for question in base_questions:
                example = {
                    'instruction': f'AAC Logic: Detect yes/no question and provide binary + elaborative options',
                    'input': question,
                    'output': 'Yes, No, Maybe, Not sure',
                    'logic_tree': {
                        'type': 'binary_decision',
                        'primary_options': ['Yes', 'No'],
                        'secondary_options': ['Maybe', 'Not sure']
                    }
                }
                examples.append(example)
        
        elif q_type == 'choice_question':
            choice_questions = [
                "Do you want apple or orange?",
                "Should we play inside or outside?",
                "Would you like juice, water, or milk?"
            ]
            
            for question in choice_questions:
                # Extract choices from question
                choices = self.extract_choices_from_question(question)
                example = {
                    'instruction': 'AAC Logic: Extract choices from question and add neutral options',
                    'input': question,
                    'output': ', '.join(choices + ['Maybe', 'Neither']),
                    'logic_tree': {
                        'type': 'choice_extraction',
                        'extracted_choices': choices,
                        'neutral_options': ['Maybe', 'Neither']
                    }
                }
                examples.append(example)
        
        return examples
    
    def generate_context_examples(self, tree: Dict) -> List[Dict]:
        """Generate examples for context-based responses"""
        examples = []
        context_word = tree['context_word']
        responses = tree['response_patterns']
        
        # Create context-aware examples
        context_sentences = [
            f"Let's go to the {context_word}",
            f"How do you feel about {context_word}?",
            f"It's time for {context_word}",
            f"Do you need help with {context_word}?"
        ]
        
        for sentence in context_sentences:
            example = {
                'instruction': f'AAC Logic: Context-aware responses for "{context_word}"',
                'input': sentence,
                'output': ', '.join(responses),
                'logic_tree': {
                    'type': 'context_triggered',
                    'trigger_word': context_word,
                    'context_responses': responses
                }
            }
            examples.append(example)
        
        return examples
    
    def generate_user_adaptation_examples(self, tree: Dict) -> List[Dict]:
        """Generate examples for user type adaptations"""
        examples = []
        user_type = tree['user_type']
        
        # Same input, different user type responses
        base_inputs = [
            "How are you today?",
            "Do you need anything?", 
            "Are you ready to go?",
            "What would you like to do?"
        ]
        
        for input_text in base_inputs:
            adapted_responses = self.adapt_responses_for_user_type(input_text, tree)
            
            example = {
                'instruction': f'AAC Logic: Adapt responses for {user_type} user',
                'input': input_text,
                'output': ', '.join(adapted_responses),
                'logic_tree': {
                    'type': 'user_adaptation',
                    'user_type': user_type,
                    'adaptation_rules': tree
                }
            }
            examples.append(example)
        
        return examples
    
    def adapt_responses_for_user_type(self, input_text: str, tree: Dict) -> List[str]:
        """Adapt responses based on user type specifications"""
        user_type = tree['user_type']
        complexity = tree['complexity_level']
        style = tree['vocabulary_style']
        
        if user_type == 'adult':
            if 'feel' in input_text.lower():
                return ["I'm doing well", "Could be better", "Not great today", "Pretty good"]
            else:
                return ['Yes please', 'No thank you', 'Let me think', 'I understand']
        
        elif 'child' in user_type.lower():
            if 'feel' in input_text.lower():
                return ['Happy!', 'Sad', 'Okay', 'Tired']
            else:
                return ['Yes!', 'No thanks', 'Maybe', 'I dunno']
        
        elif user_type in ['medical', 'stroke']:
            if 'feel' in input_text.lower():
                return ['Better today', 'Not well', 'Same as before', 'Need help']
            else:
                return ['Yes', 'No', 'Help please', 'Thank you']
        
        return ['Yes', 'No', 'Maybe', 'Not sure']
    
    def extract_choices_from_question(self, question: str) -> List[str]:
        """Extract explicit choices from choice questions"""
        # Simple extraction of choices separated by 'or'
        if ' or ' in question:
            # Find the part with choices
            parts = question.split(' or ')
            choices = []
            for part in parts:
                # Clean up the choice text
                choice = re.sub(r'[^\w\s]', '', part).strip()
                # Take last word(s) as the choice
                words = choice.split()
                if words:
                    choices.append(words[-1].capitalize())
            return choices[:3]  # Max 3 choices
        
        return ['Option 1', 'Option 2']
    
    def save_advanced_training_data(self, examples: List[Dict], filename: str):
        """Save advanced training data with logic trees"""
        with open(filename, 'w') as f:
            for example in examples:
                f.write(json.dumps(example) + '\n')
        
        print(f"💾 Saved {len(examples)} advanced logic tree examples to {filename}")

def main():
    print("🌳 Building AAC Logic Trees from All Training Data")
    print("=" * 55)
    
    builder = AACLogicTreeBuilder()
    
    # Step 1: Analyze existing data
    print("\n📊 Step 1: Analyzing existing training data...")
    existing_examples = builder.analyze_existing_data()
    
    # Step 2: Extract logic patterns
    print("\n🧠 Step 2: Extracting decision logic patterns...")
    patterns = builder.extract_logic_patterns(existing_examples)
    
    print(f"   Found {len(patterns['question_types'])} question types")
    print(f"   Found {len(patterns['context_triggers'])} context triggers")
    print(f"   Found {len(patterns['user_adaptations'])} user adaptations")
    
    # Step 3: Build decision trees
    print("\n🌳 Step 3: Building decision trees...")
    decision_trees = builder.build_decision_trees(patterns)
    
    print(f"   Created {len(decision_trees)} decision trees")
    
    # Step 4: Generate advanced training data
    print("\n⚡ Step 4: Generating advanced logic-based training data...")
    advanced_examples = builder.generate_advanced_training_data(decision_trees)
    
    # Step 5: Save everything
    print("\n💾 Step 5: Saving advanced training data...")
    builder.save_advanced_training_data(advanced_examples, 'tinkybink_logic_trees.jsonl')
    
    # Save decision trees for reference
    with open('aac_decision_trees.json', 'w') as f:
        json.dump(decision_trees, f, indent=2)
    
    print(f"🌳 Saved decision trees to aac_decision_trees.json")
    
    # Show summary
    print(f"\n✅ Logic Tree Training Complete!")
    print(f"📊 Total examples: {len(existing_examples)} + {len(advanced_examples)} = {len(existing_examples) + len(advanced_examples)}")
    print(f"🌳 Decision trees: {len(decision_trees)}")
    print(f"🎯 Ready for advanced AAC model training!")

if __name__ == "__main__":
    main()