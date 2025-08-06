#!/usr/bin/env python3
"""
Combine All Training Files and Remove Duplicates
Merges all JSONL files and creates final unique dataset
"""
import json
import glob
from collections import defaultdict

def combine_all_unique():
    """Combine all training files and remove duplicates"""
    
    print("🌟 TinkyBink Ultimate Combiner")
    print("=" * 50)
    print("🔄 Combining ALL training files")
    print("💯 Removing ALL duplicates")
    print()
    
    # Get all JSONL files
    jsonl_files = glob.glob("*.jsonl")
    print(f"📁 Found {len(jsonl_files)} training files")
    
    all_examples = []
    file_counts = {}
    
    # Load all files
    for file_path in jsonl_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_examples = []
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            example = json.loads(line)
                            file_examples.append(example)
                            all_examples.append(example)
                        except json.JSONDecodeError:
                            continue
                
                file_counts[file_path] = len(file_examples)
                print(f"   📄 {file_path}: {len(file_examples)} examples")
                
        except Exception as e:
            print(f"   ❌ Error reading {file_path}: {e}")
    
    print(f"\n📊 Total examples loaded: {len(all_examples)}")
    
    # Remove duplicates based on output (the AAC response)
    unique_outputs = set()
    unique_examples = []
    output_counts = defaultdict(int)
    
    for example in all_examples:
        output = example.get('output', '')
        if not output:
            continue
            
        output_counts[output] += 1
        
        if output not in unique_outputs:
            unique_outputs.add(output)
            unique_examples.append(example)
    
    # Stats
    total_examples = len(all_examples)
    unique_count = len(unique_examples)
    duplicates_removed = total_examples - unique_count
    
    print(f"\n🎯 DEDUPLICATION RESULTS:")
    print(f"   📈 Total examples: {total_examples:,}")
    print(f"   ✅ Unique examples: {unique_count:,}")
    print(f"   🗑️  Duplicates removed: {duplicates_removed:,}")
    print(f"   📊 Uniqueness: {(unique_count/total_examples)*100:.1f}%")
    
    # Show most duplicated responses
    print(f"\n🔍 Most duplicated responses:")
    sorted_counts = sorted(output_counts.items(), key=lambda x: x[1], reverse=True)
    for output, count in sorted_counts[:10]:
        if count > 1:
            print(f"   {count}x: {output[:80]}...")
    
    # Save final unique dataset
    output_file = "tinkybink_master_unique_final.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in unique_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"\n🏆 SUCCESS!")
    print(f"✅ Created master unique dataset: {output_file}")
    print(f"🌟 Contains {unique_count:,} completely unique responses")
    print(f"💯 Zero duplicates guaranteed!")
    
    # Create summary file
    summary = {
        "total_files_processed": len(jsonl_files),
        "total_examples_loaded": total_examples,
        "unique_examples_final": unique_count,
        "duplicates_removed": duplicates_removed,
        "uniqueness_percentage": round((unique_count/total_examples)*100, 2),
        "output_file": output_file,
        "file_breakdown": file_counts
    }
    
    with open("combination_summary.json", 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Summary saved to: combination_summary.json")
    
    return unique_count

if __name__ == "__main__":
    final_count = combine_all_unique()
    print(f"\n🎯 FINAL RESULT: {final_count:,} unique AAC training examples ready!")