#Librerias de procesamiento natural de lenguaje (NLP / Natural Language Processing)
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Verificar si es necesairo descargar algun fichero necesario
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    #Descargar si es necesario
    nltk.download('vader_lexicon')

comentarios_prueba = [
    "I love this product! It's amazing.",
    "This is the worst experience ever.",
    "I'm not sure how I feel about this.",
    "I love it!.",
    "Fuck off!."
]

def evaluarPolaridad(polaridad):
    if polaridad >= 0.05:
        return "Positivo"
    elif polaridad <= -0.05:
        return "Negativo"
    else:
        return "Neutral"
    
def analizarSentimientosIngles():
    for comentario in comentarios_prueba:
        analizador = SentimentIntensityAnalyzer() #Instancia
        analisis = analizador.polarity_scores(comentario)
        print(f"Texto: '{comentario}'")
        print(f"Evaluacion total: {evaluarPolaridad(analisis['compound'])}")
        print(f"Positividad: {analisis['pos']:.2f}")
        print(f"Neutralidad: {analisis['neu']:.2f}")
        print(f"Negatividad: {analisis['neg']:.2f}")
        print()

