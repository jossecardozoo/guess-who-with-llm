import nltk
nltk.download('punkt')
nltk.download('stopwords')

# from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktTrainer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

pregunta = "Is a woman? Or is a man?"
tokenize_pregunta = word_tokenize(pregunta)

print(tokenize_pregunta)

english_sw = set(stopwords.words('english'))

print(english_sw)

# Me falta definir de donde sacar el corpus para entrenar mi modelo
# corpus = "hola"
# trainer = PunktTrainer()
# trainer.train(corpus, finalize=False, verbose=True)