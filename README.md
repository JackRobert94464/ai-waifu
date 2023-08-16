# ai-waifu

## Requirements
- Node.js
- Python 3.6+
- pipenv

## Current State
- rewriting runner.js for node_characterAI (done!)
- connect python driver code with node.js server man im stuck (done!)
- make it work with the node.js server (done!)
- Creating the first WebGUI (done!)
- Improving the WebGUI (done - now with scrolling history chatbox!)
- Adding pixi.js live2d module (done - with Tsukuyomi as sample live2d model!)
- Adding a TTS 
- Lipsyncing the TTS with pixi-live2d

## Bugs
- nodejs server double start causing error in log

## Tasks
- make a keyboard chatbot using API (from characterAIpuppeteer/localrun)
- make it talk (TTS)
- train a TTS model using RVC and use it here
- integrate Whisper for Speech-to-Text capability, allow it to listen
- creating a WebGUI for the chatbot
- integrate live2d from pixi.js into the webgui
- clean the code

## Future Expectations
- rewriting runner.js to allow image recognition (already implemented in the node module)
- make it sing
- make it a discord bot
- allow for input from other AI models (for commentary during actions)