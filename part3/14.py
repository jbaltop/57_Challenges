def main():
    order_amount = float(input("What is the order amount? "))
    state = input("What is the state? ")

    vat = 5.5

    result = "\nThe total is $" + str(order_amount)

    if state.lower() == "wisconsin" or state.lower() == "wi":
        tax = order_amount * vat / 100
        total = round(order_amount + tax, 2)
        result = (
            "\nThe subtotal is $"
            + str(order_amount)
            + "\nThe tax is $"
            + str(round(tax, 2))
            + "\nThe total is $"
            + str(total)
        )

    print(result)


main()
