def main():
    first_number = input("Enter a first number: ")
    second_number = input("Enter a second number: ")

    a = float(first_number)
    b = float(second_number)
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    if b == 0:
        result = (
            "\nAddition: "
            + str(addition)
            + "\nSubtraction: "
            + str(subtraction)
            + "\nMultiplication: "
            + str(multiplication)
            + "\nDivision: N/A"
        )
    else:
        division = a / b
        result = (
            "\nAddition: "
            + str(addition)
            + "\nSubtraction: "
            + str(subtraction)
            + "\nMultiplication: "
            + str(multiplication)
            + "\nDivision: "
            + str(division)
        )

    print(result)


main()
