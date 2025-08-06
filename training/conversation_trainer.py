#!/usr/bin/env python3
"""
Multi-Turn Conversation Trainer
Creates realistic conversation flow training for AAC
"""
import json

def create_conversation_flows():
    """Create multi-turn conversation training examples"""
    print("💬 Creating Multi-Turn Conversation Flows")
    print("=" * 50)
    
    conversations = []
    
    # Common conversation starters and follow-ups
    conversation_patterns = [
        # Greeting sequences
        {
            'starter': 'Hello',
            'responses': [
                ('Hi there', '👋 Hello back, 😊 Nice to see you, 💬 How are you, 🌟 Good to meet'),
                ('How are you', '😊 Pretty good, 😐 Okay I guess, 😔 Not so great, 💭 Let me think'),
                ('What are you doing', '💭 Just thinking, 📺 Watching TV, 🍽️ Eating food, 🎮 Playing games'),
                ('Where are you going', '🏠 Going home, 🏪 To the store, 🚗 For a drive, 🤷 Not sure yet')
            ]
        },
        
        # Need/want sequences
        {
            'starter': 'I need help',
            'responses': [
                ('What do you need', '🤔 Not sure exactly, 💭 Hard to explain, 🤲 Many things, 📝 Let me think'),
                ('How can I help', '🤗 Just be here, 💪 Give me strength, 🧠 Help me think, 🎯 Show me way'),
                ('What happened', '😔 Long story, 💔 Feeling overwhelmed, 🌀 Everything at once, ⏰ Bad day'),
                ('Are you okay', '😐 Not really, 💪 Trying to be, 🤗 Need support, 🌈 Will get better')
            ]
        },
        
        # Feeling sequences
        {
            'starter': 'I feel sad',
            'responses': [
                ('Why are you sad', '💔 Many reasons, 😔 Hard to explain, 🤷 Not sure why, 💭 Long story'),
                ('What happened', '😢 Bad day, 💔 Someone hurt me, 😞 Things went wrong, 🌧️ Just feeling down'),
                ('Can I help', '🤗 Just listen, 💪 Give me hope, 🌈 Remind me better days, ⏰ Be patient'),
                ('Do you want to talk', '💬 Maybe later, 😔 Not ready yet, 🤗 Just need comfort, 👥 Stay with me')
            ]
        },
        
        # Activity sequences
        {
            'starter': 'I want to go out',
            'responses': [
                ('Where do you want to go', '🌳 To the park, 🏪 To the store, 🚗 For a drive, 🤷 Anywhere really'),
                ('When do you want to go', '⏰ Right now, 🕐 Later today, 🌅 Tomorrow maybe, 🤔 When ready'),
                ('Who will go with you', '👥 Want company, 🤗 You come too, 👨‍👩‍👧‍👦 Family maybe, 🚶 Go alone'),
                ('How will you get there', '🚗 Drive car, 🚌 Take bus, 🚶 Walk there, 🚕 Call taxi')
            ]
        },
        
        # Problem-solving sequences
        {
            'starter': 'Something is wrong',
            'responses': [
                ('What is wrong', '💭 Hard to say, 🤔 Not sure exactly, 😰 Feels off, 🌀 Everything'),
                ('When did it start', '⏰ Just now, 🌅 This morning, 📅 Few days ago, 🤷 Been while'),
                ('How does it feel', '😰 Scary feeling, 💔 Heart hurts, 🤢 Sick feeling, 😵 Dizzy'),
                ('Do you need a doctor', '👨‍⚕️ Maybe yes, 🤔 Not sure, 😰 Am scared, ⏰ Wait and see')
            ]
        },
        
        # Daily routine sequences
        {
            'starter': 'I am getting ready',
            'responses': [
                ('Ready for what', '💼 For work, 🏫 For school, 🛒 To go shopping, 🎉 For party'),
                ('What do you need to do', '🚿 Take shower, 👕 Get dressed, 🍳 Eat breakfast, 🚗 Get keys'),
                ('Are you running late', '⏰ Little late, 🏃 Need to hurry, 😰 Very late, 😌 Have time'),
                ('Do you need help', '🤗 Yes please, 💪 I can do it, 🤔 Maybe little, 🙏 Thank you')
            ]
        }
    ]
    
    # Generate conversation training examples
    for pattern in conversation_patterns:
        starter = pattern['starter']
        
        for response_input, response_output in pattern['responses']:
            conversations.append({
                'instruction': f'AAC Conversation Flow: {starter} -> {response_input}',
                'input': response_input,
                'output': response_output,
                'conversation_metadata': {
                    'starter': starter,
                    'conversation_type': 'multi_turn',
                    'social_context': True
                }
            })
    
    # Add follow-up conversation examples
    followup_patterns = [
        # Emotional support follow-ups
        {
            'context': 'after expressing sadness',
            'examples': [
                ('Thank you for listening', '🤗 Always here, ❤️ Care about you, 💪 You are strong, 🌈 Better days coming'),
                ('I feel a little better', '😊 Good to hear, 🌟 Progress made, 💪 Keep going, 🤗 Proud of you'),
                ('I still feel bad', '💔 Understand that, ⏰ Takes time, 🤗 Not alone, 💪 Will get through'),
                ('What should I do now', '🧘 Take deep breaths, 🚶 Go for walk, 📞 Call friend, 🛌 Rest if tired')
            ]
        },
        
        # Planning follow-ups
        {
            'context': 'after making plans',
            'examples': [
                ('What time should we go', '🕐 Up to you, ⏰ When ready, 🌅 Earlier better, 🌆 Later fine'),
                ('Should I bring anything', '💧 Bring water, 💰 Bring money, 📱 Bring phone, 🤷 Not sure'),
                ('What if it rains', '☔ Check weather, 🏠 Stay inside, 🌂 Bring umbrella, 📅 Go tomorrow'),
                ('I changed my mind', '🤷 That happens, 😊 No problem, 💭 Think about it, ✅ Whatever works')
            ]
        },
        
        # Problem resolution follow-ups
        {
            'context': 'after identifying problem',
            'examples': [
                ('I think I know what to do', '💪 Good for you, 🎯 Make plan, 🤗 You got this, ⭐ Believe in you'),
                ('I need more help', '🤲 Ask someone, 📞 Call expert, 👥 Get support, 💪 Team effort'),
                ('It is getting worse', '🚨 Get help now, 👨‍⚕️ Call doctor, 📞 Emergency number, 🏥 Go hospital'),
                ('I feel overwhelmed', '🧘 Take breaks, 📝 One step time, 🤗 Not alone, 💪 Can handle this')
            ]
        }
    ]
    
    # Generate follow-up training examples
    for followup in followup_patterns:
        context = followup['context']
        
        for followup_input, followup_output in followup['examples']:
            conversations.append({
                'instruction': f'AAC Conversation Follow-up: {context}',
                'input': followup_input,
                'output': followup_output,
                'conversation_metadata': {
                    'context': context,
                    'conversation_type': 'follow_up',
                    'emotional_support': True
                }
            })
    
    print(f"✅ Created {len(conversations)} conversation flow examples")
    return conversations

