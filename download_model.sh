#!/bin/bash

# 🦙 TinkyBink AI Model Downloader
# Downloads free, open-source language models for child-like AAC responses

echo "🦙 TinkyBink AI Model Downloader"
echo "================================"
echo ""

# Create models directory if it doesn't exist
mkdir -p models

echo "Choose a model to download:"
echo "1) TinyLlama 1.1B (Recommended - 638MB) - Best for child-like responses"
echo "2) Phi-3 Mini 4K (3.8B parameters - 2.3GB) - More advanced but larger"
echo "3) TinyStories 33M (Very small - 65MB) - Fast but limited"
echo "4) OpenLlama 3B (1.5GB) - Good balance"
echo ""

read -p "Enter choice (1-4): " choice

case $choice in
    1)
        echo "📥 Downloading TinyLlama 1.1B..."
        curl -L https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
             -o models/tinyllama-1.1b-q4_k_m.gguf \
             --progress-bar
        echo "✅ TinyLlama downloaded to models/tinyllama-1.1b-q4_k_m.gguf"
        ;;
    2)
        echo "📥 Downloading Phi-3 Mini..."
        curl -L https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf \
             -o models/phi3-mini-q4.gguf \
             --progress-bar
        echo "✅ Phi-3 Mini downloaded to models/phi3-mini-q4.gguf"
        ;;
    3)
        echo "📥 Downloading TinyStories 33M..."
        curl -L https://huggingface.co/roneneldan/TinyStories-33M/resolve/main/model.safetensors \
             -o models/tinystories-33m.safetensors \
             --progress-bar
        echo "✅ TinyStories downloaded to models/tinystories-33m.safetensors"
        ;;
    4)
        echo "📥 Downloading OpenLlama 3B..."
        curl -L https://huggingface.co/SlyEcho/open_llama_3b_v2_gguf/resolve/main/open-llama-3b-v2-q4_K_M.gguf \
             -o models/openllama-3b-q4_k_m.gguf \
             --progress-bar
        echo "✅ OpenLlama 3B downloaded to models/openllama-3b-q4_k_m.gguf"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Model downloaded successfully!"
echo ""
echo "To use the AI model:"
echo "1. Build with AI feature: cargo build --features ai-candle"
echo "2. Run the demo: cargo run --features ai-candle demo"
echo ""
echo "The AI will automatically load the model and generate child-like responses!"