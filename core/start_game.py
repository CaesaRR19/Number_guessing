from os import system
from colorama import init, Fore, Style

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
    

start_game()