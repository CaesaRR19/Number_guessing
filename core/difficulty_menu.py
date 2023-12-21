from os import system
from colorama import init, Fore, Style

init(True)

def difficulty_menu():
    system("cls")
    print(
        f"""
┏┓┓              ┳┓•┏┏•   ┓   
┃ ┣┓┏┓┏┓┏┏┓  ┏┓  ┃┃┓╋╋┓┏┓┏┃╋┓┏
┗┛┛┗┗┛┗┛┛┗   ┗┻  ┻┛┗┛┛┗┗┗┻┗┗┗┫
-----------------------------┛   
{Fore.GREEN}1) EASY (Each failure will deduct 1 to 20 seconds)
{Fore.YELLOW}2) MEDIUM (Each failure will deduct 20 to 40 seconds)
{Fore.RED}3) HARD (Each failure will deduct 40 to 60 seconds)   
    """
    )
    option = input(
        f"{Style.BRIGHT}Argh! select a difficulty, you rascal! (Or press enter to exit this menu) \
            {Style.RESET_ALL}"
    )
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "":
        pass
    else:
        print(
            f"{Fore.RED}{Style.BRIGHT}Argh! Select a valid difficulty or I'll make you walk the \
                plank!"
        )
        input("")
