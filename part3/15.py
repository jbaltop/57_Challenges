def main():
    print("Username: Hello\nPassword: World")

    username = input("Username: ")
    password = input("Password: ")

    if username == "Hello":
        if password == "World":
            message = "\nWelcome, " + username + "!"
        else:
            message = "\nYour password is incorrect."
    else:
        message = "\nYour username or password is incorrect."

    print(message)


main()
