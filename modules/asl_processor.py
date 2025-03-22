from transformers import pipeline

asl_converter = pipeline("text2text-generation", model="./asl_bart")

def convert_to_asl_grammar(text):
    result = asl_converter(text, max_length=50)
    return result[0]['generated_text'].strip().upper()