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

                // Enviar una solicitud POST al backend con el src de la imagen
                var src = image.getAttribute('src');
                fetch('/image_clicked', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ src: src }),
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message); // Imprimirá el resultado de la función en la consola del navegador
                    if (data.message === "Game over") {
                        var modal = document.getElementById('gameOverModal');
                        modal.style.display = 'flex'; // Cambia la propiedad display para mostrar el modal
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });

            });
        });

    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// // Obtener el modal
// var modal = document.getElementById("gameOverModal");

// // Obtener el botón para cerrar el modal
// var span = document.getElementsByClassName("close")[0];

// // Cuando el usuario hace click en cualquier lugar fuera del modal, lo cierra
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

// // Cuando el usuario hace click en el botón de cerrar, lo cierra
// span.onclick = function() {
//   modal.style.display = "none";
// }

// Cuando el usuario hace click en el botón de jugar de nuevo, lo cierra y reinicia el juego
document.getElementById("playAgainButton").onclick = function() {
    console.log("llegue al boton volver a jugar");
    var modal = document.getElementById("gameOverModal");
    modal.style.display = "none";
    // startGame();
    window.location.reload();
}
