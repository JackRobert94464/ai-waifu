from flask import Flask, render_template
from flask_socketio import SocketIO
import characterAI

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('user_message')
def handle_user_message(message):
    characterAI.send_message_to_process_via_websocket(message)

@socketio.on('connect')
def test_connect():
    print('Connected to the web GUI')

@socketio.on('disconnect')
def test_disconnect():
    print('Disconnected from the web GUI')

def run_flask_server():
    socketio.run(app, debug=True)

if __name__ == "__main__":
    run_flask_server()
