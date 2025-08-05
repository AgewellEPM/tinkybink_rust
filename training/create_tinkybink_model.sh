#!/bin/bash
# Create TinkyBink SLM using Ollama

echo "🧠 Creating TinkyBink Small Language Model"
echo "========================================"

# Create a Modelfile that customizes an existing small model
cat > Modelfile.tinkybink << 'EOF'
# TinkyBink AAC Small Language Model
FROM tinyllama

# Set the temperature for more predictable child-like responses
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
PARAMETER stop "Parent:"
PARAMETER stop "###"

# System prompt that shapes all responses
SYSTEM """You are TinkyBink, an AI assistant helping nonverbal children communicate through an AAC (Augmentative and Alternative Communication) device.

Your role:
- Generate 4 simple response options a child might want to say
- Use child-appropriate language (1-5 words per response)
- Include emotions and natural child expressions
- Format: Return ONLY 4 comma-separated responses

Examples:
Parent: "Do you want a snack?"
You: "Yes please!, Not hungry, Just water, Maybe later"

Parent: "Time for bed"
You: "Not tired!, Story first?, Five minutes?, Okay mommy"

Parent: "How are you feeling?"
You: "Happy today!, Little sad, Tummy hurts, Want hug"

Remember: Be a child, not an adult. Keep it simple and emotional."""

# Template for conversations
TEMPLATE """{{ .System }}
Parent: {{ .Prompt }}
Child responses: """
EOF

echo "📄 Created Modelfile.tinkybink"

# Create the model in Ollama
echo "🔨 Building TinkyBink model..."
ollama create tinkybink -f Modelfile.tinkybink

# Test the model
echo -e "\n🧪 Testing TinkyBink model..."
echo "================================"

test_prompts=(
    "Let's go to the park"
    "Are you hungry?"
    "Time to brush teeth"
    "Want to play a game?"
)

for prompt in "${test_prompts[@]}"; do
    echo -e "\n👨 Parent: \"$prompt\""
    echo -n "👶 Child options: "
    ollama run tinkybink "$prompt" --verbose=false
done

echo -e "\n✅ TinkyBink SLM created successfully!"
echo "📱 Use in your app with: ollama run tinkybink"

# Create enhanced training data for future fine-tuning
cat > generate_training_data.py << 'EOF'
import json
import random

# Core AAC scenarios
scenarios = {
    "daily_routines": [
        ("Time to wake up", ["Five more minutes", "Good morning!", "Too early", "Where's teddy?"]),
        ("Let's get dressed", ["I do it!", "You help", "Comfy clothes", "Favorite shirt"]),
        ("Breakfast time", ["Cereal please", "Not hungry yet", "Pancakes?", "Just milk"]),
    ],
    "emotions": [
        ("You seem upset", ["Need hug", "I'm okay", "Feel angry", "Want mommy"]),
        ("What's wrong?", ["Nothing", "Hurts here", "Someone was mean", "Just tired"]),
        ("Are you happy?", ["Very happy!", "I'm silly", "Feel good", "Love you"]),
    ],
    "activities": [
        ("Want to color?", ["Yes! Crayons", "Draw together?", "Not now", "Paint instead?"]),
        ("Clean up time", ["Almost done", "Too much", "Help me?", "Five more"]),
        ("Let's read a book", ["Pick story!", "You read", "Look pictures", "Bedtime story?"]),
    ],
    "social": [
        ("Say hi to grandma", ["Hi grandma!", "Show my toy", "Shy now", "Hug?"]),
        ("Share with brother", ["My turn", "He can have", "We trade?", "Not this one"]),
        ("Friend is here", ["Play together!", "My toys", "Hide and seek?", "Show my room"]),
    ]
}

# Generate comprehensive training data
training_data = []

for category, conversations in scenarios.items():
    for parent_input, child_responses in conversations:
        # Add variations
        for _ in range(5):
            # Shuffle responses
            responses = random.sample(child_responses, 4)
            
            # Sometimes modify responses slightly
            if random.random() > 0.5:
                responses[0] = responses[0].rstrip("!?.") + random.choice(["!", "?", "..."])
            
            training_data.append({
                "instruction": "Generate 4 simple AAC responses for a nonverbal child.",
                "input": f"Parent says: '{parent_input}'",
                "output": ", ".join(responses),
                "category": category
            })

# Save training data
with open("tinkybink_training.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

print(f"Generated {len(training_data)} training examples")
EOF

python3 generate_training_data.py

echo -e "\n🎓 Training data generated for future fine-tuning"
echo "📚 Saved to: tinkybink_training.jsonl"