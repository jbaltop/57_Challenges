def main():
    price = float(input("price($): "))
    tip_rate = float(input("tip rate(%): "))

    tip = round(price * tip_rate / 100, 2)
    total = price + tip

    if price < 0:
        if tip_rate < 0:
            print("price and tip rate can't be a negative number")
        else:
            print("price can't be a negative number")
    elif tip_rate < 0:
        print("tip rate can't be a negative number")
    else:
        print("\nprice:", "$", price)
        print("tip rate:", tip_rate, "%")
        print("tip:", "$", tip)
        print("total:", "$", total)


main()
