#!/usr/bin/env python3
"""
TinkyBink AAC Dataset Preparation
Creates training data for our custom small language model
"""

import json
import random
from typing import List, Dict, Tuple

# Real AAC conversation patterns from nonverbal children
AAC_CONVERSATIONS = [
    # Food/Drink contexts
    ("Do you want a snack?", ["Yes please!", "Not hungry", "Water please", "Later"]),
    ("Cookie or apple?", ["Cookie!", "Apple please", "Both?", "Neither"]),
    ("Time for lunch", ["Yay food!", "Not yet", "What's for lunch?", "I'm full"]),
    ("Are you thirsty?", ["Yes water", "Juice please", "No thanks", "Milk?"]),
    
    # Emotions/Feelings
    ("How are you feeling?", ["Happy!", "Tired", "Sad", "Silly today"]),
    ("Are you okay?", ["I'm good", "Hurts here", "Need hug", "Feel sick"]),
    ("You look tired", ["Very sleepy", "Not tired!", "Little bit", "Nap time?"]),
    
    # Activities
    ("Let's go to the park", ["Yes! Fun!", "Too hot", "Playground!", "Stay home"]),
    ("Time for bath", ["No bath!", "Bubbles?", "Five minutes", "Okay"]),
    ("Want to play?", ["Yes play!", "Watch TV?", "Too tired", "What game?"]),
    ("Ready for bed?", ["Story first", "Not sleepy", "Teddy bear", "Kiss goodnight"]),
    
    # Daily routines
    ("Time to get dressed", ["Help me", "I can do it", "Comfy clothes", "Not yet"]),
    ("Brush your teeth", ["Already did", "You help", "Where's toothbrush?", "After breakfast"]),
    ("Clean up toys", ["Too many", "You help me", "Almost done", "Five more minutes"]),
    
    # Social/Family
    ("Grandma's here!", ["Yay grandma!", "Show my drawing", "Hide", "Hug grandma"]),
    ("Say hi to friend", ["Hi!", "Shy today", "Want to play?", "Wave hello"]),
    ("Share with sister", ["Okay", "Mine!", "Take turns", "She first"]),
    
    # Needs/Wants
    ("What do you need?", ["Bathroom", "Help please", "Find teddy", "Nothing"]),
    ("Tell me what's wrong", ["Tummy hurts", "Too loud", "Miss mommy", "I'm okay"]),
    ("Use your words", ["Can't", "Trying", "Show you", "Too hard"]),
]

# Emotional states that affect responses
EMOTIONAL_CONTEXTS = [
    "happy", "tired", "excited", "anxious", "playful", "cranky", "calm", "energetic"
]

# Response styles based on child's personality
RESPONSE_STYLES = [
    "shy", "confident", "silly", "serious", "creative", "literal"
]

def generate_training_examples() -> List[Dict]:
    """Generate diverse training examples with context"""
    examples = []
    
    for parent_input, child_responses in AAC_CONVERSATIONS:
        # Generate multiple variants with different contexts
        for emotional_state in random.sample(EMOTIONAL_CONTEXTS, 3):
            for response_style in random.sample(RESPONSE_STYLES, 2):
                # Create a training example
                context = {
                    "emotion": emotional_state,
                    "style": response_style,
                    "time_of_day": random.choice(["morning", "afternoon", "evening", "bedtime"]),
                    "energy_level": random.choice(["high", "medium", "low"])
                }
                
                # Adjust responses based on context
                contextual_responses = adjust_responses_for_context(
                    child_responses, context
                )
                
                example = {
                    "instruction": "You are a nonverbal child using an AAC device. Respond in a simple, child-like way.",
                    "input": f"Context: Child is feeling {emotional_state}. Parent says: \"{parent_input}\"",
                    "output": format_aac_responses(contextual_responses),
                    "metadata": {
                        "category": categorize_conversation(parent_input),
                        "context": context
                    }
                }
                examples.append(example)
    
    return examples

