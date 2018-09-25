def is_it_included(string, type_of_data):
    for i in string:
        if i.lower() in type_of_data:
            return True
    return False


def password_validator(password):
    numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    alphabets = {
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
    }
    symbols = {
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
    }

    if len(password) < 8:
        if password.isdigit():
            return 0
        elif password.isalpha():
            return 1
    else:
        if is_it_included(password, numbers) and is_it_included(password, alphabets):
            if is_it_included(password, symbols):
                return 3
            else:
                return 2
    return 4


def main():
    password = input("\npassword: ")

    m1 = "\nThe password '" + password + "' is a "
    m2 = " password."

    password_power = ["very weak", "weak", "strong", "very strong", "normal"]

    answer = password_validator(password)

    message = m1 + password_power[answer] + m2
    print(message)


main()
