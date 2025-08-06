#!/usr/bin/env python3
"""
Create Completely Unique Responses
Generates 100% unique responses for every input scenario
"""
import json
import random

def create_unique_emotional_responses():
    """Create unique responses for emotional states"""
    print("😊 Creating Unique Emotional Responses")
    print("=" * 40)
    
    unique_responses = []
    
    # Happy variations - each completely different
    happy_inputs = [
        "I feel happy",
        "I am happy", 
        "Feeling happy today",
        "So happy right now",
        "Really happy",
        "Very happy",
        "Extremely happy",
        "Kind of happy",
        "Happy about this",
        "Happy to be here"
    ]
    
    happy_responses = [
        "😊 Joy fills heart, 🌞 Sunshine inside me, 🎉 Celebrate this feeling, 💕 Share the love",
        "🌟 Glowing with joy, 😄 Smile won't stop, 🦋 Butterflies dancing inside, 🎈 Floating on air",
        "💫 Sparkles everywhere today, 🌈 Rainbow in soul, 🎵 Heart singing songs, 🌺 Blooming with happiness",
        "🎊 Party in heart, ✨ Magic moment captured, 🌻 Sunflower feelings growing, 💝 Gift of joy",
        "🎨 Painting world bright, 🏃 Energy overflowing today, 🎭 Comedy not tragedy, 🍀 Lucky and blessed",
        "🚀 Flying high now, 🌊 Waves of good, 🎪 Circus of delight, 🏆 Winning at life",
        "🎯 Hit happiness jackpot, 🌸 Petals of joy, 🎤 Singing inside out, 🏖️ Vacation vibes",
        "💎 Diamond bright mood, 🎢 Rollercoaster going up, 🌅 Dawn breaking beautifully, 🎁 Present moment gift",
        "🦄 Unicorn level joy, 🏔️ Mountain top feeling, 🎸 Rock star mood, 🌙 Moon and stars",
        "🎪 Carnival in soul, 🌺 Tropical paradise feeling, 🎯 Bullseye of bliss, 🏃 Running on sunshine"
    ]
    
    for i, (input_text, response) in enumerate(zip(happy_inputs, happy_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Happy Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    # Sad variations - each completely different
    sad_inputs = [
        "I feel sad",
        "I am sad",
        "Feeling sad today",
        "So sad right now",
        "Really sad",
        "Very sad", 
        "Extremely sad",
        "Kind of sad",
        "Sad about this",
        "Sad to be here"
    ]
    
    sad_responses = [
        "😢 Tears like rain, 💙 Ocean of sorrow, 🌧️ Storm clouds gathering, 🍂 Autumn in heart",
        "🌊 Drowning in feelings, 😔 Weight on shoulders, 🌑 Eclipse of joy, 🥀 Wilted flower",
        "💧 River of tears, 🌫️ Fog surrounds me, 🎭 Tragedy mask on, ❄️ Winter inside",
        "🌧️ Personal rain cloud, 💔 Shattered glass heart, 🌙 Dark side moon, 🍃 Leaves falling",
        "☔ Umbrella can't help, 😞 Gravity pulls down, 🌊 Tidal wave hit, 🎻 Violin plays",
        "🌑 New moon darkness, 💙 Bruised soul showing, 🌧️ Monsoon of emotion, 🕯️ Candle flickering",
        "😢 Well of sadness, 🌊 Undertow pulling me, 🍂 Everything falling apart, ⛈️ Thunder in chest",
        "💧 Leaking heart vessel, 🌫️ Lost in mist, 🎭 Behind the mask, 🌊 Waves crash over",
        "☁️ Grey sky mind, 💔 Pieces scattered everywhere, 🌧️ Endless rain falling, 🍃 Wind took joy",
        "🌊 Deep ocean blues, 😔 Anchor dragging down, 🌑 Void opening up, 🥀 Garden died inside"
    ]
    
    for i, (input_text, response) in enumerate(zip(sad_inputs, sad_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Sad Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    return unique_responses

def create_unique_activity_responses():
    """Create unique responses for activities"""
    print("🎯 Creating Unique Activity Responses")
    print("=" * 40)
    
    unique_responses = []
    
    # Eating variations - each completely different
    eating_inputs = [
        "I want to eat",
        "I am hungry",
        "Need food now",
        "Time to eat",
        "Want some food",
        "Getting hungry",
        "Need to eat",
        "Food please",
        "Hungry for food",
        "Ready to eat"
    ]
    
    eating_responses = [
        "🍕 Pizza sounds perfect, 🥗 Salad feels right, 🍜 Soup warms soul, 🧃 Juice too please",
        "🥪 Sandwich quick fix, 🍎 Apple for health, 🧀 Cheese and crackers, 🫖 Tea with it",
        "🍳 Eggs hit spot, 🥓 Bacon smells amazing, 🍞 Toast with butter, ☕ Coffee essential",
        "🍝 Pasta fills belly, 🥦 Veggies for nutrition, 🍰 Dessert after maybe, 💧 Water first",
        "🌮 Tacos sound fun, 🥑 Avocado on side, 🌶️ Spicy kicks good, 🥤 Cold drink needed",
        "🍱 Bento box variety, 🍙 Rice balls filling, 🥢 Chopsticks ready go, 🍵 Green tea calm",
        "🥘 Stew hearty meal, 🥖 Fresh bread dipping, 🧈 Butter melts nicely, 🥛 Milk feels right",
        "🍔 Burger hits different, 🍟 Fries on side, 🥒 Pickles add crunch, 🧃 Lemonade refreshing",
        "🥞 Pancakes stack high, 🍯 Honey drizzle sweet, 🫐 Berries fresh topping, 🥤 Orange juice bright",
        "🍖 Meat satisfies hunger, 🥔 Potatoes fill up, 🥕 Carrots add color, 🧊 Ice water cool"
    ]
    
    for i, (input_text, response) in enumerate(zip(eating_inputs, eating_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Eating Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    # Sleep variations - each completely different  
    sleep_inputs = [
        "I am tired",
        "I need sleep",
        "Want to sleep",
        "Time for bed",
        "Getting sleepy",
        "Need rest now",
        "So tired",
        "Ready for bed",
        "Want to rest",
        "Feeling sleepy"
    ]
    
    sleep_responses = [
        "😴 Eyelids heavy weights, 🛏️ Bed calls name, 🌙 Moon says goodnight, 💤 Dreams await arrival",
        "🌃 Night owl retiring, 🛌 Pillow looks perfect, 🌟 Stars counting me, 😪 Yawn escapes lips",
        "💤 Battery needs charging, 🏠 Nest feels cozy, 🌙 Luna lullaby playing, 🧸 Teddy bear ready",
        "😴 Sandman knocking door, 🛏️ Sheets feel inviting, 🌌 Galaxy of dreams, 💫 Shooting star wishes",
        "🌙 Crescent moon pillow, 😪 Drowsy train arriving, 🛌 Blanket fort building, ⭐ Constellation counting",
        "💤 Sleep mode activating, 🌃 Twilight zone entering, 🛏️ Mattress cloud floating, 🌙 Lunar landing soon",
        "😴 Hibernation time now, 🏠 Cave feels safe, 🌟 Starlight nightlight glowing, 💤 Z's incoming fast",
        "🌙 Moonbeam highway traveling, 😪 Exhaustion winning battle, 🛌 Dream theater opening, ⭐ Wish upon star",
        "💤 Recharge station needed, 🌃 Night shift over, 🛏️ Cloud nine waiting, 🌙 Lunar eclipse eyes",
        "😴 Sleepy town resident, 🏠 Dreamland passport ready, 🌌 Astral projection starting, 💫 Stardust sprinkling down"
    ]
    
    for i, (input_text, response) in enumerate(zip(sleep_inputs, sleep_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Sleep Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    return unique_responses

def create_unique_social_responses():
    """Create unique responses for social situations"""
    print("👥 Creating Unique Social Responses")
    print("=" * 40)
    
    unique_responses = []
    
    # Help requests - each completely different
    help_inputs = [
        "I need help",
        "Can you help",
        "Help me please",
        "Need assistance",
        "Help needed",
        "Please help me",
        "Need some help",
        "Could use help",
        "Help required",
        "Assistance please"
    ]
    
    help_responses = [
        "🤲 Hands reaching out, 🧩 Puzzle piece missing, 🔦 Light the way, 🗺️ Map needed",
        "🆘 SOS sending now, 🤝 Partnership required here, 🧭 Compass broken somehow, 🔑 Key lost somewhere",
        "🚨 Alert going out, 👥 Team effort needed, 🎯 Target too far, 🪜 Ladder too short",
        "📣 Calling all allies, 🤲 Village takes child, 🌉 Bridge needs building, 🧰 Tools not enough",
        "🔔 Bell ringing loud, 👫 Buddy system activate, 🗼 Tower too tall, 🎪 Circus needs ringmaster",
        "📢 Megaphone moment here, 🤝 Contract needs signing, 🏗️ Construction crew wanted, 🧮 Math doesn't add",
        "🚦 Signal sent up, 👥 Assembly required now, 🎲 Dice rolled wrong, 🏔️ Mountain needs guide",
        "🎺 Trumpet call sounding, 🤲 Many hands lighter, 🌊 Tide turning against, 🧗 Cliff face steep",
        "📯 Herald announcing need, 👫 Partner dance starting, 🎯 Bullseye moved away, 🏗️ Scaffold needed high",
        "🔔 Church bells ringing, 🤝 Alliance forming now, 🌉 Gap needs spanning, 🧰 Toolbox half empty"
    ]
    
    for i, (input_text, response) in enumerate(zip(help_inputs, help_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Help Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    # Love expressions - each completely different
    love_inputs = [
        "I love you",
        "Love you lots",
        "Love you so much",
        "I really love you",
        "Love you tons",
        "Love you forever",
        "Love you always",
        "Love you dearly",
        "Love you truly",
        "Love you deeply"
    ]
    
    love_responses = [
        "❤️ Heart overflowing rivers, 🌹 Rose garden blooming, 💕 Soul recognizes soul, ✨ Universe aligned perfectly",
        "💝 Gift beyond measure, 🦋 Metamorphosis complete now, 🌟 Constellation named you, 🏰 Castle built together",
        "💖 Heartbeat synchronizes yours, 🌺 Paradise found here, 💫 Shooting stars caught, 🎨 Masterpiece painted daily",
        "❤️‍🔥 Fire burns eternal, 🌈 Spectrum complete now, 💎 Diamond formed pressure, 🌊 Ocean meets ocean",
        "💗 Expanding like universe, 🦢 Swan song beautiful, ⭐ North star guiding, 🏔️ Mountain moved already",
        "💞 Infinity symbol us, 🌸 Cherry blossoms forever, 💫 Meteor shower wishes, 🎪 Greatest show earth",
        "💕 Quantum entanglement proven, 🌹 Thorns worth roses, ✨ Sparklers lit permanently, 🏰 Fairy tale real",
        "💝 Wrapped in ribbons, 🦋 Chrysalis emerged beautiful, 🌟 Supernova explosion joy, 🌊 Waves crash together",
        "💖 Treasure chest opened, 🌺 Lei around heart, 💫 Comet tail following, 🎨 Colors never seen",
        "❤️ Cardiac symphony playing, 🌈 Pot gold found, 💎 Precious beyond words, 🌊 Depths unmeasurable here"
    ]
    
    for i, (input_text, response) in enumerate(zip(love_inputs, love_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Love Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    return unique_responses

def create_unique_question_responses():
    """Create unique responses for common questions"""
    print("❓ Creating Unique Question Responses")
    print("=" * 40)
    
    unique_responses = []
    
    # How are you - 20 unique variations
    how_are_you = [
        "How are you?", "How are you doing?", "How are you feeling?", "How are you today?",
        "How's it going?", "How do you feel?", "How have you been?", "How are things?",
        "How you doing?", "How are you now?", "How you feeling?", "How's everything?",
        "How are you right now?", "How you been?", "How's life?", "How goes it?",
        "How are you this morning?", "How are you this evening?", "How are you lately?", "How ya doing?"
    ]
    
    how_responses = [
        "🌟 Constellation aligning nicely, 😊 Sunbeam caught today, 💭 Thoughts like butterflies, 🎪 Juggling many plates",
        "🎢 Roller coaster ride, 😌 Zen garden peaceful, 🌊 Surfing life waves, 💫 Stardust settling down",
        "🏔️ Climbing steady upward, 😴 Energy conserving mode, 🌈 Chasing rainbow ends, 🎯 Dart hit board",
        "🦋 Metamorphosis ongoing currently, 😊 Smile muscles exercising, 💭 Brain fog lifting, 🎪 Balancing act continues",
        "🌊 Tide ebbing flowing, 😌 Meditation mode activated, 🎨 Painting new canvas, 💫 Cosmic dust settling",
        "🚀 Launch sequence initiated, 😊 Vitamin D absorbed, 🌺 Blooming where planted, 🎯 Arrows finding targets",
        "🎭 Masks switching hourly, 😴 Recharge cable connected, 🌟 Shine getting polished, 💭 Synapses firing well",
        "🏃 Marathon not sprint, 😌 Float tank feeling, 🎪 Tightrope walking carefully, 🌊 Wave riding smoothly",
        "🦅 Eagle eye view, 😊 Serotonin levels good, 💫 Orbit maintaining stable, 🎨 Palette mixing nicely",
        "🌱 Growing inch daily, 😴 Power save mode, 🎯 Target practice improving, 💭 Neural pathways clearing",
        "🎢 Loop-de-loop completed, 😌 Buddha smile forming, 🌊 Current carrying forward, 🌟 Glow stick activated",
        "🏔️ Summit visible now, 😊 Dimples showing through, 💫 Satellite connection strong, 🎪 Juggler improving skills",
        "🦋 Wings drying nicely, 😴 Sleep debt reducing, 🌈 Prism refracting light, 🎯 Bullseye getting closer",
        "🌊 Surfboard waxed ready, 😌 Inner peace found, 🎨 Brushstrokes getting bolder, 💭 Clarity emerging slowly",
        "🚀 Afterburners engaged fully, 😊 Endorphins releasing naturally, 🌺 Petals opening up, 💫 Gravity defying today",
        "🎭 Comedy mask winning, 😴 REM cycles completing, 🌟 Supernova potential building, 🎪 Circus running smoothly",
        "🏃 Stride hitting rhythm, 😌 Chakras aligning properly, 🌊 Wavelength synchronized well, 🎯 Accuracy improving daily",
        "🦅 Thermal riding high, 😊 Happiness index rising, 💫 Cosmic joke understood, 🎨 Masterpiece progressing nicely",
        "🌱 Roots spreading deeper, 😴 Circadian rhythm balanced, 🌈 Full spectrum visible, 💭 Thoughts crystallizing clearly",
        "🎢 Stomach settling down, 😌 Nirvana glimpsed briefly, 🌊 Flow state achieved, 🌟 Inner light brightening"
    ]
    
    for i, (input_text, response) in enumerate(zip(how_are_you, how_responses)):
        unique_responses.append({
            'instruction': f'AAC Unique Greeting Response {i+1}',
            'input': input_text,
            'output': response
        })
    
    return unique_responses

def compile_all_unique_responses():
    """Compile all unique response categories"""
    print("\n🚀 Compiling All Unique Responses")
    print("=" * 50)
    
    all_unique = []
    
    # Generate all unique categories
    all_unique.extend(create_unique_emotional_responses())
    all_unique.extend(create_unique_activity_responses())
    all_unique.extend(create_unique_social_responses())
    all_unique.extend(create_unique_question_responses())
    
    # Add more unique categories...
    
    # Save all unique responses
    filename = 'tinkybink_100_percent_unique_train.jsonl'
    with open(filename, 'w') as f:
        for example in all_unique:
            f.write(json.dumps(example) + '\n')
    
    print(f"\n✅ Created {len(all_unique)} 100% unique training examples")
    print(f"📁 Saved to: {filename}")
    
    return all_unique

def main():
    print("🌟 TinkyBink 100% Unique Response Creator")
    print("=" * 70)
    print("🎯 Creating completely unique responses for every scenario")
    print("💯 No duplicates, pure variety!")
    print()
    
    unique_responses = compile_all_unique_responses()
    
    print(f"\n🏆 SUCCESS!")
    print(f"✅ Created {len(unique_responses)} completely unique responses")
    print("🌟 Every single response is different!")
    print("🚀 Ready for diverse AAC training!")

if __name__ == "__main__":
    main()