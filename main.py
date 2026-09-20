import asyncio
import edge_tts
import os


async def main():

    # Open the text file
    with open("sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # British English male voice
    voice = "en-GB-RyanNeural"

    # Convert text to speech
    communicate = edge_tts.Communicate(
        text,
        voice
    )

    # Save audio
    await communicate.save("sample.mp3")


asyncio.run(main())

# Play the audio
os.system("start sample.mp3")