def create_contextual_responses():
    """Create context-aware response training"""
    print("🎯 Creating Contextual Response Training")
    print("=" * 45)
    
    contextual_responses = []
    
    # Context-dependent scenarios
    contexts = [
        {
            'situation': 'at doctor office',
            'examples': [
                ('How are you feeling', '🤒 Not well, 🤕 Something hurts, 😰 Am worried, 💊 Need medicine'),
                ('What brings you here', '😷 Feel sick, 🤕 Got injured, 💊 Need checkup, 🧠 Mental health'),
                ('Any pain', '🤕 Yes hurts, 😐 Little bit, 🚫 No pain, 🤔 Hard to tell'),
                ('Take any medications', '💊 Yes these ones, 🚫 No medicine, 📋 Check my list, 🤔 Not sure')
            ]
        },
        
        {
            'situation': 'at grocery store',
            'examples': [
                ('Can I help you find something', '📝 Looking for items, 🛒 Just browsing, 🤔 Where is milk, 🙏 Yes please'),
                ('Do you have a rewards card', '💳 Yes here it is, 🚫 No card, 📱 On my phone, 🤔 What is that'),
                ('Paper or plastic', '📦 Plastic please, 📄 Paper bags, 🛍️ Bring own bags, 🤷 Either fine'),
                ('Did you find everything', '✅ Got everything, 🤔 Missing some items, 📝 Check my list, 😊 All good')
            ]
        },
        
        {
            'situation': 'at work',
            'examples': [
                ('How is the project going', '💼 Going well, 😰 Having trouble, 🤔 Need more time, 🤲 Need help'),
                ('Can you stay late today', '⏰ Yes can stay, 🏠 Need to go home, 📅 Maybe tomorrow, 🤔 How late'),
                ('Any questions about the task', '✅ Understand it, 🤔 Few questions, 😰 Very confused, 📚 Need training'),
                ('Ready for the meeting', '📋 All prepared, 😰 Need more time, 📝 Have questions, 💻 Technical problems')
            ]
        },
        
        {
            'situation': 'at home with family',
            'examples': [
                ('What do you want for dinner', '🍕 Order pizza, 🍳 Cook something, 🥪 Make sandwich, 🤷 You choose'),
                ('How was your day', '😊 Really good day, 😐 Okay I guess, 😔 Not great, 🎉 Amazing day'),
                ('Want to watch a movie', '📺 Yes sounds fun, 📚 Rather read, 😴 Too tired, 🎮 Play games instead'),
                ('Need help with anything', '🤗 Just company, 💪 Yes please, 😊 I am good, 🧹 Help clean')
            ]
        }
    ]
    
    # Generate contextual response training
    for context in contexts:
        situation = context['situation']
        
        for example_input, example_output in context['examples']:
            contextual_responses.append({
                'instruction': f'AAC Contextual Response: {situation}',
                'input': example_input,
                'output': example_output,
                'context_metadata': {
                    'situation': situation,
                    'context_aware': True,
                    'social_appropriateness': True
                }
            })
    
    print(f"✅ Created {len(contextual_responses)} contextual response examples")
    return contextual_responses

