def validate_notnull(arg):
    if arg != "":
        return True
    else:
        return False


def validate_name(arg):
    if len(arg) >= 2:
        return True
    else:
        return False


def validate_zip_code(arg):
    return arg.isdigit()


def validate_employee_id(arg):
    if (
        len(arg) == 7
        and arg[0:1].isalpha() == True
        and arg[2] == "-"
        and arg[3:-1].isdigit() == True
    ):
        return True
    else:
        return False


def validate_input(first_name, last_name, zip_code, employee_id):
    error_message_template = [
        "\nThere were no errors found.",
        "\n'{f1}' is not a valid {f2}.",
        "\nThe '{f1}' must be filled in.",
        " It is too short.",
        "\nThe ZIP code must be numeric.",
    ]

    result = 4
    error_ids = []
    error_formats = []
    if not validate_notnull(first_name):
        error_ids.append(2)
        error_formats.append({"f1": "first name"})
        result -= 1
    elif not validate_name(first_name):
        result -= 1
        error_ids.append(1)
        error_formats.append({"f1": first_name, "f2": "first name"})
        error_ids.append(3)
        error_formats.append({})

    if not validate_notnull(last_name):
        error_ids.append(2)
        error_formats.append({"f1": "last name"})
        result -= 1
    elif not validate_name(last_name):
        result -= 1
        error_ids.append(1)
        error_formats.append({"f1": last_name, "f2": "last name"})
        error_ids.append(3)
        error_formats.append({})

    if not validate_notnull(zip_code):
        error_ids.append(2)
        error_formats.append({"f1": "ZIP code"})
        result -= 1
    elif not validate_zip_code(zip_code):
        result -= 1
        error_ids.append(4)
        error_formats.append({})

    if not validate_notnull(employee_id):
        error_ids.append(2)
        error_formats.append({"f1": "employee ID"})
        result -= 1
    elif not validate_employee_id(employee_id):
        result -= 1
        error_ids.append(1)
        error_formats.append({"f1": "employee ID", "f2": "ID"})

    if error_ids == []:
        error_ids.append(0)
        error_formats.append({})

    for index, error_id in enumerate(error_ids):
        error_format = error_formats[index]
        print(error_message_template[error_id].format(**error_format), end="")

    return result


def main():
    question_messages = [
        "\nfirst name: ",
        "last name: ",
        "ZIP code: ",
        "employee ID(AA-0000): ",
    ]

    result = 0
    while result < 4:
        answers = []
        for question_message in question_messages:
            answers.append(input(question_message))

        result = validate_input(answers[0], answers[1], answers[2], answers[3])
        if result < 4:
            print("\nPlease try again.")
        else:
            print("\n")
            break


main()
