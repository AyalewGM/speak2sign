from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

df = pd.read_csv("data/asl_data.csv")
dataset = Dataset.from_pandas(df)

model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

def tokenize(examples):
    inputs = [f"Convert to ASL grammar: {text}" for text in examples["source"]]
    model_inputs = tokenizer(inputs, max_length=64, truncation=True, padding="max_length")

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["target"], max_length=64, truncation=True, padding="max_length")

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(tokenize, batched=True)

training_args = TrainingArguments(
    output_dir="models/asl_flan_t5",
    per_device_train_batch_size=8,
    num_train_epochs=5,
    logging_steps=100,
    save_steps=300,
    save_total_limit=2,
    learning_rate=2e-5,
    fp16=True if device == "cuda" else False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
trainer.save_model("models/asl_flan_t5")
tokenizer.save_pretrained("models/asl_flan_t5")
