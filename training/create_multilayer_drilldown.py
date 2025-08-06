#!/usr/bin/env python3
"""
Create Multi-Layer Drill-Down Conversation System
Build contextual follow-up responses with multiple layers
"""
import json

def create_multilayer_drilldown():
    """Create multi-layer drill-down conversation examples"""
    
    print("🎯 TinkyBink Multi-Layer Drill-Down Creator")
    print("=" * 60)
    print("🔄 Building contextual follow-up responses")
    print("🍕 Pizza → Toppings → Size → Crust examples")
    print("📱 Multi-level conversation navigation")
    print()
    
    all_drilldown_examples = []
    
    # FOOD ORDERING DRILL-DOWNS
    food_drilldowns = create_food_ordering_drilldowns()
    all_drilldown_examples.extend(food_drilldowns)
    print(f"✅ Food Ordering Drill-downs: {len(food_drilldowns)} examples")
    
    # ACTIVITY SELECTION DRILL-DOWNS
    activity_drilldowns = create_activity_selection_drilldowns()
    all_drilldown_examples.extend(activity_drilldowns)
    print(f"✅ Activity Selection Drill-downs: {len(activity_drilldowns)} examples")
    
    # MEDICAL APPOINTMENT DRILL-DOWNS
    medical_drilldowns = create_medical_appointment_drilldowns()
    all_drilldown_examples.extend(medical_drilldowns)
    print(f"✅ Medical Appointment Drill-downs: {len(medical_drilldowns)} examples")
    
    # SHOPPING DRILL-DOWNS
    shopping_drilldowns = create_shopping_drilldowns()
    all_drilldown_examples.extend(shopping_drilldowns)
    print(f"✅ Shopping Drill-downs: {len(shopping_drilldowns)} examples")
    
    # TRANSPORTATION DRILL-DOWNS
    transport_drilldowns = create_transportation_drilldowns()
    all_drilldown_examples.extend(transport_drilldowns)
    print(f"✅ Transportation Drill-downs: {len(transport_drilldowns)} examples")
    
    total_examples = len(all_drilldown_examples)
    
    print(f"\n🎯 TOTAL DRILL-DOWN EXAMPLES: {total_examples}")
    
    # Save drill-down examples
    output_file = "tinkybink_multilayer_drilldown.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in all_drilldown_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved: {output_file}")
    print(f"🔄 Multi-layer conversation system complete!")
    
    return total_examples

