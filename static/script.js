// Agrega un event listener para el evento 'keypress' en el campo de entrada
document.getElementById("userInput").addEventListener("keypress", function(event) {
    // Verifica si la tecla presionada es 'Enter'
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
      loadImages(); // Llama a la función para cargar las imágenes
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

// Función para cargar las imágenes desde el backend
function loadImages() {
    fetch('/get_image_paths')
    .then(response => response.json())
    .then(imagePaths => {
        var imageGallery = document.getElementById("imageGallery");
        imagePaths.forEach((imagePath, index) => {
            var img = document.createElement("img");
            img.src = imagePath;
            img.className = "clickable";

            var gridItem = document.createElement("div");
            gridItem.className = "grid-item";
            gridItem.appendChild(img);

            imageGallery.appendChild(gridItem);
        });

        // Listener de clics para que se desactiven los characters a volutad del usuario
        var images = document.querySelectorAll('.clickable');
        images.forEach(function(image) {
            image.addEventListener('click', function() {
                console.log("Pude hacerle click");
                image.className = "no-my-character";
            });
        });

    })
    .catch(error => {
        console.error('Error:', error);
    });
}