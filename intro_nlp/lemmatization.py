import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

words = ["Run", "Cat", "Good", "Goose", "Rock", "City", "Big", "Happy", "Run", "Sleep"]

for word in words:
    lemma_word = lemmatizer.lemmatize(word.lower())
    print(f"Kata asli: {word}, lematisasi: {lemma_word}")