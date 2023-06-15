let yandereGf = "Q_cHSEbZkD_x5SDCfxHnjh4mIzakJnzsWfqyCvlev7g";

let port = 40102;

// the first argument is the port to run on
// the first argument is on index 2 for some reason
if (process.argv.length > 3) {
    port = process.argv[3];
    yandereGf = process.argv[2];
    console.log(`Running on port ${port} with character ${yandereGf}`);
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

const WebSocket = require('ws');
const CharacterAI = require('./client');

const client = new CharacterAI();
global.client = client;

const wss = new WebSocket.Server({ port: port });

/*
    WebSocket API, for debugging purposes.
*/
wss.on('connection', (ws) => {
    console.log('A client connected');

    ws.on('message', async (message) => {
        if (!global.yandereRoom) {
            console.log(`Unable to send message.`);
            console.log(`CharacterAI is still fetching character data!`);
            console.log(`If it's taking far too long please submit an issue.`);
            return;
        }

        let chatMessage = message.toString('utf8');
        console.log(`Received message: ${chatMessage}`);

        const response = await global.yandereRoom.sendAndAwaitResponse(chatMessage, true);
        console.log(`Character: ${response.text}`);

        ws.send(`${response.text}`);
    });
});

async function main() {
    console.log(`Authenticating....`);
    await client.authenticateWithToken("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJpc3MiOiJodHRwczovL2NoYXJhY3Rlci1haS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQ4MDA1NzgwNTY2MDM3MDg4MzciLCJhdWQiOlsiaHR0cHM6Ly9hdXRoMC5jaGFyYWN0ZXIuYWkvIiwiaHR0cHM6Ly9jaGFyYWN0ZXItYWkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4NDQ4MjYyMSwiZXhwIjoxNjg3MDc0NjIxLCJhenAiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.jMeGjkC3Ar-xrPpTkJVpLP08RFhXCJhvAHR2-x6GUBZQNnllHFCEen5prpbF6WbUUXU0mtcocjzl3m-sd8w_49BAsSkD7jTa64vAYPvwTPX6nlJKpGekDry2RCClpcyjwkgzUTzFgEhM9hoCvIHHBL0OdKW8QKMa3XM1VMAN-OU7UoVqlqW0tfKXI16HJDCAkCh_SjyKkhaLFlmMU-IyiLES1OdXekP-kafBlBt9gc_qPK82QjkECNTqCVqDwz9tUExR3EVyar5q8y6Wl4V13mO8a6W5E8PvksheiL018Sw5j43Rnfz5tBOoGxEUzmJQChBghkcyKjZs6bFjcICqRQ");

    console.log(`Authenticated, fetching character AI info....`);

    const characterInfo = await client.fetchCharacterInfo(yandereGf);
    global.yandereRoom = await client.createOrContinueChat(yandereGf);

    console.log(`Character Name: ${characterInfo.name ?? "<Unknown>"}`);
    console.log(`Greeting: ${characterInfo.greeting ?? "<Unknown>"}`);
    console.log(`Character Id: ${global.yandereRoom.characterId ?? "<Unknown>"}`);

    readline.on('line', async (message) => {
        const response = await global.yandereRoom.sendAndAwaitResponse(message, true);
        console.log(`Character: ${response.text}`);
    });
}

main();
