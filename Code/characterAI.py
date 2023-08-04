import subprocess
import websocket
from websocket import create_connection
import asyncio

async def run_node_server():
    # Create a subprocess object that runs the node command with the arguments
    p = await asyncio.create_subprocess_exec("node", ".\\node_modules\\node_characterai\\runner.js", "Q_cHSEbZkD_x5SDCfxHnjh4mIzakJnzsWfqyCvlev7g", "40034", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    # Read the output and error streams of the subprocess
    output, error = await p.communicate()

    # Print the output and error streams to the console
    print(output)
    print(error)

async def run_websocket_client():
    # Create a WebSocket object and connect it to the Node.js server URL
    ws = websocket.WebSocket()
    ws.create_connection("ws://localhost:40034")

    # Use a while loop to read input from the console and send it to the Node.js server via WebSocket
    while True:
        message = input("Enter your message: ")
        if message == "quit":
            break
        ws.send(message)

        # Use the recv method of the WebSocket object to receive the response from the Node.js server via WebSocket and print it to the console
        response = ws.recv()
        print(response)

    # Close the WebSocket connection when the loop ends
    ws.close()

# Create an event loop object that manages async tasks
loop = asyncio.get_event_loop()

# Run both async functions as tasks in the event loop
loop.run_until_complete(asyncio.gather(run_node_server(), run_websocket_client()))

# Close the event loop
loop.close()
