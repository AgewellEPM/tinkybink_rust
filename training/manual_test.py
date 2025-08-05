#!/usr/bin/env python3
"""
Manual test of TinkyBink AAC adaptive user profiles
"""
import subprocess
import time
import os

def test_user_profile(user_type, test_input, description):
    """Test a specific user type with input"""
    print(f"\n🔎 Testing: {description}")
    print(f"User Type: {user_type}, Input: '{test_input}'")
    print("-" * 50)
    
    # Change to the right directory
    os.chdir('/Users/lukekist/tinkybink_rust')
    
    # Create the input sequence
    input_sequence = f"{user_type}\n{test_input}\nquit\n"
    
    try:
        # Run the demo with input
        cargo_path = os.path.expanduser('~/.cargo/bin/cargo')
        result = subprocess.run(
            [cargo_path, 'run', 'demo'],
            input=input_sequence,
            text=True,
            capture_output=True,
            timeout=15
        )
        
        # Parse the output to find the relevant section
        lines = result.stdout.split('\n')
        
        # Look for the user selection and responses
        capturing = False
        for line in lines:
            if "can tap these to communicate" in line:
                capturing = True
                print(line)
            elif capturing and line.strip():
                if line.strip().startswith(('1.', '2.', '3.', '4.')):
                    print(line)
                elif "taps number" in line:
                    break
                    
        if result.stderr:
            print(f"Note: Some warnings in stderr (expected)")
            
    except subprocess.TimeoutExpired:
        print("⚠️ Test timed out")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🧪 TinkyBink AAC Adaptive User Profile Test")
    print("=" * 50)
    
    # Test same input with different user types
    test_cases = [
        ("1", "How are you feeling?", "Child user response to feelings"),
        ("2", "How are you feeling?", "Adult user response to feelings"),
        ("3", "How are you feeling?", "Stroke survivor response to feelings"),
        ("3", "Ready for speech therapy?", "Stroke survivor therapy context"),
        ("2", "Ready for the meeting?", "Adult work context"),
        ("1", "Do you want a cookie?", "Child food choice"),
        ("3", "How is your pain level?", "Stroke survivor medical query"),
        ("2", "Should I speak slower?", "Adult communication preference"),
    ]
    
    for user_type, test_input, description in test_cases:
        test_user_profile(user_type, test_input, description)
        time.sleep(1)  # Brief pause between tests

if __name__ == "__main__":
    main()