def adjust_responses_for_context(responses: List[str], context: Dict) -> List[str]:
    """Modify responses based on emotional context"""
    adjusted = []
    
    for response in responses:
        if context["emotion"] == "tired" and context["energy_level"] == "low":
            # Make responses shorter/simpler when tired
            if len(response.split()) > 2:
                response = response.split()[0] + "..."
        
        elif context["emotion"] == "excited" and context["style"] == "silly":
            # Add excitement to positive responses
            if any(word in response.lower() for word in ["yes", "yay", "fun"]):
                response = response.upper() + "!!!"
        
        elif context["emotion"] == "anxious":
            # Add uncertainty markers
            if "?" not in response:
                response = response + "?"
        
        adjusted.append(response)
    
    return adjusted

def format_aac_responses(responses: List[str]) -> str:
    """Format as child AAC responses"""
    # Add appropriate emojis based on content
    formatted = []
    for r in responses:
        emoji = get_response_emoji(r)
        formatted.append(f"{emoji} {r}")
    
    return ", ".join(formatted[:4])  # Always provide 4 options

def get_response_emoji(text: str) -> str:
    """Map responses to appropriate emojis"""
    text_lower = text.lower()
    
    emoji_map = {
        # Positive
        "yes": "✅", "yay": "🎉", "okay": "👍", "good": "😊",
        # Negative  
        "no": "❌", "not": "🚫", "don't": "⛔",
        # Food
        "hungry": "🍽️", "eat": "🍴", "cookie": "🍪", "juice": "🧃",
        # Emotions
        "happy": "😊", "sad": "😢", "tired": "😴", "sick": "🤒",
        # Activities
        "play": "🎮", "park": "🏞️", "tv": "📺", "book": "📚",
        # Needs
        "help": "🆘", "bathroom": "🚽", "hug": "🤗", "hurt": "🤕"
    }
    
    for keyword, emoji in emoji_map.items():
        if keyword in text_lower:
            return emoji
    
    return "💭"  # Default thinking emoji

def categorize_conversation(parent_input: str) -> str:
    """Categorize the type of interaction"""
    input_lower = parent_input.lower()
    
    if any(word in input_lower for word in ["eat", "hungry", "food", "drink", "thirsty"]):
        return "food_drink"
    elif any(word in input_lower for word in ["feel", "okay", "tired", "sad", "happy"]):
        return "emotions"
    elif any(word in input_lower for word in ["play", "park", "bath", "bed"]):
        return "activities"
    elif any(word in input_lower for word in ["need", "want", "help", "wrong"]):
        return "needs"
    else:
        return "general"

def create_instruction_variants():
    """Create different instruction prompts for variety"""
    return [
        "You are a nonverbal child using AAC tiles to communicate. Give 4 short responses.",
        "Help a child who can't speak by providing 4 simple communication options.",
        "Generate 4 child-friendly AAC responses that a nonverbal child might select.",
        "Create 4 simple tiles a child could tap to respond to their parent.",
    ]

def save_dataset(examples: List[Dict], filename: str):
    """Save in JSONL format for training"""
    with open(filename, 'w') as f:
        for example in examples:
            f.write(json.dumps(example) + '\n')
    print(f"✅ Saved {len(examples)} training examples to {filename}")

def create_validation_set():
    """Create validation examples for model evaluation"""
    val_examples = [
        {
            "instruction": "You are a nonverbal child using AAC. Respond simply.",
            "input": "Want to go swimming?",
            "output": "🏊 Yes swim!, 🏠 Stay home, 🥶 Too cold, ⏰ Later?"
        },
        {
            "instruction": "Generate child AAC responses.",
            "input": "Time for medicine",
            "output": "😣 Yucky, ✅ Okay, 🍯 With honey?, ⏰ Not yet"
        }
    ]
    return val_examples

if __name__ == "__main__":
    print("🧠 TinkyBink AAC Dataset Generator")
    print("==================================\n")
    
    # Generate training data
    train_examples = generate_training_examples()
    print(f"Generated {len(train_examples)} training examples")
    
    # Add more variety with instruction variants
    final_examples = []
    instructions = create_instruction_variants()
    
    for example in train_examples:
        example["instruction"] = random.choice(instructions)
        final_examples.append(example)
    
    # Save datasets
    save_dataset(final_examples, "tinkybink_train.jsonl")
    save_dataset(create_validation_set(), "tinkybink_val.jsonl")
    
    # Show sample
    print("\n📝 Sample training example:")
    print(json.dumps(final_examples[0], indent=2))
    
    print("\n✨ Dataset ready for training custom TinkyBink SLM!")