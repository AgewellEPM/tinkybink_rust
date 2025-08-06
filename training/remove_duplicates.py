#!/usr/bin/env python3
"""
Remove All Duplicates
Removes duplicate outputs and shows unique responses only
"""
import json
import os
from collections import defaultdict

def analyze_and_remove_duplicates():
    """Analyze all training data and remove duplicates"""
    print("🔍 Analyzing Training Data for Duplicates")
    print("=" * 50)
    
    # Load the ultimate comprehensive dataset
    filename = 'tinkybink_ultimate_comprehensive_train.jsonl'
    
    all_examples = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                if line.strip():
                    all_examples.append(json.loads(line))
    
    print(f"📊 Total examples loaded: {len(all_examples)}")
    
    # Track unique outputs
    unique_outputs = set()
    output_counts = defaultdict(int)
    unique_examples = []
    
    # Find all unique outputs
    for example in all_examples:
        output = example.get('output', '')
        output_counts[output] += 1
        
        if output not in unique_outputs:
            unique_outputs.add(output)
            unique_examples.append(example)
    
    # Show duplicate analysis
    print("\n📊 DUPLICATE ANALYSIS:")
    print("=" * 30)
    
    # Find most duplicated outputs
    sorted_outputs = sorted(output_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("\n🔴 Most duplicated outputs:")
    for output, count in sorted_outputs[:10]:
        if count > 1:
            print(f"Count: {count} - {output[:60]}...")
    
    print(f"\n📈 STATISTICS:")
    print(f"Total examples: {len(all_examples)}")
    print(f"Unique outputs: {len(unique_outputs)}")
    print(f"Duplicates removed: {len(all_examples) - len(unique_outputs)}")
    
    # Save unique examples only
    unique_filename = 'tinkybink_unique_only_train.jsonl'
    with open(unique_filename, 'w') as f:
        for example in unique_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"\n✅ Saved {len(unique_examples)} unique examples to: {unique_filename}")
    
    # Show sample of unique examples
    print("\n📋 SAMPLE UNIQUE EXAMPLES:")
    print("=" * 50)
    
    for i, example in enumerate(unique_examples[:20]):
        print(f"\n{i+1}. Input: {example.get('input', '')}")
        print(f"   Output: {example.get('output', '')}")
    
    return unique_examples, len(unique_outputs)

def create_truly_unique_responses():
    """Create completely unique responses for common inputs"""
    print("\n\n🌟 Creating Truly Unique Responses")
    print("=" * 50)
    
    unique_variations = []
    
    # Common inputs that need unique responses
    common_inputs = [
        "How are you?",
        "I feel sad",
        "I am hungry",
        "I want to play",
        "I need help",
        "What do you want?",
        "I am tired",
        "I love you",
        "Thank you",
        "I am scared"
    ]
    
    # Create 10 completely unique responses for each
    unique_response_sets = {
        "How are you?": [
            "😊 Pretty good thanks, 😐 Just okay today, 😔 Been better honestly, 💭 Hard to say",
            "🌟 Fantastic actually, 😴 Bit tired though, 🤔 Not sure really, 😊 Doing alright",
            "💪 Feeling strong today, 😰 Little anxious actually, 🌈 Better than yesterday, 🤷 So-so",
            "🎉 Great day today, 😤 Bit frustrated honestly, 💭 Complicated feelings, ✨ Wonderful thanks",
            "😌 Very peaceful now, 🔥 Full of energy, 😢 Kinda sad today, 🌺 Beautiful day",
            "🚀 Ready for anything, 😴 Need more sleep, 🌊 Going with flow, 💕 Feel loved",
            "⚡ Super energetic today, 🌙 Bit sleepy still, 🎨 Feeling creative, 🍃 Very calm",
            "🏃 Ready to go, 🛌 Want to rest, 🎵 Music helps me, 🌻 Sunny mood",
            "💫 Stars aligned today, 🌧️ Under the weather, 🦋 Light as butterfly, 🏔️ On top",
            "🌅 New day feelings, 🌃 Night owl mode, 🌸 Blooming nicely thanks, 🎭 Mixed emotions"
        ],
        "I feel sad": [
            "😢 Sad feelings hurt, 💔 Heart feels heavy, 🤗 Here for you, ⏰ Temporary feeling",
            "🌧️ Rainy day inside, 😔 Understand that feeling, 💪 You are strong, 🌈 Sun comes again",
            "💙 Blue feelings okay, 😢 Tears help sometimes, 🫂 Virtual hug sent, 🌟 Better days ahead",
            "🥺 Sorry you hurt, 💭 Talk helps lots, 🎵 Music soothes soul, 🕊️ Peace will come",
            "😞 Down days happen, 🌊 Ride the wave, 💕 You are loved, 🌺 Beauty remains",
            "🍃 Gentle with yourself, 😢 Let it out, 🏠 Safe space here, ✨ This shall pass",
            "🌙 Dark before dawn, 💧 Cleansing tears flow, 🤲 Hold my hand, 🦋 Transform pain",
            "☁️ Clouds hide sun, 😔 Valid feelings friend, 🎨 Express through art, 🌻 Growth through pain",
            "🕯️ Light in darkness, 💔 Broken but healing, 📝 Write it out, 🌈 Spectrum of feelings",
            "🍂 Seasons change hearts, 😢 Honor your feelings, 🧘 Breathe through this, 🌟 Inner strength shines"
        ]
    }
    
    # Generate unique examples
    for input_text, response_list in unique_response_sets.items():
        for i, response in enumerate(response_list):
            unique_variations.append({
                'instruction': f'AAC Unique Response Variation {i+1}',
                'input': input_text,
                'output': response
            })
    
    print(f"✅ Created {len(unique_variations)} truly unique response variations")
    
    # Save unique variations
    with open('tinkybink_unique_variations_train.jsonl', 'w') as f:
        for example in unique_variations:
            f.write(json.dumps(example) + '\n')
    
    return unique_variations

def main():
    print("🔍 TinkyBink Duplicate Removal System")
    print("=" * 70)
    
    # Analyze and remove duplicates
    unique_examples, unique_count = analyze_and_remove_duplicates()
    
    # Create truly unique responses
    unique_variations = create_truly_unique_responses()
    
    print(f"\n\n🏆 FINAL RESULTS:")
    print("=" * 30)
    print(f"✅ {unique_count} completely unique responses")
    print(f"🌟 {len(unique_variations)} new unique variations created")
    print(f"📁 Saved to: tinkybink_unique_only_train.jsonl")

if __name__ == "__main__":
    main()