import random


def generate_password(number_of_symbols, number_of_numbers, remain_length):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    alphabets = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    symbols = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "\\",
        "]",
        "^",
        "_",
        "`",
        "{",
        "|",
        "}",
        "~",
    ]

    all_characters = numbers + alphabets + symbols

    character_list = []
    a = 1
    b = 1
    c = 1
    while a <= number_of_symbols:
        character_list.append(random.choice(symbols))
        a += 1
    while b <= number_of_numbers:
        character_list.append(random.choice(numbers))
        b += 1
    while c <= remain_length:
        character_list.append(random.choice(all_characters))
        c += 1
    random.shuffle(character_list)
    return character_list


def main():
    messages = {
        "length": "\nWhat's the minimum length? ",
        "symbols": "How many special characters? ",
        "numbers": "How many numbers? ",
        "password": "Your password is: \n",
    }

    length = int(input(messages["length"]))
    number_of_symbols = int(input(messages["symbols"]))
    number_of_numbers = int(input(messages["numbers"]))
    remain_length = length - number_of_symbols - number_of_numbers
    remain_length2 = random.randint(remain_length, remain_length + 5)

    character_list = generate_password(
        number_of_symbols, number_of_numbers, remain_length2
    )

    print(messages["password"], end="")

    for character in character_list:
        print(character, end="")

    print("\n")


main()
