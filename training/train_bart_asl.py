from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset, Dataset
import pandas as pd
import torch

# Check for GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load data
df = pd.read_csv("asl_data.csv")
dataset = Dataset.from_pandas(df)

# Load tokenizer/model
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-base").to(device)

# Tokenization
def tokenize(example):
    inputs = tokenizer(example["source"], max_length=64, padding="max_length", truncation=True)
    targets = tokenizer(example["target"], max_length=64, padding="max_length", truncation=True)
    inputs["labels"] = targets["input_ids"]
    return inputs

tokenized_dataset = dataset.map(tokenize)

# Training Arguments
training_args = TrainingArguments(
    output_dir="./asl_bart",
    per_device_train_batch_size=8,
    num_train_epochs=5,
    logging_dir="./logs",
    logging_steps=50,
    save_steps=200,
    save_total_limit=2,
    learning_rate=3e-5,
    evaluation_strategy="no",
    fp16=True if device == "cuda" else False
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train!
trainer.train()

# Save model & tokenizer
trainer.save_model("./asl_bart")
tokenizer.save_pretrained("./asl_bart")
print("✅ Model saved in ./asl_bart")
