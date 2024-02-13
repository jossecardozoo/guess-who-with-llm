// Agrega un event listener para el evento 'keypress' en el campo de entrada
document.getElementById("userInput").addEventListener("keypress", function(event) {
    // Verifica si la tecla presionada es 'Enter' (código 13)
    if (event.key === "Enter") {
        sendMessage(); // Llama a la función para enviar el mensaje
    }
});

function startGame() {
    document.getElementById("inputArea").style.display = "block";

    fetch('/start_game')
    .then(response => response.text())
    .then(data => {
      console.log(data); // Imprimirá el resultado de la función en la consola del navegador
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    addQuestion(userInput); // Agrega la pregunta del usuario al chatbox

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        addResponse(data.response); // Agrega la respuesta del chatbot al chatbox
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Limpiar el campo de entrada
    document.getElementById("userInput").value = "";
}

function addQuestion(question) {
    var chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<p>You: " + question + "</p>";
}

function addResponse(response) {
    var chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<p>Chatbot: " + response + "</p>";
}
