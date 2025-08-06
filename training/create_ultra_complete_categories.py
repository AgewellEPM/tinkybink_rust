#!/usr/bin/env python3
"""
Create Ultra Complete AAC Categories
Add EVERY possible communication scenario
"""
import json

def create_ultra_complete_categories():
    """Create absolutely every AAC communication category possible"""
    
    print("🌟 TinkyBink Ultra Complete Categories Creator")
    print("=" * 70)
    print("🚀 Creating EVERY possible AAC communication scenario")
    print("💯 Achieving 100% complete coverage")
    print()
    
    all_new_examples = []
    
    # ADVANCED EMOTIONAL NUANCES (25 examples)
    emotional_examples = create_advanced_emotional_nuances()
    all_new_examples.extend(emotional_examples)
    print(f"✅ Advanced Emotional Nuances: {len(emotional_examples)} examples")
    
    # SENSORY & ACCESSIBILITY (20 examples)
    sensory_examples = create_sensory_accessibility()
    all_new_examples.extend(sensory_examples)
    print(f"✅ Sensory & Accessibility: {len(sensory_examples)} examples")
    
    # INTIMATE & PERSONAL CARE (18 examples)
    intimate_examples = create_intimate_personal_care()
    all_new_examples.extend(intimate_examples)
    print(f"✅ Intimate & Personal Care: {len(intimate_examples)} examples")
    
    # PHILOSOPHICAL & EXISTENTIAL (15 examples)
    philosophical_examples = create_philosophical_existential()
    all_new_examples.extend(philosophical_examples)
    print(f"✅ Philosophical & Existential: {len(philosophical_examples)} examples")
    
    # ADDICTION & RECOVERY (18 examples)
    addiction_examples = create_addiction_recovery()
    all_new_examples.extend(addiction_examples)
    print(f"✅ Addiction & Recovery: {len(addiction_examples)} examples")
    
    # MILITARY & VETERANS (12 examples)
    military_examples = create_military_veterans()
    all_new_examples.extend(military_examples)
    print(f"✅ Military & Veterans: {len(military_examples)} examples")
    
    # DISABILITY & ACCOMMODATION (20 examples)
    disability_examples = create_disability_accommodation()
    all_new_examples.extend(disability_examples)
    print(f"✅ Disability & Accommodation: {len(disability_examples)} examples")
    
    # GRIEF & LOSS (15 examples)
    grief_examples = create_grief_loss()
    all_new_examples.extend(grief_examples)
    print(f"✅ Grief & Loss: {len(grief_examples)} examples")
    
    # CREATIVITY & ARTISTIC (18 examples)
    creative_examples = create_creativity_artistic()
    all_new_examples.extend(creative_examples)
    print(f"✅ Creativity & Artistic: {len(creative_examples)} examples")
    
    # SCIENCE & DISCOVERY (12 examples)
    science_examples = create_science_discovery()
    all_new_examples.extend(science_examples)
    print(f"✅ Science & Discovery: {len(science_examples)} examples")
    
    # ENVIRONMENTAL & NATURE (15 examples)
    environmental_examples = create_environmental_nature()
    all_new_examples.extend(environmental_examples)
    print(f"✅ Environmental & Nature: {len(environmental_examples)} examples")
    
    # CELEBRATIONS & MILESTONES (20 examples)
    celebration_examples = create_celebrations_milestones()
    all_new_examples.extend(celebration_examples)
    print(f"✅ Celebrations & Milestones: {len(celebration_examples)} examples")
    
    # CONFLICT RESOLUTION (15 examples)
    conflict_examples = create_conflict_resolution()
    all_new_examples.extend(conflict_examples)
    print(f"✅ Conflict Resolution: {len(conflict_examples)} examples")
    
    # MEMORY & NOSTALGIA (12 examples)
    memory_examples = create_memory_nostalgia()
    all_new_examples.extend(memory_examples)
    print(f"✅ Memory & Nostalgia: {len(memory_examples)} examples")
    
    # PRODUCTIVITY & TIME MANAGEMENT (15 examples)
    productivity_examples = create_productivity_time()
    all_new_examples.extend(productivity_examples)
    print(f"✅ Productivity & Time Management: {len(productivity_examples)} examples")
    
    # VOLUNTEERING & SERVICE (12 examples)
    volunteer_examples = create_volunteering_service()
    all_new_examples.extend(volunteer_examples)
    print(f"✅ Volunteering & Service: {len(volunteer_examples)} examples")
    
    # AGING & ELDERLY CARE (18 examples)
    aging_examples = create_aging_elderly_care()
    all_new_examples.extend(aging_examples)
    print(f"✅ Aging & Elderly Care: {len(aging_examples)} examples")
    
    # CULTURAL EXCHANGE (15 examples)
    cultural_examples = create_cultural_exchange()
    all_new_examples.extend(cultural_examples)
    print(f"✅ Cultural Exchange: {len(cultural_examples)} examples")
    
    # PROFESSIONAL DEVELOPMENT (18 examples)
    professional_examples = create_professional_development()
    all_new_examples.extend(professional_examples)
    print(f"✅ Professional Development: {len(professional_examples)} examples")
    
    # EMERGENCY PREPAREDNESS (15 examples)
    emergency_examples = create_emergency_preparedness()
    all_new_examples.extend(emergency_examples)
    print(f"✅ Emergency Preparedness: {len(emergency_examples)} examples")
    
    # SEASONAL & WEATHER SPECIFIC (20 examples)
    seasonal_examples = create_seasonal_weather_specific()
    all_new_examples.extend(seasonal_examples)
    print(f"✅ Seasonal & Weather Specific: {len(seasonal_examples)} examples")
    
    # SOCIAL MEDIA & DIGITAL LIFE (18 examples)
    social_media_examples = create_social_media_digital()
    all_new_examples.extend(social_media_examples)
    print(f"✅ Social Media & Digital Life: {len(social_media_examples)} examples")
    
    # FEAR & PHOBIAS (12 examples)
    fear_examples = create_fear_phobias()
    all_new_examples.extend(fear_examples)
    print(f"✅ Fear & Phobias: {len(fear_examples)} examples")
    
    # MINDFULNESS & MEDITATION (15 examples)
    mindfulness_examples = create_mindfulness_meditation()
    all_new_examples.extend(mindfulness_examples)
    print(f"✅ Mindfulness & Meditation: {len(mindfulness_examples)} examples")
    
    # NUTRITION & COOKING (18 examples)
    nutrition_examples = create_nutrition_cooking()
    all_new_examples.extend(nutrition_examples)
    print(f"✅ Nutrition & Cooking: {len(nutrition_examples)} examples")
    
    total_new = len(all_new_examples)
    
    print(f"\n🎯 TOTAL ULTRA COMPLETE EXAMPLES: {total_new:,}")
    
    # Save ultra complete categories
    output_file = "tinkybink_ultra_complete_categories.jsonl"
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in all_new_examples:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')
    
    print(f"✅ Saved: {output_file}")
    print(f"🏆 AAC coverage now 100% COMPLETE!")
    
    return total_new