def compile_conversation_training():
    """Compile complete conversation training dataset"""
    print("\n🚀 Compiling Complete Conversation Training")
    print("=" * 50)
    
    # Generate conversation training data
    conversation_flows = create_conversation_flows()
    contextual_responses = create_contextual_responses()
    
    # Combine all conversation examples
    all_examples = []
    all_examples.extend(conversation_flows)
    all_examples.extend(contextual_responses)
    
    # Save conversation training dataset
    filename = 'tinkybink_conversation_train.jsonl'
    with open(filename, 'w') as f:
        for example in all_examples:
            f.write(json.dumps(example) + '\n')
    
    total_examples = len(all_examples)
    
    print(f"\n🎉 CONVERSATION TRAINING COMPLETE!")
    print("=" * 45)
    print(f"💬 Conversation flows: {len(conversation_flows)}")
    print(f"🎯 Contextual responses: {len(contextual_responses)}")
    print(f"🚀 Total conversation examples: {total_examples}")
    print(f"📁 Saved to: {filename}")
    
    return filename, total_examples

def main():
    print("💬 TinkyBink Multi-Turn Conversation Trainer")
    print("=" * 70)
    print("🎯 Creating realistic conversation flow training")
    print("🗣️ Multi-turn dialogues with contextual awareness!")
    print()
    
    dataset_file, total_examples = compile_conversation_training()
    
    print(f"\n✅ SUCCESS! Created {total_examples} conversation training examples")
    print("🌟 AAC system now ready for natural conversation flow!")

if __name__ == "__main__":
    main()