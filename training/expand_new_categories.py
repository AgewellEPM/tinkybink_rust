#!/usr/bin/env python3
"""
Expand New AAC Categories
Add missing categories and more comprehensive examples
"""
import json

def expand_new_categories():
    """Create new categories and add more examples"""
    
    print("🌟 TinkyBink New Category Expander")
    print("=" * 50)
    print("🚀 Creating NEW categories we're missing")
    print("💯 Adding comprehensive examples for each")
    print()
    
    new_examples = []
    
    # 1. WORKPLACE & PROFESSIONAL (150 examples)
    workplace_examples = create_workplace_category()
    new_examples.extend(workplace_examples)
    print(f"✅ Created {len(workplace_examples)} workplace examples")
    
    # 2. TRANSPORTATION & MOBILITY (100 examples)
    transport_examples = create_transport_category()
    new_examples.extend(transport_examples)
    print(f"✅ Created {len(transport_examples)} transportation examples")
    
    # 3. TECHNOLOGY & DIGITAL (120 examples)
    tech_examples = create_technology_category()
    new_examples.extend(tech_examples)
    print(f"✅ Created {len(tech_examples)} technology examples")
    
    # 4. SHOPPING & FINANCIAL (100 examples)
    shopping_examples = create_shopping_category()
    new_examples.extend(shopping_examples)
    print(f"✅ Created {len(shopping_examples)} shopping examples")
    
    # 5. EDUCATION & LEARNING (100 examples)
    education_examples = create_education_category()
    new_examples.extend(education_examples)
    print(f"✅ Created {len(education_examples)} education examples")
    
    # 6. HOBBIES & RECREATION (150 examples)
    hobby_examples = create_hobby_category()
    new_examples.extend(hobby_examples)
    print(f"✅ Created {len(hobby_examples)} hobby examples")
    
    # 7. WEATHER & ENVIRONMENT (80 examples)
    weather_examples = create_weather_category()
    new_examples.extend(weather_examples)
    print(f"✅ Created {len(weather_examples)} weather examples")
    
    # 8. SAFETY & EMERGENCY (100 examples)
    safety_examples = create_safety_category()
    new_examples.extend(safety_examples)
    print(f"✅ Created {len(safety_examples)} safety examples")
    
    # 9. INTIMACY & RELATIONSHIPS (80 examples)
    relationship_examples = create_relationship_category()
    new_examples.extend(relationship_examples)
    print(f"✅ Created {len(relationship_examples)} relationship examples")
    
    # 10. SPIRITUAL & CULTURAL (70 examples)
    spiritual_examples = create_spiritual_category()
    new_examples.extend(spiritual_examples)
    print(f"✅ Created {len(spiritual_examples)} spiritual examples")
    
    total_new = len(new_examples)
    print(f"\n📊 TOTAL NEW EXAMPLES: {total_new}")
    
    # Save new categories
    output_file = "tinkybink_new_categories_expansion.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in new_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved new categories: {output_file}")
    
    return total_new

