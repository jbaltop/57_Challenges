import math


def calculate_average(arg):
    total = 0
    for number in arg:
        total = total + number
    average = total / len(arg)
    return average


def calculate_minimum(arg):
    minimum = min(arg)
    return minimum


def calculate_maximum(arg):
    maximum = max(arg)
    return maximum


def calculate_dispersion(arg):
    average = calculate_average(arg)
    sum = 0
    for number in arg:
        a = math.pow(number - average, 2)
        sum = sum + a
    dispersion = sum / len(arg)
    return dispersion


def calculate_standard_deviation(arg):
    dispersion = calculate_dispersion(arg)
    standard_deviation = math.sqrt(dispersion)
    return standard_deviation


def calculate_everything(arg):
    average = calculate_average(arg)
    minimum = calculate_minimum(arg)
    maximum = calculate_maximum(arg)
    standard_deviation = calculate_standard_deviation(arg)
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
