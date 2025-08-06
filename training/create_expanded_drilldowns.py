#!/usr/bin/env python3
"""
Create Expanded Multi-Layer Drill-Downs
Add holidays, weather, emotions, and more complex navigation
"""
import json

def create_expanded_drilldowns():
    """Create expanded multi-layer drill-down examples"""
    
    print("🎯 TinkyBink Expanded Drill-Down Creator")
    print("=" * 60)
    print("🎄 Holiday celebrations → specific activities")
    print("🌤️ Weather discussion → clothing choices")
    print("😊 Emotions → coping strategies")
    print("🏠 Home activities → room → specific task")
    print()
    
    all_expanded_examples = []
    
    # HOLIDAY CELEBRATION DRILL-DOWNS
    holiday_drilldowns = create_holiday_drilldowns()
    all_expanded_examples.extend(holiday_drilldowns)
    print(f"✅ Holiday Celebration Drill-downs: {len(holiday_drilldowns)} examples")
    
    # WEATHER & CLOTHING DRILL-DOWNS
    weather_drilldowns = create_weather_clothing_drilldowns()
    all_expanded_examples.extend(weather_drilldowns)
    print(f"✅ Weather & Clothing Drill-downs: {len(weather_drilldowns)} examples")
    
    # EMOTION & COPING DRILL-DOWNS
    emotion_drilldowns = create_emotion_coping_drilldowns()
    all_expanded_examples.extend(emotion_drilldowns)
    print(f"✅ Emotion & Coping Drill-downs: {len(emotion_drilldowns)} examples")
    
    # HOME ACTIVITIES DRILL-DOWNS
    home_drilldowns = create_home_activities_drilldowns()
    all_expanded_examples.extend(home_drilldowns)
    print(f"✅ Home Activities Drill-downs: {len(home_drilldowns)} examples")
    
    # SCHOOL SUBJECTS DRILL-DOWNS
    school_drilldowns = create_school_subject_drilldowns()
    all_expanded_examples.extend(school_drilldowns)
    print(f"✅ School Subject Drill-downs: {len(school_drilldowns)} examples")
    
    # BEDTIME ROUTINE DRILL-DOWNS
    bedtime_drilldowns = create_bedtime_routine_drilldowns()
    all_expanded_examples.extend(bedtime_drilldowns)
    print(f"✅ Bedtime Routine Drill-downs: {len(bedtime_drilldowns)} examples")
    
    total_examples = len(all_expanded_examples)
    
    print(f"\n🎯 TOTAL EXPANDED DRILL-DOWN EXAMPLES: {total_examples}")
    
    # Save expanded drill-down examples
    output_file = "tinkybink_expanded_drilldowns.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in all_expanded_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved: {output_file}")
    print(f"🔄 Expanded multi-layer conversation system complete!")
    
    return total_examples

def create_holiday_drilldowns():
    """Create holiday celebration drill-down conversations"""
    examples = []
    
    # Layer 1: Holiday Selection
    layer1_scenarios = [
        ("What holiday celebrating?", "🎄 Christmas is coming, 🎃 Halloween is spooky, 🦃 Thanksgiving feast time, 🎆 New Year party", "holiday_selection_layer1"),
        ("Which celebration today?", "🎂 Birthday party special, 💕 Valentine's Day love, 🍀 St Patrick's green, 🇺🇸 Fourth July fireworks", "holiday_selection_layer1")
    ]
    
    # Layer 2: Christmas Activities (after selecting Christmas)
    layer2_christmas_scenarios = [
        ("Christmas chosen! What activity?", "🎁 Opening presents exciting, 🍪 Baking cookies together, 🎄 Decorating tree beautiful, 🎵 Singing carols joyful", "christmas_activity_layer2"),
        ("Christmas time! What doing?", "🧑‍🎄 Visit Santa Claus, 🎬 Watch Christmas movies, 🕯️ Light advent candles, 🎪 Christmas pageant performing", "christmas_activity_layer2")
    ]
    
    # Layer 3: Present Opening Details (after selecting presents)
    layer3_present_scenarios = [
        ("Opening presents! Which first?", "📦 Big box mysterious, 🎁 Small gift wrapped, 👕 Clothing package soft, 📚 Book shape rectangular", "present_opening_layer3"),
        ("Gift time! What order?", "👶 Kids open first, 👨‍👩‍👧‍👦 Family takes turns, 🎲 Random selection fun, 📋 List order organized", "gift_order_layer3")
    ]
    
    # Layer 2: Halloween Activities (after selecting Halloween)
    layer2_halloween_scenarios = [
        ("Halloween picked! What doing?", "🎃 Carving pumpkins creative, 👻 Trick or treating, 🍬 Candy collecting fun, 👕 Costume wearing exciting", "halloween_activity_layer2"),
        ("Spooky Halloween! Which activity?", "🏠 Haunted house visiting, 🎬 Horror movies watching, 🕷️ Scary decorating house, 🎪 Halloween party attending", "halloween_activity_layer2")
    ]
    
    all_scenarios = layer1_scenarios + layer2_christmas_scenarios + layer3_present_scenarios + layer2_halloween_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC Holiday Celebrations")
        examples.append(example)
    
    return examples

