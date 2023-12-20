from colorama import init, Fore, Style
from os import system

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
        print("q")
    elif option == "2":
        print("q")
    elif option == "3":
        return True
    else:
        print(
            f"{Fore.RED}{Style.BRIGHT}Argh! Select a valid option or I'll make you walk the plank!"
        )
        input("")
    return False
