import httpx
import tomllib
import json
import copy

def load_config() -> str:
    try:
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)
        if "api_key" not in config or "model" not in config:
            print("config.toml should have \"api_key\" and \"model\"")
            exit()
    except FileNotFoundError:
        print("no config.toml?")
        exit()
    return config

config = load_config()

client = httpx.AsyncClient(timeout=None)
async def chat_completion(messages: list) -> str:
    request_data = {
        "model": config["model"],
        "messages": messages,
        "temperature": 0
    }

    response = await client.post(f"{config['api_base']}/chat/completions" if "api_base" in config else "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {config['api_key']}"},
        json=request_data)

    response_json = response.json()

    return response_json["choices"][0]["message"]["content"]

try:
    with open("cache.json", "r") as f:
        cache = json.load(f)
except FileNotFoundError:
    cache = {}

def tuple_to_str(key: tuple[str, str]) -> str:
    return f"{key[0]}, {key[1]}"

def set_cache(key: tuple[str, str], value: dict) -> None:
    cache[tuple_to_str(key)] = copy.deepcopy(value)
    with open("cache.json", "w") as f:
        json.dump(cache, f, indent=4)

def get_cache(key: tuple[str, str]) -> dict | None:
    if tuple_to_str(key) in cache:
        return copy.deepcopy(cache[tuple_to_str(key)])
    key = key[::-1]
    if tuple_to_str(key) in cache:
        return copy.deepcopy(cache[tuple_to_str(key)])
    return None
