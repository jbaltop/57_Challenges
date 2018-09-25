def main():
    messages = [
        "\nrate of return(%): ",
        "\nSorry. That's not a valid input.",
        "\nIt will take {} years to double your initial investment.",
        "\nThe rate of return can't be 0%.",
    ]

    def is_valid_input(arg):
        if arg.isdigit():
            if int(arg) == 0:
                return 0
            return 1
        return -1

    result = -1

    while result < 0:
        r = input(messages[0])
        result = is_valid_input(r)
        if result == 1:
            years = 72 / int(r)
            answer_message = messages[2].format(years)
        elif result == 0:
            answer_message = messages[3]
        else:
            answer_message = messages[1]
        print(answer_message)


main()
