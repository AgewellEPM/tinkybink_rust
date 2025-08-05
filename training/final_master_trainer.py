#!/usr/bin/env python3
"""
Final Master TinkyBink Trainer
Last attempt - using structured template approach
"""
import subprocess

def create_final_master_model():
    """Create the final master model using structured approach"""
    print("👑 Creating Final Master TinkyBink")
    print("=" * 50)
    
    # Use a completely different approach - template-based
    modelfile_content = '''FROM llama3.2

PARAMETER temperature 0.3
PARAMETER top_p 0.8
PARAMETER repeat_penalty 1.0
PARAMETER top_k 30
PARAMETER num_predict 50

SYSTEM """You are TinkyBink, an AAC communication assistant.

When given an input, you respond with exactly 4 options using this format:
[emoji] [text], [emoji] [text], [emoji] [text], [emoji] [text]

Examples:
Input: How are you?
Output: 😊 Really good, 😐 I'm okay, 😔 Not great, 💭 Let me think

Input: I want food
Output: 🍕 Pizza sounds good, 🥗 Maybe salad, 💧 Just water, 🤔 Not hungry

Input: I have pain  
Output: 🤕 It hurts, 💊 Need medicine, 🤲 Help me, 📞 Call doctor

Always provide exactly 4 responses with emojis and text."""

TEMPLATE """{{ if .System }}{{ .System }}

{{ end }}{{ if .Prompt }}{{ .Prompt }}{{ end }}

Response: """
'''
    
    # Save modelfile
    with open('Modelfile.final_master', 'w') as f:
        f.write(modelfile_content)
    
    # Remove existing models
    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
    subprocess.run(['ollama', 'rm', 'tinkybink_final_master'], capture_output=True)
    
    # Create final master model
    result = subprocess.run(['ollama', 'create', 'tinkybink_final_master', '-f', 'Modelfile.final_master'],
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Final Master Model Created!")
        
        # Update main tinkybink model
        subprocess.run(['ollama', 'create', 'tinkybink', '-f', 'Modelfile.final_master'])
        print("✅ Updated main 'tinkybink' model")
        
        return 'tinkybink_final_master'
    else:
        print(f"❌ Failed: {result.stderr}")
        return None

def ultimate_validation(model_name):
    """Ultimate validation focusing on key scenarios"""
    print(f"\n👑 Ultimate Master Validation: {model_name}")
    print("=" * 60)
    
    # Comprehensive scenarios you requested
    ultimate_tests = [
        # Basic scenarios
        ('How are you feeling today?', 'Basic emotions'),
        ('I feel happy', 'Positive emotion'),
        ('I feel sad', 'Negative emotion'),
        
        # Medical scenarios  
        ('I have chest pain', 'Medical emergency'),
        ('My head hurts', 'Health issue'),
        ('I need medicine', 'Medical care'),
        
        # Pet scenarios
        ('I want to pet the dog', 'Pet interaction'),
        ('The cat is meowing', 'Pet communication'), 
        ('My bird is singing', 'Pet behavior'),
        ('Can I feed the fish?', 'Pet care'),
        
        # Mall/Shopping scenarios
        ('I want to buy shoes', 'Shopping purchase'),
        ('This store is too crowded', 'Shopping overwhelm'),
        ('Where is the bathroom?', 'Shopping navigation'),
        ('The line is very long', 'Shopping wait'),
        ('I need help finding something', 'Shopping assistance'),
        ('How much does this cost?', 'Shopping price'),
        
        # Food scenarios
        ('What should I eat for lunch?', 'Food choice'),
        ('I am hungry', 'Food need'),
        ('This food is too spicy', 'Food problem'),
        ('Can I have dessert?', 'Food request'),
        
        # Transportation
        ('The bus is late', 'Transport delay'),
        ('I missed my stop', 'Transport error'),
        ('I need a ride', 'Transport help'),
        
        # Technology
        ('My phone is broken', 'Tech problem'),
        ('The wifi is not working', 'Tech connectivity'),
        
        # Weather/Outdoor
        ('It is raining outside', 'Weather challenge'),
        ('I want to go to the park', 'Outdoor activity'),
        
        # Social situations
        ('I want to make friends', 'Social connection'),
        ('Someone was mean to me', 'Social conflict'),
        
        # Choices
        ('Pizza or salad for dinner?', 'Food choice'),
        ('Red shirt or blue shirt?', 'Clothing choice'),
        ('Should we stay or go?', 'Activity choice')
    ]
    
    perfect_10_count = 0
    excellent_count = 0
    
    print(f"🎯 Testing {len(ultimate_tests)} comprehensive scenarios...")
    print()
    
    for i, (test_input, category) in enumerate(ultimate_tests, 1):
        print(f"🔍 Test {i:2d}/{len(ultimate_tests)}: {category}")
        print(f"Input: '{test_input}'")
        
        try:
            result = subprocess.run(['ollama', 'run', model_name],
                                  input=test_input, text=True,
                                  capture_output=True, timeout=15)
            
            if result.stdout:
                # Get clean response
                full_response = result.stdout.strip()
                response = full_response.split('\n')[0]
                
                # Clean up any "Response:" prefix
                if response.startswith('Response:'):
                    response = response[9:].strip()
                
                print(f"Response: {response}")
                
                # Scoring criteria
                comma_count = response.count(',')
                emojis = [char for char in response if ord(char) > 127]
                text_words = [word for word in response.split() if any(c.isalpha() for c in word)]
                
                # Perfect 10/10 criteria
                format_perfect = comma_count == 3  # Exactly 4 responses
                emoji_perfect = len(emojis) >= 4   # At least 4 emojis
                text_perfect = len(text_words) >= 8  # At least 8 meaningful words
                length_perfect = 30 <= len(response) <= 120  # Good length
                
                score = sum([format_perfect, emoji_perfect, text_perfect, length_perfect])
                
                if score == 4:
                    print("👑 PERFECT 10/10!")
                    perfect_10_count += 1
                elif score == 3:
                    print("✨ EXCELLENT 9/10")
                    excellent_count += 1
                elif score >= 2:
                    print("✅ GOOD 7-8/10")
                else:
                    print(f"🔧 NEEDS WORK ({score}/4 criteria met)")
                    print(f"   Format: {format_perfect}, Emojis: {emoji_perfect}, Text: {text_perfect}, Length: {length_perfect}")
                
            else:
                print("❌ NO RESPONSE")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
        
        print()  # Space between tests
    
    # Final results
    total_tests = len(ultimate_tests)
    perfect_rate = (perfect_10_count / total_tests) * 100
    excellent_rate = ((perfect_10_count + excellent_count) / total_tests) * 100
    
    print("👑 ULTIMATE MASTER VALIDATION RESULTS")
    print("=" * 50)
    print(f"🏆 Perfect 10/10: {perfect_10_count}/{total_tests} ({perfect_rate:.1f}%)")
    print(f"✨ Excellent 9/10: {excellent_count}/{total_tests}")
    print(f"📊 Combined Excellence: {excellent_rate:.1f}%")
    
    if perfect_rate >= 80:
        print("👑 ULTIMATE MASTERY ACHIEVED!")
        print("🌟 TinkyBink is now a 10/10 AAC assistant!")
        return True
    elif excellent_rate >= 80:
        print("✨ NEAR PERFECTION - Excellent quality!")
        return True
    elif excellent_rate >= 60:
        print("✅ HIGH QUALITY - Very good performance")
        return True
    else:
        print("🔧 Additional refinement needed")
        return False

def main():
    print("👑 Final Master TinkyBink Training")
    print("=" * 60)
    print("🎯 Ultimate attempt at 10/10 perfection")
    print("🔥 ALL scenarios: pets, shopping, medical, social!")
    print()
    
    model_name = create_final_master_model()
    
    if model_name:
        success = ultimate_validation(model_name)
        
        if success:
            print("\n🎊 ULTIMATE SUCCESS!")
            print("👑 TinkyBink Master is ready!")
        else:
            print("\n🔄 Model may need further iteration")

if __name__ == "__main__":
    main()