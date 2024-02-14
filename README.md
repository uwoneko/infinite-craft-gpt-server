# Infinity Craft OpenAI server
This is an alternative server that uses OpenAI API instead of infinite craft's internal api.

## Installation
1. Install tampermonkey
2. Go to https://github.com/YuraSuper2048/infinite-craft-gpt-server/raw/main/interceptor.user.js and install the userscript
3. Clone the repository (make sure you have git installed in your system)
```sh
git clone https://github.com/YuraSuper2048/infinite-craft-gpt-server
cd infinite-craft-gpt-server
```
4. Install the requirements
```sh
pip install -r requirements.txt
```
5. Rename "config.toml.example" to "config.toml"
6. Edit "config.toml" and put your OpenAI API key
7. Run the server
```sh
uvicorn server:app
```
8. Go to [Infinite Craft](https://neal.fun/infinite-craft/) and enjoy your GPT 4 enhanced infinite craft

## Notes
GPT 4 is kinda too smart and it will do things that actually make sense, so its much harder to reach things

If you wanna "hard code" some result just put it into SYSTEM_PROMPT in server.py

I think the original used a fine tuned model so i assumed GPT 4 may be not the best at it but it works surprizingly well...