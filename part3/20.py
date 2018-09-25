def main():
    order_amount = float(input("What is the order amount? "))
    state = input("What state do you live in? ")
    if state.lower() == "wisconsin" or state.lower() == "wi":
        county = input("what county do you live in? ")

    wisconsin_state_tax = 5.5
    eau_claire_county_tax = 0.5
    dunn_county_tax = 0.4
    illinois_state_tax = 8

    if state.lower() == "wisconsin" or state.lower() == "wi":
        if county.lower() == "eau claire":
            county_tax = order_amount * eau_claire_county_tax / 100
        elif county.lower() == "dunn":
            county_tax = order_amount * dunn_county_tax / 100
        else:
            county_tax = 0

        state_tax = order_amount * wisconsin_state_tax / 100
        tax = state_tax + county_tax
        total = round(order_amount + tax, 2)
        result = (
            "\nThe state tax is $"
            + str(round(state_tax, 2))
            + "\nThe county tax is $"
            + str(round(county_tax, 2))
            + "\nThe total tax is $"
            + str(round(tax, 2))
            + "\nThe total is $"
            + str(total)
        )
    elif state.lower() == "illinois" or state.lower() == "il":
        tax = state_tax = order_amount * illinois_state_tax / 100
        total = round(order_amount + tax, 2)
        result = (
            "\nThe state tax is $"
            + str(round(state_tax, 2))
            + "\nThe total is $"
            + str(total)
        )
    else:
        total = order_amount
        result = "\nThe total is $" + str(total)

    print(result)


main()
