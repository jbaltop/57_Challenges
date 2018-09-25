def main():
    c1 = float(input("temperature(c): "))
    f1 = float(input("temperature(f): "))

    c2 = (f1 - 32) * 5 / 9
    f2 = (c1 * 9 / 5) + 32

    message = (
        "\n"
        + str(c1)
        + " Celsius is "
        + str(f2)
        + " Fahrenheit."
        + "\n"
        + str(f1)
        + " in Fahrenheit is "
        + str(c2)
        + " Celsius."
    )

    print(message)


main()
