def main():
    age = int(input("What is your age? "))

    m = 16

    if age >= m:
        message = "\nYou are old enough to legally drive."
    else:
        message = "\nYou are not old enough to legally drive."

    print(message)


main()
