from os import system
from colorama import init, Fore, Style
from random import randint
from clues import clue

init(True)


def start_game():
    system("cls")
    print(
        f"""{Style.DIM}
In Davy Jones' quest for gold, a chest of secrets found,
A voice proclaimed, a challenge set, a number to unbound.

"Speak the number swift and true, or treasures vanish fast,
Time's the key to fortunes grand, in this enigmatic cast."
        """
    )
    mystic_number = randint(1, 100)
    guessing = input(
        f"{Style.BRIGHT}Arr, tell me what the mystic number is. I'll give you a hint, you rascal: {clue(mystic_number)} -> {Style.RESET_ALL}"
    )
    


