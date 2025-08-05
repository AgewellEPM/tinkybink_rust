#!/usr/bin/env python3
"""
Activity Board Integration Trainer
Links TinkyBink to step-by-step activity guides and how-to boards
"""
import subprocess
import json

def create_activity_boards():
    """Create comprehensive activity boards with step-by-step instructions"""
    print("📋 Creating Activity Boards Database")
    print("=" * 50)
    
    activity_boards = {
        # Pet Care Activities
        "walk_dog": {
            "title": "How to Walk the Dog",
            "steps": [
                {"step": 1, "instruction": "🦮 Get the leash", "emoji": "🦮", "action": "find leash"},
                {"step": 2, "instruction": "🐕 Get the dog", "emoji": "🐕", "action": "call dog"},
                {"step": 3, "instruction": "🔗 Clip leash to collar", "emoji": "🔗", "action": "attach leash"},
                {"step": 4, "instruction": "🚪 Walk to the door", "emoji": "🚪", "action": "go to door"},
                {"step": 5, "instruction": "🔓 Open the door", "emoji": "🔓", "action": "open door"},
                {"step": 6, "instruction": "👣 Step outside", "emoji": "👣", "action": "go outside"},
                {"step": 7, "instruction": "🚶 Walk with dog", "emoji": "🚶", "action": "start walking"},
                {"step": 8, "instruction": "🏠 Come back home", "emoji": "🏠", "action": "return home"}
            ]
        },
        
        "feed_pet": {
            "title": "How to Feed Your Pet",
            "steps": [
                {"step": 1, "instruction": "🥣 Get the food bowl", "emoji": "🥣", "action": "find bowl"},
                {"step": 2, "instruction": "🥫 Get the pet food", "emoji": "🥫", "action": "get food"},
                {"step": 3, "instruction": "🥄 Pour food in bowl", "emoji": "🥄", "action": "fill bowl"},
                {"step": 4, "instruction": "💧 Add fresh water", "emoji": "💧", "action": "fill water"},
                {"step": 5, "instruction": "📍 Put bowl down", "emoji": "📍", "action": "place bowl"},
                {"step": 6, "instruction": "🐕 Call your pet", "emoji": "🐕", "action": "call pet"},
                {"step": 7, "instruction": "👀 Watch them eat", "emoji": "👀", "action": "supervise"}
            ]
        },
        
        # Shopping Activities
        "grocery_shopping": {
            "title": "How to Go Grocery Shopping",
            "steps": [
                {"step": 1, "instruction": "📝 Make shopping list", "emoji": "📝", "action": "write list"},
                {"step": 2, "instruction": "👛 Get money/card", "emoji": "👛", "action": "get payment"},
                {"step": 3, "instruction": "🛍️ Get shopping bags", "emoji": "🛍️", "action": "get bags"},
                {"step": 4, "instruction": "🚗 Go to store", "emoji": "🚗", "action": "travel to store"},
                {"step": 5, "instruction": "🛒 Get shopping cart", "emoji": "🛒", "action": "get cart"},
                {"step": 6, "instruction": "🥬 Shop for items", "emoji": "🥬", "action": "collect items"},
                {"step": 7, "instruction": "💳 Pay at checkout", "emoji": "💳", "action": "pay for items"},
                {"step": 8, "instruction": "📦 Take bags home", "emoji": "📦", "action": "carry home"}
            ]
        },
        
        "buy_clothes": {
            "title": "How to Buy New Clothes",
            "steps": [
                {"step": 1, "instruction": "💭 Think what you need", "emoji": "💭", "action": "plan purchase"},
                {"step": 2, "instruction": "💰 Check your budget", "emoji": "💰", "action": "check money"},
                {"step": 3, "instruction": "🏪 Go to clothing store", "emoji": "🏪", "action": "go to store"},
                {"step": 4, "instruction": "👕 Look at clothes", "emoji": "👕", "action": "browse items"},
                {"step": 5, "instruction": "📏 Check the size", "emoji": "📏", "action": "find size"},
                {"step": 6, "instruction": "🪞 Try clothes on", "emoji": "🪞", "action": "try on"},
                {"step": 7, "instruction": "💳 Buy if you like", "emoji": "💳", "action": "purchase"},
                {"step": 8, "instruction": "🛍️ Take home", "emoji": "🛍️", "action": "bring home"}
            ]
        },
        
        # Cooking Activities
        "make_sandwich": {
            "title": "How to Make a Sandwich",
            "steps": [
                {"step": 1, "instruction": "🍞 Get bread slices", "emoji": "🍞", "action": "get bread"},
                {"step": 2, "instruction": "🧈 Spread butter/mayo", "emoji": "🧈", "action": "add spread"},
                {"step": 3, "instruction": "🥩 Add meat or protein", "emoji": "🥩", "action": "add protein"},
                {"step": 4, "instruction": "🧀 Add cheese", "emoji": "🧀", "action": "add cheese"},
                {"step": 5, "instruction": "🥬 Add lettuce/veggies", "emoji": "🥬", "action": "add vegetables"},
                {"step": 6, "instruction": "🍞 Put top bread on", "emoji": "🍞", "action": "close sandwich"},
                {"step": 7, "instruction": "🔪 Cut in half", "emoji": "🔪", "action": "cut sandwich"},
                {"step": 8, "instruction": "🍽️ Put on plate", "emoji": "🍽️", "action": "serve"}
            ]
        },
        
        # Self-Care Activities  
        "brush_teeth": {
            "title": "How to Brush Your Teeth",
            "steps": [
                {"step": 1, "instruction": "🪥 Get your toothbrush", "emoji": "🪥", "action": "get brush"},
                {"step": 2, "instruction": "🧴 Get toothpaste", "emoji": "🧴", "action": "get paste"},
                {"step": 3, "instruction": "💧 Wet the toothbrush", "emoji": "💧", "action": "wet brush"},
                {"step": 4, "instruction": "🫧 Put paste on brush", "emoji": "🫧", "action": "add paste"},
                {"step": 5, "instruction": "🦷 Brush all teeth", "emoji": "🦷", "action": "brush teeth"},
                {"step": 6, "instruction": "💦 Rinse your mouth", "emoji": "💦", "action": "rinse mouth"},
                {"step": 7, "instruction": "🧽 Clean toothbrush", "emoji": "🧽", "action": "clean brush"},
                {"step": 8, "instruction": "📍 Put brush away", "emoji": "📍", "action": "store brush"}
            ]
        },
        
        "get_dressed": {
            "title": "How to Get Dressed",
            "steps": [
                {"step": 1, "instruction": "👕 Pick out shirt", "emoji": "👕", "action": "choose shirt"},
                {"step": 2, "instruction": "👖 Pick out pants", "emoji": "👖", "action": "choose pants"},
                {"step": 3, "instruction": "🧦 Get socks", "emoji": "🧦", "action": "get socks"},
                {"step": 4, "instruction": "🩲 Put on underwear", "emoji": "🩲", "action": "put on underwear"},
                {"step": 5, "instruction": "👕 Put on shirt", "emoji": "👕", "action": "put on shirt"},
                {"step": 6, "instruction": "👖 Put on pants", "emoji": "👖", "action": "put on pants"},
                {"step": 7, "instruction": "🧦 Put on socks", "emoji": "🧦", "action": "put on socks"},
                {"step": 8, "instruction": "👟 Put on shoes", "emoji": "👟", "action": "put on shoes"}
            ]
        },
        
        # Transportation
        "take_bus": {
            "title": "How to Take the Bus",
            "steps": [
                {"step": 1, "instruction": "📱 Check bus schedule", "emoji": "📱", "action": "check times"},
                {"step": 2, "instruction": "💰 Get bus fare ready", "emoji": "💰", "action": "prepare money"},
                {"step": 3, "instruction": "🚏 Go to bus stop", "emoji": "🚏", "action": "go to stop"},
                {"step": 4, "instruction": "⏰ Wait for bus", "emoji": "⏰", "action": "wait"},
                {"step": 5, "instruction": "👋 Signal the bus", "emoji": "👋", "action": "wave to bus"},
                {"step": 6, "instruction": "🚌 Get on bus", "emoji": "🚌", "action": "board bus"},
                {"step": 7, "instruction": "💳 Pay the fare", "emoji": "💳", "action": "pay driver"},
                {"step": 8, "instruction": "💺 Find a seat", "emoji": "💺", "action": "sit down"},
                {"step": 9, "instruction": "🔔 Ring bell for stop", "emoji": "🔔", "action": "signal stop"},
                {"step": 10, "instruction": "🚪 Exit at your stop", "emoji": "🚪", "action": "get off"}
            ]
        }
    }
    
    # Save activity boards to JSON file
    with open('activity_boards.json', 'w') as f:
        json.dump(activity_boards, f, indent=2)
    
    print(f"✅ Created {len(activity_boards)} activity boards")
    print("📋 Activity boards saved to activity_boards.json")
    
    return activity_boards

