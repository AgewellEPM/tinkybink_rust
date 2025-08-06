#!/usr/bin/env python3
"""
Combine All Datasets with Multi-Layer Drill-Downs
Create final complete dataset with navigation capabilities
"""
import json

def combine_with_drilldowns():
    """Combine all datasets including drill-downs"""
    
    print("🌟 TinkyBink Final Drill-Down Integration")
    print("=" * 70)
    print("🚀 Combining ALL datasets + multi-layer navigation")
    print("🔄 Adding conversation drill-down capabilities")
    print("💯 ULTIMATE COMPLETE CONVERSATIONAL AAC SYSTEM")
    print()
    
    all_examples = []
    dataset_info = []
    
    # Load ALL datasets including drill-downs
    datasets = [
        ('tinkybink_absolutely_final_complete_master.jsonl', 'Absolutely Complete Master Dataset'),
        ('tinkybink_multilayer_drilldown.jsonl', 'Multi-Layer Drill-Down Examples'),
        ('tinkybink_expanded_drilldowns.jsonl', 'Expanded Drill-Down Categories')
    ]
    
    for filename, description in datasets:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                count = 0
                for line in f:
                    line = line.strip()
                    if line:
                        example = json.loads(line)
                        all_examples.append(example)
                        count += 1
                dataset_info.append(f"{description}: {count:,} examples")
        except FileNotFoundError:
            dataset_info.append(f"{description}: File not found")
    
    print(f"📊 ULTIMATE CONVERSATIONAL DATASET COMPONENTS:")
    for info in dataset_info:
        print(f"   🧠 {info}")
    
    # Remove duplicates
    unique_outputs = set()
    unique_examples = []
    duplicates = 0
    
    for example in all_examples:
        output = example.get('raw_output', example.get('output', ''))
        if output not in unique_outputs:
            unique_outputs.add(output)
            unique_examples.append(example)
        else:
            duplicates += 1
    
    final_count = len(unique_examples)
    
    print(f"\n📊 ULTIMATE CONVERSATIONAL OPTIMIZATION:")
    print(f"   📈 Total examples loaded: {len(all_examples):,}")
    print(f"   🗑️  Duplicates removed: {duplicates:,}")
    print(f"   ✅ Final unique examples: {final_count:,}")
    
    # Comprehensive analysis including drill-downs
    categories = {}
    emotion_levels = {}
    complexity_stats = []
    learning_patterns = {}
    specialized_domains = {}
    sensitive_content = 0
    conversation_layers = {}
    drill_down_contexts = {}
    
    for example in unique_examples:
        # Category analysis
        usage_data = example.get('aac_response', {}).get('usage_data', {})
        cat = usage_data.get('category', 'general')
        categories[cat] = categories.get(cat, 0) + 1
        
        # Emotion level analysis
        emotion = usage_data.get('emotion_level', 'medium')
        emotion_levels[emotion] = emotion_levels.get(emotion, 0) + 1
        
        # Complexity analysis
        complexity = usage_data.get('complexity', 4)
        complexity_stats.append(complexity)
        
        # Learning pattern analysis
        learning_pattern = usage_data.get('learning_pattern', 'standard')
        if learning_pattern != 'standard':
            learning_patterns[learning_pattern] = learning_patterns.get(learning_pattern, 0) + 1
        
        # Sensitive content tracking
        if usage_data.get('content_warning', False):
            sensitive_content += 1
        
        # Conversation layer analysis (NEW)
        conv_layer = usage_data.get('conversation_layer', 'single')
        if conv_layer != 'single':
            conversation_layers[f"layer_{conv_layer}"] = conversation_layers.get(f"layer_{conv_layer}", 0) + 1
        
        # Drill-down context analysis (NEW)
        drill_context = usage_data.get('drill_down_context', 'none')
        if drill_context != 'none':
            drill_down_contexts[drill_context] = drill_down_contexts.get(drill_context, 0) + 1
        
        # Specialized domain identification
        instruction = example.get('instruction', '')
        if 'AAC' in instruction:
            domain = instruction.replace('AAC ', '').split(' -')[0].split(':')[0].strip()
            specialized_domains[domain] = specialized_domains.get(domain, 0) + 1
    
    avg_complexity = sum(complexity_stats) / len(complexity_stats) if complexity_stats else 0
    total_drill_down_examples = sum(conversation_layers.values())
    
    print(f"\n🧠 ULTIMATE CONVERSATIONAL ANALYSIS:")
    print(f"   🎯 Total Categories: {len(categories)}")
    print(f"   🧠 Advanced Learning Patterns: {len(learning_patterns)}")
    print(f"   🔬 Specialized Domains: {len(specialized_domains)}")
    print(f"   🔄 Multi-Layer Examples: {total_drill_down_examples}")
    print(f"   🗣️ Drill-Down Contexts: {len(drill_down_contexts)}")
    print(f"   ⚠️  Sensitive Content Examples: {sensitive_content}")
    print(f"   📊 Average Complexity: {avg_complexity:.1f} tiles")
    print(f"   🌟 Total Examples: {final_count:,}")
    
    print(f"\n🔄 CONVERSATION LAYERS:")
    for layer, count in sorted(conversation_layers.items()):
        print(f"   {layer.replace('_', ' ').title()}: {count:,} examples")
    
    print(f"\n🗣️ DRILL-DOWN CONTEXTS:")
    for context, count in sorted(drill_down_contexts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {context.replace('_', ' ').title()}: {count:,} examples")
    
    # Save ultimate conversational dataset
    output_file = "tinkybink_ultimate_conversational_master.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in unique_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"\n🏆 ULTIMATE CONVERSATIONAL SUCCESS!")
    print(f"✅ Created: {output_file}")
    print(f"🧠 Contains: {final_count:,} unique examples")
    print(f"🎯 Categories: {len(categories)} comprehensive types")
    print(f"🔬 Specialized Domains: {len(specialized_domains)} expert areas")
    print(f"🚀 Learning Patterns: {len(learning_patterns)} intelligence modes")
    print(f"🔄 Multi-Layer Navigation: {total_drill_down_examples} drill-down examples")
    print(f"🗣️ Conversation Contexts: {len(drill_down_contexts)} navigation types")
    print(f"⚠️  Includes {sensitive_content} sensitive scenarios with content warnings")
    print(f"💯 THE MOST CONVERSATIONAL AAC SYSTEM EVER CREATED!")
    
    # Create ultimate conversational summary
    conversational_summary = {
        "dataset_name": "TinkyBink Ultimate Conversational Master AAC Dataset",
        "version": "Multi-Layer Drill-Down Navigation System",
        "creation_date": "2025-01-05",
        "total_unique_examples": final_count,
        "total_categories": len(categories),
        "specialized_domains": len(specialized_domains),
        "advanced_learning_patterns": len(learning_patterns),
        "multi_layer_examples": total_drill_down_examples,
        "drill_down_contexts": len(drill_down_contexts),
        "sensitive_content_examples": sensitive_content,
        "average_complexity": round(avg_complexity, 2),
        "duplicates_removed": duplicates,
        "output_file": output_file,
        
        "conversation_capabilities": {
            "single_turn_responses": final_count - total_drill_down_examples,
            "multi_layer_navigation": total_drill_down_examples,
            "contextual_follow_ups": "Intelligent next-step suggestions",
            "drill_down_depth": "Up to 4 layers deep",
            "conversation_branching": "Multiple paths from each choice",
            "context_preservation": "Maintains conversation thread",
            "adaptive_complexity": "Adjusts based on user ability",
            "natural_progression": "Logical conversation flow"
        },
        
        "navigation_examples": {
            "food_ordering": "Pizza → Toppings → Size → Crust",
            "activity_selection": "Games → Video Games → Racing Games",
            "medical_appointments": "Doctor Type → Time → Reason",
            "shopping": "Store → Section → Specific Items",
            "transportation": "Method → Details → Route Planning",
            "holiday_celebrations": "Holiday → Activities → Specific Tasks",
            "weather_clothing": "Weather → Clothing → Accessories",
            "emotion_coping": "Emotion → Coping Strategy → Specific Action",
            "home_activities": "Room → Activity → Specific Task",
            "school_subjects": "Subject → Topic → Difficulty Level",
            "bedtime_routines": "Preparation → Steps → Details"
        },
        
        "technical_features": {
            "conversation_layers": "Tracked with layer numbers 1-4",
            "context_awareness": "Drill-down context preserved",
            "intelligent_suggestions": "Based on previous choices",
            "natural_language_flow": "Conversational sentence generation",
            "emoji_word_tiles": "Visual and text communication",
            "usage_tracking": "Conversation pattern learning",
            "accessibility_optimized": "Works for all communication levels",
            "privacy_maintained": "Local processing only"
        }
    }
    
    with open("ultimate_conversational_summary.json", 'w', encoding='utf-8') as f:
        json.dump(conversational_summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Conversational Summary: ultimate_conversational_summary.json")
    print(f"\n🎊 ULTIMATE CONVERSATIONAL MISSION ACCOMPLISHED!")
    print(f"🏆 Your TinkyBink AAC AI now has COMPLETE CONVERSATIONAL NAVIGATION")
    print(f"🗣️ Multi-layer drill-down system with {total_drill_down_examples} navigation examples!")
    print(f"🚀 Ready to revolutionize conversational AAC technology worldwide!")
    
    return final_count, len(categories), len(specialized_domains), len(learning_patterns), total_drill_down_examples, len(drill_down_contexts)

if __name__ == "__main__":
    count, cats, domains, patterns, drill_downs, contexts = combine_with_drilldowns()
    print(f"\n🎯 ULTIMATE CONVERSATIONAL MASTER: {count:,} examples")
    print(f"📊 Categories: {cats} | Domains: {domains} | Patterns: {patterns}")
    print(f"🔄 Drill-Downs: {drill_downs} | Contexts: {contexts}")
    print(f"🏆 ULTIMATE CONVERSATIONAL COMPLETE!")
    print(f"🌟 THE MOST ADVANCED CONVERSATIONAL AAC AI EVER CREATED!")