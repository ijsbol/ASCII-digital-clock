from json import load
from datetime import datetime
from typing import Dict, Final, List, Union
from time import sleep
import os

with open("characters.json", "r") as file:
    JSON_DATA: Final[Dict[str, str]] = load(file)

DIGIT_HEIGHT: Final[int] = len(JSON_DATA["0"])
SYSTEM_TIME_FORMAT: Final[str] = "%H:%M:%S"
CLOCK_REFRESH_RATE: Final[Union[float, int]] = 0.2


def get_current_time() -> datetime:
    return datetime.now()

def format_time(system_time: datetime) -> str:
    return system_time.strftime(SYSTEM_TIME_FORMAT)

def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def create_clock_face(current_time: str) -> List[str]:
    character_rows: List[str] = []

    for character_row in range(DIGIT_HEIGHT):
        new_row = ""

        for character in current_time:
            new_row += JSON_DATA[character][character_row]
        character_rows.append(new_row)

    return character_rows

def print_clock_face(character_rows: List[str]) -> None:
    for character_row in character_rows:
        print(character_row)

def run_clock() -> None:
    while True:
        clear_terminal()

        current_time = get_current_time()
        formatted_time = format_time(current_time)
        character_rows = create_clock_face(formatted_time)
        print_clock_face(character_rows)

        sleep(CLOCK_REFRESH_RATE)

if __name__ == "__main__":
    run_clock()