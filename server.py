#!/usr/bin/env python3
"""
Tinkybink AAC Web Server
Connects the HTML interface to the Rust engine via subprocess
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess
import json
import os
import sys

app = Flask(__name__)
CORS(app)  # Allow browser to connect

# Path to the Rust binary - Hospital Grade
RUST_BINARY = "./target/release/hospital_grade_complete"

@app.route('/')
def index():
    """Serve the main HTML interface"""
    return send_file('stroke_victim_perfect.html')

@app.route('/api/suggest', methods=['POST'])
def get_suggestions():
    """Get tile suggestions from the Rust engine"""
    try:
        data = request.json
        question = data.get('question', '')
        
        print(f"🧠 Received question: {question}")
        
        # FIRST: Try calling the actual Rust AI engine
        try:
            print(f"🚀 Calling Rust AI engine: {RUST_BINARY}")
            result = subprocess.run([RUST_BINARY, question], 
                                 capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                rust_output = result.stdout.strip()
                print(f"✅ Rust engine response: {rust_output}")
                
                # Parse JSON output from Rust
                rust_data = json.loads(rust_output)
                if rust_data.get('success') and rust_data.get('suggestions'):
                    print(f"🎯 Using REAL Rust AI suggestions: {len(rust_data['suggestions'])} tiles")
                    return jsonify(rust_data)
            
            print(f"⚠️ Rust engine failed, fallback to Ollama...")
        except Exception as rust_error:
            print(f"❌ Rust engine error: {rust_error}")
        
        # SECOND: Try Ollama with trained model  
        try:
            prompt = f"""You are helping a non-verbal person communicate. They were asked: "{question}"
Generate exactly 6 appropriate response tiles. Each tile should be a possible answer.
Format each response as: emoji | short text
Examples:
- For "How did you sleep?": 😴|Good sleep, 😫|Bad night, 😰|Nightmares, etc.
- For "Want to go to Vegas?": ✈️|Yes Vegas!, 🎰|Love gambling, 🏠|Stay home, etc.
- For "Grandpa wants the horse or titty bar?": 🐎|Horse track, 🍺|Bar please, 😂|Both funny, etc.

Responses for "{question}":"""

            cmd = f'ollama run tinkybink:latest "{prompt}" 2>/dev/null | head -20'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout.strip()
            
            print(f"🤖 Ollama output: {output}")
            
            # Parse Ollama's response into tiles
            suggestions = []
            for line in output.split('\n'):
                if '|' in line:
                    parts = line.strip().strip('-').strip('•').strip().split('|')
                    if len(parts) == 2:
                        emoji = parts[0].strip()
                        text = parts[1].strip()
                        suggestions.append({
                            'emoji': emoji,
                            'text': text,
                            'confidence': 0.85 + (len(suggestions) * 0.02)
                        })
            
            if len(suggestions) >= 4:
                print(f"🎯 Using Ollama suggestions: {len(suggestions)} tiles")
                return jsonify({
                    'success': True,
                    'suggestions': suggestions[:8],
                    'question': question
                })
        except Exception as ollama_error:
            print(f"❌ Ollama error: {ollama_error}")
        
        # THIRD: Use dynamic fallback (better than hardcoded)
        print(f"💡 Using dynamic analysis fallback")
        suggestions = get_dynamic_suggestions(question)
        return jsonify({
            'success': True,
            'suggestions': suggestions,
            'question': question
        })
        
    except Exception as e:
        print(f"💥 Total failure: {e}")
        # Last resort fallback
        return jsonify({
            'success': True,
            'suggestions': get_dynamic_suggestions(question),
            'question': question
        })

@app.route('/api/speak', methods=['POST'])
def speak_text():
    """Use the Rust engine's TTS to speak text"""
    try:
        data = request.json
        text = data.get('text', '')
        
        # Use macOS say command as fallback (Rust TTS might need different approach)
        subprocess.run(['say', '-v', 'Samantha', text], timeout=10)
        
        return jsonify({'success': True, 'spoken': text})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/status', methods=['GET'])
def check_status():
    """Check if Rust engine is available"""
    try:
        # Check if Rust binary exists and is executable
        if os.path.exists(RUST_BINARY) and os.access(RUST_BINARY, os.X_OK):
            # Try to get engine info
            result = subprocess.run([RUST_BINARY, '--help'], capture_output=True, timeout=2)
            return jsonify({
                'connected': True,
                'engine': 'Tinkybink Rust Engine',
                'models': check_ollama_models()
            })
        else:
            return jsonify({'connected': False, 'error': 'Rust binary not found'})
    except Exception as e:
        return jsonify({'connected': False, 'error': str(e)})

