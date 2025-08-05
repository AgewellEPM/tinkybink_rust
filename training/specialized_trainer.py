#!/usr/bin/env python3
"""
Specialized TinkyBink AAC Training System
Focuses on specific AAC capabilities and user scenarios
"""
import json
import subprocess
import time
from typing import Dict, List
import random

class SpecializedTrainer:
    def __init__(self):
        self.specializations = []
        
    def generate_medical_emergency_training(self) -> List[Dict]:
        """Generate specialized medical emergency training"""
        print("🚨 Generating medical emergency training...")
        
        emergency_scenarios = [
            {
                'trigger': "I'm having trouble breathing",
                'responses': ["🚨 Call 911", "💊 Get inhaler", "🪑 Sit down", "🤲 Help me"],
                'urgency': 'high',
                'category': 'respiratory'
            },
            {
                'trigger': "My chest hurts badly",
                'responses': ["🚨 Emergency", "📞 Call doctor", "💊 Heart medicine", "🛏️ Lie down"],
                'urgency': 'high', 
                'category': 'cardiac'
            },
            {
                'trigger': "I fell and can't get up",
                'responses': ["🚨 Need help", "🤕 I'm hurt", "📞 Call someone", "⚡ Don't move me"],
                'urgency': 'high',
                'category': 'injury'
            },
            {
                'trigger': "I feel very dizzy and confused",
                'responses': ["🪑 Need to sit", "💧 Get water", "📞 Call nurse", "🤲 Stay with me"],
                'urgency': 'medium',
                'category': 'neurological'
            },
            {
                'trigger': "I'm choking",
                'responses': ["🚨 Help choking", "👋 Can't breathe", "🤲 Help me now", "☎️ Call 911"],
                'urgency': 'critical',
                'category': 'airway'
            }
        ]
        
        training_data = []
        for scenario in emergency_scenarios:
            example = {
                'instruction': f'AAC Medical Emergency: {scenario["urgency"].upper()} priority response',
                'input': scenario['trigger'],
                'output': ', '.join(scenario['responses']),
                'medical_emergency': {
                    'urgency_level': scenario['urgency'],
                    'medical_category': scenario['category'],
                    'requires_immediate_action': scenario['urgency'] in ['high', 'critical'],
                    'emergency_protocol': True
                }
            }
            training_data.append(example)
        
        return training_data
    
    def generate_therapy_progression_training(self) -> List[Dict]:
        """Generate therapy progression tracking training"""
        print("🏥 Generating therapy progression training...")
        
        therapy_progressions = [
            {
                'stage': 'assessment',
                'scenarios': [
                    ("How does this movement feel?", ["😣 Hurts a lot", "😐 Uncomfortable", "😌 Not too bad", "😊 Feels good"]),
                    ("Can you try this exercise?", ["💪 I'll try", "😰 Looks hard", "🤔 Show me first", "❌ Too difficult"]),
                    ("Rate your pain from 1 to 10", ["1️⃣ Very little", "5️⃣ Medium pain", "🔟 Very painful", "❓ Hard to say"])
                ]
            },
            {
                'stage': 'active_therapy',
                'scenarios': [
                    ("Let's work on your speech sounds", ["🗣️ Ready to try", "😮‍💨 Take it slow", "🔄 Again please", "✅ Think I got it"]),
                    ("Time for walking practice", ["🚶 Let's walk", "🦵 Legs feel weak", "🤲 Need support", "⏰ Rest first"]),
                    ("How did that exercise feel?", ["💪 Getting stronger", "😓 Still hard", "🔄 Want to repeat", "😌 Not too bad"])
                ]
            },
            {
                'stage': 'maintenance',
                'scenarios': [
                    ("Keep practicing at home", ["✅ Will do", "📝 Write it down", "❓ How often?", "🤔 Need reminders"]),
                    ("How are you doing with exercises?", ["📈 Getting better", "😐 About the same", "📉 Struggling", "💪 Feeling stronger"]),
                    ("Any questions about your progress?", ["❓ How am I doing?", "⏰ How much longer?", "🏠 Home exercises?", "👍 All good"])
                ]
            }
        ]
        
        training_data = []
        for progression in therapy_progressions:
            stage = progression['stage']
            for scenario_input, responses in progression['scenarios']:
                example = {
                    'instruction': f'AAC Therapy: {stage.replace("_", " ").title()} stage responses',
                    'input': scenario_input,
                    'output': ', '.join(responses),
                    'therapy_context': {
                        'stage': stage,
                        'therapeutic_value': True,
                        'progress_tracking': True,
                        'motivational': stage == 'active_therapy'
                    }
                }
                training_data.append(example)
        
        return training_data
    
    def generate_social_integration_training(self) -> List[Dict]:
        """Generate social integration and relationship training"""
        print("👥 Generating social integration training...")
        
        social_scenarios = [
            {
                'context': 'making_friends',
                'interactions': [
                    ("Would you like to be friends?", ["😊 Yes please", "🤔 Maybe", "👋 Hi there", "😅 I'm shy"]),
                    ("What do you like to do for fun?", ["🎮 Play games", "📚 Read books", "🎨 Draw pictures", "⚽ Play sports"]),
                    ("Want to play together?", ["✅ Yes let's play", "❓ What game?", "⏰ Maybe later", "🤗 Sounds fun"])
                ]
            },
            {
                'context': 'family_interaction',
                'interactions': [
                    ("How was your day with family?", ["❤️ Really good", "😊 Had fun", "😐 It was okay", "😔 Kind of hard"]),
                    ("What did you do together?", ["🎮 Played games", "📺 Watched movies", "🗣️ Just talked", "🍽️ Ate together"]),
                    ("Do you feel supported by family?", ["❤️ Very much", "👍 Most times", "🤔 Sometimes", "😢 Not really"])
                ]
            },
            {
                'context': 'community_participation',
                'interactions': [
                    ("How do you feel in group activities?", ["😊 I enjoy them", "😰 A bit nervous", "🤔 Depends on group", "😔 Prefer alone"]),
                    ("Would you like to join our activity?", ["✅ Yes please", "❓ What activity?", "🤔 Let me think", "👥 Who else coming?"]),
                    ("How can we help you participate?", ["🗣️ Speak slower", "📝 Write it down", "🤲 Stay close by", "⏰ Give me time"])
                ]
            }
        ]
        
        training_data = []
        for scenario in social_scenarios:
            context = scenario['context']
            for interaction_input, responses in scenario['interactions']:
                example = {
                    'instruction': f'AAC Social: {context.replace("_", " ").title()} context',
                    'input': interaction_input,
                    'output': ', '.join(responses),
                    'social_context': {
                        'interaction_type': context,
                        'social_skill_building': True,
                        'relationship_focused': True,
                        'community_integration': context == 'community_participation'
                    }
                }
                training_data.append(example)
        
        return training_data
    
    def generate_independence_training(self) -> List[Dict]:
        """Generate independence and life skills training"""
        print("🏠 Generating independence training...")
        
        independence_scenarios = [
            {
                'skill_area': 'self_care',
                'situations': [
                    ("Do you need help getting dressed?", ["👕 Pick clothes", "🤲 Need help", "✅ I can do it", "⏰ Give me time"]),
                    ("Time to brush your teeth", ["🦷 Doing it now", "💧 Need toothpaste", "🤲 Help me reach", "✅ Already done"]),
                    ("Are you ready for your shower?", ["🚿 Yes ready", "⏰ Few minutes", "🤒 Don't feel well", "❓ Water temperature?"])
                ]
            },
            {
                'skill_area': 'household_tasks',
                'situations': [
                    ("Can you help with dishes?", ["🍽️ I'll help", "💧 Wash or dry?", "🤲 Show me how", "😰 Afraid to break"]),
                    ("Time to make your bed", ["🛏️ I'll do it", "📝 Remind me how", "🤲 Help me start", "😓 Too hard today"]),
                    ("Would you like to help cook?", ["🍳 Yes please", "❓ What can I do?", "👀 Just watch", "🔥 Scared of stove"])
                ]
            },
            {
                'skill_area': 'community_skills',
                'situations': [
                    ("Ready to go shopping?", ["🛒 Let's go", "📝 Make a list", "💰 Have money?", "😰 Too crowded"]),
                    ("Can you order your food?", ["✅ I'll try", "📝 Write it down", "🤲 Help me", "👉 Point to menu"]),
                    ("Do you know how to get home?", ["✅ I remember", "🗺️ Need directions", "📞 Call someone", "🚌 Take the bus"])
                ]
            }
        ]
        
        training_data = []
        for scenario in independence_scenarios:
            skill_area = scenario['skill_area']
            for situation_input, responses in scenario['situations']:
                example = {
                    'instruction': f'AAC Independence: {skill_area.replace("_", " ").title()} skills',
                    'input': situation_input,
                    'output': ', '.join(responses),
                    'independence_context': {
                        'skill_area': skill_area,
                        'life_skills_building': True,
                        'autonomy_focused': True,
                        'practical_application': True
                    }
                }
                training_data.append(example)
        
        return training_data
    
    def generate_emotional_regulation_training(self) -> List[Dict]:
        """Generate emotional regulation and coping training"""
        print("💭 Generating emotional regulation training...")
        
        regulation_scenarios = [
            {
                'emotion': 'frustration',
                'situations': [
                    ("I can see you're getting frustrated", ["😤 Yes I am", "😮‍💨 Need break", "🤲 Help me", "💭 Trying to calm"]),
                    ("What helps when you feel frustrated?", ["😮‍💨 Deep breaths", "🚶 Take a walk", "🎵 Listen music", "🤗 Need hug"]),
                    ("Would you like to try a coping strategy?", ["✅ Yes please", "❓ Like what?", "🤔 Maybe later", "💭 Tell me more"])
                ]
            },
            {
                'emotion': 'anxiety',
                'situations': [
                    ("You seem worried about something", ["😰 I am worried", "💭 Thinking a lot", "❓ What if happens?", "🤲 Stay with me"]),
                    ("What makes you feel anxious?", ["👥 Too many people", "🔊 Loud noises", "❓ Unknown things", "⏰ Being late"]),
                    ("How can we help you feel calmer?", ["😮‍💨 Practice breathing", "🎵 Quiet music", "🤗 Someone close", "📱 Call someone"])
                ]
            },
            {
                'emotion': 'sadness',
                'situations': [
                    ("It's okay to feel sad sometimes", ["😢 I know", "💭 Missing someone", "🤗 Need comfort", "⏰ Will pass"]),
                    ("What would help you feel better?", ["🤗 Hug please", "📞 Talk to someone", "🎵 Happy music", "🐶 Pet animal"]),
                    ("Would you like to talk about it?", ["✅ Yes please", "😔 Not ready", "📝 Write it down", "🤔 Maybe later"])
                ]
            }
        ]
        
        training_data = []
        for scenario in regulation_scenarios:
            emotion = scenario['emotion']
            for situation_input, responses in scenario['situations']:
                example = {
                    'instruction': f'AAC Emotional Regulation: {emotion.title()} management',
                    'input': situation_input, 
                    'output': ', '.join(responses),
                    'emotional_regulation': {
                        'target_emotion': emotion,
                        'coping_focused': True,
                        'therapeutic_value': True,
                        'self_awareness_building': True
                    }
                }
                training_data.append(example)
        
        return training_data
    
    def create_specialized_model(self, specialization: str, training_data: List[Dict]) -> str:
        """Create a specialized model for specific AAC needs"""
        print(f"\n🎯 Creating Specialized Model: {specialization}")
        print("=" * 50)
        
        # Save specialized training data
        filename = f'tinkybink_{specialization}_train.jsonl'
        with open(filename, 'w') as f:
            for example in training_data:
                f.write(json.dumps(example) + '\n')
        
        print(f"💾 Saved {len(training_data)} specialized examples")
        
        # Create specialized Modelfile
        modelfile_content = f"""# TinkyBink {specialization.title()} Specialist Model
FROM tinyllama

# Specialized parameters for {specialization}
PARAMETER temperature 0.65
PARAMETER top_p 0.88
PARAMETER repeat_penalty 1.15
PARAMETER top_k 45
PARAMETER num_predict 40

# Specialized system prompt
SYSTEM \"\"\"You are TinkyBink {specialization.title()} Specialist, an AAC assistant specialized in {specialization.replace('_', ' ')}.

🎯 SPECIALIZATION: {specialization.replace('_', ' ').title()}
🧠 EXPERTISE: Deep understanding of {specialization.replace('_', ' ')} contexts
💡 FOCUS: Provide the most appropriate responses for {specialization.replace('_', ' ')} situations
🎨 FORMAT: Always include relevant emojis that match the emotional and contextual needs

SPECIALIZED CAPABILITIES:
{'✨ Emergency response protocols' if 'emergency' in specialization else ''}
{'🏥 Therapeutic communication patterns' if 'therapy' in specialization else ''}
{'👥 Social interaction facilitation' if 'social' in specialization else ''}
{'🏠 Independence skill building' if 'independence' in specialization else ''}
{'💭 Emotional regulation support' if 'emotional' in specialization else ''}

Always provide exactly 4 contextually perfect responses with appropriate emojis.
Prioritize {specialization.replace('_', ' ')} specific needs and communication patterns.\"\"\"

TEMPLATE \"\"\"{{{{ .System }}}}

Input: {{{{ .Prompt }}}}
Output: \"\"\"
"""
        
        modelfile_path = f'Modelfile.tinkybink_{specialization}'
        with open(modelfile_path, 'w') as f:
            f.write(modelfile_content)
        
        # Create the specialized model
        model_name = f'tinkybink_{specialization}'
        
        # Remove if exists
        subprocess.run(['ollama', 'rm', model_name], capture_output=True)
        
        # Create new specialized model
        result = subprocess.run(['ollama', 'create', model_name, '-f', modelfile_path],
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Successfully created {model_name}")
            return model_name
        else:
            print(f"❌ Failed to create {model_name}: {result.stderr}")
            return None
    
    def train_all_specializations(self):
        """Train all specialized models"""
        print("🎯 Training All AAC Specializations")
        print("=" * 50)
        
        specializations = [
            ('medical_emergency', self.generate_medical_emergency_training),
            ('therapy_progression', self.generate_therapy_progression_training),
            ('social_integration', self.generate_social_integration_training),
            ('independence', self.generate_independence_training),
            ('emotional_regulation', self.generate_emotional_regulation_training)
        ]
        
        trained_models = []
        
        for spec_name, generator_func in specializations:
            print(f"\n{'='*20} {spec_name.upper()} {'='*20}")
            
            # Generate training data
            training_data = generator_func()
            
            # Create specialized model
            model_name = self.create_specialized_model(spec_name, training_data)
            
            if model_name:
                trained_models.append(model_name)
                self.specializations.append(spec_name)
                
                # Test the specialized model
                self.test_specialized_model(model_name, spec_name)
            
            time.sleep(2)
        
        print(f"\n🎉 All Specializations Complete!")
        print(f"✅ Trained Models: {len(trained_models)}")
        print(f"🎯 Specializations: {', '.join(self.specializations)}")
        
        return trained_models
    
    def test_specialized_model(self, model_name: str, specialization: str):
        """Test a specialized model"""
        print(f"\n🧪 Testing {model_name}")
        print("-" * 30)
        
        # Specialization-specific test cases
        test_cases = {
            'medical_emergency': ["I'm having trouble breathing", "My chest hurts badly"],
            'therapy_progression': ["How does this movement feel?", "Let's work on your speech sounds"],
            'social_integration': ["Would you like to be friends?", "How was your day with family?"],
            'independence': ["Do you need help getting dressed?", "Can you help with dishes?"],
            'emotional_regulation': ["I can see you're getting frustrated", "You seem worried about something"]
        }
        
        test_inputs = test_cases.get(specialization, ["How are you?", "What do you need?"])
        
        for test_input in test_inputs[:2]:  # Test 2 examples
            print(f"🔬 Testing: '{test_input}'")
            
            try:
                result = subprocess.run(['ollama', 'run', model_name],
                                      input=test_input, text=True,
                                      capture_output=True, timeout=15)
                
                if result.stdout:
                    response = result.stdout.strip()[:80]
                    print(f"Response: {response}...")
                else:
                    print("No response")
                    
            except Exception as e:
                print(f"Error: {e}")

def main():
    print("🎯 TinkyBink Specialized Training System")
    print("=" * 50)
    
    trainer = SpecializedTrainer()
    trainer.train_all_specializations()

if __name__ == "__main__":
    main()