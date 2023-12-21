from os import system
from colorama import init, Fore, Style
from difficulty_menu import difficulty_menu
from start_game import start_game


init(True)


def menu():
    system("cls")
    print(
        """   
┏┳┓┓     ┳┓              ╹   ┏┓┓           ┏┓      
 ┃ ┣┓┏┓  ┣┫┓┏┏┏┏┓┏┓┏┓┏┓┏┓ ┏  ┃ ┣┓┏┓┏┓┏┓┏┓  ┃┃┓┏┏┓┏╋
 ┻ ┛┗┗   ┻┛┗┻┗┗┗┻┛┗┗ ┗ ┛  ┛  ┗┛┛┗┛ ┗┛┛┗┗┛  ┗┻┗┻┗ ┛┗   
 --------------------------------------------------
1) Start Game
2) Choose Difficulty
3) Close Game                  
          """
    )
    option = input(
        f"{Style.BRIGHT}Argh! select an option, you rascal! {Style.RESET_ALL}"
    )

    if option == "1":
        start_game()
    elif option == "2":
        difficulty_menu()
    elif option == "3":
        print(
            f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}See you on another adventure, buccaneer!"
        )
        return True
    else:
        print(
            f"{Fore.RED}{Style.BRIGHT}Argh! Select a valid option or I'll make you walk the plank!"
        )
        input("")
    return False
