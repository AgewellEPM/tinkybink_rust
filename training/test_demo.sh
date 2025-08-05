#!/bin/bash
# Test script for TinkyBink AAC adaptive user profiles

cd "$(dirname "$0")/.."

echo "🧪 Testing TinkyBink AAC Adaptive User Profiles"
echo "==============================================="

# Function to test a user type
test_user_type() {
    local user_type=$1
    local test_input=$2
    local expected_behavior=$3
    
    echo ""
    echo "🔎 Testing User Type: $user_type"
    echo "Input: '$test_input'"
    echo "Expected: $expected_behavior"
    echo "---"
    
    # Send input to the demo
    echo -e "$user_type\n$test_input\nquit" | timeout 10s $HOME/.cargo/bin/cargo run demo 2>/dev/null | \
        grep -A 10 "can tap these to communicate" | \
        head -6
    
    echo ""
}

# Test different user types with the same input
echo "Testing how different user types respond to the same medical question:"

test_user_type "1" "How are you feeling?" "Child-like responses (Yes!, No thanks, Maybe, I don't know)"
test_user_type "2" "How are you feeling?" "Adult responses (I agree, I disagree, Please clarify, I understand)" 
test_user_type "3" "How are you feeling?" "Stroke survivor responses (Yes, No, Help, Thank you)"

echo "Testing therapy context for stroke survivor:"
test_user_type "3" "Ready for speech therapy?" "Adaptive therapy responses"

echo "Testing work context for adult:"
test_user_type "2" "Ready for the meeting?" "Professional responses"

echo ""
echo "✅ Test completed! Check outputs above for adaptive behavior."