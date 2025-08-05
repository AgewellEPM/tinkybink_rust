#!/usr/bin/env python3
"""
Train TinkyBink Small Language Model
Fine-tunes a small base model for AAC-specific responses
"""

import os
import json
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import Dataset
import numpy as np

# Base models suitable for AAC (small, fast, efficient)
BASE_MODELS = {
    "tinyllama": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "phi": "microsoft/phi-2", 
    "opt": "facebook/opt-350m",
    "pythia": "EleutherAI/pythia-410m",
    "bloom": "bigscience/bloom-560m"
}

class AACDataset:
    """Custom dataset for AAC training"""
    
    def __init__(self, filepath):
        self.examples = []
        with open(filepath, 'r') as f:
            for line in f:
                self.examples.append(json.loads(line))
    
    def format_for_training(self, tokenizer):
        """Format examples for causal language modeling"""
        formatted = []
        
        for ex in self.examples:
            # Create conversational format
            text = f"""### Instruction:
{ex['instruction']}

### Input:
{ex['input']}

### Response:
{ex['output']}"""
            
            # Tokenize
            encoded = tokenizer(
                text,
                truncation=True,
                padding="max_length",
                max_length=256,  # Keep short for AAC
                return_tensors="pt"
            )
            
            formatted.append({
                'input_ids': encoded['input_ids'].squeeze(),
                'attention_mask': encoded['attention_mask'].squeeze(),
                'labels': encoded['input_ids'].squeeze()  # For CLM
            })
        
        return formatted

def load_base_model(model_name="tinyllama"):
    """Load a small base model suitable for AAC"""
    model_path = BASE_MODELS.get(model_name, BASE_MODELS["tinyllama"])
    
    print(f"📥 Loading base model: {model_path}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,  # Use FP16 for efficiency
        device_map="auto"
    )
    
    # Add padding token if needed
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    return model, tokenizer

def create_training_args(output_dir="./tinkybink-slm"):
    """Training arguments optimized for small AAC model"""
    return TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=100,
        learning_rate=2e-5,
        fp16=True,  # Mixed precision
        logging_steps=10,
        save_steps=500,
        eval_steps=100,
        evaluation_strategy="steps",
        save_strategy="steps",
        load_best_model_at_end=True,
        push_to_hub=False,
        optim="adamw_torch",
        gradient_checkpointing=True,  # Save memory
        report_to=["tensorboard"],
    )

def train_tinkybink_model():
    """Main training function"""
    print("🚀 Starting TinkyBink SLM Training")
    print("==================================\n")
    
    # Load model and tokenizer
    model, tokenizer = load_base_model("tinyllama")
    
    # Load datasets
    print("📊 Loading training data...")
    train_dataset = AACDataset("tinkybink_train.jsonl")
    train_data = train_dataset.format_for_training(tokenizer)
    
    val_dataset = AACDataset("tinkybink_val.jsonl")
    val_data = val_dataset.format_for_training(tokenizer)
    
    # Convert to HuggingFace Dataset
    train_ds = Dataset.from_list(train_data)
    val_ds = Dataset.from_list(val_data)
    
    print(f"Training samples: {len(train_ds)}")
    print(f"Validation samples: {len(val_ds)}")
    
    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,  # Causal LM
    )
    
    # Training arguments
    training_args = create_training_args()
    
    # Create trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=data_collator,
        tokenizer=tokenizer,
    )
    
    # Train!
    print("\n🏋️ Training model...")
    trainer.train()
    
    # Save final model
    print("\n💾 Saving trained model...")
    trainer.save_model("./tinkybink-slm-final")
    tokenizer.save_pretrained("./tinkybink-slm-final")
    
    print("\n✅ Training complete!")
    
    # Test the model
    test_model(model, tokenizer)

def test_model(model, tokenizer):
    """Test the trained model with sample inputs"""
    print("\n🧪 Testing trained model...")
    
    test_inputs = [
        "Parent says: 'Do you want to go outside?'",
        "Parent says: 'Time for dinner'",
        "Parent says: 'How are you feeling?'"
    ]
    
    model.eval()
    
    for test_input in test_inputs:
        prompt = f"""### Instruction:
You are a nonverbal child using AAC tiles to communicate. Give 4 short responses.

### Input:
{test_input}

### Response:"""
        
        inputs = tokenizer(prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=50,
                temperature=0.7,
                do_sample=True,
                top_p=0.9,
                pad_token_id=tokenizer.pad_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.split("### Response:")[-1].strip()
        
        print(f"\n📥 Input: {test_input}")
        print(f"📤 Output: {response}")

def convert_to_gguf(model_path="./tinkybink-slm-final", quantization="Q4_K_M"):
    """Convert to GGUF format for use with llama.cpp/Ollama"""
    print("\n🔧 Converting to GGUF format...")
    
    # This would use llama.cpp's convert script
    convert_script = """
# Install llama.cpp if not already installed
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make

# Convert to GGUF
python convert.py {model_path} --outtype f16 --outfile tinkybink-slm.gguf

# Quantize for efficiency  
./quantize tinkybink-slm.gguf tinkybink-slm-{quantization}.gguf {quantization}
    """.format(model_path=model_path, quantization=quantization)
    
    print("Run these commands to convert:")
    print(convert_script)
    
    # Create Ollama Modelfile
    modelfile = f"""FROM ./tinkybink-slm-{quantization}.gguf

TEMPLATE "\"\"{{ .System }}
Parent: {{ .Prompt }}
Child: "\""

SYSTEM "\"\"You are a nonverbal child using an AAC device. Respond with 4 simple, child-like options separated by commas. Use emotions and be natural."\""

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER stop "Parent:"
"""
    
    with open("Modelfile.tinkybink", "w") as f:
        f.write(modelfile)
    
    print("\n📦 Modelfile created! To use with Ollama:")
    print("ollama create tinkybink -f Modelfile.tinkybink")

if __name__ == "__main__":
    # First generate the dataset
    os.system("python prepare_dataset.py")
    
    # Then train the model
    train_tinkybink_model()
    
    # Convert for deployment
    convert_to_gguf()
    
    print("\n🎉 TinkyBink SLM is ready!")
    print("Use with: ollama run tinkybink")