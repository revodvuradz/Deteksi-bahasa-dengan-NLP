from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"

# Contoh teks dalam beberapa bahasa
texts = [
    "Hello, how are you?",
    "Bonjour, comment ça va?",
    "Hola, ¿cómo estás?",
    "Ciao, come stai?",
    "Привет, как дела?"
]

# Deteksi bahasa untuk setiap teks
for text in texts:
    language = detect_language(text)
    print("Teks:", text)
    print("Bahasa:", language)
    print()
