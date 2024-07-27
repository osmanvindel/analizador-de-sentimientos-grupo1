from transformers import pipeline # Libreria desarrollada por Hugging Face. Herramienta para el procesamiento de lenguaje natural (NLP)

# Crear el pipeline para el análisis de sentimientos, sirve para la abstraccion del procesamiento del modelo
evaluar_comentario = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

def analizarComentario(comentario):
    # Obtener el resultado del análisis de sentimientos
    resultado = evaluar_comentario(comentario)
    return resultado[0]['label'], resultado[0]['score']

"""
-- EVALUACION DEL MODELO --
1 star: Muy negativo
2 stars: Negativo
3 stars: Neutral
4 stars: Positivo
5 stars: Muy positivo

-- WEB --
https://huggingface.co/

-- RECURSO --
https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment

-- PRESICION --
En el idioma español presenta un 58% segun la evaluacion exacta del modelo y 
95% de diferencia entre la evaluacion del modelo y el criterio del humano (reviewer)
"""

# Lista de comentarios en español para analizar (Prueba)
"""
comentarios = [
    "¡Horrible! No funciona para nada y es un desperdicio de dinero.",
    "No está mal, pero podría ser mucho mejor. Algo decepcionante.",
    "Es un producto promedio. No está mal, pero tampoco es excelente.",
    "Muy bueno. Cumple con la mayoría de mis expectativas y lo recomendaría.",
    "¡Excelente! Superó todas mis expectativas y lo recomiendo sin dudarlo."
]
"""

# Analizar cada comentario
def analizarSentimientoEspanol(comentarios):
    for comentario in comentarios:
        texto_comentario = comentario[0]
        label, score = analizarComentario(texto_comentario)
        print(f"Comentario: {texto_comentario}")
        print(f"Etiqueta de Sentimiento: {label}")
        print(f"Puntuación: {score:.2f}")
        print()  # Línea en blanco para separar los comentarios


