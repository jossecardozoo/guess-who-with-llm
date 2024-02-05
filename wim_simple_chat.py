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
    chatbot['responses'] = {
        "hello": "Hello! How can I help you?",
        "goodbye": "Goodbye. Have a great day!"
    }

    # Ruta a donde estan todos mis characters
    json_file_path = 'all_my_characters.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Seleccionar nueve personajes, de los cuales elegire uno como el candidato
    random_list_characters = random.sample(list(data.keys()), 9)
    my_group_of_characters = {key: data[key] for key in random_list_characters if key in data}

    # Seleccionar un personaje aleatorio del diccionario
    random_element_code = random.choice(random_list_characters)

    # Guardar la info de esta partida en `chatbot`
    chatbot['my_group_of_chars'] = my_group_of_characters
    chatbot['my_character'] = random_element_code
    chatbot['my_character_attributes'] = data[random_element_code]
    del  chatbot['my_character_attributes']['image_file']

    chatbot['my_character_in_one_line'] = character_attributes_in_a_sentence(chatbot['my_character_attributes'])
    print (chatbot['my_character_in_one_line'])

    return chatbot

def character_attributes_in_a_sentence(attributes_in_json):
    sentence = f"The person has {attributes_in_json['eye_color']} eyes, {attributes_in_json['face_color']} skin, and {attributes_in_json['hair_color']} hair."

    if attributes_in_json['glasses'] == 'yes glasses':
        sentence += f" They are wearing {attributes_in_json['glasses_color']} glasses."
    else:
        sentence += "They aren't wearing glasses."

    return sentence

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
    # processed_question = preprocess_text(question)
    # print(processed_question)

    # Le pregunto a mi modelo si es correcta o no la pregunta en funcion de mi personaje elegido
    return ask_wim_model(question, chatbot['my_character_in_one_line'])

def find_criteria_by_question_and_aswer(user_question, bot_answer):
    criteria = {"eye_color": "green"}

    return criteria, True

def filter_candidates(candidates, criteria, include_matching=True):
    filtered_candidates = {}

    for candidate_id, attributes in candidates.items():
        meets_criteria = all(attributes.get(attribute, "") == value for attribute, value in criteria.items())

        if include_matching and meets_criteria:
            filtered_candidates[candidate_id] = attributes
        elif not include_matching and not meets_criteria:
            filtered_candidates[candidate_id] = attributes

    return filtered_candidates


# Main function
def run_chat():
    print("Hello! Let's start playing. Type 'goodbye' to exit.")
    
    chatbot = configure_chat()

    while True:
        user_question = input("Ask about my character: ")

        if user_question.lower() == 'goodbye':
            print("Goodbye. Have a great day!")
            break

        bot_response = search_response(chatbot, user_question)
        # Luego de obtener la respuesta, es aca donde deberia eliminar candidatos
        # print(chatbot['my_group_of_chars'])
        # criteria = {"eye_color": "green"} tiene que ser algo asi lo retorne mi funcion
        criteria, positive_or_negative_matching = find_criteria_by_question_and_aswer(user_question, bot_response)
        filtered_candidates = filter_candidates(chatbot['my_group_of_chars'], criteria, include_matching=positive_or_negative_matching)
        # print(filtered_candidates)
        print(bot_response)

if __name__ == "__main__":
    run_chat()