def create_advanced_emotional_nuances():
    """Advanced emotional nuance examples"""
    examples = []
    
    scenarios = [
        ("Feeling emotionally overwhelmed", "🌊 Emotions like tsunami, 🤯 Mind completely overloaded, 😵 Can't process everything, 🆘 Need emotional rescue", "emotional_nuances"),
        ("Experiencing bittersweet feelings", "😢 Happy and sad, 🎭 Mixed emotions swirling, 💭 Complex feelings inside, 🌗 Light and shadow", "emotional_nuances"),
        ("Feeling emotionally numb", "🧊 Nothing feels real, 😶 Emotions shut down, 🚫 Can't feel anything, 💤 Heart gone dormant", "emotional_nuances"),
        ("Experiencing imposter syndrome", "🎭 Feel like fraud, 😰 Don't deserve success, 🤔 Everyone will discover, 💭 Not good enough", "emotional_nuances"),
        ("Feeling emotionally drained", "🔋 Battery completely empty, 😴 Emotional exhaustion complete, 🏜️ Desert inside soul, 💧 Need emotional refill", "emotional_nuances"),
        ("Experiencing existential dread", "🌌 Universe feels meaningless, 😨 Fear of nothing, 💭 What's the point, 🕳️ Void staring back", "emotional_nuances"),
        ("Feeling emotionally triggered", "⚡ Past trauma activated, 🚨 Alarm bells ringing, 😰 Fight flight response, 🛡️ Need safety now", "emotional_nuances"),
        ("Experiencing emotional catharsis", "🌋 Release pressure building, 😭 Good cry needed, 💨 Let emotions flow, 🌅 Cleansing emotional storm", "emotional_nuances"),
        ("Feeling emotionally vulnerable", "🐚 Soft inside exposed, 😢 Heart on sleeve, 🤲 Open to hurt, 💕 Brave enough anyway", "emotional_nuances"),
        ("Experiencing emotional breakthrough", "💡 Sudden clarity moment, 🌅 Dawn after darkness, 🔓 Locked door opens, 🦋 Transformation beginning", "emotional_nuances"),
        ("Feeling emotionally guarded", "🏰 Walls built high, 🛡️ Heart under protection, 🚪 Keep others out, 🔒 Safe but lonely", "emotional_nuances"),
        ("Experiencing emotional whiplash", "🎢 Up down rapidly, 😵 Can't keep up, 🌪️ Emotional tornado inside, 🤹 Juggling too many", "emotional_nuances"),
        ("Feeling emotionally raw", "🩹 Wounds still bleeding, 😖 Everything hurts more, 👶 Like newborn sensitive, 🌡️ Temperature too high", "emotional_nuances"),
        ("Experiencing emotional resilience", "🌱 Bend don't break, 💪 Stronger than before, 🌅 Rise after fall, 🏔️ Mountain inside soul", "emotional_nuances"),
        ("Feeling emotionally conflicted", "⚖️ Heart mind battle, 🤔 Don't know right, 🌀 Spinning in circles, 🎭 Want opposite things", "emotional_nuances"),
        ("Experiencing emotional liberation", "🕊️ Caged bird flying, 🔓 Chains finally broken, 🌈 Colors vivid again, 💨 Breathing freely now", "emotional_nuances"),
        ("Feeling emotionally suffocated", "🫁 Can't breathe properly, 😰 Walls closing in, 🌊 Drowning in feelings, 🆘 Need space air", "emotional_nuances"),
        ("Experiencing emotional clarity", "🔍 Finally see clearly, 💡 Light bulb moment, 🧩 Pieces fit together, 🎯 Know what want", "emotional_nuances"),
        ("Feeling emotionally isolated", "🏝️ Alone on island, 📞 No one understands, 🌌 Space between us, 🤝 Need human connection", "emotional_nuances"),
        ("Experiencing emotional integration", "🧩 All parts together, ⚖️ Balance finally found, 🌈 Harmony inside soul, 🎼 Orchestra playing beautifully", "emotional_nuances"),
        ("Feeling emotionally frozen", "🧊 Heart turned ice, 😶 Can't express anything, 🚫 Emotions locked away, 🔥 Need warmth thaw", "emotional_nuances"),
        ("Experiencing emotional awakening", "👁️ Eyes opening wide, 🌅 Dawn consciousness rising, 💡 Awareness flooding in, 🦋 Metamorphosis beginning now", "emotional_nuances"),
        ("Feeling emotionally hypersensitive", "🎚️ Volume turned maximum, 😖 Everything hurts more, 🌊 Waves crashing harder, 🛡️ Need gentle protection", "emotional_nuances"),
        ("Experiencing emotional equilibrium", "⚖️ Perfect balance achieved, 🌊 Calm waters finally, 🧘 Inner peace found, 🏠 Home inside self", "emotional_nuances"),
        ("Feeling emotionally transcendent", "🌌 Beyond earthly concerns, 🕊️ Spirit soaring high, ✨ Connected to everything, 🙏 Blessed peaceful state", "emotional_nuances")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I feel {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Advanced Emotional Nuances",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_sensory_accessibility():
    """Sensory and accessibility examples"""
    examples = []
    
    scenarios = [
        ("Sound is too loud", "🔊 Volume hurts ears, 🎧 Need headphones protection, 🤫 Quiet space please, 🔇 Turn it down", "sensory"),
        ("Light is too bright", "💡 Eyes hurt pain, 🕶️ Need sunglasses now, 🌑 Dim lights please, 🏠 Dark room better", "sensory"),
        ("Texture feels uncomfortable", "🤢 Makes skin crawl, 🧤 Need gloves wear, 🚫 Can't touch that, 🛁 Wash hands now", "sensory"),
        ("Need visual accommodations", "👓 Larger text please, 🔍 Magnification helps me, 🌈 High contrast better, 📱 Screen reader use", "sensory"),
        ("Hearing accommodations needed", "👂 Sign language prefer, 📝 Write it down, 🔊 Speak louder please, 👥 Face me talk", "sensory"),
        ("Motor accessibility needs", "♿ Wheelchair accessible entrance, 🚪 Automatic doors help, 🛗 Elevator not stairs, 🤝 Physical assistance please", "sensory"),
        ("Cognitive processing time", "⏰ Need more time, 🧠 Processing information slowly, 📋 Step by step, 🔄 Repeat that please", "sensory"),
        ("Overstimulation happening", "🌪️ Too much input, 🚪 Need quiet space, 😵 Brain shutting down, 🛡️ Sensory break needed", "sensory"),
        ("Sensory seeking behavior", "🤗 Need pressure hugs, 🎵 Music helps calm, 🌊 Rocking motion soothes, 🧸 Fidget toy helps", "sensory"),
        ("Communication device needed", "📱 Speech generating device, 🖼️ Picture symbols help, 👆 Touch screen easier, 🔊 Voice output clear", "sensory"),
        ("Environmental modifications", "🏠 Remove distracting noise, 💡 Soft lighting better, 🪑 Comfortable seating needed, 🌿 Calm space create", "sensory"),
        ("Sensory diet planning", "🏃 Movement breaks needed, 🤗 Deep pressure activities, 🧘 Calming sensory input, ⏰ Regular sensory schedule", "sensory"),
        ("Assistive technology", "💻 Computer voice control, 🖱️ Special mouse trackball, ⌨️ Keyboard with guards, 📱 Accessibility apps help", "sensory"),
        ("Sensory preferences", "🌊 Blue calming color, 🎵 Classical music soothes, 🧸 Soft textures preferred, ☀️ Natural light best", "sensory"),
        ("Accommodations workplace", "🏢 Quiet workspace needed, 💡 Adjustable lighting controls, 🪑 Ergonomic chair required, ⏰ Flexible break schedule", "sensory"),
        ("Sensory meltdown prevention", "⚠️ Warning signs appearing, 🚪 Exit strategy ready, 🧘 Breathing techniques use, 🤝 Support person call", "sensory"),
        ("Adaptive equipment", "🍴 Special utensils needed, 👕 Clothing tag removal, 🛏️ Weighted blanket helps, 🎧 Noise canceling headphones", "sensory"),
        ("Sensory integration therapy", "🤸 Occupational therapy helps, 🎯 Sensory goals working, 🏃 Movement activities daily, 📊 Progress tracking important", "sensory"),
        ("Communication backup plans", "📝 Writing as backup, 🖼️ Pictures show meaning, 👥 Interpreter available sometimes, 📱 Text to speech", "sensory"),
        ("Sensory friendly environments", "🏪 Sensory friendly shopping, 🎭 Quiet theater times, 🏥 Medical sensory accommodations, 🎪 Sensory friendly events", "sensory")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Sensory Accessibility",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_intimate_personal_care():
    """Intimate and personal care examples"""
    examples = []
    
    scenarios = [
        ("Need help with personal hygiene", "🛁 Bathing assistance needed, 🦷 Teeth brushing help, 💇 Hair washing support, 👔 Dressing assistance please", "personal_care"),
        ("Bathroom privacy concerns", "🚪 Need privacy please, 🔒 Lock the door, ⏰ Take my time, 🤝 Call when done", "personal_care"),
        ("Personal boundaries", "🛑 That's too close, 🤝 Ask permission first, 🚫 Don't touch there, ✋ Personal space please", "personal_care"),
        ("Intimate relationship communication", "💕 Need more affection, 💬 Talk about intimacy, ⏰ Not tonight please, 🤗 Just cuddling tonight", "personal_care"),
        ("Menstrual care needs", "🩸 Period pain today, 🧻 Need feminine products, 🛁 Hot bath helps, 💊 Pain medication please", "personal_care"),
        ("Body image concerns", "😔 Don't like body, 🪞 Mirror makes sad, 👕 Clothes don't fit, 💪 Want feel better", "personal_care"),
        ("Medical examination anxiety", "😰 Nervous about exam, 🩺 Doctor gentle please, 🤝 Support person stay, 📋 Explain what doing", "personal_care"),
        ("Sexual health discussion", "🩺 Need sexual health, 📋 STD testing please, 💊 Birth control options, 💬 Safe sex education", "personal_care"),
        ("Changing assistance", "👶 Diaper change needed, 👔 Help changing clothes, 🛏️ Bed linens dirty, 🧼 Clean up please", "personal_care"),
        ("Personal grooming", "💅 Nail care needed, 🪒 Shaving help please, 💄 Makeup assistance wanted, 👂 Ear cleaning needed", "personal_care"),
        ("Physical discomfort", "😣 Body aches everywhere, 🔥 Burning sensation here, 🧊 Ice pack needed, 💊 Pain relief please", "personal_care"),
        ("Dignity preservation", "🙏 Treat with respect, 👔 Cover me up, 🤫 Keep this private, 💪 Still have dignity", "personal_care"),
        ("Personal care routine", "🕐 Morning routine time, 🛁 Evening bath ready, ⏰ Medication schedule now, 🛏️ Bedtime routine start", "personal_care"),
        ("Assistance with mobility", "🚶 Help walking please, 🪑 Transfer to chair, 🛏️ Help getting up, ♿ Wheelchair position correctly", "personal_care"),
        ("Emotional support during care", "🤝 Stay with me, 💬 Talk while helping, 😊 Be gentle kind, 🙏 Thank you caring", "personal_care"),
        ("Medical device management", "📱 Check blood sugar, 💊 Insulin injection time, 🫁 Inhaler assistance needed, 🔋 Device battery low", "personal_care"),
        ("Skin care needs", "🧴 Lotion dry skin, ☀️ Sunscreen application please, 🩹 Wound care needed, 🛁 Gentle soap use", "personal_care"),
        ("Adaptive clothing", "👕 Easy on clothing, 🔘 Velcro instead buttons, 👟 Slip on shoes, 🧥 Jacket with zipper", "personal_care")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Personal Care",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_philosophical_existential():
    """Philosophical and existential examples"""
    examples = []
    
    scenarios = [
        ("What is the meaning of life?", "🌟 Find personal purpose, 💕 Love and connection, 🎯 Make positive impact, 🙏 Spiritual growth journey", "philosophical"),
        ("Contemplating mortality", "⏳ Life is precious, 🌅 Each day gift, 💭 Legacy I leave, 🕊️ Peace with death", "philosophical"),
        ("Free will vs destiny", "🎯 Choices shape future, 🌊 Go with flow, ⚖️ Balance control surrender, 🤔 Mystery of existence", "philosophical"),
        ("Nature of consciousness", "🧠 Mind creates reality, 👁️ Awareness watching thoughts, 🌌 Part of universe, 💭 Who am really", "philosophical"),
        ("Suffering and growth", "🌱 Pain teaches lessons, 💪 Struggle builds strength, 🌅 Dawn after darkness, 🦋 Transform through trials", "philosophical"),
        ("The concept of time", "⏰ Present moment only, 🔄 Cycles repeat patterns, 🌊 Time flows river, 💫 Eternity in now", "philosophical"),
        ("Truth and reality", "🔍 Seeking deeper truth, 🎭 Reality subjective experience, 🌈 Multiple perspectives valid, 💎 Core truth exists", "philosophical"),
        ("Purpose and fulfillment", "🎯 Living with intention, 🌟 Following inner calling, 💼 Work meaningful contribution, 🏔️ Climbing personal mountain", "philosophical"),
        ("Good and evil", "⚖️ Moral compass guides, 💡 Choose light darkness, 🤝 Compassion over hatred, 🌱 Good grows good", "philosophical"),
        ("Identity and self", "🪞 Who am really, 🎭 Roles I play, 💎 Essence beyond labels, 🌊 Changing yet constant", "philosophical"),
        ("Love and connection", "💕 Love transcends everything, 🌐 All beings connected, 🤝 Relationships define us, 💫 Unity in diversity", "philosophical"),
        ("Knowledge and wisdom", "📚 Learning never ends, 🧠 Experience teaches most, 🙏 Humility before mystery, 🌟 Wisdom beyond knowledge", "philosophical"),
        ("Hope and despair", "🌅 Hope conquers darkness, 💪 Resilience through trials, 🌱 Growth from struggle, 🕊️ Peace after storm", "philosophical"),
        ("Art and beauty", "🎨 Beauty feeds soul, 🌸 Art expresses inexpressible, 🎵 Music universal language, ✨ Creating meaning together", "philosophical"),
        ("Solitude and community", "🧘 Alone with thoughts, 👥 Need human connection, ⚖️ Balance solitude society, 🏝️ Island connected ocean", "philosophical")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I believe {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Philosophical Existential",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with remaining categories in similar format...

def create_addiction_recovery():
    examples = []
    scenarios = [
        ("Craving substance right now", "🆘 Call sponsor immediately, 🏃 Leave this place, 👥 Go to meeting, 💪 This will pass", "addiction"),
        ("Relapse happened yesterday", "💔 Disappointed in myself, 📞 Tell sponsor truth, 🔄 Start over again, 🤝 Need support now", "addiction"),
        ("One year sober today", "🎉 Celebrate milestone achievement, 🙏 Grateful for support, 💪 Stronger than before, 🌟 Hope for others", "addiction"),
        ("Tempting situation ahead", "🚫 Avoid trigger places, 🤝 Bring sober friend, 📞 Exit strategy ready, 🧘 Use coping skills", "addiction"),
        ("Recovery meeting tonight", "👥 Share my story, 👂 Listen to others, 🤝 Fellowship strengthens me, 📚 Work the steps", "addiction"),
        ("Family trust broken", "💔 Hurt people deeply, ⏰ Trust takes time, 🔧 Actions rebuild relationships, 🙏 Ask for forgiveness", "addiction"),
        ("Withdrawal symptoms", "😰 Body feels terrible, 🏥 Medical supervision needed, 💊 Safe detox important, ⏰ This is temporary", "addiction"),
        ("Sober living challenges", "🏠 New way living, 😰 Everything feels different, 📚 Learning life skills, 🌱 Growing every day", "addiction"),
        ("Sponsorship relationship", "🤝 Guide through recovery, 📞 Available when struggling, 📚 Teach the steps, 🌟 Hope through example", "addiction"),
        ("Recovery program choice", "👥 12 step program, 🧠 SMART recovery approach, 🏥 Medical assisted treatment, 🤝 Multiple paths work", "addiction"),
        ("Amends process", "🙏 Apologize for harm, 💰 Make financial amends, 🔧 Change harmful behavior, ❤️ Heal relationships possible", "addiction"),
        ("Sober socializing", "🎉 Fun without substances, 👥 Sober friends important, 🏃 New activities discover, ☕ Coffee shop meetings", "addiction"),
        ("Addiction understanding", "🧠 Disease not choice, 💊 Chemical brain changes, 🤝 Treatment not punishment, 🌟 Recovery is possible", "addiction"),
        ("Relapse prevention plan", "⚠️ Know my triggers, 🆘 Emergency contact list, 🧘 Healthy coping strategies, 📅 Daily routine structure", "addiction"),
        ("Supporting loved one", "🤝 Love without enabling, 🚫 Set healthy boundaries, 👥 Al-Anon family support, 🙏 Let go control", "addiction"),
        ("Recovery anniversary", "📅 Mark sobriety date, 🎁 Reward myself healthy, 📸 Remember how far, 🌟 Inspire others struggling", "addiction"),
        ("Medication assisted treatment", "💊 Methadone clinic daily, 💊 Suboxone prescription helps, 🩺 Doctor monitors progress, 🤝 Combined with counseling", "addiction"),
        ("Dealing with shame", "💔 Shame keeps sick, 🌟 Separate actions identity, 🤝 Share in meetings, 🙏 Self forgiveness important", "addiction")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In recovery I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Addiction Recovery",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# I'll create more efficient versions of the remaining categories to save space...

def create_military_veterans():
    examples = []
    scenarios = [
        ("PTSD flashback happening", "🆘 Grounding techniques now, 🤝 Safe person call, 🏥 VA crisis line, 💊 Medication if needed", "military"),
        ("Veteran benefits questions", "🏛️ VA office visit, 📋 Disability claim file, 💰 GI Bill education, 🏥 Healthcare enrollment", "military"),
        ("Military transition civilian", "💼 Job skills translate, 🎓 Education benefits use, 🤝 Veteran support groups, 🏠 Housing assistance available", "military"),
        ("Combat memories haunting", "🧠 Therapy helps process, 👥 Veteran group understands, 🏃 Physical exercise releases, 🎯 Focus on present", "military"),
        ("Survivor guilt feeling", "💔 Why did survive, 🤝 Honor fallen comrades, 🌟 Live worthy life, 🙏 Their sacrifice matters", "military"),
        ("Military spouse challenges", "🏠 Frequent moves difficult, 👶 Single parenting deployments, 💼 Career sacrifices made, 🤝 Spouse support groups", "military"),
        ("Deployment preparation", "👨‍👩‍👧‍👦 Family goodbyes hard, 📋 Affairs in order, 💪 Mental preparation needed, 📞 Communication plan set", "military"),
        ("Coming home adjustment", "🏠 Home feels different, 👥 Family changed too, ⏰ Need readjustment time, 🤝 Patience from everyone", "military"),
        ("Military pride", "🇺🇸 Served country proudly, 🎖️ Honor in service, 🤝 Brotherhood bonds strong, 🌟 Values guide life", "military"),
        ("Veteran healthcare", "🏥 VA medical care, 🧠 Mental health services, 💊 Prescription benefits available, 🤝 Peer support programs", "military"),
        ("Military funeral", "🎖️ Honor guard ceremony, 🇺🇸 Flag folded family, 🎺 Taps played final, 🙏 Service remembered always", "military"),
        ("Veteran community", "👥 Brothers sisters understand, 🤝 Help fellow veterans, 🏛️ Advocate for services, 🌟 Legacy of service", "military")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"As a veteran, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Military Veterans",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with remaining categories... I'll create them efficiently
def create_disability_accommodation():
    examples = []
    scenarios = [
        ("Disability accommodation workplace", "♿ Reasonable accommodations law, 🏢 Accessible workspace needed, ⏰ Flexible schedule request, 🤝 Equal opportunity employment", "disability"),
        ("Public accessibility issues", "🚪 Ramp access needed, 🚌 Bus wheelchair lift, 🅿️ Accessible parking spaces, 🔊 Audio announcements helpful", "disability"),
        ("Disability benefits application", "📋 Social Security disability, 🏥 Medical documentation required, ⏰ Long process wait, 🤝 Advocate assistance helpful", "disability"),
        ("Independent living goals", "🏠 Live on own, 🚗 Transportation independence needed, 💰 Financial management skills, 🤝 Support services available", "disability"),
        ("Assistive technology needs", "💻 Screen reader software, 🖱️ Voice recognition programs, 📱 Communication apps helpful, 🦽 Mobility equipment updated", "disability"),
        ("Disability pride", "💪 Proud of identity, 🌈 Disability community strong, 🚫 Not inspiration porn, ✊ Rights advocate always", "disability"),
        ("Medical appointments", "🏥 Specialist consultation today, 💊 Medication adjustment needed, 🩺 Physical therapy session, 📋 Insurance pre authorization", "disability"),
        ("Accessible travel", "✈️ Airport assistance request, 🏨 Hotel accessibility features, 🚗 Rental car modifications, 🗺️ Accessible route planning", "disability"),
        ("Disability discrimination", "⚖️ File ADA complaint, 🤝 Disability rights advocate, 📋 Document discrimination incidents, 💪 Stand up rights", "disability"),
        ("Caregiver support", "🤝 Personal care assistant, 👨‍👩‍👧‍👦 Family caregiver support, ⏰ Respite care needed, 💰 Funding assistance programs", "disability"),
        ("Adaptive sports", "🏀 Wheelchair basketball team, 🏊 Paralympic swimming goals, 🎾 Adaptive tennis lessons, 🏃 Racing wheelchair training", "disability"),
        ("Disability education", "📚 Special education services, 🎓 College disability office, 📝 Testing accommodations needed, 🤝 Academic support available", "disability"),
        ("Employment challenges", "💼 Job interview accommodations, 🏢 Workplace accessibility audit, 💰 Vocational rehabilitation services, 🎯 Career development planning", "disability"),
        ("Health insurance", "📋 Coverage for equipment, 💊 Prescription medication costs, 🏥 Specialist copays high, 🤝 Insurance advocate help", "disability"),
        ("Social barriers", "👥 Attitudinal barriers common, 🗣️ Self advocacy important, 📚 Disability awareness education, 🌉 Bridge understanding gaps", "disability"),
        ("Transportation challenges", "🚌 Public transit accessibility, 🚗 Paratransit service application, 🚕 Accessible taxi options, 🚶 Sidewalk barriers exist", "disability"),
        ("Recreation access", "🎬 Movie theater accessibility, 🏊 Pool lift needed, 🎭 Theater accommodations available, 🏃 Accessible trails maps", "disability"),
        ("Emergency preparedness", "🚨 Evacuation plan needed, 📋 Medical information accessible, 🔋 Backup power equipment, 🤝 Emergency contact network", "disability"),
        ("Technology barriers", "💻 Website not accessible, 📱 App compatibility issues, 🔊 Audio descriptions missing, ⌨️ Keyboard navigation broken", "disability"),
        ("Community integration", "🏠 Neighborhood accessibility survey, 👥 Inclusive community events, 🛒 Accessible business directory, 🤝 Disability mentorship programs", "disability")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"For disability access, I need {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Disability Accommodation",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create remaining categories efficiently...
def create_grief_loss():
    examples = []
    scenarios = [
        ("Just lost loved one", "💔 Heart completely broken, 😭 Tears won't stop, 🤝 Need support now, 🙏 Memories give comfort", "grief"),
        ("Funeral planning", "⚰️ Burial or cremation, 🌹 Flowers for service, 📋 Obituary write together, 💰 Funeral costs overwhelming", "grief"),
        ("Grief comes waves", "🌊 Overwhelming sadness hits, 😢 Unexpected crying spells, 💪 Getting stronger slowly, ⏰ Healing takes time", "grief"),
        ("Missing them today", "📸 Looking at photos, 🎵 Their favorite song, 📞 Wish could call, 💕 Love never dies", "grief"),
        ("Anniversary of death", "📅 Hard day remember, 🕯️ Light candle memory, 🌹 Visit grave today, 💭 Share favorite stories", "grief"),
        ("Guilt about moving on", "😔 Feel guilty laughing, 💭 Would they approve, 🌱 Life must continue, 💕 Honor by living", "grief"),
        ("Supporting grieving friend", "🤝 Just be present, 👂 Listen without fixing, 🍲 Bring food comfort, 📞 Check in regularly", "grief"),
        ("Grief counseling", "🤝 Therapist helps process, 👥 Grief support group, 📚 Books about loss, 🧘 Meditation for peace", "grief"),
        ("Pet loss grief", "🐕 Beloved pet died, 💔 Grief is real, 📸 Remember good times, 🌈 Rainbow bridge waiting", "grief"),
        ("Complicated grief", "💔 Can't move forward, 😵 Stuck in pain, 🤝 Professional help needed, 💊 Medication might help", "grief"),
        ("Sudden unexpected loss", "⚡ Shock and disbelief, 🤯 Can't process reality, 🆘 Crisis support needed, 👥 Family gathering together", "grief"),
        ("Anticipatory grief", "😰 Watching them decline, 💔 Grieving while alive, ⏰ Precious time together, 🙏 Preparing for goodbye", "grief"),
        ("Children's grief", "👶 Kids grieve differently, 🎨 Art therapy helps, 📚 Age appropriate explanations, 🤝 Extra support needed", "grief"),
        ("Holiday grief", "🎄 First holiday without, 💔 Empty chair hurts, 🕯️ Special memorial ritual, 👥 Different traditions maybe", "grief"),
        ("Creating memorial", "📸 Photo memory book, 🌳 Plant memorial tree, 💰 Charity donation honor, 🎵 Memorial service music", "grief")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In grief, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Grief Loss",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# I'll continue with the remaining categories using similar efficient structures...

def create_creativity_artistic():
    examples = []
    scenarios = [
        ("Artistic inspiration today", "🎨 Colors calling me, 🖌️ Paint brush ready, 💡 Creative vision clear, ✨ Magic in making", "creativity"),
        ("Creative block frustration", "🧱 Ideas won't come, 😤 Frustrated with work, 🚶 Walk for inspiration, ⏰ Take creative break", "creativity"),
        ("Sharing artistic work", "🖼️ Ready show piece, 😰 Nervous about reception, 🤝 Feedback helps grow, 🌟 Art speaks itself", "creativity"),
        ("Learning new technique", "📚 Tutorial videos helpful, 🤝 Teacher guidance needed, 🎯 Practice makes better, 💪 Challenge myself more", "creativity"),
        ("Art supply shopping", "🛒 Need new brushes, 💰 Budget for supplies, 🎨 Quality materials matter, ♻️ Reuse what have", "creativity"),
        ("Creative collaboration", "👥 Working with others, 💡 Ideas build together, 🤝 Different perspectives valuable, 🎭 Theater group project", "creativity"),
        ("Art gallery visit", "🖼️ Inspiration from masters, 📸 Take reference photos, 💭 Analyze techniques used, 🎫 Opening reception tonight", "creativity"),
        ("Digital art creation", "💻 Software learning curve, 🖱️ Digital brush control, 📱 Tablet makes easier, ☁️ Cloud storage backup", "creativity"),
        ("Performance anxiety", "🎭 Stage fright normal, 🫁 Breathing exercises help, 🎯 Focus on art, 👥 Audience wants success", "creativity"),
        ("Creative career", "💼 Art as profession, 💰 Financial stability challenging, 🌟 Following artistic passion, 📈 Building client base", "creativity"),
        ("Artistic community", "👥 Fellow artists understand, 🤝 Mutual support important, 📢 Promote each other, 🏠 Studio space sharing", "creativity"),
        ("Creative process", "💭 Ideas come randomly, 📝 Sketch first thoughts, 🔄 Revise and refine, ✨ Magic in process", "creativity"),
        ("Art criticism", "📝 Constructive feedback valuable, 😔 Harsh criticism hurts, 💪 Thick skin needed, 🎯 Focus on growth", "creativity"),
        ("Artistic expression", "💭 Art shows feelings, 🗣️ Voice through creation, 🌈 Colors express emotions, 🎵 Music tells stories", "creativity"),
        ("Creative workspace", "🏠 Studio setup important, 💡 Good lighting essential, 🧹 Organization helps flow, 🎵 Music sets mood", "creativity"),
        ("Selling artwork", "💰 Price work fairly, 🛒 Online marketplace options, 🖼️ Gallery representation goal, 🤝 Commission work available", "creativity"),
        ("Artistic legacy", "📸 Document creative journey, 📚 Teach others skills, 🎁 Art as gifts, 🌟 Leave creative mark", "creativity"),
        ("Creative burnout", "😴 Exhausted from creating, 🌱 Need creative rest, 🚶 Nature walks restore, 💡 Inspiration will return", "creativity")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In my art, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Creativity Artistic",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with remaining categories efficiently...

def create_science_discovery():
    examples = []
    scenarios = [
        ("Scientific experiment", "🔬 Lab results exciting, 📊 Data shows pattern, 🧪 Chemical reaction unexpected, 📋 Record observations carefully", "science"),
        ("Research breakthrough", "💡 Discovery changes everything, 📚 Literature review complete, 🎯 Hypothesis proven correct, 🌟 Nobel prize worthy", "science"),
        ("Technology advancement", "🤖 AI learning faster, 🚀 Space exploration amazing, 💻 Quantum computing breakthrough, 🧬 Gene therapy promising", "science"),
        ("Environmental science", "🌍 Climate change urgent, 🌱 Renewable energy solutions, 🔄 Carbon cycle disrupted, 🦋 Biodiversity loss critical", "science"),
        ("Medical research", "💊 New drug trials, 🧬 Genetic mapping progress, 🩺 Disease mechanism understood, 🔬 Microscopic world fascinating", "science"),
        ("Space exploration", "🚀 Mars mission planned, 🌌 Galaxy formation studied, 👽 Search for life, 🛰️ Satellite data collection", "science"),
        ("Scientific method", "❓ Question everything always, 🧪 Experiment tests hypothesis, 📊 Data analysis reveals, 🔄 Peer review process", "science"),
        ("Physics discoveries", "⚛️ Particle accelerator results, 🌊 Wave particle duality, 🕳️ Black hole imaged, 💫 Quantum entanglement proven", "science"),
        ("Biology research", "🧬 DNA sequencing complete, 🦠 Microbiome affects health, 🌱 Plant genetics studied, 🐛 Evolution evidence found", "science"),
        ("Chemistry applications", "⚗️ New compound synthesized, 💊 Drug delivery improved, 🔋 Battery technology advanced, 🧪 Catalyst efficiency increased", "science"),
        ("Scientific collaboration", "👥 International research team, 💻 Data sharing platforms, 📞 Virtual conferences important, 🤝 Peer review network", "science"),
        ("Science education", "📚 STEM programs essential, 🔬 Lab safety training, 👩‍🔬 Women in science, 🎓 Graduate research focus", "science")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In science, I find {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Science Discovery",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with the remaining categories in similar efficient format...

def create_environmental_nature():
    examples = []
    scenarios = [
        ("Nature connection", "🌳 Trees calm soul, 🌊 Ocean waves soothe, 🏔️ Mountains inspire awe, 🌸 Flowers bring joy", "environmental"),
        ("Climate action", "♻️ Reduce reuse recycle, 🌱 Plant trees today, 🚗 Walk bike more, 💡 Energy conservation important", "environmental"),
        ("Wildlife conservation", "🐻 Protect endangered species, 🌍 Habitat preservation critical, 🦋 Pollinator gardens help, 📸 Wildlife photography respectful", "environmental"),
        ("Sustainable living", "🌱 Organic food choices, 🏠 Solar panels installed, 💧 Water conservation daily, 🚲 Bike commute option", "environmental"),
        ("Outdoor activities", "🥾 Hiking trail today, 🎣 Fishing peaceful activity, 🏕️ Camping under stars, 🚣 Kayaking river adventure", "environmental"),
        ("Weather patterns", "🌪️ Storms more intense, ☀️ Heat waves increasing, 🌨️ Snow patterns changing, 🌊 Sea levels rising", "environmental"),
        ("Gardening passion", "🌱 Seeds sprouting life, 🥕 Vegetables growing well, 🌺 Flowers attract bees, 🍃 Compost enriches soil", "environmental"),
        ("Pollution concerns", "🏭 Air quality poor, 🌊 Water contamination danger, 🗑️ Plastic waste everywhere, 🚗 Traffic emissions high", "environmental"),
        ("National parks", "🏞️ Natural beauty preserved, 🥾 Hiking trails maintained, 📸 Photography opportunities abundant, 🦅 Wildlife viewing spectacular", "environmental"),
        ("Environmental education", "📚 Learn about ecosystems, 👶 Teach children nature, 🔬 Citizen science projects, 📊 Climate data tracking", "environmental"),
        ("Green technology", "🔋 Battery storage advancing, 🌊 Tidal energy potential, ☀️ Solar efficiency improving, 💨 Wind power expanding", "environmental"),
        ("Seasonal changes", "🍂 Fall colors beautiful, ❄️ Winter quiet contemplation, 🌸 Spring renewal energy, ☀️ Summer growth abundance", "environmental"),
        ("Nature therapy", "🌳 Forest bathing healing, 🌊 Beach walks meditative, 🏔️ Mountain air purifying, 🌙 Night sky inspiring", "environmental"),
        ("Environmental activism", "📢 Speak for voiceless, 🗳️ Vote environmental candidates, 💰 Support green organizations, 🤝 Community action groups", "environmental"),
        ("Biodiversity appreciation", "🦋 Species interconnected web, 🌺 Native plants important, 🐝 Bees essential pollinators, 🌍 Ecosystems delicate balance", "environmental")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"With nature, I feel {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Environmental Nature",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# I'll create the remaining categories efficiently to complete the ultra-comprehensive dataset...

def create_celebrations_milestones():
    examples = []
    scenarios = [
        ("Birthday milestone", "🎂 Another year wiser, 🎉 Celebrate life achievements, 🎁 Gifts from heart, 🤗 Surrounded by love", "celebrations"),
        ("Wedding anniversary", "💍 Years together strong, 💕 Love grown deeper, 📸 Memories we've made, 🥂 Toast to future", "celebrations"),
        ("Graduation achievement", "🎓 Hard work paid, 📚 Knowledge gained valuable, 🌟 Future looks bright, 👨‍👩‍👧‍👦 Family so proud", "celebrations"),
        ("New baby arrival", "👶 Bundle of joy, 💕 Love instantly overwhelming, 😴 Sleep becomes rare, 🍼 New parent challenges", "celebrations"),
        ("Retirement celebration", "🏆 Career well done, ⏰ Time for hobbies, 🌅 New chapter begins, 💰 Financial security important", "celebrations"),
        ("Achievement recognition", "🏆 Award well deserved, 💪 Hard work recognized, 🌟 Moment to shine, 🙏 Grateful for opportunity", "celebrations"),
        ("Religious milestone", "🙏 Confirmation ceremony today, 📖 Spiritual growth important, 👥 Community celebration together, ✨ Faith journey continues", "celebrations"),
        ("Cultural celebration", "🎭 Heritage traditions honored, 🍽️ Traditional foods shared, 👥 Community gathers together, 🎵 Music and dancing", "celebrations"),
        ("Personal breakthrough", "💪 Overcame major obstacle, 🌅 New perspective gained, 🦋 Transformation complete now, 🎯 Goal finally achieved", "celebrations"),
        ("Sobriety milestone", "🏆 One year clean, 💪 Strength found within, 🤝 Support system strong, 🌟 Life has meaning", "celebrations"),
        ("Health recovery", "🏥 Beat the illness, 💪 Body healing well, 🙏 Grateful for life, 👨‍⚕️ Medical team amazing", "celebrations"),
        ("New home", "🏠 Keys in hand, 📦 Moving day chaos, 🎉 Housewarming party planned, 🌱 New memories start", "celebrations"),
        ("Career promotion", "💼 Hard work recognized, 💰 Financial improvement welcome, 📈 New responsibilities exciting, 🎯 Career goals advancing", "celebrations"),
        ("Anniversary of loss", "🕯️ Remembering with love, 💔 Grief still present, 📸 Celebrating their life, 💕 Love never dies", "celebrations"),
        ("Holiday traditions", "🎄 Christmas morning magic, 🦃 Thanksgiving gratitude gathering, 🎆 New Year resolutions, 🎃 Halloween costume fun", "celebrations"),
        ("Sports victory", "🏆 Team won championship, 🎉 Celebrate hard work, 👥 Teammates became family, 🥇 Victory tastes sweet", "celebrations"),
        ("Artistic achievement", "🎨 Artwork displayed publicly, 🌟 Creative vision realized, 👏 Audience appreciation felt, 💫 Artistic dream fulfilled", "celebrations"),
        ("Learning milestone", "📚 Degree finally earned, 🧠 Knowledge expanded greatly, 🎯 Educational goal achieved, 🚀 Future opportunities opened", "celebrations"),
        ("Volunteer recognition", "🤝 Service to others, 💕 Community impact made, 🏆 Volunteer award received, 🌟 Making difference matters", "celebrations"),
        ("Technology achievement", "💻 App launched successfully, 🚀 Innovation brought life, 🎯 Problem solving successful, 🌟 Technology helps people", "celebrations")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I celebrate {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Celebrations Milestones",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Final categories for completeness...

def create_conflict_resolution():
    examples = []
    scenarios = [
        ("Disagreement with partner", "💬 Talk it through, 👂 Listen their perspective, 🤝 Find common ground, 💕 Love conquers all", "conflict"),
        ("Workplace tension", "💼 Professional approach needed, 📝 Document incidents clearly, 🤝 Mediation might help, 💪 Stay calm professional", "conflict"),
        ("Family argument", "👨‍👩‍👧‍👦 Family bonds strong, ⏰ Cooling off period, 🤗 Forgiveness heals wounds, 💕 Love remains constant", "conflict"),
        ("Neighbor dispute", "🏠 Property line issues, 💬 Direct conversation first, 📋 HOA involvement maybe, ⚖️ Legal advice last", "conflict"),
        ("Online disagreement", "📱 Internet arguments pointless, 🚫 Block toxic users, 💻 Log off walk, 🧘 Don't take bait", "conflict"),
        ("Apologizing sincerely", "🙏 Sorry for hurt, 💔 Take full responsibility, 🔧 Make amends possible, ⏰ Change behavior going", "conflict"),
        ("Setting boundaries", "🛑 This crosses line, 💪 Stand up yourself, 🗣️ Communicate limits clearly, 🔒 Protect your energy", "conflict"),
        ("De-escalating tension", "🕊️ Peace over winning, 🫁 Breathe before responding, 👂 Validate their feelings, 🤝 Find win win", "conflict"),
        ("Forgiveness process", "💕 Let go anger, 🌱 Growth from pain, 🕊️ Peace in forgiveness, ⏰ Time heals wounds", "conflict"),
        ("Mediation session", "🤝 Neutral third party, 📋 Rules for discussion, 🎯 Focus on solutions, 💬 Both sides heard", "conflict"),
        ("Avoiding conflict", "🚶 Walk away now, 🤐 Choose battles wisely, 🧘 Inner peace priority, 🕊️ Harmony over discord", "conflict"),
        ("Compromise solution", "⚖️ Both give little, 🤝 Meet in middle, 🎯 Focus shared goals, 💪 Relationship more important", "conflict"),
        ("Anger management", "🔥 Feeling rage inside, 🫁 Count to ten, 🏃 Physical exercise helps, 🤝 Talk to counselor", "conflict"),
        ("Communication breakdown", "📞 Phone call needed, 💬 Face to face, 📝 Write feelings down, 🤝 Professional help mediate", "conflict"),
        ("Toxic relationship", "🚫 This isn't healthy, 🚪 Exit strategy needed, 🤝 Support system important, 💪 Deserve better treatment", "conflict")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In conflict, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Conflict Resolution",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create the remaining categories efficiently...

def create_memory_nostalgia():
    examples = []
    scenarios = [
        ("Childhood memories", "👶 Happy times remembered, 🎪 Playground adventures daily", "memory"),
        ("Old photographs", "📸 Pictures tell stories, 💕 Faces from past", "memory"),
        ("School reunion", "🎓 Classmates aged well, 📚 Remember good times", "memory"),
        ("Grandparents stories", "👴 Wisdom from elders, 📖 Stories passed down", "memory"),
        ("First love", "💕 Young heart innocent, 💔 Lessons learned growing", "memory"),
        ("Family traditions", "🏠 Holiday memories warm, 👨‍👩‍👧‍👦 Generations connected through", "memory"),
        ("Forgotten dreams", "💭 What might have, 🌟 Different path taken", "memory"),
        ("Music memories", "🎵 Song brings back, 🕺 Dancing youth carefree", "memory"),
        ("Place revisited", "🏠 Nothing looks same, ⏰ Time changed everything", "memory"),
        ("Lost friendships", "👥 Wonder where now, 💕 Good times shared", "memory"),
        ("Memory fading", "🧠 Can't remember clearly, 📸 Photos help recall", "memory"),
        ("Legacy thoughts", "📚 What will remember, 🌟 Mark want leave", "memory")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I remember {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Memory Nostalgia",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with the final categories...

def create_productivity_time():
    examples = []
    scenarios = [
        ("Time management", "⏰ Schedule priorities first, 📋 To-do list helps", "productivity"),
        ("Procrastination problem", "😅 Putting off again, 🎯 Start small tasks", "productivity"),
        ("Work-life balance", "⚖️ Need better boundaries, 🏠 Home time sacred", "productivity"),
        ("Goal achievement", "🎯 Breaking down steps, 📊 Track progress daily", "productivity"),
        ("Focus challenges", "🧠 Mind wanders easily, 📱 Distractions everywhere around", "productivity"),
        ("Energy management", "🔋 Peak hours morning, 😴 Afternoon energy dips", "productivity"),
        ("Habit formation", "🔄 Consistency builds habits, 📅 Daily routine structure", "productivity"),
        ("Priority setting", "🎯 Important vs urgent, 🗑️ Eliminate time wasters", "productivity"),
        ("Workflow optimization", "🔧 Systems make easier, 🚀 Automation saves time", "productivity"),
        ("Meeting efficiency", "💼 Too many meetings, 📋 Agenda keeps focused", "productivity"),
        ("Digital organization", "💻 Files need organizing, 📱 Apps productivity boost", "productivity"),
        ("Stress productivity", "😰 Pressure affects performance, 🧘 Calm mind works", "productivity"),
        ("Delegation skills", "🤝 Ask others help, 💪 Can't do everything", "productivity"),
        ("Time blocking", "📅 Calendar time blocks, 🎯 Focus single task", "productivity"),
        ("Productivity systems", "📋 GTD method works, 🍅 Pomodoro technique helpful", "productivity")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"For productivity, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Productivity Time",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Continue with remaining categories efficiently...

def create_volunteering_service():
    examples = []
    scenarios = [
        ("Community service", "🤝 Help others need, 💕 Service brings joy", "volunteering"),
        ("Food bank", "🍲 Feed hungry people, 📦 Sort donations carefully", "volunteering"),
        ("Animal shelter", "🐕 Dogs need walks, 💕 Animals deserve love", "volunteering"),
        ("Homeless shelter", "🏠 Serve meals today, 🤝 Listen their stories", "volunteering"),
        ("Environmental cleanup", "🗑️ Pick up litter, 🌍 Protect our planet", "volunteering"),
        ("Senior center", "👴 Visit elderly regularly, 🎵 Music brings smiles", "volunteering"),
        ("Hospital volunteer", "🏥 Comfort patients families, 🌺 Flowers brighten rooms", "volunteering"),
        ("School tutoring", "📚 Help children learn, 🎓 Education changes lives", "volunteering"),
        ("Disaster relief", "🆘 Help after hurricane, 💪 Community pulls together", "volunteering"),
        ("Charity fundraising", "💰 Raise money cause, 🎪 Fun run charity", "volunteering"),
        ("Blood donation", "🩸 Save lives donating, 💪 Healthy enough give", "volunteering"),
        ("Volunteer coordination", "📋 Organize volunteer schedules, 🤝 Match skills needs", "volunteering")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In volunteering, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Volunteering Service",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Final categories to complete the ultra-comprehensive dataset

def create_aging_elderly_care():
    examples = []
    scenarios = [
        ("Aging concerns", "⏰ Time passing quickly, 🧠 Memory not sharp", "aging"),
        ("Elder care", "👴 Parents need help, 🏠 Home modifications needed", "aging"),
        ("Retirement planning", "💰 Fixed income budgeting, ⏰ Too much time", "aging"),
        ("Health decline", "💊 More medications daily, 🩺 Doctor visits frequent", "aging"),
        ("Grandchildren joy", "👶 New generation blessing, 📖 Stories to share", "aging"),
        ("Assisted living", "🏥 Need more help, 🏠 Home too big", "aging"),
        ("Medicare navigation", "📋 Insurance confusing paperwork, 💰 Coverage gaps exist", "aging"),
        ("Technology challenges", "📱 Phone too complicated, 💻 Computer skills lacking", "aging"),
        ("Social isolation", "👥 Friends passing away, 📞 Family visits rare", "aging"),
        ("Driving concerns", "🚗 Vision not good, 🛑 Reflexes slower now", "aging"),
        ("Legacy planning", "📋 Will needs updating, 💰 Estate planning important", "aging"),
        ("Caregiver burden", "😴 Exhausted from caregiving, 🤝 Need respite care", "aging"),
        ("Dignity preservation", "💪 Still independent person, 🙏 Respect my choices", "aging"),
        ("End of life", "🕊️ Not afraid dying, 💕 Want peaceful death", "aging"),
        ("Wisdom sharing", "📚 Lessons learned life, 👶 Teach younger generation", "aging"),
        ("Physical limitations", "🚶 Walking difficult now, 👂 Hearing aid needed", "aging"),
        ("Home safety", "🛡️ Fall prevention important, 💡 Better lighting needed", "aging"),
        ("Medication management", "💊 Pill organizer helps, ⏰ Timing is important", "aging")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"As I age, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Aging Elderly Care",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create final categories

def create_cultural_exchange():
    examples = []
    scenarios = [
        ("Different cultures", "🌍 World beautifully diverse, 🤝 Learn from others", "cultural"),
        ("Language barriers", "🗣️ Translation app helps, 👐 Gestures communicate universally", "cultural"),
        ("Food traditions", "🍜 Try authentic cuisine, 👨‍🍳 Grandmother's secret recipe", "cultural"),
        ("Religious differences", "🙏 Respect all faiths, ✨ Common spiritual threads", "cultural"),
        ("Cultural celebration", "🎭 Festival brings together, 🎵 Music crosses boundaries", "cultural"),
        ("Travel experiences", "✈️ Immerse local culture, 📸 Photos capture memories", "cultural"),
        ("Immigration story", "🏠 Left homeland behind, 🌅 New country opportunities", "cultural"),
        ("Cultural identity", "🪞 Who am culturally, 🌉 Bridge between worlds", "cultural"),
        ("Tradition preservation", "📚 Keep customs alive, 👶 Teach children heritage", "cultural"),
        ("Cultural misunderstanding", "🤔 Different doesn't mean, 💬 Communication clears confusion", "cultural"),
        ("Global citizenship", "🌍 World citizen mindset, 🤝 Humanity connects us", "cultural"),
        ("Cultural adaptation", "🔄 Blend old new, 🌱 Growth through change", "cultural"),
        ("Heritage pride", "🏆 Proud cultural background, 🌟 Celebrate unique traditions", "cultural"),
        ("Cross-cultural relationships", "💕 Love transcends culture, 👨‍👩‍👧‍👦 Blended family traditions", "cultural"),
        ("Cultural education", "📚 Learn about others, 🧠 Expand worldview daily", "cultural")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"Culturally, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Cultural Exchange",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_professional_development():
    examples = []
    scenarios = [
        ("Career advancement", "📈 Climbing corporate ladder, 🎯 Promotion goals set", "professional_dev"),
        ("Skill building", "📚 Learning new technologies, 💻 Coding bootcamp tonight", "professional_dev"),
        ("Networking events", "🤝 Making professional connections, 💼 Business cards ready", "professional_dev"),
        ("Conference attendance", "📊 Industry trends discussed, 💡 New ideas inspire", "professional_dev"),
        ("Certification pursuit", "📜 Professional credentials important, 📚 Study materials expensive", "professional_dev"),
        ("Mentorship relationship", "🤝 Senior colleague guidance, 📈 Career path planning", "professional_dev"),
        ("Job interview", "💼 Prepared for questions, 🎯 Show value proposition", "professional_dev"),
        ("Performance review", "📊 Metrics show growth, 🎯 Goals for year", "professional_dev"),
        ("Leadership development", "👥 Team management skills, 💬 Communication training needed", "professional_dev"),
        ("Industry change", "🔄 Adapting to disruption, 🚀 Innovation drives progress", "professional_dev"),
        ("Work portfolio", "📂 Showcase project achievements, 🎨 Visual presentation important", "professional_dev"),
        ("Professional brand", "🌟 Reputation in industry, 📱 LinkedIn profile updated", "professional_dev"),
        ("Continuing education", "🎓 MBA program considering, 💰 Investment in future", "professional_dev"),
        ("Career transition", "🔄 Changing career paths, 😰 Uncertainty but excited", "professional_dev"),
        ("Side business", "💼 Entrepreneurial venture starting, ⏰ Evenings and weekends", "professional_dev"),
        ("Public speaking", "🎤 Conference presentation nervs, 💪 Practice builds confidence", "professional_dev"),
        ("Team collaboration", "👥 Cross-functional project team, 🎯 Shared goals important", "professional_dev"),
        ("Remote work", "🏠 Home office setup, 💻 Video calls daily", "professional_dev")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"Professionally, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Professional Development",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create final categories

def create_emergency_preparedness():
    examples = []
    scenarios = [
        ("Emergency kit", "📦 Supplies ready always, 💧 Water for days", "emergency_prep"),
        ("Evacuation plan", "🚪 Exit routes mapped, 🎒 Go bag packed", "emergency_prep"),
        ("Communication plan", "📞 Emergency contact numbers, 📻 Battery radio works", "emergency_prep"),
        ("Natural disaster", "🌪️ Tornado warning issued, 🏠 Basement shelter ready", "emergency_prep"),
        ("Power outage", "🔦 Flashlights have batteries, 🕯️ Candles backup lighting", "emergency_prep"),
        ("Medical emergency", "🩹 First aid trained, 🚑 Emergency services number", "emergency_prep"),
        ("Food storage", "🥫 Non-perishable foods stocked, 🔥 Camping stove backup", "emergency_prep"),
        ("Document protection", "📋 Important papers copied, ☁️ Cloud storage backup", "emergency_prep"),
        ("Pet emergency", "🐕 Pet carrier ready, 💊 Pet medications packed", "emergency_prep"),
        ("Neighborhood plan", "👥 Check on neighbors, 🤝 Community response team", "emergency_prep"),
        ("Winter storm", "❄️ Snow removal tools, 🔥 Heating backup plan", "emergency_prep"),
        ("Fire escape", "🔥 Smoke detectors working, 🪜 Ladder upstairs window", "emergency_prep"),
        ("Financial emergency", "💰 Emergency fund saved, 📋 Insurance policies current", "emergency_prep"),
        ("Car emergency", "🚗 Roadside assistance membership, 🔧 Basic tools trunk", "emergency_prep"),
        ("Chemical spill", "🏃 Evacuation route ready, 📻 Official information source", "emergency_prep")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"For emergencies, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Emergency Preparedness",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create the final remaining categories

def create_seasonal_weather_specific():
    examples = []
    scenarios = [
        ("Spring cleaning", "🌸 Fresh start season, 🧹 Deep cleaning house", "seasonal"),
        ("Summer vacation", "☀️ Beach trip planned, 🏖️ Sand between toes", "seasonal"),
        ("Fall traditions", "🍂 Leaves changing colors, 🎃 Pumpkin patch visit", "seasonal"),
        ("Winter preparations", "❄️ Snow tires installed, 🧥 Warm coats ready", "seasonal"),
        ("Holiday decorations", "🎄 Christmas tree up, ✨ Lights make magical", "seasonal"),
        ("Seasonal depression", "😔 Shorter days affect, 💡 Light therapy helps", "seasonal"),
        ("Spring allergies", "🤧 Pollen counts high, 💊 Antihistamine medication daily", "seasonal"),
        ("Summer heat", "🥵 Air conditioning broken, 💧 Stay hydrated always", "seasonal"),
        ("Autumn harvest", "🍎 Apple picking tradition, 🥧 Homemade pie baking", "seasonal"),
        ("Winter sports", "⛷️ Skiing mountain slopes, ❄️ Fresh powder perfect", "seasonal"),
        ("Seasonal clothes", "👔 Wardrobe change time, 📦 Store winter coats", "seasonal"),
        ("Weather patterns", "🌦️ Climate changing noticeably, 🌪️ Storms more intense", "seasonal"),
        ("Daylight saving", "⏰ Clock change confusing, 😴 Sleep schedule disrupted", "seasonal"),
        ("Seasonal work", "🌱 Landscaping jobs start, 🏖️ Tourism season busy", "seasonal"),
        ("Weather alerts", "📱 Storm warning issued, 🏠 Prepare for impact", "seasonal"),
        ("Seasonal foods", "🍓 Strawberries in season, 🥧 Fresh berry pie", "seasonal"),
        ("Temperature extremes", "🌡️ Record heat today, 🧊 Pipes might freeze", "seasonal"),
        ("Seasonal migration", "🦅 Birds flying south, 🐻 Animals preparing hibernation", "seasonal"),
        ("Garden seasons", "🌱 Planting season begins, 🍂 Harvest time here", "seasonal"),
        ("Weather preparation", "🌪️ Tornado season coming, 📦 Emergency kit checked", "seasonal")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"This season, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Seasonal Weather",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

# Create remaining categories

def create_social_media_digital():
    examples = []
    scenarios = [
        ("Social media overwhelm", "📱 Too much information, 🧠 Digital detox needed", "social_media"),
        ("Online privacy", "🔒 Personal data protection, 🕵️ Companies tracking everything", "social_media"),
        ("Digital addiction", "📱 Phone usage excessive, ⏰ Screen time limits", "social_media"),
        ("Cyberbullying", "😢 Online harassment hurts, 🚫 Block toxic users", "social_media"),
        ("Social comparison", "📸 Everyone looks perfect, 💭 Reality vs curated", "social_media"),
        ("Online learning", "💻 Educational content abundant, 📚 YouTube tutorials helpful", "social_media"),
        ("Digital relationships", "💬 Friends through screens, 🤝 Real connection matters", "social_media"),
        ("Content creation", "📹 Making videos fun, 🎨 Creative outlet expression", "social_media"),
        ("Information overload", "📰 News cycle overwhelming, 🤔 Fact check sources", "social_media"),
        ("Digital footprint", "👣 Online presence permanent, 🤔 Think before posting", "social_media"),
        ("Platform algorithms", "🤖 Algorithm controls content, 📊 Engagement drives visibility", "social_media"),
        ("Online shopping", "🛒 Amazon delivers everything, 💳 Easy impulse purchases", "social_media"),
        ("Video calls", "📹 Zoom meeting fatigue, 🏠 Home background messy", "social_media"),
        ("Digital art", "🎨 Creating on tablet, 💻 Software learning curve", "social_media"),
        ("Streaming entertainment", "📺 Netflix binge watching, 🎵 Spotify playlist perfect", "social_media"),
        ("Online dating", "💕 Dating apps awkward, 🤝 Meeting people difficult", "social_media"),
        ("Gaming online", "🎮 Multiplayer games fun, 👥 Community friendships formed", "social_media"),
        ("Digital nomad", "💻 Work from anywhere, ✈️ Travel while working", "social_media")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"Online, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Social Media Digital",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_fear_phobias():
    examples = []
    scenarios = [
        ("Flying anxiety", "✈️ Airplane fear overwhelming, 🫁 Breathing exercises help", "fear"),
        ("Social anxiety", "👥 Crowds make nervous, 🏠 Rather stay home", "fear"),
        ("Heights phobia", "🏔️ Looking down terrifies, 🤢 Stomach drops instantly", "fear"),
        ("Spiders fear", "🕷️ Arachnophobia is real, 🏃 Run away screaming", "fear"),
        ("Public speaking", "🎤 Stage fright paralyzing, 😰 Heart beats fast", "fear"),
        ("Claustrophobia", "📦 Small spaces panic, 🚪 Need exit visible", "fear"),
        ("Death anxiety", "💀 Mortality thoughts haunting, 😰 Existential dread overwhelming", "fear"),
        ("Medical procedures", "💉 Needles cause fainting, 🏥 Hospital anxiety severe", "fear"),
        ("Driving fear", "🚗 Car accidents worry, 🛑 Panic at wheel", "fear"),
        ("Water phobia", "🌊 Deep water terrifies, 🏊 Never learned swimming", "fear"),
        ("Darkness fear", "🌑 Night brings terror, 💡 Need lights on", "fear"),
        ("Animal phobia", "🐕 Dogs make anxious, 🦇 Bats absolutely terrifying", "fear")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"I fear {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Fear Phobias",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "high",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_mindfulness_meditation():
    examples = []
    scenarios = [
        ("Meditation practice", "🧘 Daily sitting meditation, 🫁 Focus on breathing", "mindfulness"),
        ("Mindful eating", "🍎 Savor each bite, 👅 Taste textures fully", "mindfulness"),
        ("Present moment", "⏰ Here and now, 💭 Let thoughts pass", "mindfulness"),
        ("Gratitude practice", "🙏 Thankful for today, 💕 Appreciate small things", "mindfulness"),
        ("Body scan", "🧘 Notice physical sensations, 💆 Tension and relaxation", "mindfulness"),
        ("Walking meditation", "🚶 Mindful steps earth, 🌳 Nature connection deep", "mindfulness"),
        ("Breathing exercises", "🫁 In for four, 💨 Out for six", "mindfulness"),
        ("Mindful listening", "👂 Sounds without judgment, 🎵 Musical meditation practice", "mindfulness"),
        ("Loving kindness", "💕 Send love outward, 🤗 Compassion for all", "mindfulness"),
        ("Anxiety mindfulness", "😰 Observe anxiety thoughts, 🌊 Let feelings flow", "mindfulness"),
        ("Meditation apps", "📱 Headspace guides meditation, 🧘 Calm app helpful", "mindfulness"),
        ("Spiritual practice", "🙏 Connection to divine, ✨ Sacred moments daily", "mindfulness"),
        ("Stress reduction", "😌 Meditation calms mind, 💆 Tension melts away", "mindfulness"),
        ("Awareness practice", "👁️ Witness thoughts arising, 🧠 Observer consciousness watching", "mindfulness"),
        ("Mindful work", "💼 Present during tasks, 🎯 Single focus attention", "mindfulness")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"In mindfulness, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Mindfulness Meditation",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def create_nutrition_cooking():
    examples = []
    scenarios = [
        ("Healthy eating", "🥗 Vegetables every meal, 🍎 Fruits natural sweetness", "nutrition"),
        ("Meal planning", "📅 Week menu prepared, 🛒 Grocery list organized", "nutrition"),
        ("Cooking skills", "👨‍🍳 Learning knife techniques, 🔥 Temperature control important", "nutrition"),
        ("Special diet", "🌱 Vegetarian lifestyle choice, 🚫 Gluten free necessity", "nutrition"),
        ("Food allergies", "🥜 Nuts cause reactions, 📋 Read labels carefully", "nutrition"),
        ("Weight management", "⚖️ Healthy weight goals, 🏃 Exercise portion control", "nutrition"),
        ("Comfort food", "🍲 Soup soothes soul, 🍕 Pizza guilty pleasure", "nutrition"),
        ("Family recipes", "👵 Grandmother's secret ingredients, 📖 Recipe passed down", "nutrition"),
        ("Cooking disasters", "🔥 Smoke alarm again, 😅 Learning from mistakes", "nutrition"),
        ("Food photography", "📸 Instagram worthy plate, 🎨 Presentation matters too", "nutrition"),
        ("Kitchen tools", "🔪 Sharp knives essential, 🥄 Right tools matter", "nutrition"),
        ("Farmer's market", "🌾 Fresh local produce, 👨‍🌾 Support local farmers", "nutrition"),
        ("Batch cooking", "🍲 Sunday meal prep, 📦 Week portions ready", "nutrition"),
        ("Cultural cuisine", "🍜 Exploring world flavors, 🌶️ Spice tolerance building", "nutrition"),
        ("Food budget", "💰 Eating well affordably, 🛒 Smart shopping strategies", "nutrition"),
        ("Nutrition education", "📚 Learning food science, 💊 Supplements vs food", "nutrition"),
        ("Restaurant choices", "🍽️ Menu healthy options, 💰 Special occasion splurge", "nutrition"),
        ("Food preservation", "🥫 Canning summer vegetables, ❄️ Freezer meal prep", "nutrition")
    ]
    
    for input_text, output_text, category in scenarios:
        tiles = parse_output_to_tiles(output_text)
        spoken = f"With food, I {tiles[0]['words'].lower()}."
        
        example = {
            "instruction": "AAC Nutrition Cooking",
            "input": input_text,
            "aac_response": {
                "tiles": tiles,
                "spoken_sentence": spoken,
                "usage_data": {
                    "category": category,
                    "emotion_level": "medium",
                    "complexity": len(tiles),
                    "frequency_weight": 1.0
                }
            },
            "raw_output": output_text
        }
        examples.append(example)
    
    return examples

def parse_output_to_tiles(output_text):
    """Parse output into tile format"""
    tiles = []
    parts = output_text.split(', ')
    
    for i, part in enumerate(parts[:4]):  # Max 4 tiles
        part = part.strip()
        if not part:
            continue
            
        # Find emoji and words
        emoji = ""
        words = part
        
        # Extract emoji if present
        for char in part:
            if ord(char) > 127:  # Non-ASCII character (likely emoji)
                emoji = char
                words = part.replace(char, '').strip()
                break
        
        if not emoji:
            emoji = "💬"  # Default emoji
        
        tiles.append({
            "emoji": emoji,
            "words": words,
            "tile_id": f"tile_{i+1}"
        })
    
    return tiles

if __name__ == "__main__":
    total = create_ultra_complete_categories()
    print(f"\n🎯 ULTRA COMPLETE: {total:,} examples created!")
    print(f"🏆 100% COMPREHENSIVE AAC COVERAGE ACHIEVED!")