 - Diet Agent 

Bu proje, diyetle ilgili soru-cevap verilerini embedding (vektörleştirme) formatına  dönüştürerek daha sonra benzerlik 
karşılaştırmaları ya da bilgi sorgulamaları için kullanılabilir hale getirir.


*KULLANILAN TEKNOLOJİLER VE NEDENLERİ* 

- Python (pandas, json, tqdm) -> Veri manipülasyonu, JSON dosyalarını okuyup yazmak ve işlem sürecini izlemek için kullanıldı. 
- sentence-transformers (all-MiniLM-L6-v2) -> Küçük ama güçlü, hızlı çalışan, çok iyi sonuçlar veren bir dil modeli. Özellikle embedding işlemleri için optimize edilmiştir. 
- Custom Model Class (models/embedding_model.py) -> Modeli dışarıdan bağımsız olarak yüklemek ve yeniden kullanılabilir hale getirmek için yazıldı. Proje yapısını daha düzenli kılar. 
- Embeddings (JSON formatında) -> Vektör çıktıları daha sonra kullanılabilmek üzere '.json' formatında saklanır. Bu format, sistemler arası veri alışverişi için uygundur.

## 📁 Proje Yapısı

.
├── data/                    # Girdi veri dosyaları
│   └── diet_dataset.json
│
├── embeddings/              # Embed edilmiş sonuçlar
│   └── diet_embeddings.json
│
├── main/                    # Uygulama akışını yürüten dosyalar
│   ├── embedder.py
│
├── models/                  # Model sınıfları ve yardımcı modüller
│   └── embedding_model.py
│
├── README.md



- Model olarak all-MiniLM-L6-v2 seçilmesinin nedeni, hem hızlı hem de çok güçlü sonuçlar vermesidir.

- Embedding için json formatı tercih edildi çünkü veri paylaşımı ve kontrolü açısından daha şeffaftır.

- Eğer ilerleyen süreçte daha büyük bir veri ile çalışacak olursak, embedding verilerini .pkl ile saklamak daha verimli olabilir.
