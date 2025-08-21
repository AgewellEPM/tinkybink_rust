#!/bin/bash

# Comprehensive AAC Brain Test Suite
# Tests all critical communication scenarios for non-verbal users

BRAIN="/Users/lukekist/tinkybink_rust/target/release/tinkybink_complete"
PASS="✅"
FAIL="❌"
TOTAL=0
PASSED=0

echo "═══════════════════════════════════════════════════════════════"
echo "     🧠 TINKYBINK AAC BRAIN - COMPREHENSIVE TEST SUITE 🧠     "
echo "═══════════════════════════════════════════════════════════════"
echo

# Function to test a scenario
test_scenario() {
    local description="$1"
    local input="$2"
    local expected_keyword="$3"
    
    TOTAL=$((TOTAL + 1))
    
    # Run the brain and check if expected keyword appears in response
    result=$($BRAIN "$input" 2>/dev/null)
    
    if echo "$result" | grep -q "$expected_keyword"; then
        echo "$PASS $description"
        echo "   Input: '$input'"
        echo "   ✓ Found: $expected_keyword"
        PASSED=$((PASSED + 1))
    else
        echo "$FAIL $description"
        echo "   Input: '$input'"
        echo "   ✗ Missing: $expected_keyword"
        echo "   Response: $(echo $result | jq -r '.suggestions[0].text' 2>/dev/null)"
    fi
    echo
}

echo "🏥 MEDICAL EMERGENCIES"
echo "────────────────────────────────────────"
test_scenario "Chest pain emergency" "My chest hurts badly" "Emergency"
test_scenario "Severe headache" "My head is killing me" "Medicine"
test_scenario "Breathing difficulty" "I can't breathe" "Emergency"
test_scenario "Pain with aches variant" "My body aches all over" "Medicine"
test_scenario "Injury report" "I fell and hurt myself" "Nurse"

echo "🚽 BATHROOM NEEDS"
echo "────────────────────────────────────────"
test_scenario "Urgent bathroom" "I need to go right now" "bathroom"
test_scenario "Bathroom assistance" "I need help in the bathroom" "bathroom"
test_scenario "Toilet paper need" "I need toilet paper" "Toilet paper"
test_scenario "Bathroom accident" "I had an accident" "bathroom"

echo "🌡️ COMFORT & TEMPERATURE"
echo "────────────────────────────────────────"
test_scenario "Too cold" "I'm freezing" "cold"
test_scenario "Too hot" "I'm burning up" "hot"
test_scenario "Need blanket" "I need a blanket" "blanket"
test_scenario "Temperature adjustment" "Can you adjust the temperature" "temperature"

echo "🛏️ POSITIONING & MOVEMENT"
echo "────────────────────────────────────────"
test_scenario "Position change" "Help me turn over" "Turn over"
test_scenario "Sitting up" "I want to sit up" "Sit up"
test_scenario "Lying down" "I need to lie down" "Lie down"
test_scenario "Chair transfer" "Move me to the chair" "chair"
test_scenario "Uncomfortable position" "This position hurts" "Uncomfortable"

echo "😢 EMOTIONAL SUPPORT"
echo "────────────────────────────────────────"
test_scenario "Feeling sad" "I'm feeling really sad" "Sad"
test_scenario "Anxiety" "I'm worried about everything" "Worried"
test_scenario "Fear" "I'm scared" "comfort"
test_scenario "Loneliness" "I feel so alone" "comfort"
test_scenario "Frustration" "This is so frustrating" "Frustrated"

echo "🗣️ COMMUNICATION NEEDS"
echo "────────────────────────────────────────"
test_scenario "Repetition request" "Can you repeat that" "Repeat"
test_scenario "Volume request" "Please speak louder" "louder"
test_scenario "Confusion" "I don't understand" "understand"
test_scenario "Clarification" "What do you mean" "explain"

echo "🏠 LOCATION & ORIENTATION"
echo "────────────────────────────────────────"
test_scenario "Want to go home" "I want to go home" "home"
test_scenario "Go outside" "Take me outside" "outside"
test_scenario "Room navigation" "Take me to my room" "room"
test_scenario "Garden visit" "I want to see the garden" "garden"

echo "❓ INFORMATION NEEDS"
echo "────────────────────────────────────────"
test_scenario "Time inquiry" "What time is it" "time"
test_scenario "Day inquiry" "What day is today" "day"
test_scenario "Visitor inquiry" "Who is here with me" "Who"
test_scenario "Location inquiry" "Where am I" "Where"

echo "🍽️ FOOD & DRINK"
echo "────────────────────────────────────────"
test_scenario "Hunger" "I'm starving" "Hungry"
test_scenario "Thirst" "I need water" "Water"
test_scenario "Food preference" "I want something sweet" "Dessert"
test_scenario "Hot food" "I want hot food" "Hot meal"

echo "🎯 ORIGINAL BUG FIXES"
echo "────────────────────────────────────────"
test_scenario "Help (not music)" "I need help" "assistance"
test_scenario "Play (not music)" "I want to play" "games"
test_scenario "General assistance" "Can someone help me" "Get staff"

echo "💤 SLEEP & REST"
echo "────────────────────────────────────────"
test_scenario "Tired" "I'm exhausted" "sleep"
test_scenario "Bedtime" "I want to go to bed" "bed"
test_scenario "Can't sleep" "I can't sleep" "sleep"
test_scenario "Rest needed" "I need to rest" "rest"

echo "📺 ENTERTAINMENT"
echo "────────────────────────────────────────"
test_scenario "TV request" "I want to watch TV" "TV"
test_scenario "Music request" "Play some music" "Music"
test_scenario "Movie preference" "I want to watch a movie" "Movie"
test_scenario "Radio request" "Turn on the radio" "Radio"

echo "👥 SOCIAL NEEDS"
echo "────────────────────────────────────────"
test_scenario "Family contact" "I want to see my family" "Family"
test_scenario "Phone call" "I want to call someone" "Call"
test_scenario "Visitor request" "I want visitors" "Visit"

echo
echo "═══════════════════════════════════════════════════════════════"
echo "                       TEST RESULTS                             "
echo "═══════════════════════════════════════════════════════════════"
echo "  Total Tests: $TOTAL"
echo "  Passed: $PASSED"
echo "  Failed: $((TOTAL - PASSED))"
echo "  Success Rate: $(( (PASSED * 100) / TOTAL ))%"
echo

if [ $PASSED -eq $TOTAL ]; then
    echo "  🎉 ALL TESTS PASSED! BRAIN IS FULLY FUNCTIONAL! 🎉"
else
    echo "  ⚠️  Some tests failed. Review and fix detected issues."
fi
echo "═══════════════════════════════════════════════════════════════"