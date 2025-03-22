from asl_processor_flant5 import convert_to_asl_grammar as flan_t5_convert
from bart_model.asl_processor import convert_to_asl_grammar as bart_convert

samples = [
    "Where is the bathroom?",
    "I am learning sign language.",
    "Can you help me?",
    "What is your name?",
    "I feel sick."
]

print("\nComparison of BART vs Flan-T5 for ASL Grammar:\n")

for sentence in samples:
    flan_out = flan_t5_convert(sentence)
    bart_out = bart_convert(sentence)

    print(f"English: {sentence}")
    print(f"BART:    {bart_out}")
    print(f"Flan-T5: {flan_out}\n")
