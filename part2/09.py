import math


def main():
    length = float(input("ceiling length(m): "))
    width = float(input("ceiling width(m): "))

    liter_per_square_meter = 9

    area = length * width
    amount_of_paint = math.ceil(area / liter_per_square_meter)
    result = (
        "\nYou will need to purchase "
        + str(amount_of_paint)
        + " liter(s) of paint to cover "
        + str(area)
        + " square meter(s)."
    )

    print(result)


main()
