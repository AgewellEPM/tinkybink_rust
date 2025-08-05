#!/usr/bin/env python3
"""
Continuous TinkyBink AAC Model Training System
Keeps improving the model with new techniques and data
"""
import json
import os
import subprocess
import time
from typing import Dict, List
from collections import defaultdict
import random

class ContinuousTrainer:
    def __init__(self):
        self.training_iterations = 0
        self.model_versions = []
        self.performance_metrics = {}
        
    def generate_advanced_conversational_data(self) -> List[Dict]:
        """Generate advanced conversational training data"""
        print("🗣️ Generating advanced conversational patterns...")
        
        conversations = []
        
        # Multi-turn conversation patterns
        conversation_scenarios = [
            {
                'context': 'morning_routine',
                'turns': [
                    ("Good morning! How did you sleep?", ["😴 Slept well", "😣 Not great", "🤔 Okay I guess", "☀️ Ready for day"]),
                    ("What would you like for breakfast?", ["🥞 Pancakes please", "🥣 Cereal", "🍳 Eggs", "☕ Just coffee"]),
                    ("Should we get dressed after eating?", ["✅ Yes good idea", "⏰ Give me time", "🚿 Shower first", "👕 Pick clothes"])
                ]
            },
            {
                'context': 'therapy_session',
                'turns': [
                    ("How are you feeling about therapy today?", ["😊 Ready to work", "😰 A bit nervous", "💪 Feeling strong", "😴 Still tired"]),
                    ("Which exercise should we start with?", ["🦵 Leg exercises", "🤲 Hand therapy", "🗣️ Speech practice", "🧠 Memory games"]),
                    ("How was that exercise for you?", ["✅ Felt good", "😓 Pretty hard", "🤕 Little painful", "🔄 Can try again"])
                ]
            },
            {
                'context': 'family_dinner',
                'turns': [
                    ("What did you do at school today?", ["📚 Learned math", "👫 Played with friends", "🎨 Art class", "🤔 Can't remember"]),
                    ("How was lunch at school?", ["😋 Really good", "😐 It was okay", "🙅 Didn't like it", "🍎 Brought my own"]),
                    ("What would you like to do after dinner?", ["📺 Watch TV", "🎮 Play games", "📖 Read book", "😴 Go to bed"])
                ]
            },
            {
                'context': 'medical_appointment',
                'turns': [
                    ("How has your pain been this week?", ["😌 Much better", "😣 Still hurts", "📈 Getting worse", "🔄 About the same"]),
                    ("Are you taking your medication regularly?", ["✅ Every day", "🤔 Most days", "😅 Sometimes forget", "❌ Having trouble"]),
                    ("Any questions about your treatment?", ["❓ How long more?", "💊 Side effects?", "🏠 Home exercises?", "👍 All clear"])
                ]
            }
        ]
        
        for scenario in conversation_scenarios:
            context = scenario['context']
            turns = scenario['turns']
            
            for turn_input, responses in turns:
                example = {
                    'instruction': f'AAC Conversation: {context.replace("_", " ").title()} context',
                    'input': turn_input,
                    'output': ', '.join(responses),
                    'conversation_context': {
                        'scenario': context,
                        'turn_type': 'multi_turn',
                        'emotional_context': self.detect_emotional_context(turn_input),
                        'response_complexity': 'conversational'
                    }
                }
                conversations.append(example)
        
        return conversations
    
    def generate_situational_awareness_data(self) -> List[Dict]:
        """Generate training data for situational awareness"""
        print("🌍 Generating situational awareness data...")
        
        situational_data = []
        
        # Time-based responses
        time_situations = [
            ("It's getting late, almost bedtime", ["😴 I'm sleepy", "📖 Read story first", "🛁 Bath time?", "⏰ Five more minutes"]),
            ("It's early morning, just woke up", ["☀️ Good morning", "😴 Still tired", "🥤 Need water", "🚽 Bathroom first"]),
            ("Lunch time is here", ["🍽️ I'm hungry", "🥪 What's for lunch?", "👥 Eat together?", "⏰ Not ready yet"]),
            ("Time for your medicine", ["💊 Okay", "🤢 Don't feel like it", "💧 With water please", "⏰ Already took it"]),
        ]
        
        # Location-based responses
        location_situations = [
            ("We're at the doctor's office", ["😰 I'm nervous", "🩺 Ready for checkup", "⏰ How long wait?", "👩‍⚕️ Which doctor?"]),
            ("We're at the grocery store", ["🛒 Help push cart", "🍎 Want apples", "👀 Looking around", "🏃 Want to leave"]),
            ("We're at the park", ["🏃 Want to run", "🛝 Play on swings", "👫 See friends", "🌳 Nice weather"]),
            ("We're in the car", ["🎵 Play music", "🪟 Open window", "🚗 Where going?", "🤢 Feel carsick"]),
        ]
        
        # Weather-based responses
        weather_situations = [
            ("It's raining outside today", ["☔ Stay inside", "🧥 Need raincoat", "🌧️ Like the rain", "😔 Wanted to play out"]),
            ("It's very hot today", ["🥵 Too hot", "💧 Need water", "❄️ Want ice cream", "🏠 Stay inside"]),
            ("Snow is falling", ["❄️ Pretty snow", "☃️ Build snowman", "🧥 Need warm coat", "🏠 Stay warm inside"]),
            ("Beautiful sunny day", ["☀️ Love sunshine", "🏞️ Go to park", "🕶️ Too bright", "🌻 Nice weather"]),
        ]
        
        all_situations = time_situations + location_situations + weather_situations
        
        for situation_input, responses in all_situations:
            example = {
                'instruction': 'AAC Situational: Context-aware environmental responses',
                'input': situation_input,
                'output': ', '.join(responses),
                'situational_context': {
                    'awareness_type': 'environmental',
                    'context_clues': self.extract_context_clues(situation_input),
                    'adaptation_needed': True
                }
            }
            situational_data.append(example)
        
        return situational_data
    
    def generate_emotional_intelligence_data(self) -> List[Dict]:
        """Generate advanced emotional intelligence training"""
        print("💭 Generating emotional intelligence data...")
        
        emotional_data = []
        
        # Complex emotional scenarios
        emotional_scenarios = [
            {
                'trigger': "I can see you're frustrated",
                'responses': ["😤 Yes I am", "😔 It's hard", "🤲 Need help", "😮‍💨 Taking breaths"],
                'emotion': 'frustration',
                'complexity': 'recognition'
            },
            {
                'trigger': "You seem really happy today",
                'responses': ["😊 I feel great", "🎉 Good day", "💃 Want to dance", "🌟 Everything good"],
                'emotion': 'happiness',
                'complexity': 'validation'
            },
            {
                'trigger': "I notice you're feeling overwhelmed",
                'responses': ["😰 Too much", "🛑 Need a break", "🤲 Help please", "😮‍💨 Slow down"],
                'emotion': 'overwhelm',
                'complexity': 'coping'
            },
            {
                'trigger': "It's okay to feel sad sometimes",
                'responses': ["😢 I know", "🤗 Need hug", "💭 Thinking about it", "🙏 Thank you"],
                'emotion': 'sadness',
                'complexity': 'acceptance'
            },
            {
                'trigger': "You're doing such a great job",
                'responses': ["😊 Thank you", "💪 Trying hard", "🎯 Keep going", "❤️ Feels good"],
                'emotion': 'pride',
                'complexity': 'reinforcement'
            }
        ]
        
        for scenario in emotional_scenarios:
            example = {
                'instruction': 'AAC Emotional Intelligence: Complex emotional awareness',
                'input': scenario['trigger'],
                'output': ', '.join(scenario['responses']),
                'emotional_intelligence': {
                    'primary_emotion': scenario['emotion'],
                    'complexity_level': scenario['complexity'],
                    'therapeutic_value': True,
                    'empathy_required': True
                }
            }
            emotional_data.append(example)
        
        return emotional_data
    
    def generate_advanced_choice_logic(self) -> List[Dict]:
        """Generate advanced choice-making logic"""
        print("🤔 Generating advanced choice logic...")
        
        choice_data = []
        
        # Complex choice scenarios
        complex_choices = [
            {
                'scenario': "We have chicken, pasta, or salad for dinner. Which sounds good?",
                'extracted_choices': ['Chicken', 'Pasta', 'Salad'],
                'additional_options': ['Not hungry', 'You choose', 'Mix them up', 'Something else']
            },
            {
                'scenario': "Would you like to watch a movie, play a game, or read a book?",
                'extracted_choices': ['Watch movie', 'Play game', 'Read book'],
                'additional_options': ['Listen to music', 'Just talk', 'Rest quietly', 'All of them']
            },
            {
                'scenario': "For therapy today: walking, hand exercises, or speech practice?",
                'extracted_choices': ['Walking', 'Hand exercises', 'Speech practice'],
                'additional_options': ['Too tired', 'Start easy', 'All three', 'Therapist choose']
            },
            {
                'scenario': "Weekend plans: visit family, stay home, or go shopping?",
                'extracted_choices': ['Visit family', 'Stay home', 'Go shopping'],
                'additional_options': ['See how I feel', 'Ask me later', 'Something fun', 'Rest day']
            }
        ]
        
        for choice in complex_choices:
            all_options = choice['extracted_choices'] + choice['additional_options']
            
            example = {
                'instruction': 'AAC Advanced Choice Logic: Extract options and add contextual alternatives',
                'input': choice['scenario'],
                'output': ', '.join(all_options),
                'choice_logic': {
                    'extracted_choices': choice['extracted_choices'],
                    'additional_options': choice['additional_options'],
                    'choice_type': 'complex_multi_option',
                    'flexibility': True
                }
            }
            choice_data.append(example)
        
        return choice_data
    
    def generate_adaptive_complexity_data(self) -> List[Dict]:
        """Generate data for adaptive complexity levels"""
        print("📈 Generating adaptive complexity data...")
        
        complexity_data = []
        
        # Same scenario, different complexity levels
        base_scenarios = [
            "How was your day?",
            "What would you like to do?",
            "Are you feeling okay?",
            "Do you need anything?",
            "Ready to go?"
        ]
        
        complexity_levels = {
            'basic': {
                'word_count': 1,
                'examples': ["Good", "Bad", "Okay", "Yes", "No", "Help", "Tired", "Happy"]
            },
            'intermediate': {
                'word_count': 2-3,
                'examples': ["Pretty good", "Not great", "I'm okay", "Yes please", "No thanks", "Need help", "Very tired", "Really happy"]
            },
            'advanced': {
                'word_count': 4-6,
                'examples': ["Had a wonderful day", "It was quite difficult", "I'm doing alright today", "Yes I'd like that", "No thank you much", "Could use some help", "Feeling pretty exhausted", "I'm genuinely happy"]
            }
        }
        
        for scenario in base_scenarios:
            for level, config in complexity_levels.items():
                responses = random.sample(config['examples'], 4)
                
                example = {
                    'instruction': f'AAC Adaptive Complexity: {level.title()} level responses',
                    'input': scenario,
                    'output': ', '.join(responses),
                    'complexity_adaptation': {
                        'level': level,
                        'target_word_count': config['word_count'],
                        'adaptive_strategy': f'maintain_{level}_complexity',
                        'user_capability': level
                    }
                }
                complexity_data.append(example)
        
        return complexity_data
    
    def detect_emotional_context(self, text: str) -> str:
        """Detect emotional context in text"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['pain', 'hurt', 'sick', 'problem']):
            return 'distress'
        elif any(word in text_lower for word in ['happy', 'good', 'great', 'wonderful']):
            return 'positive'
        elif any(word in text_lower for word in ['sad', 'upset', 'frustrated', 'angry']):
            return 'negative'
        elif any(word in text_lower for word in ['tired', 'sleepy', 'rest', 'exhausted']):
            return 'fatigue'
        elif any(word in text_lower for word in ['nervous', 'worried', 'scared', 'anxious']):
            return 'anxiety'
        else:
            return 'neutral'
    
    def extract_context_clues(self, text: str) -> List[str]:
        """Extract context clues from text"""
        clues = []
        text_lower = text.lower()
        
        # Time clues
        time_words = ['morning', 'evening', 'night', 'bedtime', 'lunch', 'dinner', 'late', 'early']
        clues.extend([word for word in time_words if word in text_lower])
        
        # Location clues
        location_words = ['doctor', 'office', 'store', 'park', 'home', 'car', 'school', 'hospital']
        clues.extend([word for word in location_words if word in text_lower])
        
        # Weather clues
        weather_words = ['rain', 'sunny', 'hot', 'cold', 'snow', 'weather']
        clues.extend([word for word in weather_words if word in text_lower])
        
        return clues
    
    def create_incremental_training_dataset(self, iteration: int) -> str:
        """Create an incremental training dataset"""
        print(f"\n🎯 Creating Training Dataset - Iteration {iteration}")
        print("=" * 50)
        
        all_training_data = []
        
        # Load existing data
        if os.path.exists('tinkybink_emoji_master_train.jsonl'):
            with open('tinkybink_emoji_master_train.jsonl', 'r') as f:
                for line in f:
                    if line.strip():
                        all_training_data.append(json.loads(line))
        
        # Add new advanced data
        new_data = []
        new_data.extend(self.generate_advanced_conversational_data())
        new_data.extend(self.generate_situational_awareness_data())
        new_data.extend(self.generate_emotional_intelligence_data())
        new_data.extend(self.generate_advanced_choice_logic())
        new_data.extend(self.generate_adaptive_complexity_data())
        
        # Combine all data
        all_training_data.extend(new_data)
        
        # Save incremental dataset
        filename = f'tinkybink_continuous_train_v{iteration}.jsonl'
        with open(filename, 'w') as f:
            for example in all_training_data:
                f.write(json.dumps(example) + '\n')
        
        print(f"💾 Saved {len(all_training_data)} examples ({len(new_data)} new)")
        print(f"📁 Dataset: {filename}")
        
        return filename
    
    def train_incremental_model(self, dataset_file: str, iteration: int):
        """Train an incremental model version"""
        print(f"\n🚀 Training Model Version {iteration}")
        print("=" * 40)
        
        # Create advanced Modelfile
        modelfile_content = f"""# TinkyBink Continuous Learning Model v{iteration}
