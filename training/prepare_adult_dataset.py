#!/usr/bin/env python3
"""
TinkyBink AAC Dataset - Adult & Medical Contexts
Training data for stroke survivors, adults with disabilities, and medical AAC users
"""

import json
import random
from typing import List, Dict

# Adult daily living contexts
ADULT_DAILY_CONTEXTS = [
    # Basic needs
    ("I need to use the bathroom", ["Right now", "Can wait", "Need help", "Emergency"]),
    ("Are you comfortable?", ["I'm fine", "Too hot", "Too cold", "Need to move"]),
    ("Do you need anything?", ["Water please", "I'm good", "Bathroom", "Pain medication"]),
    
    # Medical/Healthcare
    ("How is your pain level?", ["No pain", "Mild pain", "Moderate", "Severe pain"]),
    ("Time for medication", ["Thank you", "Already took it", "What is it?", "Not yet"]),
    ("The doctor is here", ["Okay", "Not ready", "Need family here", "What for?"]),
    
    # Therapy sessions
    ("Ready for speech therapy?", ["Yes, ready", "Too tired", "Few minutes", "Let's try"]),
    ("Let's practice walking", ["I'll try", "Need support", "Legs hurt", "Maybe later"]),
    ("How was therapy today?", ["Good progress", "Very hard", "Exhausting", "Getting better"]),
    
    # Communication about communication
    ("Is the AAC device helping?", ["Yes, very much", "Still learning", "It's okay", "Need practice"]),
    ("Should I speak slower?", ["Yes please", "I'm fine", "Write it down", "Say again"]),
    ("Do you understand?", ["Yes", "No", "Partly", "Confused"]),
]

# Stroke-specific contexts
STROKE_RECOVERY_CONTEXTS = [
    # Physical challenges
    ("Can you move your arm?", ["A little", "It's stuck", "Hurts to try", "Getting better"]),
    ("Feeling dizzy?", ["Very dizzy", "A bit", "No", "When I stand"]),
    ("Any numbness?", ["Left side", "Right side", "Face only", "No numbness"]),
    
    # Cognitive/Memory
    ("Do you remember me?", ["Of course", "Look familiar", "Sorry, no", "Your name?"]),
    ("What day is it?", ["Not sure", "Tuesday?", "Tell me", "Does it matter?"]),
    ("Where are we?", ["Hospital", "Home", "Don't know", "Rehab center"]),
    
    # Emotional support
    ("How are you feeling?", ["Frustrated", "Hopeful", "Scared", "Determined"]),
    ("It's okay to be upset", ["I know", "So hard", "Want to go home", "Thank you"]),
    ("You're making progress", ["Am I?", "Doesn't feel like it", "Thank you", "Hope so"]),
]

# Professional/Work contexts (for adults returning to work)
PROFESSIONAL_CONTEXTS = [
    # Meetings
    ("Can you join the meeting?", ["Yes", "Need assistance", "Virtual is better", "Not today"]),
    ("Do you have questions?", ["Yes, several", "No questions", "Email me", "Later please"]),
    ("Your thoughts on this?", ["I agree", "Need time", "Have concerns", "Good idea"]),
    
    # Accommodations
    ("What do you need?", ["More time", "Written notes", "Quiet space", "I'm okay"]),
    ("Is this working for you?", ["Yes, helpful", "Not really", "Could be better", "Let's adjust"]),
    ("Should we take a break?", ["Yes please", "Five minutes", "I'm okay", "Almost done"]),
]

# Social contexts for adults
ADULT_SOCIAL_CONTEXTS = [
    # Family/Friends
    ("Want to video call the kids?", ["Yes!", "Not now", "Too tired", "Later tonight"]),
    ("Visitors are here", ["Who is it?", "Send them in", "Not today", "Five minutes"]),
    ("Want to go outside?", ["Yes please", "Too cold", "Maybe later", "Where to?"]),
    
    # Daily decisions
    ("What would you like to eat?", ["Something soft", "Not hungry", "You choose", "Same as yesterday"]),
    ("TV or music?", ["TV please", "Music", "Quiet please", "Neither"]),
    ("Ready for bed?", ["Yes", "Not tired", "Read first", "In a bit"]),
]

