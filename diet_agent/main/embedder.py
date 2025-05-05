import pandas as pd
import json
from tqdm import tqdm
from models.embedding_model import EmbeddingModel
import os

# Dosya yolları
DATA_PATH = os.path.join("data", "diet_dataset.json")
OUTPUT_PATH = os.path.join("embeddings", "diet_embeddings.json")

# Veriyi oku
df = pd.read_json(DATA_PATH, encoding="utf-8")

# Modeli yükle
model = EmbeddingModel()

# Soru ve cevap embed işlemi
print("Soru ve cevap embedding işlemi başlatılıyor...")

output = []
for idx, row in tqdm(df.iterrows(), total=len(df)):
    soru_embedding = model.encode([row["Soru"]])[0].tolist()
    cevap_embedding = model.encode([row["Cevap"]])[0].tolist()
    
    output.append({
        "id": idx,
        "soru": row["Soru"],
        "cevap": row["Cevap"],
        "soru_embedding": soru_embedding,
        "cevap_embedding": cevap_embedding
    })

# Sonuçları kaydet
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("Embedding işlemi tamamlandı. Kayıt yeri:", OUTPUT_PATH)
