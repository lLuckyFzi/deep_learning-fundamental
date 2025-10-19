import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "runs", "runner", "ran", "easily", "fairness", "better", "best", "cats", "cacti", "geese", "rocks", "oxen"]

for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"Kata asli: {word}, kata setelah stemming: {stemmed_word}")