def generate_adult_training_data() -> List[Dict]:
    """Generate training data for adult AAC users"""
    examples = []
    
    all_contexts = [
        ("daily", ADULT_DAILY_CONTEXTS),
        ("stroke", STROKE_RECOVERY_CONTEXTS),
        ("professional", PROFESSIONAL_CONTEXTS),
        ("social", ADULT_SOCIAL_CONTEXTS),
    ]
    
    for category_name, contexts in all_contexts:
        for input_text, responses in contexts:
            # Generate variations
            for _ in range(3):
                # Vary formality
                formality = random.choice(["formal", "casual", "medical"])
                
                # Adjust responses based on formality
                adjusted_responses = responses.copy()
                if formality == "formal":
                    adjusted_responses = [r + "." if not r.endswith(('.', '?', '!')) else r for r in adjusted_responses]
                
                example = {
                    "instruction": f"Generate 4 AAC response options for an adult user. Style: {formality}",
                    "input": input_text,
                    "output": ", ".join(adjusted_responses),
                    "metadata": {
                        "category": category_name,
                        "user_type": "adult",
                        "formality": formality
                    }
                }
                examples.append(example)
    
    return examples

def generate_medical_emergency_data() -> List[Dict]:
    """Generate emergency medical communication data"""
    emergency_contexts = [
        ("I need help", ["Call nurse", "Can't breathe", "Chest pain", "Emergency"]),
        ("What's wrong?", ["Pain here", "Can't move", "Feel sick", "Confused"]),
        ("Emergency button?", ["Press it", "Already did", "Where is it?", "Help me"]),
    ]
    
    examples = []
    for input_text, responses in emergency_contexts:
        example = {
            "instruction": "URGENT: Generate emergency AAC responses",
            "input": input_text,
            "output": ", ".join(responses),
            "metadata": {
                "category": "emergency",
                "priority": "high"
            }
        }
        examples.append(example)
    
    return examples

def generate_adaptive_responses():
    """Generate responses that adapt to user capability"""
    adaptive_examples = []
    
    # Same question, different complexity levels
    base_questions = [
        "How are you?",
        "What do you need?",
        "Ready to go?",
    ]
    
    complexity_responses = {
        "basic": {
            "How are you?": ["Good", "Bad", "OK", "Tired"],
            "What do you need?": ["Water", "Help", "Rest", "Nothing"],
            "Ready to go?": ["Yes", "No", "Wait", "Soon"],
        },
        "intermediate": {
            "How are you?": ["I'm doing well", "Not great", "Been better", "Feeling tired"],
            "What do you need?": ["Glass of water", "Some help please", "Need to rest", "I'm fine thanks"],
            "Ready to go?": ["Yes, ready", "Not yet", "Few minutes", "Almost ready"],
        },
        "advanced": {
            "How are you?": ["I'm doing quite well today", "Having a difficult day", "Better than yesterday", "Exhausted but managing"],
            "What do you need?": ["Could I have some water please?", "I need assistance with this", "I'd like to rest for a bit", "Nothing at the moment, thank you"],
            "Ready to go?": ["Yes, I'm ready to go", "I need a few more minutes", "Please wait a moment", "I'll be ready soon"],
        }
    }
    
    for question in base_questions:
        for level, responses_dict in complexity_responses.items():
            example = {
                "instruction": f"Generate AAC responses. Complexity: {level}",
                "input": question,
                "output": ", ".join(responses_dict[question]),
                "metadata": {
                    "complexity_level": level,
                    "adaptive": True
                }
            }
            adaptive_examples.append(example)
    
    return adaptive_examples

def create_complete_dataset():
    """Create comprehensive dataset for all user types"""
    print("🏥 Generating Adult & Medical AAC Dataset")
    print("=" * 50)
    
    all_examples = []
    
    # Adult contexts
    adult_examples = generate_adult_training_data()
    all_examples.extend(adult_examples)
    print(f"✅ Generated {len(adult_examples)} adult context examples")
    
    # Medical emergencies
    emergency_examples = generate_medical_emergency_data()
    all_examples.extend(emergency_examples)
    print(f"🚨 Generated {len(emergency_examples)} emergency examples")
    
    # Adaptive complexity
    adaptive_examples = generate_adaptive_responses()
    all_examples.extend(adaptive_examples)
    print(f"🔄 Generated {len(adaptive_examples)} adaptive examples")
    
    # Save datasets
    with open("tinkybink_adult_train.jsonl", "w") as f:
        for example in all_examples:
            f.write(json.dumps(example) + "\n")
    
    print(f"\n💾 Total examples: {len(all_examples)}")
    print("📁 Saved to: tinkybink_adult_train.jsonl")
    
    # Show samples
    print("\n📋 Sample examples:")
    for i in range(min(3, len(all_examples))):
        print(f"\n{i+1}. {all_examples[i]['input']}")
        print(f"   → {all_examples[i]['output']}")

if __name__ == "__main__":
    create_complete_dataset()