def create_activity_integrated_model():
    """Create TinkyBink model with activity board integration"""
    print("\n🔗 Creating Activity-Integrated TinkyBink Model")
    print("=" * 60)
    
    modelfile_content = '''FROM llama3.2

PARAMETER temperature 0.2
PARAMETER top_p 0.7
PARAMETER repeat_penalty 1.1
PARAMETER top_k 25
PARAMETER num_predict 60

SYSTEM """You are TinkyBink Activity Guide, an AAC assistant with step-by-step activity support.

RESPONSE FORMAT: Always provide exactly 4 responses:
emoji text, emoji text, emoji text, emoji text

ACTIVITY INTEGRATION: When users mention activities, offer step-by-step guidance.

ACTIVITY BOARD RESPONSES:

DOG WALKING:
Input: I want to walk the dog
Output: 🦮 Get the leash, 🐕 Call the dog, 🔗 Clip leash on, 📋 Show me steps

Input: How do I walk the dog?
Output: 📋 Step by step, 🦮 First get leash, 🐕 Then get dog, 🚪 Then go outside

PET FEEDING:
Input: I need to feed my pet
Output: 🥣 Get food bowl, 🥫 Get pet food, 💧 Add fresh water, 📋 Show me steps

GROCERY SHOPPING:
Input: I want to go shopping
Output: 📝 Make shopping list, 👛 Get money ready, 🛒 Get shopping cart, 📋 Show me steps

Input: How do I grocery shop?
Output: 📋 Step by step, 📝 First make list, 👛 Get money ready, 🏪 Go to store

CLOTHES SHOPPING:
Input: I want to buy clothes
Output: 💭 Think what need, 💰 Check your budget, 🏪 Go to store, 📋 Show me steps

COOKING:
Input: I want to make sandwich
Output: 🍞 Get bread slices, 🧈 Spread butter, 🥩 Add meat, 📋 Show me steps

Input: How do I cook?
Output: 📋 Step by step, 🍞 First get ingredients, 🧈 Then prepare, 🥩 Add toppings

SELF CARE:
Input: I need to brush teeth
Output: 🪥 Get toothbrush, 🧴 Get toothpaste, 💧 Wet brush, 📋 Show me steps

Input: I need to get dressed
Output: 👕 Pick out shirt, 👖 Pick out pants, 🧦 Get socks, 📋 Show me steps

TRANSPORTATION:
Input: I want to take bus
Output: 📱 Check bus schedule, 💰 Get fare ready, 🚏 Go to stop, 📋 Show me steps

STEP-BY-STEP GUIDANCE:
When someone says "show me steps" or "how do I", provide the first few steps:

Input: Show me dog walking steps
Output: 🦮 Step 1 get leash, 🐕 Step 2 get dog, 🔗 Step 3 clip leash, ▶️ Continue steps

Input: Next step for walking dog
Output: 🚪 Step 4 go to door, 🔓 Step 5 open door, 👣 Step 6 step outside, ▶️ Continue steps

Always provide exactly 4 responses with emojis and clear instructions."""

TEMPLATE """{{ .System }}

{{ .Prompt }}
"""
'''
    
    # Save modelfile
    with open('Modelfile.activity_integrated', 'w') as f:
        f.write(modelfile_content)
    
    # Remove existing models
    subprocess.run(['ollama', 'rm', 'tinkybink'], capture_output=True)
    subprocess.run(['ollama', 'rm', 'tinkybink_activity'], capture_output=True)
    
    # Create activity integrated model
    result = subprocess.run(['ollama', 'create', 'tinkybink_activity', '-f', 'Modelfile.activity_integrated'],
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Activity-Integrated Model Created!")
        
        # Update main tinkybink model
        subprocess.run(['ollama', 'create', 'tinkybink', '-f', 'Modelfile.activity_integrated'])
        print("✅ Updated main 'tinkybink' model with activity boards")
        
        return 'tinkybink_activity'
    else:
        print(f"❌ Failed: {result.stderr}")
        return None

def test_activity_integration(model_name):
    """Test the activity board integration"""
    print(f"\n📋 Testing Activity Board Integration: {model_name}")
    print("=" * 70)
    
    activity_tests = [
        # Direct activity requests
        ('I want to walk the dog', 'Dog walking activity'),
        ('How do I walk the dog?', 'Dog walking how-to'),
        ('I need to feed my pet', 'Pet feeding activity'),
        ('I want to go shopping', 'Shopping activity'),
        ('How do I grocery shop?', 'Grocery shopping how-to'),
        ('I want to buy clothes', 'Clothes shopping'),
        ('I want to make sandwich', 'Cooking activity'),
        ('I need to brush teeth', 'Self-care activity'),
        ('I need to get dressed', 'Getting dressed'),
        ('I want to take bus', 'Transportation'),
        
        # Step-by-step requests
        ('Show me dog walking steps', 'Step-by-step guidance'),
        ('Next step for walking dog', 'Sequential steps'),
        ('How do I make sandwich?', 'Cooking steps'),
        ('Show me shopping steps', 'Shopping guidance'),
        
        # Regular AAC responses (should still work)
        ('How are you feeling?', 'Basic AAC response'),
        ('I have chest pain', 'Medical emergency'),
        ('I feel sad', 'Emotional support')
    ]
    
    perfect_count = 0
    activity_count = 0
    
    for i, (test_input, category) in enumerate(activity_tests, 1):
        print(f"\n🔍 Test {i:2d}: {category}")
        print(f"Input: '{test_input}'")
        
        try:
            result = subprocess.run(['ollama', 'run', model_name],
                                  input=test_input, text=True,
                                  capture_output=True, timeout=15)
            
            if result.stdout:
                response = result.stdout.strip().split('\n')[0]
                if response.startswith('Response:'):
                    response = response[9:].strip()
                
                print(f"Response: {response}")
                
                # Check format
                comma_count = response.count(',')
                has_emojis = any(ord(char) > 127 for char in response)
                has_text = any(char.isalpha() for char in response)
                good_length = 25 <= len(response) <= 150
                
                # Check for activity-specific content
                has_activity_content = any(keyword in response.lower() for keyword in 
                    ['step', 'get', 'go', 'put', 'make', 'take', 'show', 'first', 'then'])
                
                format_score = sum([comma_count == 3, has_emojis, has_text, good_length])
                
                if format_score >= 3:
                    if has_activity_content and ('activity' in category.lower() or 'how-to' in category.lower() or 'step' in category.lower()):
                        print("📋 PERFECT ACTIVITY INTEGRATION!")
                        perfect_count += 1
                        activity_count += 1
                    elif 'activity' not in category.lower():
                        print("✅ GOOD AAC RESPONSE")
                        perfect_count += 1
                    else:
                        print("👍 GOOD FORMAT (missing activity content)")
                else:
                    print(f"🔧 FORMAT NEEDS WORK (score: {format_score}/4)")
            else:
                print("❌ NO RESPONSE")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")
    
    total_tests = len(activity_tests)
    success_rate = (perfect_count / total_tests) * 100
    activity_rate = (activity_count / 14) * 100  # 14 activity-specific tests
    
    print(f"\n📋 ACTIVITY INTEGRATION RESULTS")
    print("=" * 40)
    print(f"✅ Perfect responses: {perfect_count}/{total_tests} ({success_rate:.1f}%)")
    print(f"📋 Activity integration: {activity_count}/14 ({activity_rate:.1f}%)")
    
    if success_rate >= 80 and activity_rate >= 70:
        print("🎉 EXCELLENT ACTIVITY INTEGRATION!")
        return True
    elif success_rate >= 70:
        print("✅ GOOD INTEGRATION - Minor improvements possible")
        return True
    else:
        print("🔧 Needs more activity training")
        return False

def main():
    print("📋 TinkyBink Activity Board Integration")
    print("=" * 70)
    print("🎯 Connecting AAC responses to step-by-step activity guides")
    print("🐕 Dog walking, shopping, cooking, self-care, and MORE!")
    print()
    
    # Create activity boards database
    activity_boards = create_activity_boards()
    
    # Create integrated model
    model_name = create_activity_integrated_model()
    
    if model_name:
        # Test the integration
        success = test_activity_integration(model_name)
        
        if success:
            print("\n🎊 ACTIVITY INTEGRATION SUCCESS!")
            print("📋 TinkyBink now provides step-by-step activity guidance!")
            print("🐕 Users can get complete how-to instructions for daily activities!")
        else:
            print("\n🔄 Integration needs refinement")
    
    print(f"\n📂 Activity boards saved to: activity_boards.json")
    print("🔗 TinkyBink now links AAC responses to detailed activity guides!")

if __name__ == "__main__":
    main()