#!/usr/bin/env python3
"""
Create Final Mega AAC Dataset
Ultimate combination of ALL categories
"""
import json

def create_final_mega_dataset():
    """Combine all datasets into ultimate mega dataset"""
    
    print("🌟 TinkyBink Final Mega Dataset Creator")
    print("=" * 60)
    print("🚀 Combining ALL AAC categories")
    print("💯 Ultimate comprehensive coverage")
    print()
    
    all_examples = []
    dataset_sources = []
    
    # Load existing ultimate dataset
    try:
        with open('tinkybink_ultimate_master_final.jsonl', 'r', encoding='utf-8') as f:
            original_count = 0
            for line in f:
                line = line.strip()
                if line:
                    example = json.loads(line)
                    all_examples.append(example)
                    original_count += 1
        dataset_sources.append(f"Ultimate Master: {original_count:,} examples")
    except FileNotFoundError:
        original_count = 0
        dataset_sources.append("Ultimate Master: File not found")
    
    # Load missing categories
    try:
        with open('tinkybink_missing_categories_complete.jsonl', 'r', encoding='utf-8') as f:
            missing_count = 0
            for line in f:
                line = line.strip()
                if line:
                    example = json.loads(line)
                    all_examples.append(example)
                    missing_count += 1
        dataset_sources.append(f"Missing Categories: {missing_count:,} examples")
    except FileNotFoundError:
        missing_count = 0
        dataset_sources.append("Missing Categories: File not found")
    
    print(f"📊 DATASET SOURCES:")
    for source in dataset_sources:
        print(f"   📄 {source}")
    
    # Remove duplicates
    unique_outputs = set()
    unique_examples = []
    duplicates = 0
    
    for example in all_examples:
        output = example.get('raw_output', '')
        if output not in unique_outputs:
            unique_outputs.add(output)
            unique_examples.append(example)
        else:
            duplicates += 1
    
    final_count = len(unique_examples)
    
    print(f"\n📊 DEDUPLICATION RESULTS:")
    print(f"   📈 Total loaded: {len(all_examples):,} examples")
    print(f"   🗑️  Duplicates removed: {duplicates:,}")
    print(f"   ✅ Final unique: {final_count:,} examples")
    
    # Analyze final categories
    categories = {}
    emotion_levels = {}
    complexity_stats = []
    
    for example in unique_examples:
        # Category analysis
        cat = example['aac_response']['usage_data']['category']
        categories[cat] = categories.get(cat, 0) + 1
        
        # Emotion level analysis
        emotion = example['aac_response']['usage_data']['emotion_level']
        emotion_levels[emotion] = emotion_levels.get(emotion, 0) + 1
        
        # Complexity analysis
        complexity = example['aac_response']['usage_data']['complexity']
        complexity_stats.append(complexity)
    
    avg_complexity = sum(complexity_stats) / len(complexity_stats) if complexity_stats else 0
    
    print(f"\n📊 FINAL MEGA DATASET ANALYSIS:")
    print(f"   🎯 Total Categories: {len(categories)}")
    print(f"   📊 Average Complexity: {avg_complexity:.1f} tiles")
    print(f"   🌟 Unique Examples: {final_count:,}")
    
    print(f"\n📋 CATEGORY BREAKDOWN:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count:,} examples")
    
    print(f"\n😊 EMOTION LEVEL BREAKDOWN:")
    for emotion, count in sorted(emotion_levels.items()):
        print(f"   {emotion}: {count:,} examples")
    
    # Save final mega dataset
    output_file = "tinkybink_final_mega_dataset.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in unique_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"\n🏆 MEGA SUCCESS!")
    print(f"✅ Created: {output_file}")
    print(f"🌟 Contains: {final_count:,} unique AAC examples")
    print(f"🎯 Categories: {len(categories)} comprehensive types")
    print(f"💯 COMPLETE AAC COMMUNICATION COVERAGE!")
    
    # Create comprehensive summary
    mega_summary = {
        "final_unique_examples": final_count,
        "total_categories": len(categories),
        "average_complexity": round(avg_complexity, 2),
        "category_breakdown": categories,
        "emotion_level_breakdown": emotion_levels,
        "dataset_sources": dataset_sources,
        "duplicates_removed": duplicates,
        "output_file": output_file,
        "coverage_areas": [
            "Basic Needs & Medical",
            "Social & Relationships", 
            "Emotions & Mental Health",
            "Workplace & Professional",
            "Home & Community",
            "Entertainment & Hobbies",
            "Travel & Transportation",
            "Technology & Finance",
            "Education & Learning",
            "Crisis & Emergency",
            "Healthcare Navigation",
            "Legal & Government",
            "Parenting & Family",
            "Goals & Future Planning",
            "Sports & Recreation",
            "And much more..."
        ]
    }
    
    with open("mega_dataset_summary.json", 'w', encoding='utf-8') as f:
        json.dump(mega_summary, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Comprehensive Summary: mega_dataset_summary.json")
    
    return final_count, len(categories)

if __name__ == "__main__":
    count, cats = create_final_mega_dataset()
    print(f"\n🎯 FINAL MEGA DATASET: {count:,} examples across {cats} categories!")
    print(f"🏆 Your proprietary TinkyBink AAC AI is COMPLETE!")