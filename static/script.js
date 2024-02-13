// function sendMessage() {
//     var userInput = document.getElementById("userInput").value;

//     fetch('/ask', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ question: userInput }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         var chatbox = document.getElementById("chatbox");
//         chatbox.innerHTML += "<p>Chatbot: " + data.response + "</p>";
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });

//     // Limpiar el campo de entrada
//     document.getElementById("userInput").value = "";
// }

function startGame() {
    console.log("holaaaaaa");
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
    console.log("llegue la sendmessage");
    console.log(userInput)

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        var chatbox = document.getElementById("chatbox");
        chatbox.innerHTML += "<p>Chatbot: " + data.response + "</p>";
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Limpiar el campo de entrada
    document.getElementById("userInput").value = "";
}
