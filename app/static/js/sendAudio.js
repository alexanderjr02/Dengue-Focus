let mediaRecorder;
let audioChunks = [];
let isRecording = false;
const audioButton = document.getElementById("audio-button");
const chatWindow = document.getElementById("chat-window"); // Janela do chat

function sendAudio() {
    if (!isRecording) {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start();
                audioButton.classList.add("recording");
                audioChunks = [];
                isRecording = true;

                mediaRecorder.ondataavailable = event => {
                    audioChunks.push(event.data);
                };

                mediaRecorder.onstop = () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
                    const reader = new FileReader();
                    reader.readAsDataURL(audioBlob);
                    reader.onloadend = function () {
                        const audioUrl = reader.result;

                        // Emitir o áudio gravado via socket
                        socket.emit("send_audio", { audio: audioUrl });

                        // Exibir o áudio como uma mensagem do bot
                        addAudioMessage(audioUrl);
                    };

                    audioButton.classList.remove("recording");
                    isRecording = false;
                };
            })
            .catch(error => {
                console.error("Erro ao acessar o microfone:", error);
            });
    } else {
        mediaRecorder.stop();
    }
}

// Função para adicionar o áudio como mensagem
function addAudioMessage(audioUrl) {
    // Cria o contêiner da mensagem
    const messageDiv = document.createElement("div");
    messageDiv.className = "message bot-message";

    // Ícone do bot
    const botIcon = document.createElement("i");
    //botIcon.className = "fa-solid fa-circle-user";
    //botIcon.id = "icone-bot";

    // Contêiner do áudio
    const audioContent = document.createElement("div");
    audioContent.className = "message-content";

    // Player de áudio
    const audioPlayer = document.createElement("audio");
    audioPlayer.className = "audio-player";
    audioPlayer.controls = true; // Adiciona controles de reprodução
    audioPlayer.src = audioUrl;

    audioContent.appendChild(audioPlayer);
    messageDiv.appendChild(botIcon);
    messageDiv.appendChild(audioContent);

    // Adiciona à janela do chat
    chatWindow.appendChild(messageDiv);

    // Rola automaticamente para a última mensagem
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

audioButton.addEventListener("click", sendAudio);
