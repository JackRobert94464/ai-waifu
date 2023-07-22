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



# Main function. Will have to be isolated later

async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            "こんにちは！", speaker=1
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))


if __name__ == "__main__":
    asyncio.run(main())