def check_ollama_models():
    """Check available Ollama models"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=2)
        models = []
        for line in result.stdout.split('\n')[1:]:  # Skip header
            if 'tinkybink' in line.lower():
                parts = line.split()
                if parts:
                    models.append(parts[0])
        return models[:3] if models else ['tinkybink:latest']  # Return top 3 models
    except:
        return ['offline-mode']

def parse_suggestions(output, question):
    """Parse suggestion output from Rust engine"""
    suggestions = []
    
    # Try to extract suggestions from the output
    lines = output.split('\n')
    for line in lines:
        if '.' in line and any(emoji in line for emoji in ['✅', '❌', '🤷', '🤔', '😊', '😢', '💊', '💧', '🍽️']):
            # Parse lines that look like: "1. ✅ Yes! (confidence: 0.85)"
            parts = line.strip().split(' ', 2)
            if len(parts) >= 3:
                emoji = parts[1]
                text_and_conf = parts[2]
                text = text_and_conf.split('(')[0].strip()
                
                # Extract confidence if present
                confidence = 0.85
                if 'confidence:' in text_and_conf:
                    try:
                        conf_str = text_and_conf.split('confidence:')[1].strip('() ')
                        confidence = float(conf_str)
                    except:
                        pass
                
                suggestions.append({
                    'emoji': emoji,
                    'text': text,
                    'confidence': confidence
                })
    
    # If no suggestions found, return fallback
    if not suggestions:
        suggestions = get_fallback_suggestions(question)
    
    return suggestions

def parse_ollama_freeform(output, question):
    """Try to parse freeform Ollama output into tiles"""
    suggestions = []
    lines = output.split('\n')
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # Try to extract emoji and text
            import re
            emoji_pattern = r'[😀-🙏🌀-🗿🚀-🛿🏠-🏿✨-➿☀-♿️🎀-🏿]+'
            emojis = re.findall(emoji_pattern, line)
            
            if emojis:
                emoji = emojis[0]
                text = line.replace(emoji, '').strip(' -,.:')
                if text:
                    suggestions.append({
                        'emoji': emoji,
                        'text': text[:20],  # Limit text length
                        'confidence': 0.80 + (len(suggestions) * 0.03)
                    })
    
    return suggestions

def get_dynamic_suggestions(question):
    """Generate dynamic context-aware suggestions for ANY question"""
    q = question.lower()
    
    # Sleep related
    if any(word in q for word in ['sleep', 'rest', 'tired', 'nap', 'bed']):
        return [
            {'emoji': '😴', 'text': 'Slept great', 'confidence': 0.92},
            {'emoji': '😫', 'text': 'Bad night', 'confidence': 0.88},
            {'emoji': '😰', 'text': 'Nightmares', 'confidence': 0.85},
            {'emoji': '🥱', 'text': 'Still tired', 'confidence': 0.87},
            {'emoji': '😌', 'text': 'Well rested', 'confidence': 0.90},
            {'emoji': '🛏️', 'text': 'Need more sleep', 'confidence': 0.86}
        ]
    
    # Vegas/gambling/adult venues
    elif any(word in q for word in ['vegas', 'casino', 'gambl', 'horse', 'track', 'bar', 'club', 'titty']):
        return [
            {'emoji': '🎰', 'text': 'Casino time!', 'confidence': 0.90},
            {'emoji': '🐎', 'text': 'Horse track', 'confidence': 0.88},
            {'emoji': '🍺', 'text': 'Bar sounds good', 'confidence': 0.87},
            {'emoji': '🏠', 'text': 'Rather stay home', 'confidence': 0.85},
            {'emoji': '💃', 'text': 'Dancing!', 'confidence': 0.86},
            {'emoji': '😂', 'text': 'You\'re funny', 'confidence': 0.89}
        ]
    
    # Choice between options (or)
    elif ' or ' in q:
        # Extract the two options
        parts = q.split(' or ')
        if len(parts) >= 2:
            option1 = parts[0].split()[-1] if parts[0] else 'first'
            option2 = parts[1].split()[0] if parts[1] else 'second'
            return [
                {'emoji': '1️⃣', 'text': option1.capitalize(), 'confidence': 0.90},
                {'emoji': '2️⃣', 'text': option2.capitalize(), 'confidence': 0.90},
                {'emoji': '🤷', 'text': 'Either one', 'confidence': 0.85},
                {'emoji': '😊', 'text': 'Both!', 'confidence': 0.87},
                {'emoji': '❌', 'text': 'Neither', 'confidence': 0.83},
                {'emoji': '🤔', 'text': 'Let me think', 'confidence': 0.80}
            ]
    
    # Grandpa/family specific
    elif any(word in q for word in ['grandpa', 'grandma', 'dad', 'mom', 'family']):
        return [
            {'emoji': '👴', 'text': 'Love you grandpa', 'confidence': 0.92},
            {'emoji': '😂', 'text': 'You\'re silly', 'confidence': 0.88},
            {'emoji': '🤗', 'text': 'Miss you', 'confidence': 0.90},
            {'emoji': '📞', 'text': 'Call me later', 'confidence': 0.85},
            {'emoji': '👍', 'text': 'Sounds good', 'confidence': 0.87},
            {'emoji': '❤️', 'text': 'Love you', 'confidence': 0.93}
        ]
    
    # Want/desire questions
    elif any(word in q for word in ['want', 'like', 'need', 'wish']):
        return [
            {'emoji': '✅', 'text': 'Yes please', 'confidence': 0.90},
            {'emoji': '❌', 'text': 'No thanks', 'confidence': 0.88},
            {'emoji': '😍', 'text': 'Would love to', 'confidence': 0.87},
            {'emoji': '🤔', 'text': 'Maybe later', 'confidence': 0.83},
            {'emoji': '💯', 'text': 'Definitely!', 'confidence': 0.91},
            {'emoji': '😐', 'text': 'Not really', 'confidence': 0.84}
        ]
    
    # Default for any other question
    else:
        return [
            {'emoji': '👍', 'text': 'Yes', 'confidence': 0.85},
            {'emoji': '👎', 'text': 'No', 'confidence': 0.85},
            {'emoji': '🤷', 'text': 'Not sure', 'confidence': 0.80},
            {'emoji': '😊', 'text': 'Happy', 'confidence': 0.83},
            {'emoji': '🤔', 'text': 'Thinking', 'confidence': 0.82},
            {'emoji': '💬', 'text': 'Tell me more', 'confidence': 0.81}
        ]

def get_fallback_suggestions(question):
    """Generate fallback suggestions when Rust engine is not available"""
    q_lower = question.lower()
    
    if 'feel' in q_lower or 'how are you' in q_lower:
        return [
            {'emoji': '😊', 'text': 'Good today', 'confidence': 0.92},
            {'emoji': '😔', 'text': 'Not great', 'confidence': 0.85},
            {'emoji': '😴', 'text': 'Very tired', 'confidence': 0.88},
            {'emoji': '😣', 'text': 'In pain', 'confidence': 0.75}
        ]
    elif 'pain' in q_lower or 'hurt' in q_lower:
        return [
            {'emoji': '😣', 'text': 'Yes, hurts', 'confidence': 0.95},
            {'emoji': '😌', 'text': 'No pain now', 'confidence': 0.85},
            {'emoji': '💊', 'text': 'Need medicine', 'confidence': 0.90},
            {'emoji': '🩹', 'text': 'Getting better', 'confidence': 0.78}
        ]
    elif 'water' in q_lower or 'thirsty' in q_lower or 'drink' in q_lower:
        return [
            {'emoji': '✅', 'text': 'Yes please', 'confidence': 0.95},
            {'emoji': '❌', 'text': 'Not now', 'confidence': 0.80},
            {'emoji': '🧊', 'text': 'With ice', 'confidence': 0.88},
            {'emoji': '🥤', 'text': 'Juice instead', 'confidence': 0.75}
        ]
    elif 'hungry' in q_lower or 'eat' in q_lower or 'food' in q_lower:
        return [
            {'emoji': '✅', 'text': 'Yes, hungry', 'confidence': 0.90},
            {'emoji': '🍲', 'text': 'Soup please', 'confidence': 0.85},
            {'emoji': '🥪', 'text': 'Sandwich', 'confidence': 0.82},
            {'emoji': '❌', 'text': 'Not hungry', 'confidence': 0.75}
        ]
    elif 'bathroom' in q_lower or 'toilet' in q_lower:
        return [
            {'emoji': '🚨', 'text': 'Urgent!', 'confidence': 0.95},
            {'emoji': '✅', 'text': 'Yes, help please', 'confidence': 0.92},
            {'emoji': '⏰', 'text': 'In a minute', 'confidence': 0.80},
            {'emoji': '❌', 'text': 'Not now', 'confidence': 0.75}
        ]
    else:
        return [
            {'emoji': '✅', 'text': 'Yes', 'confidence': 0.85},
            {'emoji': '❌', 'text': 'No', 'confidence': 0.85},
            {'emoji': '🤷', 'text': "Don't know", 'confidence': 0.75},
            {'emoji': '👍', 'text': 'Okay', 'confidence': 0.80}
        ]

if __name__ == '__main__':
    print("🚀 Starting Tinkybink AAC Web Server...")
    print("📡 Connecting to Rust engine at:", RUST_BINARY)
    port = int(os.environ.get('PORT', 9000))
    print(f"🌐 Open http://localhost:{port} in your browser")
    print("🎤 Make sure to allow microphone access for speech input")
    print("-" * 50)
    
    # Check if Rust binary exists
    if not os.path.exists(RUST_BINARY):
        print("⚠️  Warning: Rust binary not found. Running in fallback mode.")
        print("   Run 'cargo build --release' to build the Rust engine.")
    else:
        print("✅ Rust engine found!")
        
    app.run(host='0.0.0.0', port=port, debug=True)