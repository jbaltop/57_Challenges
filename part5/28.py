def main():
    messages = ["\nEnter a number: ", "\nThe total is {}"]

    i = 0
    total = 0

    while i < 5:
        total = total + int(input(messages[0]))
        i += 1

    answer = messages[1].format(total)

    print(answer)


main()
