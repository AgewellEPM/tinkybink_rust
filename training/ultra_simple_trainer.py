#!/usr/bin/env python3
"""
Ultra Simple TinkyBink Trainer
The absolute simplest possible approach that might work
"""
import subprocess

def create_ultra_simple_model():
    """Create the simplest possible model"""
    print("🔧 Creating Ultra Simple Model")
    print("=" * 40)
    
    # Try with llama3.2 which might follow instructions better
    modelfile_content = '''FROM llama3.2

PARAMETER temperature 0.2
PARAMETER top_p 0.6
PARAMETER repeat_penalty 1.1
PARAMETER top_k 20
PARAMETER num_predict 30

SYSTEM """You are an AAC helper. Always give exactly 4 short responses with emojis.

Format: emoji response, emoji response, emoji response, emoji response

Example:
Input: How do you feel?
Output: 😊 Happy, 😐 Okay, 😔 Sad, 💭 Thinking

Always use this exact format."""

TEMPLATE """{{ .System }}

{{ .Prompt }}
"""
'''
    
    # Save modelfile
    with open('Modelfile.simple', 'w') as f:
        f.write(modelfile_content)
    
    # Remove existing models
    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
    subprocess.run(['ollama', 'rm', 'simple_aac'], capture_output=True)
    
    # Create simple model
    result = subprocess.run(['ollama', 'create', 'simple_aac', '-f', 'Modelfile.simple'],
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Ultra Simple Model Created!")
        
        # Update main tinkybink model
        subprocess.run(['ollama', 'create', 'tinkybink', '-f', 'Modelfile.simple'])
        print("✅ Updated main 'tinkybink' model")
        
        return 'simple_aac'
    else:
        print(f"❌ Failed: {result.stderr}")
        return None

def test_simple_model(model_name):
    """Test the simple model"""
    print(f"\n🧪 Testing Simple Model: {model_name}")
    print("=" * 40)
    
    test_inputs = [
        'How do you feel?',
        'Are you hungry?',
        'Want to play?'
    ]
    
    for test_input in test_inputs:
        print(f"\n🔍 Testing: '{test_input}'")
        
        try:
            result = subprocess.run(['ollama', 'run', model_name],
                                  input=test_input, text=True,
                                  capture_output=True, timeout=10)
            
            if result.stdout:
                response = result.stdout.strip()
                print(f"Response: {response}")
                
                # Simple check
                comma_count = response.count(',')
                print(f"Comma count: {comma_count}")
            else:
                print("❌ No response")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    print("🔧 Ultra Simple TinkyBink Training")
    print("=" * 50)
    
    model_name = create_ultra_simple_model()
    
    if model_name:
        test_simple_model(model_name)

if __name__ == "__main__":
    main()