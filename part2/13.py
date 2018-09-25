import math


def main():
    p = int(input("principal($): "))
    r = float(input("rate of interest(%): "))
    t = int(input("number of years: "))
    n = int(input("number of times the interest is compounded per year: "))

    a = math.ceil((p * (1 + r / 100 / n) ** (n * t)) * 100) / 100
    result = (
        "\n"
        + str(p)
        + " invested at "
        + str(r)
        + "% for "
        + str(t)
        + " years compounded "
        + str(n)
        + " times per years is $"
        + str(a)
    )

    print(result)


main()
