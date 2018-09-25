def main():
    p = int(input("principal($): "))
    r = float(input("rate of interest(%): "))
    t = int(input("number of years: "))

    i = round(p * r / 100 * t, 2)
    a = p + i
    result = (
        "\nAfter "
        + str(t)
        + " years at "
        + str(r)
        + "%, the investment will be worth $"
        + str(a)
    )

    print(result)


main()
