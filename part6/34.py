def make_new_list(employee_list, arg):
    employee_list2 = []

    for employee in employee_list:
        if employee == arg:
            continue
        else:
            employee_list2.append(employee)
    return employee_list2


def print_list(messages, arg):
    print(messages["m1"].format(len(arg)))

    for employee in arg:
        print(employee)


def main():
    messages = {
        "m1": "\nThere are {} employees:",
        "m2": "\nEnter an employee name to remove: ",
        "m3": "\nThe name {} is not in the list. Please enter a name in the list: ",
    }

    employee_list = [
        "John Smith",
        "Jackie Jackson",
        "Chris Jones",
        "Amanda Cullen",
        "Jeremy Goodwin",
    ]

    print_list(messages, employee_list)
    print(messages["m2"], end="")
    while True:
        name = input()
        new_list = make_new_list(name)
        if name in employee_list:
            print_list(employee_list, new_list)
            break
        print(messages["m3"].format(name), end="")


main()
