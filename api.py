from flask import Flask, request, jsonify, render_template
from wim_simple_chat import configure_chat, search_response, eliminate_candidate
import os

app = Flask(__name__)

# Variable global para almacenar la configuración del chatbot
chatbot_config = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['GET'])
def start_game():
    global chatbot_config
    chatbot_config = configure_chat()  # Guarda la configuración del chatbot en la variable global

    return jsonify({'message': 'El juego ha comenzado.'})

@app.route('/get_image_paths', methods=['GET'])
def get_image_paths():
    global chatbot_config
    # Extrae los valores de 'image_file' de cada candidato y los coloca en un array
    image_paths = ['/static/images/{}.png'.format(str(candidate_info['image_file'])) for candidate_info in chatbot_config['my_group_of_chars'].values()]

    return jsonify(image_paths)

@app.route('/ask', methods=['POST'])
def ask():
    global chatbot_config
    if chatbot_config is None:
        return jsonify({'error': 'El chatbot no está configurado todavía.'}), 500

    user_question = request.json['question']
    bot_response = search_response(chatbot_config, user_question)  # Usa la función de tu chatbot para obtener la respuesta
    return jsonify({'response': bot_response})

# Ruta para descartar candidatos
@app.route('/image_clicked', methods=['POST'])
def image_clicked():
    global chatbot_config
    # Obtener el src de la imagen desde el cuerpo de la solicitud
    src = request.json['src']

    new_chatbot_config, status = eliminate_candidate(chatbot_config, src)
    chatbot_config = new_chatbot_config

    return jsonify({'message': status})

##### Mejorar este metodo para que no hagas cosas, sino que llame una funcion nomas
@app.route('/select_character', methods=['POST'])
def select_character():
    global chatbot_config
    image_url = request.json['imageUrl']

    selected_char = os.path.basename(image_url).split('.')[0]
    is_the_correct = "Correct" if selected_char == chatbot_config['my_character'] else "Incorrect"
    # is_the_correct = eliminate_candidate(chatbot_config, imageUrl)

    return jsonify({'message': is_the_correct})

if __name__ == '__main__':
    app.run(debug=True)