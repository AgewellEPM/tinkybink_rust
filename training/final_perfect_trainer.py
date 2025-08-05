#!/usr/bin/env python3
"""
Final Perfect TinkyBink Trainer
Creates the final production-ready AAC model
"""
import subprocess

def create_final_perfect_model():
    """Create the final perfect AAC model"""
    print("🏆 Creating Final Perfect TinkyBink Model")
    print("=" * 50)
    
    modelfile_content = '''FROM llama3.2

PARAMETER temperature 0.1
PARAMETER top_p 0.5
PARAMETER repeat_penalty 1.2
PARAMETER top_k 15
PARAMETER num_predict 25

SYSTEM """You are TinkyBink AAC Assistant. Always provide exactly 4 responses with emojis.

STRICT FORMAT: emoji response, emoji response, emoji response, emoji response

EXAMPLES:
Input: How are you feeling?
Output: 😊 Really good, 😐 I'm okay, 😔 Not great, 💭 Let me think

Input: I have chest pain
Output: 🚨 Call 911, 🏥 Go hospital, 💊 Take medicine, 🤲 Stay with me

Input: Do you want pizza or salad?
Output: 🍕 Pizza please, 🥗 Salad sounds good, 💧 Just water, 🤔 Maybe later

Input: I feel sad
Output: 😢 I understand, 🤗 Need hug, 💭 Want to talk, ⏰ This will pass

Input: Are you hungry?
Output: 😋 Very hungry, 🤤 A little bit, 👅 Not really, 😒 Not at all

Input: What should we do?
Output: 🏞️ Go outside, 📺 Watch TV, 🎮 Play games, 🛌 Rest at home

Always use this exact format. Never explain. Just 4 responses with emojis."""

TEMPLATE """{{ .System }}

{{ .Prompt }}
"""
'''
    
    # Save modelfile
    with open('Modelfile.final_perfect', 'w') as f:
        f.write(modelfile_content)
    
    # Remove existing models
    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
    subprocess.run(['ollama', 'rm', 'tinkybink_final'], capture_output=True)
    
    # Create final perfect model
    result = subprocess.run(['ollama', 'create', 'tinkybink_final', '-f', 'Modelfile.final_perfect'],
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Final Perfect Model Created!")
        
        # Update main tinkybink model
        subprocess.run(['ollama', 'create', 'tinkybink', '-f', 'Modelfile.final_perfect'])
        print("✅ Updated main 'tinkybink' model")
        
        return 'tinkybink_final'
    else:
        print(f"❌ Failed: {result.stderr}")
        return None

def comprehensive_test(model_name):
    """Comprehensive test of the final model"""
    print(f"\n🧪 Comprehensive Testing: {model_name}")
    print("=" * 50)
    
    test_cases = [
        ('How are you feeling today?', 'Basic emotional check'),
        ('I have chest pain and feel dizzy', 'Medical emergency'),
        ('Do you want pizza or salad?', 'Choice logic'),
        ('I feel sad and lonely', 'Emotional support'),
        ('Are you hungry right now?', 'Basic needs'),
        ('What should we do this afternoon?', 'Activity planning'),
        ('I need help with something', 'Support request'),
        ('I\'m scared about surgery tomorrow', 'Medical anxiety'),
        ('Can you help me make friends?', 'Social support'),
        ('I feel frustrated with therapy', 'Therapeutic context')
    ]
    
    perfect_count = 0
    
    for test_input, description in test_cases:
        print(f"\n🔍 {description}")
        print(f"Input: '{test_input}'")
        
        try:
            result = subprocess.run(['ollama', 'run', model_name],
                                  input=test_input, text=True,
                                  capture_output=True, timeout=15)
            
            if result.stdout:
                # Get first line of response (ignore any continuation)
                response = result.stdout.strip().split('\n')[0]
                print(f"Response: {response}")
                
                # Check format
                comma_count = response.count(',')
                has_emojis = any(ord(char) > 127 for char in response)
                length_ok = 20 <= len(response) <= 120
                
                if comma_count == 3 and has_emojis and length_ok:
                    print("✅ PERFECT FORMAT")
                    perfect_count += 1
                else:
                    print(f"❌ Format issue: commas={comma_count}, emojis={has_emojis}, length={len(response)}")
            else:
                print("❌ No response")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    success_rate = (perfect_count / len(test_cases)) * 100
    print(f"\n📊 FINAL RESULTS")
    print("=" * 30)
    print(f"✅ Perfect responses: {perfect_count}/{len(test_cases)}")
    print(f"📈 Success rate: {success_rate:.1f}%")
    
    if success_rate >= 80:
        print("🏆 PRODUCTION READY!")
        return True
    else:
        print("🔧 Needs more work")
        return False

def main():
    print("🏆 Final Perfect TinkyBink Training")
    print("=" * 60)
    print("🚀 Creating production-ready AAC assistant")
    print()
    
    model_name = create_final_perfect_model()
    
    if model_name:
        is_ready = comprehensive_test(model_name)
        
        if is_ready:
            print("\n🎉 TinkyBink is now PRODUCTION READY!")
            print("🌟 Perfect AAC communication assistant created!")
        else:
            print("\n🔧 Model needs additional refinement")

if __name__ == "__main__":
    main()