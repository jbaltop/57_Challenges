def validate_name(arg):
    if arg == "":
        return -1
    else:
        if len(arg) < 2:
            return 0
        else:
            return 1


def validate_zip_code(arg):
    if arg == "":
        return -1
    else:
        if arg.isdigit() == True:
            return 1
        else:
            return 0


def validate_employee_id(arg):
    if arg == "":
        return -1
    else:
        if (
            len(arg) == 7
            and arg[0:1].isalpha() == True
            and arg[2] == "-"
            and arg[3:-1].isdigit() == True
        ):
            return 1
        else:
            return 0


def validate_input(first_name, last_name, zip_code, employee_id):
    m2 = "' is not a valid "
    m3 = " must be filled in."
    m4 = " It is too short."
    m5 = "\nThe ZIP code must be numeric."

    if validate_name(first_name) == 0:
        print("\n'" + first_name + m2 + "first name." + m4)
    elif validate_name(first_name) == -1:
        print("\nThe first name" + m3)
    if validate_name(last_name) == 0:
        print("\n'" + last_name + m2 + "last name." + m4)
    elif validate_name(last_name) == -1:
        print("\nThe last name" + m3)
    if validate_zip_code(zip_code) == 0:
        print(m5)
    elif validate_zip_code(zip_code) == -1:
        print("\nThe ZIP code" + m3)
    if validate_employee_id(employee_id) == 0:
        print("\n'" + employee_id + m2 + "ID.")
    elif validate_employee_id(employee_id) == -1:
        print("\nThe employee ID" + m3)


def main():
    q1 = "\nfirst name: "
    q2 = "last name: "
    q3 = "ZIP code: "
    q4 = "employee ID(AA-0000): "

    m1 = "\nThere were no errors found."

    result = 0
    while result < 4:
        a1 = input(q1)
        a2 = input(q2)
        a3 = input(q3)
        a4 = input(q4)
        result = (
            validate_name(a1)
            + validate_name(a2)
            + validate_zip_code(a3)
            + validate_employee_id(a4)
        )
        if result < 4:
            validate_input(a1, a2, a3, a4)
            print("\nPlease try again.")
        else:
            print(m1)
            break


main()
