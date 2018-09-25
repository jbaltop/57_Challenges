def make_list(arg):
    return arg.split(" ")


def filter_even_numbers(arg):
    even_numbers = []
    for i in arg:
        if int(i) % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def main():
    messages = {
        "numbers": "\nEnter a list of numbers, separated by spaces: ",
        "even_numbers": "\nThe even numbers are: ",
    }

    numbers = input(messages["numbers"])

    even_numbers = filter_even_numbers(make_list(numbers))

    print(messages["even_numbers"], end="")

    for even_number in even_numbers:
        print(even_number, end=" ")

    print("\n")


main()
