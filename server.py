from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

from utils import chat_completion, config, get_cache, set_cache

SYSTEM_PROMPT = """
Reply only with the element that comes by combining two elements using the logic on the examples below, along with it's corresponding emoji on the next line.
Examples:

Earth + Water
Plant
🌱

Earth + Lava
Stone
🪨

Earth + Island
Continent
🌎

Water + Water
Lake
🌊

Fire + Fire
Volcano
🌋
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def pair(first: str, second: str):
    cached_value = get_cache((first, second))
    if cached_value:
        cached_value["isNew"] = False
        return cached_value

    messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{first} + {second}"},
        ]

    completion = await chat_completion(messages)
    print(completion)
    lines = completion.strip().split("\n")

    result = {"result": lines[0], "emoji": lines[1]}
    set_cache((first, second), result)
    if "discovery_enabled" in config and config["discovery_enabled"]:
        result["isNew"] = True
    return result

