import pandas as pd
import requests
import zipfile
import os

def download_and_extract():
    url = "https://achrafothman.net/aslg-pc12.zip"
    zip_path = "aslg_pc12.zip"
    extract_dir = "aslg_pc12_raw"

    r = requests.get(url)
    with open(zip_path, "wb") as f:
        f.write(r.content)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir

def format_to_csv(folder):
    txt_path = os.path.join(folder, "ASLG-PC12.txt")
    if not os.path.exists(txt_path):
        raise FileNotFoundError("ASLG-PC12.txt not found in extracted folder.")

    english_sentences = []
    asl_glosses = []

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            if " ||| " in line:
                en, asl = line.strip().split(" ||| ")
                if en and asl:
                    english_sentences.append(en)
                    asl_glosses.append(asl)

    df = pd.DataFrame({"source": english_sentences, "target": asl_glosses})
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/asl_data.csv", index=False)

if __name__ == "__main__":
    folder = download_and_extract()
    format_to_csv(folder)
