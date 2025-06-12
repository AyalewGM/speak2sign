"""Utilities for converting English text to ASL grammar."""

import os
from transformers import pipeline

# Resolve the model path relative to this file so the module works
# regardless of the current working directory.
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models", "asl_flan_t5")

# Create the text2text-generation pipeline
asl_converter = pipeline("text2text-generation", model=MODEL_DIR)


def convert_to_asl_grammar(text: str) -> str:
    """Convert English sentence to ASL-friendly grammar using the fine-tuned model."""
    prompt = f"Convert to ASL grammar: {text}"
    result = asl_converter(prompt, max_length=50)
    return result[0]["generated_text"].strip().upper()
