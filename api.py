from flask import Flask, request, jsonify, render_template
from wim_simple_chat import search_response, configure_chat  # Importa la función de tu chatbot

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

if __name__ == '__main__':
    app.run(debug=True)