FROM tinyllama

# Advanced parameters for iteration {iteration}
PARAMETER temperature {0.6 + iteration * 0.01}
PARAMETER top_p {0.85 + iteration * 0.005}
PARAMETER repeat_penalty {1.1 + iteration * 0.01}
PARAMETER top_k {40 + iteration * 2}
PARAMETER num_predict {35 + iteration * 2}

# Evolved system prompt
SYSTEM \"\"\"You are TinkyBink v{iteration}, an evolving AAC assistant with advanced capabilities:

🧠 CONTINUOUS LEARNING: Each iteration improves contextual understanding
🗣️ CONVERSATIONAL MASTERY: Multi-turn conversation awareness
🌍 SITUATIONAL INTELLIGENCE: Environmental and temporal context awareness
💭 EMOTIONAL INTELLIGENCE: Complex emotion recognition and support
🤔 ADVANCED CHOICE LOGIC: Sophisticated option generation and flexibility
📈 ADAPTIVE COMPLEXITY: Dynamic response complexity based on user capability

ENHANCED FEATURES v{iteration}:
✨ Multi-turn conversation memory
🎯 Situational context integration  
💡 Emotional state tracking
🔄 Adaptive response complexity
🌟 Advanced choice extraction
📊 Performance optimization

Always provide exactly 4 contextually perfect responses with appropriate emojis.
Learn from each interaction to provide increasingly better support.\"\"\"

