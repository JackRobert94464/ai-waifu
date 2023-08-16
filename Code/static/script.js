const socket = io(); // Establish WebSocket connection

document.querySelector('#send-button').addEventListener('click', () => {
    const message = document.querySelector('#message-input').value;
    const time = new Date().toLocaleTimeString('en-GB', { hour: "numeric", minute: "numeric"});
    socket.emit('user_message', message); // Send user message to Python backend

    const chatBox = document.querySelector('ul.innerbox');
    chatBox.innerHTML += `<li class="clearfix">
    <div class="message-data text-right">
    <span class="message-data-time">${time}</span>
    <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="avatar">
    </div>
    <div class="message other-message float-right">${message}</div>
    </li>`;
});

socket.on('character_response', response => {
    const chatBox = document.querySelector('ul.innerbox');
    const time = new Date().toLocaleTimeString('en-GB', { hour: "numeric", minute: "numeric"});
    chatBox.innerHTML += `<li class="clearfix">
    <div class="message-data">
    <span class="message-data-time">${time}</span>
    </div>
    <div class="message my-message">${response}</div>
    </li>`;
    chatBox.scrollTop = chatBox.scrollHeight;
});

document.addEventListener('DOMContentLoaded', () => {
    // Set the background color of the chatroom to blue
    document.body.style.backgroundColor = '#0069c0';

    // Add a dark blue border to the chat box
    document.querySelector('#chat-box').style.borderColor = '#004d8c';
});