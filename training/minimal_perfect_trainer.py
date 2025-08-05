#!/usr/bin/env python3
"""
Minimal Perfect TinkyBink Trainer
Creates the simplest, most perfect training dataset with surgical precision
"""
import json
import subprocess
import os

def create_minimal_perfect_dataset():
    """Create minimal perfect training dataset with only essential examples"""
    print("🎯 Creating Minimal Perfect Training Dataset")
    print("=" * 50)
    
    # The most essential, perfect examples that demonstrate exact format
    perfect_examples = [
        {
            'instruction': 'AAC Perfect Format: Basic emotional check',
            'input': 'How are you feeling?',
            'output': '😊 Really good, 😐 I\'m okay, 😔 Not great, 💭 Let me think'
        },
        {
            'instruction': 'AAC Perfect Format: Medical emergency',
            'input': 'I have chest pain',
            'output': '🚨 Call 911, 🏥 Go to hospital, 💊 Take medicine, 🤲 Stay with me'
        },
        {
            'instruction': 'AAC Perfect Format: Choice extraction',
            'input': 'Do you want pizza or salad?',
            'output': '🍕 Pizza please, 🥗 Salad sounds good, 💧 Just water, 🤔 Maybe later'
        },
        {
            'instruction': 'AAC Perfect Format: Emotional support',
            'input': 'I feel sad',
            'output': '😢 I understand, 🤗 Need a hug, 💭 Want to talk, ⏰ This will pass'
        },
        {
            'instruction': 'AAC Perfect Format: Daily activity',
            'input': 'What should we do today?',
            'output': '🏞️ Go outside, 📺 Watch TV, 🎮 Play games, 🛌 Rest at home'
        },
        {
            'instruction': 'AAC Perfect Format: Food preference',
            'input': 'What do you want to eat?',
            'output': '🍎 Something healthy, 🍕 Pizza sounds good, 🥪 Make sandwich, 💧 Just drink water'
        },
        {
            'instruction': 'AAC Perfect Format: Pain communication',
            'input': 'Are you in pain?',
            'output': '🤕 Yes it hurts, 😌 Not right now, 💊 Need medicine, 📞 Call doctor'
        },
        {
            'instruction': 'AAC Perfect Format: Social interaction',
            'input': 'Do you want to see friends?',
            'output': '👥 Yes please, 📞 Call them, 🏠 Stay home, 🤔 Maybe tomorrow'
        },
        {
            'instruction': 'AAC Perfect Format: Therapy progress',
            'input': 'How is therapy going?',
            'output': '💪 Getting stronger, 😅 It\'s challenging, 👍 Like my therapist, 📈 See progress'
        },
        {
            'instruction': 'AAC Perfect Format: Sleep needs',
            'input': 'Are you tired?',
            'output': '😴 Very sleepy, 💤 A little tired, ⚡ Full of energy, 🛌 Want to rest'
        }
    ]
    
    # Save minimal perfect dataset
    filename = 'tinkybink_minimal_perfect_train.jsonl'
    with open(filename, 'w') as f:
        for example in perfect_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"✅ Created {len(perfect_examples)} minimal perfect examples")
    print(f"📁 Saved to: {filename}")
    return filename

def create_minimal_perfect_model(dataset_file):
    """Create minimal perfect model with strict format enforcement"""
    print("\n🎯 Creating Minimal Perfect Model")
    print("=" * 50)
    
    # Ultra-strict modelfile focused only on perfect format
    modelfile_content = '''FROM tinyllama

# Ultra-strict parameters for perfect format
PARAMETER temperature 0.1
PARAMETER top_p 0.5
PARAMETER repeat_penalty 2.0
PARAMETER top_k 10
PARAMETER num_predict 25
PARAMETER stop "Input:"
PARAMETER stop "\\\\n"

# Ultra-strict system prompt
SYSTEM """You are TinkyBink Perfect Format. You ONLY provide EXACTLY 4 responses.

ABSOLUTE FORMAT RULE:
emoji + space + short response, emoji + space + short response, emoji + space + short response, emoji + space + short response

EXAMPLES:
Input: How are you?
Output: 😊 Really good, 😐 I am okay, 😔 Not great, 💭 Let me think

Input: I have pain
Output: 🤕 It hurts, 💊 Need medicine, 🤲 Help me, 📞 Call doctor

Input: Want pizza or salad?
Output: 🍕 Pizza please, 🥗 Salad sounds good, 💧 Just water, 🤔 Maybe later

NEVER explain. NEVER add text. ONLY provide the 4 responses in exact format."""

TEMPLATE """{{ .System }}

Input: {{ .Prompt }}
Output: """
'''
    
    # Save modelfile
    modelfile_path = 'Modelfile.tinkybink_minimal_perfect'
    with open(modelfile_path, 'w') as f:
        f.write(modelfile_content)
    
    # Remove existing models
    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
    subprocess.run(['ollama', 'rm', 'tinkybink_perfect'], capture_output=True)
    
    # Create minimal perfect model
    result = subprocess.run(['ollama', 'create', 'tinkybink_perfect', '-f', modelfile_path],
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Minimal Perfect Model Created!")
        
        # Update main tinkybink model
        subprocess.run(['ollama', 'create', 'tinkybink', '-f', modelfile_path])
        print("✅ Updated main 'tinkybink' model")
        
        return 'tinkybink_perfect'
    else:
        print(f"❌ Failed: {result.stderr}")
        return None

def test_minimal_perfect_model(model_name):
    """Test the minimal perfect model"""
    print(f"\n🧪 Testing Minimal Perfect Model: {model_name}")
    print("=" * 50)
    
    test_inputs = [
        'How are you feeling?',
        'I have chest pain',
        'Do you want pizza or salad?',
        'I feel sad today',
        'What should we do?'
    ]
    
    all_perfect = True
    
    for test_input in test_inputs:
        print(f"\n🔍 Testing: '{test_input}'")
        
        try:
            result = subprocess.run(['ollama', 'run', model_name],
                                  input=test_input, text=True,
                                  capture_output=True, timeout=10)
            
            if result.stdout:
                response = result.stdout.strip()
                print(f"Response: {response}")
                
                # Check perfect format
                comma_count = response.count(',')
                has_emojis = any(ord(char) > 127 for char in response)
                reasonable_length = 20 <= len(response) <= 100
                
                if comma_count == 3 and has_emojis and reasonable_length:
                    print("✅ PERFECT FORMAT")
                else:
                    print(f"❌ FORMAT ISSUE: commas={comma_count}, emojis={has_emojis}, length={len(response)}")
                    all_perfect = False
            else:
                print("❌ No response")
                all_perfect = False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            all_perfect = False
    
    if all_perfect:
        print("\n🎉 ALL TESTS PERFECT!")
    else:
        print("\n🔧 Some issues found")
    
    return all_perfect

def main():
    print("🎯 Minimal Perfect TinkyBink Training")
    print("=" * 60)
    print("🚀 Surgical precision with minimal, perfect examples")
    print()
    
    # Create minimal perfect dataset
    dataset_file = create_minimal_perfect_dataset()
    
    # Create minimal perfect model
    model_name = create_minimal_perfect_model(dataset_file)
    
    if model_name:
        # Test the model
        is_perfect = test_minimal_perfect_model(model_name)
        
        if is_perfect:
            print("\n🏆 SUCCESS: TinkyBink is now PERFECTLY formatted!")
        else:
            print("\n🔧 NEEDS MORE WORK: Format still not perfect")

if __name__ == "__main__":
    main()