# Ok so lets start coding with no idea what to do
# I'm going to do the AI Vtuber thingy first

# Reverse Engineering mr aliezer code about voicevox gonna took a while
# So i just decided to host my own voicevox server instead
# then use some client api to connect to it

# value = 1
# print(f"This is a recap on f strings: {value}")

from voicevox import Client
import asyncio

# We wont be using Vtube Studio or whatever but Live2DViewerEX instead
# yawn im sleepy and i dont know what to do

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

# Main function. Will have to be isolated later

async def main():
    # Initialize environment variables
    initVar()

    while True:
        print("Running...")
        input = processingInput()
        print(input)
        if input == "exit":
            break
        


if __name__ == "__main__":
    asyncio.run(main())