#!/usr/bin/env python3
"""
Enhance AAC Format with Word-Emoji-Sentence-Tracking
Converts existing responses to full AAC format
"""
import json
import re

def enhance_aac_format():
    """Convert responses to full AAC format with tracking"""
    
    print("🌟 TinkyBink AAC Format Enhancer")
    print("=" * 50)
    print("🔄 Converting to word-emoji-sentence-tracking format")
    print()
    
    # Load master unique dataset
    input_file = "tinkybink_master_unique_final.jsonl"
    enhanced_examples = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
                
            try:
                example = json.loads(line)
                enhanced = enhance_single_example(example)
                if enhanced:
                    enhanced_examples.append(enhanced)
                    
                if line_num % 500 == 0:
                    print(f"   ✅ Processed {line_num} examples...")
                    
            except json.JSONDecodeError as e:
                print(f"   ❌ JSON error on line {line_num}: {e}")
                continue
    
    print(f"\n📊 Enhanced {len(enhanced_examples)} examples")
    
    # Save enhanced dataset
    output_file = "tinkybink_enhanced_aac_final.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in enhanced_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved enhanced dataset: {output_file}")
    
    # Show example
    if enhanced_examples:
        print(f"\n🔍 EXAMPLE ENHANCED FORMAT:")
        example = enhanced_examples[0]
        print(json.dumps(example, indent=2, ensure_ascii=False))
    
    return len(enhanced_examples)

def enhance_single_example(example):
    """Convert single example to enhanced AAC format"""
    
    input_text = example.get('input', '')
    output_text = example.get('output', '')
    
    if not output_text:
        return None
    
    # Parse emoji-word pairs from output
    # Format: "🎪 Joy circus performing, 🌟 Happiness supernova exploding, ..."
    tiles = parse_tiles(output_text)
    
    if not tiles:
        return None
    
    # Generate spoken sentence from tiles
    spoken_sentence = generate_spoken_sentence(tiles, input_text)
    
    # Create enhanced format
    enhanced = {
        "instruction": example.get('instruction', 'AAC Response'),
        "input": input_text,
        "aac_response": {
            "tiles": tiles,
            "spoken_sentence": spoken_sentence,
            "usage_data": {
                "category": categorize_input(input_text),
                "emotion_level": detect_emotion_level(input_text),
                "complexity": len(tiles),
                "frequency_weight": 1.0
            }
        },
        "raw_output": output_text
    }
    
    return enhanced

def parse_tiles(output_text):
    """Parse emoji-word pairs from output text"""
    
    tiles = []
    
    # Split by commas and parse each tile
    parts = output_text.split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        # Find emoji and extract words
        emoji_match = re.search(r'([^\w\s]+)', part)
        if emoji_match:
            emoji = emoji_match.group(1)
            # Get text after emoji
            words = part.replace(emoji, '').strip()
            
            if words:
                tiles.append({
                    "emoji": emoji,
                    "words": words,
                    "tile_id": f"tile_{len(tiles)+1}"
                })
    
    return tiles

def generate_spoken_sentence(tiles, input_text):
    """Generate natural spoken sentence from tiles"""
    
    if not tiles:
        return ""
    
    # Extract key words from tiles
    key_words = []
    for tile in tiles:
        words = tile.get('words', '').split()
        if words:
            key_words.append(words[0])  # Take first word from each tile
    
    # Generate natural sentence based on input context
    if any(word in input_text.lower() for word in ['happy', 'joy', 'good', 'great']):
        return f"I feel {' and '.join(key_words[:2])} right now."
    elif any(word in input_text.lower() for word in ['sad', 'upset', 'bad', 'hurt']):
        return f"I am feeling {key_words[0]} today."
    elif any(word in input_text.lower() for word in ['want', 'need', 'like']):
        return f"I want {' and '.join(key_words[:2])}."
    elif any(word in input_text.lower() for word in ['help', 'assistance']):
        return f"I need help with {key_words[0]}."
    else:
        # Default natural sentence
        return f"I am {key_words[0]} and {key_words[1] if len(key_words) > 1 else 'okay'}."

def categorize_input(input_text):
    """Categorize input for tracking"""
    
    input_lower = input_text.lower()
    
    if any(word in input_lower for word in ['happy', 'joy', 'excited', 'good', 'great']):
        return 'positive_emotion'
    elif any(word in input_lower for word in ['sad', 'upset', 'angry', 'mad', 'hurt']):
        return 'negative_emotion'
    elif any(word in input_lower for word in ['want', 'need', 'like', 'prefer']):
        return 'request'
    elif any(word in input_lower for word in ['help', 'assistance', 'support']):
        return 'help_seeking'
    elif any(word in input_lower for word in ['eat', 'drink', 'food', 'hungry', 'thirsty']):
        return 'basic_needs'
    elif any(word in input_lower for word in ['pain', 'hurt', 'sick', 'doctor']):
        return 'medical'
    else:
        return 'general'

def detect_emotion_level(input_text):
    """Detect emotional intensity level"""
    
    input_lower = input_text.lower()
    
    # High intensity words
    if any(word in input_lower for word in ['very', 'extremely', 'really', 'so', 'incredibly']):
        return 'high'
    # Medium intensity
    elif any(word in input_lower for word in ['pretty', 'quite', 'somewhat', 'little']):
        return 'medium'
    # Low intensity (default)
    else:
        return 'low'

if __name__ == "__main__":
    count = enhance_aac_format()
    print(f"\n🎯 ENHANCED: {count:,} examples with full AAC format!")