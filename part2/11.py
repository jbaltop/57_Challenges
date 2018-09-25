import math


def main():
    euro = float(input("How many Euros are you exchanging? "))
    exchange_rate = float(input("What is the exchange rate? "))

    dollar = math.ceil((euro * exchange_rate / 100) * 100) / 100
    result = (
        "\n"
        + str(euro)
        + " euros at an exchange rate of "
        + str(exchange_rate)
        + " is "
        + str(dollar)
        + " dollars."
    )

    print(result)


main()
