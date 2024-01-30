document.addEventListener("DOMContentLoaded", function () {
    const imageGrid = document.getElementById("imageGrid");
    const imageUrls = [
        'cs10065197235784861270',
        'cs11113165137709367664',
        'cs10131430475235060387',
        'cs11489751240431094365',
        'cs10517948723543062881',
        'cs10318546961320557133',
        'cs10338286289857586298',
        'cs11183146375700363284',
        'cs10972212930033894264'
    ];

    // Create image elements and append them to the grid
    imageUrls.forEach(function (imageUrl) {
        const imageContainer = document.createElement("div");
        imageContainer.classList.add("imageContainer");

        const image = document.createElement("img");
        image.src = "../DataSet/cartoonset10k/" + imageUrl + ".png";
        // /Users/anaclara/Desktop/Fing/Tesis/DataSet/cartoonset10k

        imageContainer.appendChild(image);
        imageGrid.appendChild(imageContainer);
    });
});
