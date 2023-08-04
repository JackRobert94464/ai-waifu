# Ok so lets start coding with no idea what to do
# I'm going to do the AI Vtuber thingy first

# Reverse Engineering mr aliezer code about voicevox gonna took a while
# So i just decided to host my own voicevox server instead
# then use some client api to connect to it

# value = 1
# print(f"This is a recap on f strings: {value}")

from voicevox import Client
import asyncio
import os
import sys
from pycolour import Colour

# Import local modules
import characterAI

# We wont be using Vtube Studio or whatever but Live2DViewerEX instead
# yawn im sleepy and i dont know what to do
# update 04/08/2023: nvm we will dev the whole WebGUI for it

def initVar():
# For the time being, we will use character AI
# in the future i hope to integrate our own self hosted llm
    return

def textToSpeech():
    return

def characterReply():
    
    return

def translate():
    return

# Accept input from user keyboard in python
def textInput():
    text = input("Enter something: ")
    return text

def microphoneInput():
    return

def processingInput():
    # Accept input from user keyboard in python
    input = textInput()

    # Accept input from user microphone in python

    # Sanitizing input

    return input

def venvCheck():
    if os.environ.get('VIRTUAL_ENV'):
        # The VIRTUAL_ENV environment variable is set
        print('You are in a virtual environment:', Colour.GREEN + os.environ['VIRTUAL_ENV'] + Colour.END)
    elif sys.prefix != sys.base_prefix:
        # sys.base_prefix and sys.prefix are different, this is a virtual environment
        # https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv
        print('You are in a virtual environment:', Colour.GREEN + sys.prefix + Colour.END)
    else:
        # Not in a virtual environment
        print(Colour.RED + 'You are not in a virtual environment' + Colour.END)



# Main function. Will have to be isolated later

async def main():
    # Initialize environment variables
    initVar()

    # Check if user is in virtual environment
    venvCheck()

    # Run nodejs server
    await characterAI.run_node_server()

    # Run websocket client
    print("Running...")

    while True:

        # Yeet input to nodejs server
        try:
            input = processingInput()
            print("You: " + input)

            # Create a characterAI client and connect it to the nodejs server
            client = characterAI.Client("ws://localhost:40034")

            # Send the input to the nodejs server via WebSocket
            client.send(input)

            # Receive the response from the nodejs server via WebSocket
            response = client.recv()

            # Print or use the response in your Python code
            print("Character: " + response)

        except Exception as e:
            print(Colour.RED + "Error: " + str(e) + Colour.END)
            continue

        # Receive output from nodejs server
        
        if input == "exit":
            break

if __name__ == "__main__":
    asyncio.run(main())