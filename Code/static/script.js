const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const socket = io();  // Establish WebSocket connection

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message.trim() !== '') {
        const newMessage = document.createElement('div');
        newMessage.classList.add('message');
        newMessage.innerText = message;
        chatBox.appendChild(newMessage);
        messageInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;

        // Send the message to the Flask backend via WebSocket
        socket.emit('user_message', message);
    }
});

socket.on('character_response', response => {
    const newMessage = document.createElement('div');
    newMessage.classList.add('message', 'character');
    newMessage.innerText = `Character: ${response}`;
    chatBox.appendChild(newMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
});
