from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize

factory = StopWordRemoverFactory()
stopwords_sastrawi = factory.get_stop_words()

teks = "Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan."

tokens_kata = word_tokenize(teks)

kata_penting = [kata for kata in tokens_kata if kata.lower() not in stopwords_sastrawi]

teks_tanpa_stopwords = ' '.join(kata_penting)

print("Teks asli: ", teks)
print("Teks setelah filtering stopwords Sastrawi: ", teks_tanpa_stopwords)