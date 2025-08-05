#!/usr/bin/env python3
"""
Test the newly trained TinkyBink model in the app
"""
import subprocess
import time
import os

def test_with_trained_model(user_type, test_input, description):
    """Test trained model with user input"""
    print(f"\n🧠 Testing: {description}")
    print(f"User Type: {user_type}, Input: '{test_input}'")
    print("-" * 50)
    
    os.chdir('/Users/lukekist/tinkybink_rust')
    
    # Input sequence for the demo
    input_sequence = f"{user_type}\n{test_input}\nquit\n"
    
    try:
        cargo_path = os.path.expanduser('~/.cargo/bin/cargo')
        result = subprocess.run(
            [cargo_path, 'run', 'demo'],
            input=input_sequence,
            text=True,
            capture_output=True,
            timeout=20
        )
        
        # Parse output for the AI-generated suggestions
        lines = result.stdout.split('\n')
        
        capturing = False
        found_ai = False
        for line in lines:
            if "Using AI-powered suggestions" in line or "Using adaptive AI suggestions" in line:
                found_ai = True
                print("🤖 " + line.strip())
            elif "can tap these to communicate" in line:
                capturing = True
                print(line.strip())
            elif capturing and line.strip():
                if line.strip().startswith(('1.', '2.', '3.', '4.')):
                    print(line.strip())
                elif "taps number" in line:
                    break
        
        if not found_ai:
            print("⚠️  AI suggestions not detected - may be using fallback")
                    
    except subprocess.TimeoutExpired:
        print("⚠️ Test timed out")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🧠 Testing Trained TinkyBink AAC Model")
    print("=" * 50)
    
    # Test the trained model with diverse inputs
    test_cases = [
        ("1", "Do you want a cookie?", "Child food preference"),
        ("1", "Time for bed", "Child bedtime routine"),
        ("2", "How are you feeling?", "Adult emotional check-in"),
        ("2", "Ready for the meeting?", "Adult work context"),
        ("3", "How is your pain level?", "Stroke survivor medical"),
        ("3", "Ready for speech therapy?", "Stroke survivor therapy"),
        ("1", "Let's go to the park", "Child outdoor activity"),
        ("2", "Do you need assistance?", "Adult help offering"),
        ("3", "Time for medication", "Medical routine"),
    ]
    
    for user_type, test_input, description in test_cases:
        test_with_trained_model(user_type, test_input, description)
        time.sleep(2)

if __name__ == "__main__":
    main()