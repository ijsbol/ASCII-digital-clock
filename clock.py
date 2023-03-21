from json import load
from typing import Dict

with open("characters.json", "r") as file:
    JSON_DATA: Dict[str, str] = load(file)

print(JSON_DATA)