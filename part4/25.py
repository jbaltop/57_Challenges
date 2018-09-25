def is_it_included(string, type_of_data):
    character_list = []
    for i in string:
        if i.lower() in type_of_data:
            character_list.append(i)
    if character_list == []:
        return False
    else:
        return True


def password_validator(password):
    m1 = "\nThe password '" + password + "' is a "
    m2 = " password."
    message1 = m1 + "very weak" + m2
    message2 = m1 + "weak" + m2
    message3 = m1 + "strong" + m2
    message4 = m1 + "very strong" + m2

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
            return message1
        elif password.isalpha():
            return message2
    else:
        if is_it_included(password, numbers) and is_it_included(password, alphabets):
            if is_it_included(password, symbols):
                return message4
            else:
                return message3


def main():
    password = input("\npassword: ")

    m1 = "\nThe password '" + password + "' is a "
    m2 = " password."
    message5 = m1 + "normal" + m2

    answer = password_validator(password)

    if answer is None:
        answer = message5

    print(answer)


main()