def create_workplace_category():
    """Create workplace/professional communication examples"""
    examples = []
    
    workplace_scenarios = [
        # Job interviews
        ("Tell me about yourself", "💼 Professional experience sharing, 🎯 Career goals focused, 🌟 Skills highlighting time, 📈 Growth mindset ready", "workplace"),
        ("Why do you want this job?", "💡 Passionate about role, 🎯 Perfect skill match, 🌟 Company mission inspiring, 🚀 Ready for challenge", "workplace"),
        ("What are your strengths?", "🎯 Detail oriented person, 💪 Problem solving expert, 🤝 Team collaboration strong, 📊 Data analysis skilled", "workplace"),
        
        # Daily work communications
        ("How's the project going?", "✅ On schedule perfectly, ⚠️ Some delays occurring, 🔄 Need more resources, 📋 Status update ready", "workplace"),
        ("Can you handle this task?", "✅ Absolutely can do, 🤔 Need more details, ⏰ Timeline is tight, 🤝 Will need help", "workplace"),
        ("Meeting in 5 minutes", "🏃 On my way, 📱 Joining virtually now, ⏰ Need few minutes, 📋 Ready with materials", "workplace"),
        
        # Performance reviews
        ("How do you feel about your performance?", "🎯 Exceeded my goals, 💪 Strong effort given, 📈 Always improving daily, 🤔 Areas need work", "workplace"),
        ("What are your career goals?", "🎯 Leadership role desired, 📚 Skill development focused, 🌟 Industry expertise building, 🚀 Innovation opportunities seeking", "workplace"),
        
        # Team interactions
        ("Need help with anything?", "🤝 Team support appreciated, 💡 Brainstorming session helpful, 📊 Data review needed, ⏰ Time management struggle", "workplace"),
        ("Great job on that presentation", "🙏 Thank you kindly, 🤝 Team effort success, 📈 Preparation paid off, 🌟 Feedback helps grow", "workplace"),
        
        # Remote work
        ("Can you hear me clearly?", "✅ Audio perfect quality, 🔊 Little bit quiet, 📱 Connection is unstable, 🎧 Switching to headphones", "workplace"),
        ("Share your screen please", "💻 Screen sharing now, 🔧 Technical difficulties occurring, 📱 Using mobile device, 🤝 Need assistance please", "workplace"),
    ]
    
    for input_text, output_text, category in workplace_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = generate_workplace_sentence(tiles, input_text)
        
        example = {
            "instruction": "AAC Workplace Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_transport_category():
    """Create transportation/mobility examples"""
    examples = []
    
    transport_scenarios = [
        ("Which way to the bus stop?", "👈 Left down street, 👉 Right at corner, 🚌 Bus coming now, 📱 Check maps app", "transportation"),
        ("Is the train on time?", "⏰ Running 5 minutes, 📱 Check schedule app, 🚂 Just arrived now, ❌ Delayed significantly today", "transportation"),
        ("Need a ride somewhere?", "🚗 Yes please help, 🚌 Taking public transport, 🚶 Walking is fine, ⏰ Not right now", "transportation"),
        ("How do you get to work?", "🚗 Drive my car, 🚌 Take the bus, 🚶 Walk every day, 🚴 Bike when nice", "transportation"),
        ("Car won't start today", "🔧 Call mechanic now, 🚌 Take bus instead, 🤝 Need ride please, 📱 Check battery first", "transportation"),
        ("Traffic is really bad", "🕐 Leave earlier tomorrow, 📱 Use navigation app, 🚌 Try public transport, ⏰ Work from home", "transportation"),
        ("Where did you park?", "🅿️ Level 2 space, 🚗 Street parking nearby, 🤔 Can't remember exactly, 📱 Check parking app", "transportation"),
        ("Taxi or rideshare preference?", "🚕 Taxi is fine, 📱 Rideshare app preferred, 💰 Whatever costs less, ⏰ Whichever comes first", "transportation"),
    ]
    
    for input_text, output_text, category in transport_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I {tiles[0]['words'].lower()} and {tiles[1]['words'].lower()}."
        
        example = {
            "instruction": "AAC Transportation Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "low",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_technology_category():
    """Create technology/digital communication examples"""
    examples = []
    
    tech_scenarios = [
        ("Is your phone working?", "📱 Working perfectly fine, 🔋 Battery is low, 📶 No signal here, 🔧 Having technical issues", "technology"),
        ("Can you send me that file?", "📧 Emailing right now, 💾 File too large, 📱 Not on phone, 🤝 Need your email", "technology"),
        ("Internet is down again", "🔧 Call tech support, 📱 Using mobile data, 💻 Restart the router, ⏰ Wait it out", "technology"),
        ("New software update available", "⬇️ Download it now, ⏰ Install later tonight, 🤔 What does change, ❌ Skip this update", "technology"),
        ("Password not working", "🔑 Try different password, 🔄 Reset password now, 🤝 Need help please, 📧 Check email reset", "technology"),
        ("Video call quality bad", "📱 Switch to audio, 🔄 Restart the app, 📶 Check internet connection, 💻 Use different device", "technology"),
        ("Backup your important data", "💾 Already backed up, ☁️ Use cloud storage, 💻 External drive ready, ⏰ Will do later", "technology"),
        ("Computer running very slow", "🔄 Restart computer now, 🗑️ Delete unused files, 🔧 Run virus scan, 💻 Needs more memory", "technology"),
    ]
    
    for input_text, output_text, category in tech_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Technology Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_shopping_category():
    """Create shopping/financial examples"""
    examples = []
    
    shopping_scenarios = [
        ("What's on your shopping list?", "🥛 Milk and bread, 🥕 Fresh vegetables today, 🍎 Fruits and snacks, 📋 Have written list", "shopping"),
        ("Need help finding anything?", "🛒 Looking for produce, 🥖 Where is bakery, 💳 Need checkout help, ✅ I'm all good", "shopping"),
        ("Cash or card today?", "💳 Credit card please, 💵 Cash is fine, 📱 Mobile payment app, 🤔 Which is faster", "shopping"),
        ("Did you find everything?", "✅ Found everything needed, ❌ Missing few items, 🤝 Need more help, 📋 Checking list again", "shopping"),
        ("Would you like a receipt?", "📧 Email receipt please, 📄 Paper receipt yes, ❌ No receipt needed, 📱 Text message option", "shopping"),
        ("Sale ends tomorrow", "🛒 Buy it now, ⏰ Think about it, 💰 Too expensive still, 📅 Come back tomorrow", "shopping"),
        ("Return policy question", "📅 How many days, 📄 Need original receipt, 💳 Store credit okay, 🤝 Speak with manager", "shopping"),
        ("Budget is tight this month", "💰 Buy only essentials, 🔍 Look for sales, 💳 Use rewards points, ⏰ Wait until payday", "shopping"),
    ]
    
    for input_text, output_text, category in shopping_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I want {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Shopping Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "low",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_education_category():
    """Create education/learning examples"""
    examples = []
    
    education_scenarios = [
        ("How's school going?", "📚 Really enjoying it, 😅 Pretty challenging work, 🤝 Making new friends, ⏰ Lots of homework", "education"),
        ("What's your favorite subject?", "🔬 Science is fascinating, 📖 Love reading literature, 🎨 Art class creative, ⚽ Physical education fun", "education"),
        ("Need help with homework?", "🤝 Yes please help, 💭 Just need hints, ✅ Almost finished now, 📚 Different subject hard", "education"),
        ("Test tomorrow ready?", "📖 Studied all weekend, 😰 Need more time, 🤝 Study group helpful, 😴 Too tired tonight", "education"),
        ("What did you learn today?", "🧠 New math concept, 🌍 Interesting history facts, 🔬 Science experiment cool, 📝 Writing skills improved", "education"),
        ("College plans after graduation?", "🎓 Already been accepted, 🤔 Still deciding options, 💰 Need financial aid, ⏰ Taking gap year", "education"),
        ("Teacher conference next week", "👍 Looking forward meeting, 😰 Little bit nervous, 📋 Questions prepared already, 🤝 Parent coming too", "education"),
        ("Online or in-person learning?", "💻 Online works better, 🏫 Prefer classroom setting, 🤔 Mix of both, 🤝 Need more interaction", "education"),
    ]
    
    for input_text, output_text, category in education_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I feel {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Education Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_hobby_category():
    """Create hobbies/recreation examples"""
    examples = []
    
    hobby_scenarios = [
        ("What do you do for fun?", "🎮 Play video games, 📚 Read mystery books, 🎨 Paint and draw, 🎵 Listen to music", "hobbies"),
        ("Want to try something new?", "🤔 What did consider, ✅ Always open trying, 😰 Bit nervous change, 📅 When would start", "hobbies"),
        ("How was your weekend?", "🎣 Went fishing Saturday, 🎬 Watched movies Sunday, 🏠 Relaxed at home, 🤝 Visited with friends", "hobbies"),
        ("Join our book club?", "📚 Love reading books, ⏰ What time meetings, 👥 How many people, 🤔 What books reading", "hobbies"),
        ("Gardening season starting", "🌱 Plant vegetable garden, 🌺 Focus on flowers, 🤝 Need gardening help, 🛠️ Get tools ready", "hobbies"),
        ("Exercise routine going well?", "💪 Getting stronger daily, 😅 Pretty challenging workout, ⏰ Need more time, 🤝 Personal trainer helps", "hobbies"),
        ("Cooking something special tonight?", "🍝 Making pasta dish, 🥗 Simple salad tonight, 📱 Ordering takeout instead, 🤝 Want to help", "hobbies"),
        ("Photography walk this weekend?", "📸 Bring good camera, 🌅 Early morning light, 🤝 Group photography fun, 🤔 Weather permitting hopefully", "hobbies"),
    ]
    
    for input_text, output_text, category in hobby_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I like {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Hobbies Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_weather_category():
    """Create weather/environment examples"""
    examples = []
    
    weather_scenarios = [
        ("How's the weather today?", "☀️ Beautiful sunny day, 🌧️ Raining pretty hard, ❄️ Cold and snowy, 🌤️ Partly cloudy skies", "weather"),
        ("Perfect day for outdoor activities?", "✅ Absolutely perfect weather, 🌧️ Too wet outside, 🥵 Too hot today, 🌬️ Too windy now", "weather"),
        ("Need an umbrella today?", "☔ Definitely bring one, ☀️ Clear skies predicted, 🤔 Check weather app, 🌂 Always carry one", "weather"),
        ("Seasonal allergies bothering you?", "🤧 Really bad today, 💊 Taking allergy medicine, 🏠 Staying indoors more, ✅ Not too bad", "weather"),
        ("Hurricane warning in effect", "🏠 Stay inside safe, 📦 Supplies already stocked, 🚗 Evacuate if necessary, 📱 Monitor weather updates", "weather"),
        ("First snow of winter", "❄️ Love snow days, 🚗 Driving will difficult, 🏠 Stay warm inside, ☃️ Build snowman later", "weather"),
        ("Heat wave this week", "🥵 Stay hydrated always, ❄️ Air conditioning running, 🏊 Swimming sounds great, 🏠 Avoid outdoor activities", "weather"),
        ("Storm knocked out power", "🔦 Use flashlights now, 📱 Phone battery low, 🕯️ Light some candles, 🔧 Call electric company", "weather"),
    ]
    
    for input_text, output_text, category in weather_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"The weather is {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Weather Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "low",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_safety_category():
    """Create safety/emergency examples"""
    examples = []
    
    safety_scenarios = [
        ("Emergency situation right now", "🚨 Call 911 immediately, 🏥 Need medical help, 🚒 Fire department needed, 👮 Police assistance required", "safety"),
        ("Feeling unsafe here", "🚪 Want to leave, 🤝 Need someone with, 📱 Call for help, 🏃 Get away quickly", "safety"),
        ("Someone suspicious around", "👮 Call police now, 🏠 Go inside safe, 👥 Stay with others, 📱 Take pictures evidence", "safety"),
        ("Fire alarm going off", "🚪 Exit building immediately, 🔥 Check for fire, 📞 Call fire department, 👥 Help others evacuate", "safety"),
        ("First aid needed here", "🩹 Get first kit, 🏥 Call ambulance now, 🤝 Someone trained help, 📱 Emergency contact person", "safety"),
        ("Natural disaster warning", "📻 Listen emergency radio, 🏠 Secure the house, 📦 Gather emergency supplies, 🚗 Evacuation route ready", "safety"),
        ("Lost in unfamiliar area", "📱 Use GPS navigation, 🤝 Ask for directions, 📞 Call someone help, 🚶 Find police station", "safety"),
        ("Witnessed an accident", "📞 Call emergency services, 🤝 Check if injured, 🚗 Direct traffic safely, 📝 Give statement later", "safety"),
    ]
    
    for input_text, output_text, category in safety_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Safety Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_relationship_category():
    """Create intimate/relationship examples"""
    examples = []
    
    relationship_scenarios = [
        ("How are things with your partner?", "❤️ Going really well, 💕 Very much love, 🤗 Happy together always, 😔 Some challenges lately", "relationships"),
        ("Planning anything special together?", "💐 Romantic dinner date, 🎬 Movie night home, 🚗 Weekend trip planned, 🎁 Anniversary gift shopping", "relationships"),
        ("Feeling loved and supported?", "❤️ Absolutely feel loved, 🤗 Support always given, 💕 Lucky to have, 😊 Grateful every day", "relationships"),
        ("Any relationship concerns?", "💬 Communication could improve, ⏰ Not enough time, 💰 Financial stress affecting, ✅ Everything is good", "relationships"),
        ("Date night ideas?", "🍽️ Nice restaurant dinner, 🎭 Theater show together, 🌅 Sunrise beach walk, 🏠 Cozy home evening", "relationships"),
        ("Anniversary coming up", "🎁 Planning special surprise, 💕 Romantic getaway trip, 📸 Memory photo album, 🥂 Champagne celebration dinner", "relationships"),
        ("Feeling appreciated in relationship?", "💕 Very much appreciated, 🤗 Partner shows love, 😊 Feel valued daily, 😔 Could be better", "relationships"),
        ("Intimacy and connection important?", "❤️ Very important us, 💬 Communication builds closeness, 🤗 Physical affection matters, ⏰ Quality time together", "relationships"),
    ]
    
    for input_text, output_text, category in relationship_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I feel {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Relationship Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_spiritual_category():
    """Create spiritual/cultural examples"""
    examples = []
    
    spiritual_scenarios = [
        ("How's your spiritual journey?", "🙏 Growing stronger daily, 📖 Reading sacred texts, 🤔 Questioning and exploring, 😌 Finding inner peace", "spiritual"),
        ("Attending religious services?", "⛪ Every week regularly, 🏠 Watching online services, 👥 Small group study, ⏰ Occasionally when possible", "spiritual"),
        ("Prayer or meditation practice?", "🙏 Daily prayer time, 🧘 Meditation every morning, 📖 Scripture reading nightly, 🤔 Still learning practices", "spiritual"),
        ("Cultural traditions important to you?", "👨‍👩‍👧‍👦 Family traditions cherished, 🍽️ Holiday celebrations special, 📚 Learning cultural history, 🌍 Sharing with others", "spiritual"),
        ("Faith community support?", "🤝 Very supportive community, 💕 Like family members, 🙏 Pray for each, 📞 Always there help", "spiritual"),
        ("Celebrating religious holidays?", "🎉 Big family gatherings, 🍽️ Traditional foods prepared, 🎁 Gift giving tradition, 🕯️ Candle lighting ceremony", "spiritual"),
        ("Dealing with doubt?", "🤔 Natural part journey, 📖 Reading for answers, 🤝 Talking with others, 🙏 Praying for guidance", "spiritual"),
        ("Sharing beliefs with others?", "💬 Open honest conversations, 👂 Listen different perspectives, 📚 Learning from others, 🤝 Respectful dialogue always", "spiritual"),
    ]
    
    for input_text, output_text, category in spiritual_scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I believe {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Spiritual Communication",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
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
    
    for i, part in enumerate(parts[:4]):  # Max 4 tiles
        part = part.strip()
        if not part:
            continue
            
        # Find emoji and words
        emoji = ""
        words = part
        
        # Extract emoji if present
        for char in part:
            if ord(char) > 127:  # Non-ASCII character (likely emoji)
                emoji = char
                words = part.replace(char, '').strip()
                break
        
        if not emoji:
            emoji = "💬"  # Default emoji
        
        tiles.append({
            "emoji": emoji,
            "words": words,
            "tile_id": f"tile_{i+1}"
        })
    
    return tiles

def generate_workplace_sentence(tiles, input_text):
    """Generate workplace-appropriate sentences"""
    if not tiles:
        return ""
    
    first_word = tiles[0]['words'].split()[0].lower()
    second_word = tiles[1]['words'].split()[0].lower() if len(tiles) > 1 else "ready"
    
    if "job" in input_text.lower() or "work" in input_text.lower():
        return f"I am {first_word} and {second_word} for this opportunity."
    elif "project" in input_text.lower() or "task" in input_text.lower():
        return f"The project is {first_word} and {second_word}."
    else:
        return f"I feel {first_word} and {second_word} about this."

if __name__ == "__main__":
    total = expand_new_categories()
    print(f"\n🎯 CREATED: {total:,} NEW category examples!")