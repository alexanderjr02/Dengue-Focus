function sendImage() {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";

    input.onchange = function (event) {
        const file = event.target.files[0];
        if (!file) return;

        // Validar tipo e tamanho da imagem
        if (!file.type.startsWith("image/")) {
            alert("Por favor, selecione um arquivo de imagem.");
            return;
        }
        if (file.size > 5 * 1024 * 1024) { // Limitar tamanho a 5MB
            alert("A imagem é muito grande! Por favor, selecione uma menor.");
            return;
        }

        // Mostrar a imagem no chat antes de enviar
        const reader = new FileReader();
        reader.onloadend = function () {
            const imageUrl = reader.result;

            // Adicionar a imagem ao chat
            const chatWindow = document.getElementById("chat-window");
            const messageDiv = document.createElement("div");
            messageDiv.className = "message user-message";

            const imageElement = document.createElement("img");
            imageElement.src = imageUrl;
            imageElement.alt = "Imagem enviada pelo usuário";
            imageElement.style.maxWidth = "200px"; // Ajustar o tamanho da imagem
            imageElement.style.borderRadius = "8px";

            messageDiv.appendChild(imageElement);
            chatWindow.appendChild(messageDiv);
            chatWindow.scrollTop = chatWindow.scrollHeight;

            // Enviar a imagem ao servidor via Socket.IO
            socket.emit("send_image", { image: imageUrl });
        };

        reader.readAsDataURL(file);
    };

    input.click();
}

// Receber e exibir a imagem no chat (do servidor)
socket.on("receive_image", function (data) {
    const chatWindow = document.getElementById("chat-window");
    const messageDiv = document.createElement("div");
    messageDiv.className = "message bot-message";

    const imageElement = document.createElement("img");
    imageElement.src = data.image; // URL da imagem recebida
    imageElement.alt = "Imagem enviada pelo bot";
    imageElement.style.maxWidth = "200px"; // Ajustar o tamanho da imagem
    imageElement.style.borderRadius = "8px";

    messageDiv.appendChild(imageElement);
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
});
