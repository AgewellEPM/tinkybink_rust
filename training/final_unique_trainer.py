#!/usr/bin/env python3
"""
Final Unique Trainer
Combines all unique responses into final training dataset
"""
import json
import os

def combine_unique_datasets():
    """Combine all unique datasets"""
    print("🌟 Combining All Unique Datasets")
    print("=" * 50)
    
    all_unique_examples = []
    
    # Files to combine
    unique_files = [
        'tinkybink_unique_only_train.jsonl',
        'tinkybink_100_percent_unique_train.jsonl',
        'tinkybink_unique_variations_train.jsonl'
    ]
    
    file_counts = {}
    
    for filename in unique_files:
        if os.path.exists(filename):
            count = 0
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip():
                        all_unique_examples.append(json.loads(line))
                        count += 1
            file_counts[filename] = count
            print(f"📁 Loaded {filename}: {count} examples")
    
    # Final deduplication check
    seen_outputs = set()
    final_unique = []
    
    for example in all_unique_examples:
        output = example.get('output', '')
        if output not in seen_outputs:
            seen_outputs.add(output)
            final_unique.append(example)
    
    # Save final unique dataset
    final_filename = 'tinkybink_final_unique_train.jsonl'
    with open(final_filename, 'w') as f:
        for example in final_unique:
            f.write(json.dumps(example) + '\n')
    
    print(f"\n📊 FINAL STATISTICS:")
    print("=" * 30)
    for filename, count in file_counts.items():
        print(f"{filename}: {count}")
    print("=" * 30)
    print(f"Total loaded: {len(all_unique_examples)}")
    print(f"After final dedup: {len(final_unique)}")
    print(f"\n✅ Saved to: {final_filename}")
    
    # Create Modelfile for unique training
    modelfile_content = '''FROM llama3.2

PARAMETER temperature 0.3
PARAMETER top_p 0.8
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 4096

SYSTEM """You are an AAC (Augmentative and Alternative Communication) assistant responding in a tile-based format. ALWAYS provide EXACTLY 4 response options separated by commas. Each response should:

1. Start with a contextually appropriate emoji
2. Be 2-4 words maximum
3. Offer different choices/responses for the same input
4. Use natural, conversational language
5. NEVER repeat the same response pattern

Your responses help users communicate through visual tiles they can tap. Keep responses unique and varied."""

TEMPLATE """{{ if .System }}{{ .System }}
{{ end }}{{ if .Prompt }}{{ .Prompt }}{{ end }}
Response: """
'''
    
    with open('Modelfile.unique', 'w') as f:
        f.write(modelfile_content)
    
    print("📁 Created Modelfile.unique for training")
    
    return final_filename, len(final_unique)

def analyze_uniqueness():
    """Analyze the uniqueness of responses"""
    print("\n📊 Analyzing Response Uniqueness")
    print("=" * 40)
    
    filename = 'tinkybink_final_unique_train.jsonl'
    
    if not os.path.exists(filename):
        print("❌ Final unique file not found")
        return
    
    examples = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                examples.append(json.loads(line))
    
    # Analyze patterns
    inputs = set()
    outputs = set()
    input_counts = {}
    
    for example in examples:
        input_text = example.get('input', '')
        output_text = example.get('output', '')
        
        inputs.add(input_text)
        outputs.add(output_text)
        
        if input_text in input_counts:
            input_counts[input_text] += 1
        else:
            input_counts[input_text] = 1
    
    print(f"📈 Unique inputs: {len(inputs)}")
    print(f"📈 Unique outputs: {len(outputs)}")
    print(f"📈 Total examples: {len(examples)}")
    
    # Show inputs with multiple unique responses
    print("\n🌟 Inputs with Multiple Unique Responses:")
    multi_response_inputs = [(k, v) for k, v in input_counts.items() if v > 1]
    multi_response_inputs.sort(key=lambda x: x[1], reverse=True)
    
    for input_text, count in multi_response_inputs[:10]:
        print(f"\n'{input_text}' has {count} unique responses:")
        # Show the unique responses for this input
        for example in examples:
            if example.get('input', '') == input_text:
                print(f"  → {example.get('output', '')}")

def main():
    print("🚀 TinkyBink Final Unique Trainer")
    print("=" * 70)
    print("💯 Creating final dataset with 100% unique responses")
    print()
    
    filename, count = combine_unique_datasets()
    analyze_uniqueness()
    
    print(f"\n🏆 FINAL RESULTS:")
    print("=" * 30)
    print(f"✅ {count} completely unique responses")
    print("🌟 Zero duplicates!")
    print("📁 Ready for training: {filename}")
    print("\n💡 Next step: Train model with unique dataset")
    print("   ollama create tinkybink-unique -f Modelfile.unique")

if __name__ == "__main__":
    main()