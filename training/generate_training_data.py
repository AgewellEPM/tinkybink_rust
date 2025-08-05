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
