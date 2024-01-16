import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import json
import random
from wim_model_using_llama2 import ask_wim_model

nltk.download('punkt')
nltk.download('stopwords')

# Configurar el chat
def configure_chat():
    chatbot = {}

    # Algunas respuestas para probar esta parte, la idea esq aca solo se defina cual es el peronaje a adivinar,
    # las respuestas van a ser dadas luego por el modelo entrenado.
    responses = {
        "hello": "Hello! How can I help you?",
        "goodbye": "Goodbye. Have a great day!",
        "Is your hair color blue?":"Yes",
        "Are your eyes brown?": "No"
    }
    chatbot['responses'] = responses

    # Ruta a donde estan todos mis characters
    json_file_path = 'all_my_characters.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Seleccionar un personaje aleatorio del diccionario
    random_element = random.choice(list(data.keys()))
    print(random_element)
    print(data[random_element])
    chatbot['my_character'] = random_element
    chatbot['my_character_attributes'] = data[random_element]

    return chatbot

# preprocesar la pregunta para que me quede todo como un conjunto de palabras -> CAPAZ NO ES NECESARIO HACERLO
def preprocess_text(question):
    # Tokenizar
    words = word_tokenize(question.lower())

    # Sacar las stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return words

# preguntarle al modelo la respuesta con la pregunta ya preprocesada
def search_response(chatbot, question):
    processed_question = preprocess_text(question)
    print(processed_question)

    # Le pregunto a mi modelo si es correcta o no la pregunta en funcion de mi personaje elegido
    # Tengo que encontrar la forma de pasar los atributos de mi personaje elegido a una oracion como la que esta abajo.
    #  "eye_color","face_color", "hair_color", "glasses", "glasses_color", "eyebrow_width"
    character = "eye color is green, face color is black, hair color is blue, i have glasses, my glasses color is black"
    return ask_wim_model(question, character)

# Main function
def run_chat():
    print("Hello! Let's start playing. Type 'goodbye' to exit.")
    
    chatbot = configure_chat()

    while True:
        user_question = input("User: ")

        if user_question.lower() == 'goodbye':
            print("Goodbye. Have a great day!")
            break

        bot_response = search_response(chatbot, user_question)
        print("Chat:", bot_response)

if __name__ == "__main__":
    run_chat()
