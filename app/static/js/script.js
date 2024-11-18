// Inicializa o socket
const socket = io();

// Elemento de entrada do usuário
const userInput = document.getElementById('user-input');

// Ajusta a altura do textarea automaticamente
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    const newHeight = Math.min(this.scrollHeight, 150);
    this.style.height = newHeight + 'px';
    this.style.overflowY = newHeight >= 150 ? 'scroll' : 'hidden';
});

// Função para enviar mensagem
function sendMessage() {
    const messageContent = userInput.value.trim();

    if (messageContent) {
        const chatWindow = document.getElementById("chat-window");
        const messageDiv = document.createElement("div");
        messageDiv.className = "message user-message";

        const messageText = document.createElement("p");
        messageText.textContent = messageContent;
        messageDiv.appendChild(messageText);
        chatWindow.appendChild(messageDiv);

        chatWindow.scrollTop = chatWindow.scrollHeight;

        // Envia a mensagem para o servidor via Socket.IO
        socket.emit("send_message", { message: messageContent });

        // Reseta o campo de entrada
        userInput.style.height = '40px';
        userInput.style.overflowY = 'hidden';
        userInput.value = "";
    }
}

// Adiciona evento de tecla Enter para enviar a mensagem
document.addEventListener("DOMContentLoaded", () => {
    userInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});

// Recebe mensagens do servidor e atualiza a interface
socket.on("receive_message", function(data) {
    console.log("Mensagem recebida:", data); // Verifique se data.audioUrl está presente e correto

    // Chama a função addBotMessage com o texto e a URL de áudio, se disponível
    addBotMessage(data.message, data.audioUrl); // data.audioUrl deve conter a URL do áudio
});

// Função para enviar áudio
function sendAudio() {
    if (!isRecording) {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();
                audioButton.classList.add("recording");
                audioChunks = [];
                
                mediaRecorder.ondataavailable = event => {
                    audioChunks.push(event.data);
                };

                mediaRecorder.onstop = () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
                    const reader = new FileReader();
                    reader.readAsDataURL(audioBlob);
                    reader.onloadend = function() {
                        // Envia áudio para o servidor via Socket.IO
                        socket.emit("send_audio", { audio: reader.result });
                    };
                    audioButton.classList.remove("recording");
                };
            })
            .catch(error => {
                console.error("Erro ao acessar o microfone:", error);
            });
    } else {
        mediaRecorder.stop();
    }
}

// Recebe áudio do servidor e toca
socket.on("receive_audio", function(data) {
    const audio = new Audio(data.audio);
    audio.play();
});

// Função para enviar imagem
function sendImage() {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.onchange = function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = function() {
                // Envia imagem para o servidor via Socket.IO
                socket.emit("send_image", { image: reader.result });
            };
        }
    };
    input.click();
}

// Recebe mensagens de imagem do servidor
socket.on("receive_card", function (data) {
    const chatWindow = document.getElementById("chat-window");

    // Criar container da mensagem
    const messageDiv = document.createElement("div");
    messageDiv.className = "message bot-message";

    // Adicionar título do card
    const titleText = document.createElement("p");
    titleText.textContent = data.title;
    messageDiv.appendChild(titleText);

    // Criar botões para o response card
    data.buttons.forEach(button => {
        const buttonElement = document.createElement("button");
        buttonElement.textContent = button.text; // Texto exibido no botão
        buttonElement.className = "response-button";

        // Evento de clique para exibir no chat e enviar ao backend
        buttonElement.onclick = () => {
            // Exibir mensagem do usuário no chat
            const userMessageDiv = document.createElement("div");
            userMessageDiv.className = "message user-message";

            const userMessageText = document.createElement("p");
            userMessageText.textContent = button.text; // Exibe o texto do botão
            userMessageDiv.appendChild(userMessageText);

            chatWindow.appendChild(userMessageDiv);
            chatWindow.scrollTop = chatWindow.scrollHeight;

            console.log(`Botão clicado: ${button.text}, Valor: ${button.value}`);
            socket.emit("send_message", { message: button.value }); // Envia valor ao backend
        };

        messageDiv.appendChild(buttonElement);
    });

    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
});

// Função para adicionar uma mensagem do bot com ícone de áudio
function addBotMessage(text, audioUrl = null) {
    const chatWindow = document.getElementById('chat-window');
    
    // Criar a mensagem do bot
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot-message');

    // Criar o contêiner para o conteúdo
    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');

    // Adicionar o texto da mensagem
    const messageText = document.createElement('p');
    messageText.textContent = text;
    messageContent.appendChild(messageText);

    // Adicionar o ícone de áudio, se houver uma URL
    if (audioUrl) {
        console.log("URL de áudio recebida:", audioUrl); // Verifica a URL no console
        const audioIcon = document.createElement('i');
        audioIcon.classList.add('fa-solid', 'fa-volume-up', 'audio-icon');
        audioIcon.setAttribute('data-audio-url', audioUrl); // Armazena a URL do áudio

        // Adiciona evento de clique para reproduzir o áudio
        audioIcon.addEventListener('click', function () {
            playAudio(audioUrl); // Passa diretamente a URL para a função
        });

        messageContent.appendChild(audioIcon); // Adiciona o ícone ao lado do texto
    } else {
        console.warn("Nenhuma URL de áudio fornecida para esta mensagem.");
    }

    botMessage.appendChild(messageContent); // Adiciona o conteúdo ao balão
    chatWindow.appendChild(botMessage); // Adiciona o balão à janela do chat
    chatWindow.scrollTop = chatWindow.scrollHeight; // Rolagem automática para o final
}

// Função para reproduzir o áudio ao clicar no ícone
function playAudio(iconElement) {
    const audioUrl = iconElement.getAttribute('data-audio-url'); // Obtém a URL do áudio

    if (audioUrl) {
        console.log("Reproduzindo áudio da URL:", audioUrl); // Verifica a URL que está sendo tocada
        const audio = new Audio(audioUrl); // Cria um objeto de áudio com a URL
        audio.play()
            .then(() => {
                console.log("Áudio está sendo reproduzido.");
            })
            .catch(error => {
                console.error("Erro ao tentar reproduzir o áudio:", error);
            });

        // Muda o estado do ícone enquanto o áudio está tocando
        iconElement.classList.add('playing-audio');

        // Remove o estado de reprodução quando o áudio terminar
        audio.onended = () => {
            iconElement.classList.remove('playing-audio');
        };
    } else {
        console.error("Nenhuma URL de áudio foi encontrada para reprodução.");
    }
}


socket.on("typing", function (data) {
    const typingIndicator = document.getElementById("typing-indicator");

    if (data.status) {
        // Exibe o indicador de digitação
        typingIndicator.style.display = "block";
    } else {
        // Oculta o indicador de digitação
        typingIndicator.style.display = "none";
    }
});