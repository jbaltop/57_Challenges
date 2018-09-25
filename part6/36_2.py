import statistics


def calculate_everything(arg):

    average = statistics.mean(arg)
    minimum = min(arg)
    maximum = max(arg)
    standard_deviation = statistics.pstdev(arg)
    return [average, minimum, maximum, standard_deviation]


def make_list(messages):
    n_list = []
    while True:
        input_number = input(messages["number"])
        if input_number.isdigit():
            number = int(input_number)
            n_list.append(number)
        elif input_number.lower() == "done":
            return n_list
        else:
            print(messages["error1"])


def main():
    messages = {
        "number": "Enter a number (type 'done' to stop entering numbers): ",
        "numbers": "\nNumbers: ",
        "average": "\nThe average is {}.",
        "minimum": "\nThe minimum is {}.",
        "maximum": "\nThe maximum is {}.",
        "standard_deviation": "\nThe standard deviation is {}.",
        "error1": "\nPlease enter a valid number.",
    }

    number_list = make_list(messages)

    if len(number_list) == 0:
        number_list = [0]

    result = calculate_everything(number_list)

    answer_message = (
        messages["average"].format(str(result[0]))
        + messages["minimum"].format(str(result[1]))
        + messages["maximum"].format(str(result[2]))
        + messages["standard_deviation"].format(str(result[3]))
    )

    print(answer_message)


main()