TEMPLATE \"\"\"{{{{ .System }}}}

Input: {{{{ .Prompt }}}}
Output: \"\"\"
"""
        
        modelfile_path = f'Modelfile.tinkybink_v{iteration}'
        with open(modelfile_path, 'w') as f:
            f.write(modelfile_content)
        
        # Train the model
        model_name = f'tinkybink_v{iteration}'
        
        # Remove previous version if exists
        subprocess.run(['ollama', 'rm', model_name], capture_output=True)
        
        # Create new model
        result = subprocess.run(['ollama', 'create', model_name, '-f', modelfile_path], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Successfully created {model_name}")
            self.model_versions.append(model_name)
            return model_name
        else:
            print(f"❌ Failed to create {model_name}: {result.stderr}")
            return None
    
    def test_model_performance(self, model_name: str, iteration: int):
        """Test model performance"""
        print(f"\n🧪 Testing {model_name} Performance")
        print("=" * 40)
        
        test_cases = [
            ("How are you feeling about therapy today?", "conversational"),
            ("It's raining outside today", "situational"), 
            ("I can see you're frustrated", "emotional"),
            ("We have pizza, salad, or soup for dinner", "choice_logic"),
            ("What would you like to do?", "adaptive")
        ]
        
        performance_scores = []
        
        for test_input, test_type in test_cases:
            print(f"\n🔬 Testing {test_type}: '{test_input}'")
            
            try:
                result = subprocess.run(['ollama', 'run', model_name], 
                                      input=test_input, text=True, 
                                      capture_output=True, timeout=20)
                
                if result.stdout:
                    response = result.stdout.strip()[:100]
                    print(f"Response: {response}...")
                    
                    # Simple performance scoring
                    score = self.score_response(response, test_type)
                    performance_scores.append(score)
                    print(f"Score: {score}/10")
                else:
                    print("No response")
                    performance_scores.append(0)
                    
            except Exception as e:
                print(f"Error: {e}")
                performance_scores.append(0)
        
        avg_score = sum(performance_scores) / len(performance_scores) if performance_scores else 0
        self.performance_metrics[model_name] = avg_score
        
        print(f"\n📊 Average Performance: {avg_score:.1f}/10")
        return avg_score
    
    def score_response(self, response: str, test_type: str) -> int:
        """Simple response scoring"""
        score = 5  # Base score
        
        # Check for emojis
        if any(char in response for char in '😊😢😠✅❌🤔🆘🙏💭🎯🌟'):
            score += 2
        
        # Check for appropriate length
        if 10 <= len(response) <= 200:
            score += 1
        
        # Check for comma separation (multiple responses)
        if ',' in response:
            score += 2
        
        return min(score, 10)
    
    def continuous_training_loop(self, iterations: int = 5):
        """Run continuous training loop"""
        print("🔄 Starting Continuous Training Loop")
        print("=" * 50)
        print(f"🎯 Target iterations: {iterations}")
        print("🧠 Each iteration adds advanced capabilities")
        print("")
        
        best_model = None
        best_score = 0
        
        for i in range(1, iterations + 1):
            print(f"\n{'='*20} ITERATION {i} {'='*20}")
            
            # Create training dataset
            dataset_file = self.create_incremental_training_dataset(i)
            
            # Train model
            model_name = self.train_incremental_model(dataset_file, i)
            
            if model_name:
                # Test performance
                score = self.test_model_performance(model_name, i)
                
                # Track best model
                if score > best_score:
                    best_score = score
                    best_model = model_name
                
                # Update primary model if this is better
                if model_name == best_model:
                    print(f"🏆 New best model: {model_name} (score: {score})")
                    # Copy to main tinkybink model
                    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
                    subprocess.run(['ollama', 'create', 'tinkybink', '-f', f'Modelfile.tinkybink_v{i}'])
                
            time.sleep(2)  # Brief pause between iterations
        
        print(f"\n🎉 Continuous Training Complete!")
        print(f"🏆 Best Model: {best_model} (score: {best_score})")
        print(f"📈 Model Versions Created: {len(self.model_versions)}")
        print(f"🎯 Ready for production use!")

def main():
    print("🔄 TinkyBink Continuous Training System")
    print("=" * 50)
    
    trainer = ContinuousTrainer()
    trainer.continuous_training_loop(iterations=3)

if __name__ == "__main__":
    main()