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
        f"{Style.BRIGHT}Argh! select a difficulty, you rascal! (Or press enter to exit this menu) {Style.RESET_ALL}"
    )

    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "":
            pass
        case _:
            print(
                f"{Fore.RED}{Style.BRIGHT}Argh! Select a valid difficulty or I'll make you walk the plank!"
            )
            input("")
