import json
import os
import random
# Dejar descomentado el import dependiendo de cual version del modelo quiero usar
from wim_llama2_model_replicate import ask_wim_model
# from wim_llama2_model_locally import ask_wim_model


# Configurar el arranque del juego
def configure_chat():
    chatbot = {}

    # Ruta a donde estan todos mis characters
    json_file_path = 'all_my_characters.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    all_characters_are_different = False
    share_attributes = False
    random_list_characters = []
    my_group_of_characters = {}

    while not (all_characters_are_different and share_attributes):
        # Seleccionar un numero de personajes, de los cuales elegire uno como el candidato
        random_list_characters = random.sample(list(data.keys()), 8)
        my_group_of_characters = {key: data[key] for key in random_list_characters if key in data}
        # Verifico que sean todos diferentes entre si
        all_characters_are_different = are_different_from_each_other(my_group_of_characters)
        # Verifico que por lo menos un par de personajes tengas dos atributos iguales
        share_attributes = have_shared_attributes(my_group_of_characters)

    # Seleccionar un personaje aleatorio del diccionario
    random_element_code = random.choice(random_list_characters)

    # Guardar la info de esta partida en `chatbot`
    chatbot['my_group_of_chars'] = my_group_of_characters
    chatbot['my_character'] = random_element_code
    chatbot['my_character_attributes'] = data[random_element_code]

    chatbot['my_character_in_one_line'] = character_attributes_in_a_sentence(chatbot['my_character_attributes'])
    print (chatbot['my_character_in_one_line'])

    return chatbot

def are_different_from_each_other(characters):
    for character_id, attributes in characters.items():
        for other_character_id, other_attributes in characters.items():
            if character_id != other_character_id:
                # Chequeo que por lo menos un atributo sea distinto
                if not any(attributes[attribute] != other_attributes[attribute] for attribute in attributes):
                    return False
    return True

def have_shared_attributes(characters):
    for character_id, attributes in characters.items():
        for other_character_id, other_attributes in characters.items():
            if character_id != other_character_id:
                shared_count = 0
                # Comparo los atributos de los personajes
                for attribute in attributes:
                    if attributes[attribute] == other_attributes.get(attribute):
                        shared_count += 1
                # Chequeo si comparten por lo menos 2 atributos
                if shared_count >= 2:
                    return True
    return False

def character_attributes_in_a_sentence(attributes_in_json):
    sentence = f"The person has {attributes_in_json['eye_color']} eyes, {attributes_in_json['face_color']} skin, and {attributes_in_json['hair_color']} hair."

    if attributes_in_json['glasses'] == 'yes glasses':
        sentence += f" They are wearing {attributes_in_json['glasses_color']} glasses."
    else:
        sentence += "They aren't wearing glasses."

    return sentence

def search_response(chatbot, question):
    return ask_wim_model(question, chatbot['my_character_in_one_line'])

def eliminate_candidate(chatbot, image_path):
    candidate_to_eliminate = os.path.basename(image_path).split('.')[0]
    chatbot['my_group_of_chars'].pop(candidate_to_eliminate)

    status = "Continue"
    if candidate_to_eliminate == chatbot['my_character']:
        status = "Game over"

    return chatbot, status
