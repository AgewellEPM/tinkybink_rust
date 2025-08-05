#!/bin/bash
# Ultimate TinkyBink AAC Master Model Training
# Uses 523 training examples with comprehensive logic trees

cd "$(dirname "$0")"

echo "🎓 Training Ultimate TinkyBink AAC Master Model"
echo "============================================="
echo "📊 Master Dataset: 523 examples"
echo "   - 60 child conversation examples"
echo "   - 111 adult/medical examples"  
echo "   - 47 basic logic tree examples"
echo "   - 305 advanced logic tree examples from 50 JSON files"
echo "🌳 69 comprehensive decision trees"
echo "🧠 Advanced logic reasoning capabilities"
echo ""

# Check Ollama status
echo "🔍 Checking Ollama status..."
if ! pgrep ollama > /dev/null; then
    echo "⚠️  Starting Ollama..."
    nohup ollama serve > ollama.log 2>&1 &
    sleep 3
fi

# Ensure base model exists
echo "📦 Verifying tinyllama base model..."
if ! ollama list | grep -q tinyllama; then
    echo "📥 Downloading tinyllama..."
    ollama pull tinyllama
fi

# Remove any existing tinkybink model
if ollama list | grep -q "tinkybink"; then
    echo "🗑️  Removing existing tinkybink model..."
    ollama rm tinkybink
fi

# Create the ultimate model
echo ""
echo "🚀 Creating TinkyBink Ultimate AAC Master Model..."
echo "🧠 Features:"
echo "   ✅ Advanced logic tree reasoning"
echo "   ✅ Context-aware decision making"
echo "   ✅ Multi-user type adaptation" 
echo "   ✅ 50+ AAC category coverage"
echo "   ✅ Medical/therapeutic specialization"
echo ""

ollama create tinkybink -f Modelfile.tinkybink_ultimate

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! TinkyBink Ultimate Master Model Created!"
    echo ""
    echo "📋 Model Specifications:"
    ollama show tinkybink | head -20
    echo ""
    echo "🧪 Testing Ultimate Logic Capabilities..."
    echo ""
    
    # Test different logic scenarios
    echo "🔬 Test 1: Yes/No Question Logic"
    echo "Do you want to play outside?" | ollama run tinkybink --verbose=false
    echo ""
    
    echo "🔬 Test 2: Medical Context Logic"
    echo "How are you feeling after therapy?" | ollama run tinkybink --verbose=false  
    echo ""
    
    echo "🔬 Test 3: Choice Question Logic"
    echo "Would you like juice, water, or milk?" | ollama run tinkybink --verbose=false
    echo ""
    
    echo "🔬 Test 4: Adult Professional Context"  
    echo "Are you ready for the meeting?" | ollama run tinkybink --verbose=false
    echo ""
    
    echo "✨ Ultimate TinkyBink AAC Master Model is ready!"
    echo ""
    echo "🎯 Capabilities:"
    echo "   • Logic tree reasoning with 69 decision trees"
    echo "   • Contextual awareness across 50+ AAC categories"
    echo "   • Adaptive responses for all user types"
    echo "   • Medical/therapeutic specialization"
    echo "   • Comprehensive communication coverage"
    echo ""
    echo "🚀 Usage:"
    echo "   CLI: ollama run tinkybink"
    echo "   App: cargo run demo (will auto-detect and use)"
    
else
    echo "❌ Model creation failed. Check ollama.log"
    exit 1
fi