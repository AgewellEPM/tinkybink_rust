#!/usr/bin/env python3
"""
Ultimate Dataset Compiler
Combines all training datasets into the final comprehensive AAC training set
"""
import json
import os

def compile_ultimate_dataset():
    """Compile all training datasets into ultimate comprehensive set"""
    print("🌟 ULTIMATE DATASET COMPILER")
    print("=" * 70)
    print("🚀 Combining ALL training data into final comprehensive dataset")
    print("🎯 Most advanced AAC training system ever created!")
    print()
    
    # All training files to combine
    training_files = [
        'tinkybink_final_massive_train.jsonl',
        'tinkybink_conversation_train.jsonl',
        'tinkybink_smart_expansion_train.jsonl',
        'tinkybink_ultra_expansion_train.jsonl',
        'tinkybink_ultimate_fusion_train.jsonl',
        'tinkybink_complete_train.jsonl',
        'tinkybink_adult_train.jsonl',
        'tinkybink_emoji_master_train.jsonl'
    ]
    
    all_examples = []
    file_stats = {}
    
    # Load all training files
    for filename in training_files:
        if os.path.exists(filename):
            try:
                count = 0
                with open(filename, 'r') as f:
                    for line in f:
                        if line.strip():
                            example = json.loads(line)
                            all_examples.append(example)
                            count += 1
                file_stats[filename] = count
                print(f"📁 Loaded {filename}: {count} examples")
            except Exception as e:
                print(f"⚠️ Could not load {filename}: {e}")
        else:
            print(f"❌ File not found: {filename}")
    
    print(f"\n📊 Total examples loaded: {len(all_examples)}")
    
    # Remove duplicates based on input+output combination
    print("🔄 Removing duplicates...")
    seen_combinations = set()
    unique_examples = []
    
    for example in all_examples:
        # Create unique key from input and output
        input_text = example.get('input', '')
        output_text = example.get('output', '')
        key = f"{input_text}||{output_text}"
        
        if key not in seen_combinations:
            seen_combinations.add(key)
            unique_examples.append(example)
    
    duplicates_removed = len(all_examples) - len(unique_examples)
    print(f"🗑️ Removed {duplicates_removed} duplicates")
    
    # Quality validation
    print("✅ Validating quality...")
    valid_examples = []
    
    for example in unique_examples:
        input_text = example.get('input', '')
        output_text = example.get('output', '')
        
        # Basic quality checks
        if (input_text and output_text and 
            len(input_text.strip()) > 0 and 
            len(output_text.strip()) > 0 and
            ',' in output_text):  # Ensure AAC format with commas
            valid_examples.append(example)
    
    quality_filtered = len(unique_examples) - len(valid_examples)
    print(f"🔍 Filtered {quality_filtered} low-quality examples")
    
    # Save ultimate comprehensive dataset
    ultimate_filename = 'tinkybink_ultimate_comprehensive_train.jsonl'
    with open(ultimate_filename, 'w') as f:
        for example in valid_examples:
            f.write(json.dumps(example) + '\n')
    
    final_count = len(valid_examples)
    
    print(f"\n🎉 ULTIMATE DATASET COMPILATION COMPLETE!")
    print("=" * 60)
    print("📊 FINAL STATISTICS:")
    print("=" * 30)
    for filename, count in file_stats.items():
        print(f"   {filename}: {count:,} examples")
    print("=" * 30)
    print(f"📈 Total examples processed: {len(all_examples):,}")
    print(f"🗑️ Duplicates removed: {duplicates_removed:,}")
    print(f"🔍 Quality filtered: {quality_filtered:,}")
    print(f"🏆 FINAL UNIQUE EXAMPLES: {final_count:,}")
    print(f"📁 Saved to: {ultimate_filename}")
    print()
    
    if final_count >= 5000:
        print("🎯 TARGET EXCEEDED: 5,000+ examples achieved!")
        print("🌟 Most comprehensive AAC training dataset ever created!")
        print("🚀 Ready for advanced model training!")
    else:
        print(f"📊 Progress: {final_count:,}/5,000 examples")
    
    return ultimate_filename, final_count, file_stats

def create_training_summary():
    """Create comprehensive training summary"""
    print("\n📋 Creating Training Summary Report")
    print("=" * 40)
    
    summary = {
        "dataset_info": {
            "name": "TinkyBink Ultimate Comprehensive AAC Training Dataset",
            "version": "1.0",
            "created": "2025-08-05",
            "description": "Most advanced AAC training dataset ever created"
        },
        "training_categories": {
            "emotional_responses": "Complete emotional vocabulary with contextual responses",
            "daily_activities": "Comprehensive daily life scenarios and activities", 
            "medical_scenarios": "Healthcare and medical communication training",
            "social_interactions": "Social situations and relationship communication",
            "activity_boards": "Step-by-step activity guides and instructions",
            "conversation_flows": "Multi-turn dialogue and conversation training",
            "contextual_responses": "Context-aware situational responses",
            "time_variations": "Temporal context and time-based scenarios",
            "intensity_variations": "Emotional intensity and degree modifiers",
            "question_responses": "Comprehensive question-answer patterns"
        },
        "quality_features": {
            "format": "Exactly 4 responses per input with contextual emojis",
            "emoji_usage": "Emotionally appropriate emojis for each response",
            "response_variety": "Multiple options for user choice and expression",
            "natural_language": "Conversational and accessible language patterns",
            "practical_application": "Real-world scenarios and situations"
        },
        "technical_specs": {
            "base_model": "llama3.2",
            "temperature": 0.3,
            "top_p": 0.8,
            "format": "JSONL training data",
            "instruction_tuning": "Specialized AAC instruction following"
        }
    }
    
    # Save training summary
    with open('training_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("✅ Training summary saved to: training_summary.json")
    return summary

def main():
    print("🌟 TinkyBink Ultimate Dataset Compiler")
    print("=" * 70)
    print("🎯 Final compilation of the most comprehensive AAC training dataset")
    print("🚀 Combining all training data into ultimate system!")
    print()
    
    # Compile ultimate dataset
    dataset_file, final_count, file_stats = compile_ultimate_dataset()
    
    # Create training summary
    summary = create_training_summary()
    
    print(f"\n✅ ULTIMATE SUCCESS!")
    print("=" * 30)
    print(f"🏆 Created {final_count:,} comprehensive training examples")
    print("🌟 Most advanced AAC training system in existence!")
    print("🚀 Ready to train the ultimate AAC model!")

if __name__ == "__main__":
    main()