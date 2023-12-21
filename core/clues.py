from random import randint, choice


def clue(mystic_number: int):
    clue_dict = {
        "first_digit": f"The first digit of the mystic number is {str(mystic_number)[0]}",
        "multiple": f"A multiple of the mystic number is {find_multiple(mystic_number)}",
        "divisor": f"A divisor of the mystic number is {find_divisor(mystic_number)}",
    }
    if mystic_number not in (1, 100):
        greater_lower_dict = {
            "greater": f"The mystic number is greater than {randint(1, mystic_number - 1)}",
            "less": f"The mystic number is less than {randint(mystic_number + 1, 100)}",
        }
        clue_dict.update(greater_lower_dict)

    return choice(list(clue_dict.values()))


def find_multiple(mystic_number: int):
    multiples = list(
        range(mystic_number, mystic_number * randint(2, 10) + 1, mystic_number)
    )
    return choice(multiples)


def find_divisor(mystic_number: int):
    divisors = [i for i in range(2, mystic_number + 1) if mystic_number % i == 0]
    return choice(divisors)
