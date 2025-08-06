#!/usr/bin/env python3
"""
Final Merge: Combine original + new categories
Create the ultimate comprehensive AAC dataset
"""
import json

def merge_all_final():
    """Merge original dataset with new categories"""
    
    print("🌟 TinkyBink Final Merger")
    print("=" * 50)
    print("🔄 Combining original + new categories")
    print("💯 Creating ultimate AAC dataset")
    print()
    
    all_examples = []
    
    # Load original enhanced dataset
    with open('tinkybink_enhanced_aac_final.jsonl', 'r', encoding='utf-8') as f:
        original_count = 0
        for line in f:
            line = line.strip()
            if line:
                example = json.loads(line)
                all_examples.append(example)
                original_count += 1
    
    print(f"📄 Original dataset: {original_count:,} examples")
    
    # Load new categories
    with open('tinkybink_new_categories_expansion.jsonl', 'r', encoding='utf-8') as f:
        new_count = 0
        for line in f:
            line = line.strip()
            if line:
                example = json.loads(line)
                all_examples.append(example)
                new_count += 1
    
    print(f"📄 New categories: {new_count:,} examples")
    
    # Check for duplicates in combined dataset
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
    print(f"📊 Total combined: {len(all_examples):,} examples")
    print(f"🗑️  Duplicates removed: {duplicates}")
    print(f"✅ Final unique: {final_count:,} examples")
    
    # Analyze categories in final dataset
    categories = {}
    for example in unique_examples:
        cat = example['aac_response']['usage_data']['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\n📊 FINAL CATEGORY BREAKDOWN:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count:,} examples")
    
    # Save final master dataset
    output_file = "tinkybink_ultimate_master_final.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in unique_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"\n🏆 ULTIMATE SUCCESS!")
    print(f"✅ Created: {output_file}")
    print(f"🌟 Contains: {final_count:,} unique AAC examples")
    print(f"🎯 Categories: {len(categories)} different types")
    print(f"💯 Ready for AAC training!")
    
    # Create final summary
    summary = {
        "final_unique_examples": final_count,
        "total_categories": len(categories),
        "category_breakdown": categories,
        "original_dataset_size": original_count,
        "new_categories_added": new_count,
        "duplicates_removed": duplicates,
        "output_file": output_file
    }
    
    with open("ultimate_final_summary.json", 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Summary: ultimate_final_summary.json")
    
    return final_count

if __name__ == "__main__":
    count = merge_all_final()
    print(f"\n🎯 FINAL AAC DATASET: {count:,} examples ready!")