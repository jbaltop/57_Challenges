def password_validator(password):
    message1 = "\nThe password '" + password + "' is a very weak password."
    message2 = "\nThe password '" + password + "' is a weak password."
    message3 = "\nThe password '" + password + "' is a strong password."
    message4 = "\nThe password '" + password + "' is a very strong password."
    message5 = "\nThe password '" + password + "' is a normal password."

    if len(password) < 8:
        if password.isdigit() == True:
            answer = message1
        elif password.isalpha() == True:
            answer = message2
        else:
            answer = message5
    else:
        if password.isdigit() == True or password.isalpha() == True:
            answer = message5
        else:
            if password.isalnum() == True:
                answer = message3
            else:
                answer = message4
    print(answer)


def main():
    password = input("\npassword: ")
    password_validator(password)


main()