def create_food_ordering_drilldowns():
    """Create food ordering drill-down conversations"""
    examples = []
    
    # Layer 1: Food Type Selection
    layer1_scenarios = [
        ("What do you want to eat?", "🍕 Pizza option available, 🍗 Chicken also good, 🍔 Burger sounds tasty, 🌮 Tacos are delicious", "food_selection_layer1"),
        ("Choose your meal", "🍝 Pasta sounds great, 🥗 Salad is healthy, 🍲 Soup warms up, 🥙 Sandwich is quick", "food_selection_layer1")
    ]
    
    # Layer 2: Pizza Toppings (after selecting pizza)
    layer2_pizza_scenarios = [
        ("You picked pizza! What toppings?", "🍄 Mushrooms are tasty, 🥓 Bacon adds flavor, 🧄 Pepperoni is classic, 🧀 Extra cheese please", "pizza_toppings_layer2"),
        ("Pizza toppings selection", "🍅 Tomatoes are fresh, 🫒 Olives add taste, 🌶️ Peppers give spice, 🥩 Sausage is hearty", "pizza_toppings_layer2")
    ]
    
    # Layer 3: Pizza Size (after selecting toppings)
    layer3_pizza_scenarios = [
        ("Mushroom pizza! What size?", "🍕 Small for one, 🍕🍕 Medium for two, 🍕🍕🍕 Large for family, 🍕🍕🍕🍕 Extra large party", "pizza_size_layer3"),
        ("Pepperoni chosen! Size needed?", "👤 Personal size perfect, 👥 Medium feeds couple, 👨‍👩‍👧‍👦 Large for family, 🎉 Party size biggest", "pizza_size_layer3")
    ]
    
    # Layer 4: Pizza Crust (after selecting size)
    layer4_pizza_scenarios = [
        ("Large pizza! Crust type?", "🥖 Thin crust crispy, 🍞 Thick crust chewy, 🧄 Garlic crust flavored, 🧀 Stuffed crust cheesy", "pizza_crust_layer4"),
        ("Medium size chosen! Crust?", "✨ Original crust classic, 🌿 Herb crust seasoned, 🔥 Spicy crust hot, 🥜 Whole wheat healthy", "pizza_crust_layer4")
    ]
    
    all_scenarios = layer1_scenarios + layer2_pizza_scenarios + layer3_pizza_scenarios + layer4_pizza_scenarios
    
    for input_text, output_text, category in all_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_drilldown_sentence(tiles, category)
        
        example = {
            "instruction": "AAC Multi-Layer Food Ordering",
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
        examples.append(example)
    
    return examples

def create_activity_selection_drilldowns():
    """Create activity selection drill-down conversations"""
    examples = []
    
    # Layer 1: Activity Type
    layer1_scenarios = [
        ("What activity today?", "🎮 Games sound fun, 🎨 Art is creative, 🏃 Exercise gets moving, 📚 Reading is quiet", "activity_selection_layer1"),
        ("Choose something to do", "🎵 Music makes happy, 🧩 Puzzles challenge mind, 🎬 Movies entertain us, 🌳 Outside is fresh", "activity_selection_layer1")
    ]
    
    # Layer 2: Game Type (after selecting games)
    layer2_game_scenarios = [
        ("Games chosen! What type?", "🃏 Card games classic, 🎲 Board games strategic, 🎮 Video games exciting, ⚽ Sports games active", "game_type_layer2"),
        ("Fun games! Which kind?", "🧩 Puzzle games thinking, 🏃 Active games moving, 🎪 Party games social, 🤔 Brain games smart", "game_type_layer2")
    ]
    
    # Layer 3: Video Game Genre (after selecting video games)
    layer3_videogame_scenarios = [
        ("Video games! What genre?", "🏎️ Racing games fast, 🎯 Shooter games action, 🧙 Fantasy games magical, ⚽ Sports games realistic", "videogame_genre_layer3"),
        ("Gaming time! Which style?", "🏗️ Building games creative, 🕵️ Mystery games puzzling, 🎨 Creative games artistic, 🌍 Adventure games exploring", "videogame_genre_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_game_scenarios + layer3_videogame_scenarios
    
    for input_text, output_text, category in all_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_drilldown_sentence(tiles, category)
        
        example = {
            "instruction": "AAC Multi-Layer Activity Selection",
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
        examples.append(example)
    
    return examples

def create_medical_appointment_drilldowns():
    """Create medical appointment drill-down conversations"""
    examples = []
    
    # Layer 1: Doctor Type
    layer1_scenarios = [
        ("Need doctor appointment?", "👨‍⚕️ Family doctor general, 👁️ Eye doctor vision, 🦷 Dentist teeth cleaning, 💊 Specialist condition specific", "doctor_type_layer1"),
        ("Medical help needed?", "🏥 Emergency room urgent, 🩺 Primary care routine, 👂 Ear nose throat, 🦴 Bone doctor orthopedic", "doctor_type_layer1")
    ]
    
    # Layer 2: Appointment Time (after selecting doctor type)
    layer2_time_scenarios = [
        ("Family doctor chosen! When?", "🌅 Morning appointment early, 🌞 Afternoon appointment later, 🌆 Evening appointment after, 📅 Next week appointment", "appointment_time_layer2"),
        ("Dentist selected! What time?", "⏰ 9 AM morning, ⏰ 1 PM afternoon, ⏰ 4 PM evening, 📆 Tomorrow if available", "appointment_time_layer2")
    ]
    
    # Layer 3: Reason for Visit (after selecting time)
    layer3_reason_scenarios = [
        ("Morning appointment! Why visiting?", "🤒 Feeling sick lately, 💊 Medication refill needed, 🩺 Regular checkup time, 🤕 Injury needs attention", "visit_reason_layer3"),
        ("Afternoon chosen! What's wrong?", "😷 Cold symptoms appearing, 🦴 Joint pain bothering, 💤 Sleep problems continuing, 🤢 Stomach issues ongoing", "visit_reason_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_time_scenarios + layer3_reason_scenarios
    
    for input_text, output_text, category in all_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_drilldown_sentence(tiles, category)
        
        example = {
            "instruction": "AAC Multi-Layer Medical Appointment",
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
        examples.append(example)
    
    return examples

def create_shopping_drilldowns():
    """Create shopping drill-down conversations"""
    examples = []
    
    # Layer 1: Store Type
    layer1_scenarios = [
        ("Where to shop today?", "🛒 Grocery store food, 👕 Clothing store fashion, 💊 Pharmacy medicine needed, 🏪 Department store everything", "store_type_layer1"),
        ("Shopping trip! Which store?", "🍎 Supermarket fresh food, 👟 Shoe store footwear, 📱 Electronics store technology, 🏠 Home store furniture", "store_type_layer1")
    ]
    
    # Layer 2: Grocery Categories (after selecting grocery store)
    layer2_grocery_scenarios = [
        ("Grocery store! What section?", "🥬 Produce section fresh, 🥩 Meat section protein, 🥛 Dairy section milk, 🥫 Canned goods shelf", "grocery_section_layer2"),
        ("Supermarket chosen! Which aisle?", "🍞 Bakery section bread, 🧊 Frozen foods section, 🧴 Cleaning supplies aisle, 🍪 Snack foods aisle", "grocery_section_layer2")
    ]
    
    # Layer 3: Produce Items (after selecting produce)
    layer3_produce_scenarios = [
        ("Produce section! What fruit?", "🍎 Apples are crisp, 🍌 Bananas are sweet, 🍇 Grapes are juicy, 🍊 Oranges are citrus", "produce_items_layer3"),
        ("Fresh produce! Which vegetable?", "🥕 Carrots are crunchy, 🥬 Lettuce is leafy, 🍅 Tomatoes are red, 🥒 Cucumbers are cool", "produce_items_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_grocery_scenarios + layer3_produce_scenarios
    
    for input_text, output_text, category in all_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_drilldown_sentence(tiles, category)
        
        example = {
            "instruction": "AAC Multi-Layer Shopping",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "low",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0,
                    "conversation_layer": extract_layer_number(category),
                    "drill_down_context": extract_context_type(category)
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_transportation_drilldowns():
    """Create transportation drill-down conversations"""
    examples = []
    
    # Layer 1: Transportation Method
    layer1_scenarios = [
        ("How to get there?", "🚗 Car is private, 🚌 Bus is public, 🚶 Walking is exercise, 🚲 Bike is fun", "transport_method_layer1"),
        ("Transportation needed?", "✈️ Plane for distance, 🚂 Train is comfortable, 🚕 Taxi is convenient, 🛴 Scooter is quick", "transport_method_layer1")
    ]
    
    # Layer 2: Car Details (after selecting car)
    layer2_car_scenarios = [
        ("Car chosen! Who drives?", "🚗 I drive myself, 👨‍👩‍👧‍👦 Family member drives, 🤝 Friend gives ride, 🚕 Uber driver comes", "car_driver_layer2"),
        ("Driving selected! Which car?", "🚙 My car personal, 🚗 Mom's car borrow, 🚐 Dad's van bigger, 🏎️ Sports car fast", "car_type_layer2")
    ]
    
    # Layer 3: Route Planning (after selecting driver)
    layer3_route_scenarios = [
        ("Self driving! Which route?", "🛣️ Highway is fastest, 🏘️ Local roads scenic, 📍 GPS suggests route, 🚦 Avoid traffic jams", "route_planning_layer3"),
        ("Family driving! How long?", "⏱️ 15 minutes close, ⏰ 30 minutes medium, 🕐 1 hour far, 🕰️ 2 hours trip", "trip_duration_layer3")
    ]
    
    all_scenarios = layer1_scenarios + layer2_car_scenarios + layer3_route_scenarios
    
    for input_text, output_text, category in all_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_drilldown_sentence(tiles, category)
        
        example = {
            "instruction": "AAC Multi-Layer Transportation",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "low",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0,
                    "conversation_layer": extract_layer_number(category),
                    "drill_down_context": extract_context_type(category)
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

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
    context = extract_context_type(category)
    
    if layer == 1:
        return f"I want to choose {tiles[0]['words'].lower()}."
    elif layer == 2:
        return f"For the next step, I pick {tiles[0]['words'].lower()}."
    elif layer == 3:
        return f"Then I select {tiles[0]['words'].lower()}."
    else:
        return f"Finally I choose {tiles[0]['words'].lower()}."

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
    if "food" in category or "pizza" in category:
        return "food_ordering"
    elif "activity" in category or "game" in category:
        return "activity_selection"
    elif "doctor" in category or "medical" in category:
        return "medical_appointment"
    elif "shopping" in category or "store" in category:
        return "shopping"
    elif "transport" in category or "car" in category:
        return "transportation"
    else:
        return "general"

if __name__ == "__main__":
    total = create_multilayer_drilldown()
    print(f"\n🎯 MULTI-LAYER DRILL-DOWN COMPLETE: {total} examples!")
    print(f"🔄 Contextual conversation navigation system ready!")