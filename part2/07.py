def main():
    length = float(input("What is the length of the room in feet? "))
    width = float(input("What is the width of the room in feet? "))

    square_feet = length * width
    square_meter = square_feet * 0.09290304
    result = (
        "\nThe area is\n"
        + str(square_feet)
        + " square feet\n"
        + str(square_meter)
        + " square meter(s)."
    )

    print(result)


main()