def create_weather_clothing_drilldowns():
    """Create weather and clothing drill-down conversations"""
    examples = []
    
    # Layer 1: Weather Check
    layer1_scenarios = [
        ("What's weather like?", "☀️ Sunny and warm, 🌧️ Rainy and wet, ❄️ Snowy and cold, 🌤️ Cloudy but nice", "weather_check_layer1"),
        ("How's weather today?", "🌨️ Blizzard very cold, 🌩️ Thunderstorm with lightning, 🌪️ Windy and breezy, 🌈 Rainbow after rain", "weather_check_layer1")
    ]
    
    # Layer 2: Clothing Choice (after weather assessment)
    layer2_sunny_scenarios = [
        ("Sunny weather! What wearing?", "👕 T-shirt light clothing, 🩳 Shorts for legs, 👟 Sneakers comfortable walking, 🕶️ Sunglasses protect eyes", "sunny_clothing_layer2"),
        ("Warm day! Clothing choice?", "👗 Summer dress flowing, 🩱 Swimsuit for pool, 🧢 Hat protects head, 🩴 Sandals for feet", "sunny_clothing_layer2")
    ]
    
    layer2_rainy_scenarios = [
        ("Rainy day! What wearing?", "🧥 Raincoat stays dry, ☂️ Umbrella blocks rain, 👢 Rain boots waterproof, 🧤 Gloves keep dry", "rainy_clothing_layer2"),
        ("Wet weather! Clothing needed?", "🪖 Rain hat protects, 🧣 Scarf around neck, 👖 Long pants covering, 🎒 Waterproof backpack dry", "rainy_clothing_layer2")
    ]
    
    # Layer 3: Accessory Details (after clothing choice)
    layer3_accessory_scenarios = [
        ("T-shirt chosen! What accessories?", "⌚ Watch tells time, 💍 Ring on finger, 🎒 Backpack carries things, 📱 Phone for communication", "clothing_accessories_layer3"),
        ("Raincoat selected! Extra protection?", "🧤 Waterproof gloves hands, 🪖 Hood covers head, 👢 Tall boots ankles, 🎒 Dry bag contents", "rain_accessories_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_sunny_scenarios + layer2_rainy_scenarios + layer3_accessory_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC Weather & Clothing")
        examples.append(example)
    
    return examples

def create_emotion_coping_drilldowns():
    """Create emotion and coping strategy drill-down conversations"""
    examples = []
    
    # Layer 1: Emotion Identification
    layer1_scenarios = [
        ("How are you feeling?", "😊 Happy and cheerful, 😢 Sad and down, 😠 Angry and mad, 😰 Worried and anxious", "emotion_identification_layer1"),
        ("What's your emotion?", "😴 Tired and sleepy, 😲 Surprised and shocked, 😕 Disappointed and let, 🤗 Excited and thrilled", "emotion_identification_layer1")
    ]
    
    # Layer 2: Coping Strategy (after emotion identified)
    layer2_sad_scenarios = [
        ("Feeling sad! What helps?", "🤗 Hugs from family, 😭 Crying releases feelings, 🎵 Music makes better, 📞 Talk to friend", "sad_coping_layer2"),
        ("Sad emotions! How cope?", "🛁 Warm bath relaxing, 📚 Read favorite book, 🍫 Comfort food nice, 🐕 Pet gives comfort", "sad_coping_layer2")
    ]
    
    layer2_angry_scenarios = [
        ("Feeling angry! What helps?", "🫁 Deep breathing calms, 🚶 Walk away situation, 🥊 Exercise releases energy, 🗣️ Talk about feelings", "angry_coping_layer2"),
        ("Mad emotions! How manage?", "🧘 Meditation centers mind, 🎯 Count to ten, 🛏️ Rest in room, ✍️ Write feelings down", "angry_coping_layer2")
    ]
    
    # Layer 3: Specific Actions (after coping strategy)
    layer3_breathing_scenarios = [
        ("Deep breathing chosen! How?", "👃 Breathe in slowly, 👄 Hold breath briefly, 💨 Exhale out completely, 🔄 Repeat pattern calmly", "breathing_technique_layer3"),
        ("Breathing helps! Which method?", "🫁 Belly breathing deep, 📦 Box breathing structured, 🌸 Flower breathing gentle, 🌊 Wave breathing rhythmic", "breathing_method_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_sad_scenarios + layer2_angry_scenarios + layer3_breathing_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC Emotion & Coping")
        examples.append(example)
    
    return examples

def create_home_activities_drilldowns():
    """Create home activities drill-down conversations"""
    examples = []
    
    # Layer 1: Room Selection
    layer1_scenarios = [
        ("Which room going?", "🛏️ Bedroom for sleeping, 🍳 Kitchen for cooking, 🛋️ Living room relaxing, 🚿 Bathroom for washing", "room_selection_layer1"),
        ("Where in house?", "📚 Study room working, 🌿 Garden room plants, 🚗 Garage for cars, 🏠 Basement storage area", "room_selection_layer1")
    ]
    
    # Layer 2: Kitchen Activities (after selecting kitchen)
    layer2_kitchen_scenarios = [
        ("Kitchen chosen! What doing?", "🍳 Cooking meal preparation, 🥤 Getting drink refreshing, 🍽️ Eating food together, 🧽 Cleaning dishes washing", "kitchen_activity_layer2"),
        ("In kitchen! Which task?", "🥘 Baking treats delicious, 🔥 Using stove carefully, ❄️ Getting food refrigerator, 🗑️ Taking out trash", "kitchen_activity_layer2")
    ]
    
    # Layer 3: Cooking Specifics (after selecting cooking)
    layer3_cooking_scenarios = [
        ("Cooking chosen! What making?", "🍝 Pasta with sauce, 🥗 Fresh salad healthy, 🍲 Soup warming up, 🥪 Sandwich quick meal", "cooking_specifics_layer3"),
        ("Meal preparation! Which dish?", "🍕 Pizza from scratch, 🧁 Cupcakes for dessert, 🥞 Pancakes for breakfast, 🍛 Rice with vegetables", "cooking_dish_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_kitchen_scenarios + layer3_cooking_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC Home Activities")
        examples.append(example)
    
    return examples

def create_school_subject_drilldowns():
    """Create school subject drill-down conversations"""
    examples = []
    
    # Layer 1: Subject Selection
    layer1_scenarios = [
        ("Which school subject?", "📚 Reading stories fun, ➕ Math numbers solving, 🔬 Science experiments exciting, 🎨 Art creativity expressing", "subject_selection_layer1"),
        ("What studying today?", "🌍 Geography world learning, 📖 History past events, 🎵 Music songs playing, 🏃 Physical education exercise", "subject_selection_layer1")
    ]
    
    # Layer 2: Math Topics (after selecting math)
    layer2_math_scenarios = [
        ("Math chosen! Which type?", "➕ Addition numbers together, ➖ Subtraction taking away, ✖️ Multiplication times tables, ➗ Division sharing equally", "math_topic_layer2"),
        ("Math class! What learning?", "📏 Measurement using rulers, 📐 Geometry shapes studying, 💰 Money counting coins, ⏰ Time reading clocks", "math_topic_layer2")
    ]
    
    # Layer 3: Addition Practice (after selecting addition)
    layer3_addition_scenarios = [
        ("Addition practice! Which problems?", "1️⃣ Single digit easy, 🔟 Double digit harder, 💯 Three digit challenging, 🎯 Word problems thinking", "addition_difficulty_layer3"),
        ("Adding numbers! What level?", "👶 Beginner level simple, 👦 Grade level appropriate, 🧠 Advanced level difficult, 🏆 Competition level expert", "addition_level_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_math_scenarios + layer3_addition_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC School Subjects")
        examples.append(example)
    
    return examples

def create_bedtime_routine_drilldowns():
    """Create bedtime routine drill-down conversations"""
    examples = []
    
    # Layer 1: Bedtime Preparation
    layer1_scenarios = [
        ("Time for bed! First?", "🦷 Brush teeth cleaning, 🚿 Take bath washing, 👕 Put on pajamas, 📚 Read bedtime story", "bedtime_prep_layer1"),
        ("Getting ready sleep! What?", "🧸 Get stuffed animal, 💤 Turn off lights, 🛏️ Make bed comfortable, 🚪 Close bedroom door", "bedtime_prep_layer1")
    ]
    
    # Layer 2: Toothbrushing Details (after selecting brush teeth)
    layer2_brushing_scenarios = [
        ("Brushing teeth! Which step?", "💧 Wet toothbrush water, 🧴 Add toothpaste small, 🦷 Brush teeth gently, 💦 Rinse mouth clean", "toothbrush_steps_layer2"),
        ("Teeth cleaning! How long?", "⏰ 30 seconds quick, 🕐 1 minute good, ⏰ 2 minutes thorough, 🎵 Song length timing", "brushing_duration_layer2")
    ]
    
    # Layer 3: Story Selection (after selecting bedtime story)
    layer3_story_scenarios = [
        ("Story time! Which book?", "🐻 Bear story adventure, 👸 Princess fairy tale, 🚂 Train journey exciting, 🌙 Moon goodnight peaceful", "story_selection_layer3"),
        ("Reading time! What story?", "🦄 Unicorn magical tale, 🐉 Dragon brave story, 🌟 Star wishes dreams, 🏰 Castle kingdom adventure", "bedtime_story_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_brushing_scenarios + layer3_story_scenarios
    
    for input_text, output_text, category in all_scenarios:
        example = create_drilldown_example(input_text, output_text, category, "AAC Bedtime Routine")
        examples.append(example)
    
    return examples

def create_drilldown_example(input_text, output_text, category, instruction):
    """Create a standardized drill-down example"""
    tiles = parse_output_to_tiles(output_text)
    spoken = generate_drilldown_sentence(tiles, category)
    
    example = {
        "instruction": instruction,
        "input": input_text,
        "aac_response": {
            "tiles": tiles,
            "spoken_sentence": spoken,
            "usage_data": {
                "category": category,
                "emotion_level": "medium",
                "complexity": len(tiles),
                "frequency_weight": 1.0,
                "conversation_layer": extract_layer_number(category),
                "drill_down_context": extract_context_type(category)
            }
        },
        "raw_output": output_text
    }
    return example

def parse_output_to_tiles(output_text):
    """Parse output into tile format"""
    tiles = []
    parts = output_text.split(', ')
    
    for i, part in enumerate(parts[:4]):
        part = part.strip()
        if not part:
            continue
            
        emoji = ""
        words = part
        
        for char in part:
            if ord(char) > 127:
                emoji = char
                words = part.replace(char, '').strip()
                break
        
        if not emoji:
            emoji = "💬"
        
        tiles.append({
            "emoji": emoji,
            "words": words,
            "tile_id": f"tile_{i+1}"
        })
    
    return tiles

def generate_drilldown_sentence(tiles, category):
    """Generate contextual drill-down sentence"""
    if not tiles:
        return "I need to choose from the options."
    
    layer = extract_layer_number(category)
    
    if layer == 1:
        return f"I choose {tiles[0]['words'].lower()}."
    elif layer == 2:
        return f"Next, I want {tiles[0]['words'].lower()}."
    elif layer == 3:
        return f"Then I select {tiles[0]['words'].lower()}."
    else:
        return f"Finally I pick {tiles[0]['words'].lower()}."

def extract_layer_number(category):
    """Extract layer number from category"""
    if "layer1" in category:
        return 1
    elif "layer2" in category:
        return 2
    elif "layer3" in category:
        return 3
    elif "layer4" in category:
        return 4
    else:
        return 1

def extract_context_type(category):
    """Extract context type from category"""
    if "holiday" in category:
        return "holiday_celebration"
    elif "weather" in category or "clothing" in category:
        return "weather_clothing"
    elif "emotion" in category or "coping" in category:
        return "emotion_management"
    elif "room" in category or "kitchen" in category:
        return "home_activities"
    elif "subject" in category or "math" in category:
        return "school_learning"
    elif "bedtime" in category or "sleep" in category:
        return "bedtime_routine"
    else:
        return "general"

if __name__ == "__main__":
    total = create_expanded_drilldowns()
    print(f"\n🎯 EXPANDED DRILL-DOWN COMPLETE: {total} examples!")
    print(f"🔄 Multi-layer conversation navigation system enhanced!")