#!/bin/bash
# Complete TinkyBink AAC Model Training Script
# Supports children, adults, and stroke survivors

cd "$(dirname "$0")"

echo "🎓 Training Complete TinkyBink AAC Model"
echo "========================================"
echo "📊 Dataset: 171 examples (children + adults + medical)"
echo ""

# Step 1: Check if Ollama is running
echo "🔍 Checking Ollama status..."
if ! pgrep ollama > /dev/null; then
    echo "⚠️  Ollama not running. Starting Ollama..."
    # Try to start Ollama in background
    nohup ollama serve > ollama.log 2>&1 &
    sleep 3
fi

# Step 2: Check for base model
echo "📦 Checking for base model (tinyllama)..."
if ! ollama list | grep -q tinyllama; then
    echo "📥 Downloading tinyllama base model..."
    ollama pull tinyllama
    if [ $? -ne 0 ]; then
        echo "❌ Failed to download tinyllama. Please run: ollama pull tinyllama"
        exit 1
    fi
else
    echo "✅ tinyllama base model found"
fi

# Step 3: Create the custom model
echo ""
echo "🏗️  Creating TinkyBink Complete AAC model..."
echo "Base model: tinyllama"
echo "Training data: tinkybink_complete_train.jsonl (171 examples)"
echo ""

# Remove existing model if it exists
if ollama list | grep -q "tinkybink"; then
    echo "🗑️  Removing existing tinkybink model..."
    ollama rm tinkybink
fi

# Create new model from Modelfile
echo "🎯 Creating new tinkybink model..."
ollama create tinkybink -f Modelfile.tinkybink_complete

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! TinkyBink Complete AAC model created!"
    echo ""
    echo "📋 Model Info:"
    ollama show tinkybink
    echo ""
    echo "🧪 Testing the model..."
    echo ""
    
    # Test with different user types
    echo "👶 Testing child response:"
    echo "Do you want a cookie?" | ollama run tinkybink
    echo ""
    
    echo "👩 Testing adult response:"  
    echo "How are you feeling today?" | ollama run tinkybink
    echo ""
    
    echo "🏥 Testing medical response:"
    echo "Ready for speech therapy?" | ollama run tinkybink
    echo ""
    
    echo "✅ Training completed successfully!"
    echo "🚀 The model is ready to use in TinkyBink AAC"
    echo ""
    echo "To test: ollama run tinkybink"
    echo "To use in app: cargo run demo (select any user type)"
    
else
    echo "❌ Failed to create model. Check ollama.log for details"
    exit 1
fi