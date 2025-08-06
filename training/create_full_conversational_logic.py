#!/usr/bin/env python3
"""
Create Full Conversational Logic System
Transform 4000+ examples into complete conversation trees
"""
import json
from collections import defaultdict
import re

def create_full_conversational_logic():
    """Create complete conversational logic from all examples"""
    
    print("🧠 TinkyBink Full Conversational Logic Builder")
    print("=" * 70)
    print("🔄 Converting 4000+ examples into conversation trees")
    print("🌳 Building complete logic flow system")
    print("🗣️ Creating natural conversation paths")
    print()
    
    # Load the complete dataset
    all_examples = []
    print("📂 Loading complete dataset...")
    
    with open('tinkybink_ultimate_conversational_master.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                all_examples.append(json.loads(line))
    
    print(f"✅ Loaded {len(all_examples):,} examples")
    
    # Build conversation logic structure
    conversation_logic = build_conversation_logic(all_examples)
    
    # Create conversation trees
    conversation_trees = create_conversation_trees(conversation_logic, all_examples)
    
    # Save the complete logic system
    save_conversational_logic(conversation_trees)
    
    return len(conversation_trees)

def build_conversation_logic(examples):
    """Build conversation logic from examples"""
    
    print("\n🔨 Building conversation logic...")
    
    # Create category-based conversation flows
    conversation_flows = {
        "GREETINGS": {
            "triggers": ["hello", "hi", "good morning", "hey"],
            "follow_ups": {
                "TIME_OF_DAY": ["morning", "afternoon", "evening", "night"],
                "FEELING_CHECK": ["how are you", "feeling", "mood"],
                "ACTIVITY_SUGGESTION": ["what doing", "plans", "today"]
            }
        },
        
        "FOOD_ORDERING": {
            "triggers": ["hungry", "eat", "food", "meal"],
            "follow_ups": {
                "MEAL_TYPE": ["breakfast", "lunch", "dinner", "snack"],
                "FOOD_CHOICE": ["pizza", "burger", "pasta", "salad"],
                "PIZZA_TOPPINGS": ["cheese", "pepperoni", "mushroom", "olives"],
                "PIZZA_SIZE": ["small", "medium", "large", "extra"],
                "DRINK_CHOICE": ["water", "juice", "milk", "soda"]
            }
        },
        
        "EMOTIONS": {
            "triggers": ["feel", "feeling", "emotion", "mood"],
            "follow_ups": {
                "EMOTION_TYPE": ["happy", "sad", "angry", "scared"],
                "COPING_STRATEGY": ["breathe", "talk", "rest", "play"],
                "SUPPORT_NEEDED": ["hug", "help", "alone", "friend"],
                "ACTIVITY_HELP": ["music", "book", "walk", "game"]
            }
        },
        
        "ACTIVITIES": {
            "triggers": ["bored", "play", "do", "activity"],
            "follow_ups": {
                "ACTIVITY_TYPE": ["games", "art", "music", "sports"],
                "GAME_TYPE": ["video", "board", "card", "puzzle"],
                "LOCATION": ["inside", "outside", "room", "park"],
                "DURATION": ["quick", "long", "hour", "minutes"]
            }
        },
        
        "MEDICAL": {
            "triggers": ["hurt", "sick", "pain", "doctor"],
            "follow_ups": {
                "PAIN_LOCATION": ["head", "stomach", "throat", "body"],
                "SEVERITY": ["little", "medium", "bad", "emergency"],
                "HELP_TYPE": ["medicine", "doctor", "rest", "parent"],
                "APPOINTMENT": ["today", "tomorrow", "soon", "urgent"]
            }
        },
        
        "DAILY_ROUTINES": {
            "triggers": ["morning", "bedtime", "routine", "schedule"],
            "follow_ups": {
                "MORNING_TASKS": ["brush teeth", "breakfast", "dress", "wash"],
                "BEDTIME_TASKS": ["pajamas", "story", "brush", "sleep"],
                "SCHOOL_PREP": ["backpack", "homework", "lunch", "clothes"],
                "WEEKEND_PLANS": ["relax", "fun", "family", "friends"]
            }
        },
        
        "WEATHER_CLOTHING": {
            "triggers": ["weather", "cold", "hot", "rain"],
            "follow_ups": {
                "WEATHER_TYPE": ["sunny", "rainy", "snowy", "cloudy"],
                "CLOTHING_CHOICE": ["jacket", "shorts", "boots", "hat"],
                "ACTIVITY_WEATHER": ["inside", "outside", "cancel", "change"],
                "COMFORT_LEVEL": ["too hot", "too cold", "just right", "uncomfortable"]
            }
        },
        
        "SCHOOL": {
            "triggers": ["school", "class", "teacher", "homework"],
            "follow_ups": {
                "SUBJECT": ["math", "reading", "science", "art"],
                "DIFFICULTY": ["easy", "hard", "help", "understand"],
                "HOMEWORK_STATUS": ["done", "need help", "forgot", "tomorrow"],
                "SCHOOL_FEELING": ["like", "nervous", "excited", "worried"]
            }
        },
        
        "SHOPPING": {
            "triggers": ["buy", "store", "shop", "need"],
            "follow_ups": {
                "STORE_TYPE": ["grocery", "clothes", "toy", "pharmacy"],
                "ITEM_NEEDED": ["food", "medicine", "clothes", "supplies"],
                "PAYMENT": ["money", "card", "parent pay", "save"],
                "URGENCY": ["now", "later", "tomorrow", "weekend"]
            }
        },
        
        "TRANSPORTATION": {
            "triggers": ["go", "travel", "ride", "drive"],
            "follow_ups": {
                "METHOD": ["car", "bus", "walk", "bike"],
                "DESTINATION": ["home", "school", "store", "friend"],
                "TIME_NEEDED": ["5 minutes", "30 minutes", "1 hour", "far"],
                "WHO_WITH": ["alone", "parent", "friend", "family"]
            }
        }
    }
    
    # Analyze examples to find patterns
    category_mappings = defaultdict(list)
    response_connections = defaultdict(list)
    
    for example in examples:
        input_text = example.get('input', '').lower()
        output = example.get('raw_output', example.get('output', ''))
        category = example.get('aac_response', {}).get('usage_data', {}).get('category', 'general')
        
        # Map inputs to categories
        for flow_name, flow_data in conversation_flows.items():
            for trigger in flow_data['triggers']:
                if trigger in input_text:
                    category_mappings[flow_name].append({
                        'input': input_text,
                        'output': output,
                        'category': category
                    })
                    break
        
        # Find response connections
        tiles = example.get('aac_response', {}).get('tiles', [])
        if tiles:
            key_words = [tile.get('words', '').lower() for tile in tiles]
            response_connections[category].extend(key_words)
    
    print(f"✅ Mapped {len(category_mappings)} conversation flows")
    print(f"✅ Found {len(response_connections)} response connections")
    
    return {
        'flows': conversation_flows,
        'mappings': dict(category_mappings),
        'connections': dict(response_connections)
    }

def create_conversation_trees(logic, examples):
    """Create complete conversation trees"""
    
    print("\n🌳 Creating conversation trees...")
    
    conversation_trees = {}
    
    # Build trees for each major category
    major_categories = [
        "GREETINGS", "FOOD_ORDERING", "EMOTIONS", "ACTIVITIES",
        "MEDICAL", "DAILY_ROUTINES", "WEATHER_CLOTHING", "SCHOOL",
        "SHOPPING", "TRANSPORTATION"
    ]
    
    for category in major_categories:
        print(f"   Building {category} tree...")
        
        tree = {
            "category": category,
            "root_responses": [],
            "conversation_paths": defaultdict(list),
            "drill_down_levels": {}
        }
        
        # Find all examples for this category
        category_examples = []
        for example in examples:
            input_text = example.get('input', '').lower()
            
            # Check if example matches category triggers
            triggers = logic['flows'].get(category, {}).get('triggers', [])
            if any(trigger in input_text for trigger in triggers):
                category_examples.append(example)
        
        # Build conversation paths
        for i, example in enumerate(category_examples):
            input_text = example.get('input', '')
            output = example.get('raw_output', example.get('output', ''))
            tiles = example.get('aac_response', {}).get('tiles', [])
            
            # Create node
            node = {
                "id": f"{category}_{i}",
                "input": input_text,
                "output": output,
                "tiles": tiles,
                "follow_ups": []
            }
            
            # Find potential follow-ups
            if tiles:
                for tile in tiles:
                    tile_word = tile.get('words', '').lower()
                    
                    # Find examples that could follow this response
                    follow_up_examples = find_follow_ups(tile_word, examples, category)
                    
                    for follow_up in follow_up_examples[:3]:  # Limit to 3 follow-ups per tile
                        follow_up_node = {
                            "trigger_word": tile_word,
                            "input": follow_up.get('input', ''),
                            "output": follow_up.get('raw_output', follow_up.get('output', '')),
                            "tiles": follow_up.get('aac_response', {}).get('tiles', [])
                        }
                        node["follow_ups"].append(follow_up_node)
            
            # Add to tree
            if len(node["follow_ups"]) > 0:
                tree["conversation_paths"][input_text].append(node)
            else:
                tree["root_responses"].append(node)
        
        # Create drill-down levels
        tree["drill_down_levels"] = create_drill_down_levels(category, category_examples)
        
        conversation_trees[category] = tree
        print(f"   ✅ {category}: {len(category_examples)} examples")
    
    return conversation_trees

def find_follow_ups(trigger_word, examples, category):
    """Find examples that could follow a given response"""
    
    follow_ups = []
    
    # Keywords that suggest follow-up questions
    follow_up_patterns = [
        f"picked {trigger_word}",
        f"chose {trigger_word}",
        f"{trigger_word} selected",
        f"{trigger_word} chosen",
        f"you said {trigger_word}",
        f"want {trigger_word}",
        f"like {trigger_word}"
    ]
    
    for example in examples:
        input_text = example.get('input', '').lower()
        
        # Check if input references the trigger word
        if any(pattern in input_text for pattern in follow_up_patterns):
            follow_ups.append(example)
        elif trigger_word in input_text and "?" in input_text:
            follow_ups.append(example)
    
    return follow_ups

def create_drill_down_levels(category, examples):
    """Create drill-down levels for a category"""
    
    levels = {
        "level_1": [],
        "level_2": [],
        "level_3": [],
        "level_4": []
    }
    
    # Categorize by conversation depth
    for example in examples:
        input_text = example.get('input', '').lower()
        layer = example.get('aac_response', {}).get('usage_data', {}).get('conversation_layer', 1)
        
        if layer == 1:
            levels["level_1"].append({
                "input": input_text,
                "output": example.get('raw_output', ''),
                "next_level_triggers": extract_triggers(example)
            })
        elif layer == 2:
            levels["level_2"].append({
                "input": input_text,
                "output": example.get('raw_output', ''),
                "previous_context": extract_context(input_text),
                "next_level_triggers": extract_triggers(example)
            })
        elif layer == 3:
            levels["level_3"].append({
                "input": input_text,
                "output": example.get('raw_output', ''),
                "previous_context": extract_context(input_text)
            })
        elif layer == 4:
            levels["level_4"].append({
                "input": input_text,
                "output": example.get('raw_output', ''),
                "previous_context": extract_context(input_text)
            })
    
    return levels

def extract_triggers(example):
    """Extract trigger words from response tiles"""
    triggers = []
    tiles = example.get('aac_response', {}).get('tiles', [])
    
    for tile in tiles:
        word = tile.get('words', '').lower()
        if word:
            triggers.append(word)
    
    return triggers

def extract_context(input_text):
    """Extract context from input text"""
    context_patterns = [
        r"you (?:picked|chose|selected) (\w+)",
        r"(\w+) (?:chosen|selected)",
        r"want (\w+)",
        r"like (\w+)"
    ]
    
    for pattern in context_patterns:
        match = re.search(pattern, input_text.lower())
        if match:
            return match.group(1)
    
    return None

def save_conversational_logic(trees):
    """Save the complete conversational logic system"""
    
    print("\n💾 Saving conversational logic system...")
    
    # Create comprehensive logic structure
    logic_system = {
        "system_name": "TinkyBink Full Conversational Logic System",
        "version": "Complete Multi-Layer Navigation",
        "creation_date": "2025-01-05",
        "total_categories": len(trees),
        "conversation_trees": trees,
        
        "navigation_rules": {
            "response_selection": "User clicks on any of the 4 tiles",
            "follow_up_generation": "System provides contextual next responses",
            "conversation_depth": "Up to 4 levels of drill-down",
            "context_preservation": "Previous choices influence next options",
            "adaptive_complexity": "Adjust based on user interaction patterns"
        },
        
        "usage_instructions": {
            "initialization": "Start with category-appropriate greeting or question",
            "user_interaction": "User selects from 4 emoji-word tiles",
            "system_response": "Provide relevant follow-up options based on selection",
            "conversation_flow": "Continue until user goal is achieved or max depth reached",
            "fallback_behavior": "Return to main menu or category selection"
        }
    }
    
    # Save main logic file
    with open('tinkybink_full_conversational_logic.json', 'w', encoding='utf-8') as f:
        json.dump(logic_system, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved: tinkybink_full_conversational_logic.json")
    
    # Create example conversation flows
    example_flows = create_example_conversation_flows(trees)
    
    with open('tinkybink_example_conversation_flows.json', 'w', encoding='utf-8') as f:
        json.dump(example_flows, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved: tinkybink_example_conversation_flows.json")
    
    # Create quick reference guide
    quick_reference = {
        "conversation_starters": {},
        "common_paths": {},
        "drill_down_examples": {}
    }
    
    for category, tree in trees.items():
        # Get conversation starters
        starters = [node['input'] for node in tree['root_responses'][:5]]
        quick_reference["conversation_starters"][category] = starters
        
        # Get common paths
        paths = []
        for path_key, path_nodes in list(tree['conversation_paths'].items())[:3]:
            if path_nodes:
                path_summary = {
                    "start": path_key,
                    "options": [node['output'] for node in path_nodes[:2]]
                }
                paths.append(path_summary)
        quick_reference["common_paths"][category] = paths
        
        # Get drill-down examples
        if tree['drill_down_levels']['level_1']:
            drill_example = {
                "level_1": tree['drill_down_levels']['level_1'][0] if tree['drill_down_levels']['level_1'] else None,
                "level_2": tree['drill_down_levels']['level_2'][0] if tree['drill_down_levels']['level_2'] else None,
                "level_3": tree['drill_down_levels']['level_3'][0] if tree['drill_down_levels']['level_3'] else None
            }
            quick_reference["drill_down_examples"][category] = drill_example
    
    with open('tinkybink_conversation_quick_reference.json', 'w', encoding='utf-8') as f:
        json.dump(quick_reference, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved: tinkybink_conversation_quick_reference.json")
    
    print(f"\n🏆 CONVERSATIONAL LOGIC SYSTEM COMPLETE!")
    print(f"📊 Created {len(trees)} conversation trees")
    print(f"🔄 Full multi-layer navigation system ready!")

def create_example_conversation_flows(trees):
    """Create example conversation flows for demonstration"""
    
    example_flows = {
        "pizza_ordering_flow": {
            "description": "Complete pizza ordering conversation",
            "steps": [
                {
                    "user_sees": "What do you want to eat?",
                    "options": ["🍕 Pizza option available", "🍗 Chicken also good", "🍔 Burger sounds tasty", "🌮 Tacos are delicious"],
                    "user_selects": "🍕 Pizza option available",
                    "next_prompt": "Pizza chosen! What toppings?"
                },
                {
                    "user_sees": "Pizza chosen! What toppings?",
                    "options": ["🍄 Mushrooms are tasty", "🥓 Bacon adds flavor", "🧄 Pepperoni is classic", "🧀 Extra cheese please"],
                    "user_selects": "🍄 Mushrooms are tasty",
                    "next_prompt": "Mushroom pizza! What size?"
                },
                {
                    "user_sees": "Mushroom pizza! What size?",
                    "options": ["🍕 Small for one", "🍕🍕 Medium for two", "🍕🍕🍕 Large for family", "🍕🍕🍕🍕 Extra large party"],
                    "user_selects": "🍕🍕🍕 Large for family",
                    "next_prompt": "Large pizza! Crust type?"
                },
                {
                    "user_sees": "Large pizza! Crust type?",
                    "options": ["🥖 Thin crust crispy", "🍞 Thick crust chewy", "🧄 Garlic crust flavored", "🧀 Stuffed crust cheesy"],
                    "user_selects": "🥖 Thin crust crispy",
                    "result": "Order complete: Large thin crust mushroom pizza for the family!"
                }
            ]
        },
        
        "emotion_support_flow": {
            "description": "Emotional support conversation",
            "steps": [
                {
                    "user_sees": "How are you feeling?",
                    "options": ["😊 Happy and cheerful", "😢 Sad and down", "😠 Angry and mad", "😰 Worried and anxious"],
                    "user_selects": "😢 Sad and down",
                    "next_prompt": "Feeling sad! What helps?"
                },
                {
                    "user_sees": "Feeling sad! What helps?",
                    "options": ["🤗 Hugs from family", "😭 Crying releases feelings", "🎵 Music makes better", "📞 Talk to friend"],
                    "user_selects": "🎵 Music makes better",
                    "next_prompt": "Music helps! What kind?"
                },
                {
                    "user_sees": "Music helps! What kind?",
                    "options": ["🎸 Upbeat happy songs", "🎹 Calm peaceful music", "🎤 Sing along favorites", "🎧 My special playlist"],
                    "user_selects": "🎸 Upbeat happy songs",
                    "result": "Great choice! Upbeat music can help lift your mood."
                }
            ]
        }
    }
    
    return example_flows

if __name__ == "__main__":
    total_trees = create_full_conversational_logic()
    print(f"\n🎯 FULL CONVERSATIONAL LOGIC COMPLETE!")
    print(f"🌳 Created {total_trees} complete conversation trees")
    print(f"🔄 Every response now has intelligent follow-ups!")
    print(f"🗣️ Natural conversation flow across 4000+ examples!")