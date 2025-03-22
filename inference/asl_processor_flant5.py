from transformers import pipeline

asl_converter = pipeline("text2text-generation", model="models/asl_flan_t5")

def convert_to_asl_grammar(text):
    prompt = f"Convert to ASL grammar: {text}"
    result = asl_converter(prompt, max_length=50)
    return result[0]['generated_text'].strip().upper()
