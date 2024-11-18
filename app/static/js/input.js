// Seleciona o elemento de entrada de usuário
const userInput = document.getElementById('user-input');

// Ajusta a altura do textarea automaticamente, limitando a 100px
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    const newHeight = Math.min(this.scrollHeight, 150); // Limita a altura em 150px
    this.style.height = newHeight + 'px';

    // Define overflow com base na altura do conteúdo
    this.style.overflowY = newHeight >= 150 ? 'scroll' : 'hidden';
});

// Função para enviar mensagem e redefinir o tamanho do textarea
function sendMessage() {
    const messageContent = userInput.value.trim();
    if (!messageContent) return;

    // Configuração da janela de chat
    const chatWindow = document.getElementById("chat-window");
    const messageDiv = document.createElement("div");
    messageDiv.className = "message user-message";

    // Adiciona o conteúdo da mensagem
    const messageText = document.createElement("p");
    messageText.textContent = messageContent;
    messageDiv.appendChild(messageText);
    chatWindow.appendChild(messageDiv);

    // Atualiza a rolagem e redefinição de estilo
    chatWindow.scrollTop = chatWindow.scrollHeight;
    userInput.style.height = '40px';
    userInput.style.overflowY = 'hidden';
    userInput.value = ""; // Limpa o input

    // Envia a mensagem via RocketIO (substitua 'chat' pelo nome correto do canal)
    RocketIO.emit('newMessage', { content: messageContent });
}

// Adiciona evento de tecla Enter para enviar a mensagem
document.addEventListener("DOMContentLoaded", () => {
    userInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });

    // Escuta mensagens recebidas em RocketIO
    RocketIO.on('messageReceived', (data) => {
        const chatWindow = document.getElementById("chat-window");
        const messageDiv = document.createElement("div");
        messageDiv.className = "message received-message";

        const messageText = document.createElement("p");
        messageText.textContent = data.content;
        messageDiv.appendChild(messageText);
        chatWindow.appendChild(messageDiv);

        // Atualiza a rolagem para a última mensagem recebida
        chatWindow.scrollTop = chatWindow.scrollHeight;
    });
});
