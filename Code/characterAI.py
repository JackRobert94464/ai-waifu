import subprocess
import websocket
# from websocket import create_connection
import asyncio

import threading
import atexit


# ok so these thing should be put in a main/start function

# Create an event loop object that manages async tasks
# loop = asyncio.get_event_loop()

# Run both async functions as tasks in the event loop
# loop.run_until_complete(asyncio.gather(run_node_server(), run_websocket_client()))

# Close the event loop
# loop.close()






# Sandboxing time! this teach me a lot about websocket ngl
# https://websocket-client.readthedocs.io/en/latest/examples.html
# websocket.enableTrace(True)
# NOTE TO SELF: LEARN ABOUT ASYNCIO AND THREADING IN PYTHON
# https://docs.python.org/3/library/asyncio-task.html#example-chain-coroutines

# Declare a global WebSocket object
wsapp = None
response = None

# Declare a global event object
ws_event = threading.Event()

def on_message(wsapp, message):
    print(message)
    response(message)

def on_close(wsapp):
    print("### websocket closed ###")

def run_websocket_client():
    global wsapp
    wsapp = websocket.WebSocketApp("ws://localhost:40034/", on_message=on_message, on_close=on_close)
    print("websocket connected!")
    # Set the event to indicate that the connection is ready
    wsapp.run_forever()

def send_message_to_process_via_websocket(message):
    global wsapp
    wsapp.send(message)

@atexit.register
def kill_process():
    global process
    print("Terminating node process...", flush=True)
    try:
        process.terminate()
        print("Node process terminated successfully.", flush=True)
    except Exception as e:
        print("Error while terminating node process:", e, flush=True)


async def handle_output(stream, suffix):
    while True:
        line = await stream.readline()
        if not line:
            break
        print(f"node js: {line.decode().rstrip()}")


async def run_node_server():
    # Declare a global process object
    global process

    # Create a subprocess object that runs the node command with the arguments
    process = await asyncio.create_subprocess_exec(
        "node", 
        ".\\node_modules\\node_characterai\\runner.js", 
        "Q_cHSEbZkD_x5SDCfxHnjh4mIzakJnzsWfqyCvlev7g", 
        "40034", 
        stdout=asyncio.subprocess.PIPE, 
        stderr=asyncio.subprocess.PIPE
    )

    # Start WebSocket client thread first
    t = threading.Thread(target=run_websocket_client)
    t.start()

    # Read the output and error streams of the subprocess
    # output, error = await process.communicate()

    # Print the output and error streams to the console
    # print(output)
    # print(error)

    # Create two tasks that handle the output and error streams
    # Ok this part is thanks to the original dude since im suck at these asyncio stuff
    tasks = [
        asyncio.create_task(handle_output(process.stdout, "stdout")),
        asyncio.create_task(handle_output(process.stderr, "stderr")),
    ]

    # Wait for both tasks to finish
    await asyncio.gather(*tasks)

    return await process.wait()

from concurrent.futures import ThreadPoolExecutor

def run_async():    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    t = threading.Thread(target=lambda: loop.run_until_complete(run_node_server()))
    t.start()
    return t