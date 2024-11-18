let currentAudio = null; // Variável global para rastrear o áudio em reprodução

function playAudio(audioUrl) {
    if (!audioUrl) {
        console.error("Nenhuma URL de áudio foi fornecida.");
        return;
    }

    console.log("Tentando reproduzir o áudio da URL:", audioUrl);

    // Pausar o áudio atual, se existir
    if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0; // Reinicia o tempo do áudio atual
    }

    // Criar um novo objeto de áudio
    const audio = new Audio(audioUrl);

    // Atualizar o áudio atual
    currentAudio = audio;

    // Reproduzir o áudio
    audio.play()
        .then(() => {
            console.log("Áudio reproduzido com sucesso:", audioUrl);
        })
        .catch((error) => {
            console.error("Erro ao reproduzir o áudio:", error);
        });

    // Evento quando o áudio termina
    audio.onended = () => {
        console.log("Áudio finalizado.");
        currentAudio = null; // Limpa o áudio atual
    };
}
