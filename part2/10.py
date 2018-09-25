def main():
    a = float(input("Price of item 1: "))
    b = int(input("Quantity of item 1: "))
    c = float(input("Price of item 2: "))
    d = int(input("Quantity of item 2: "))
    e = float(input("Price of item 3: "))
    f = int(input("Quantity of item 3: "))

    vat = 5.5

    g = a * b + c * d + e * f
    h = round(g * vat / 100, 2)
    i = g + h
    result = "\nSubtotal: " + str(g) + "\nTax: " + str(h) + "\nTotal: " + str(i)

    print(result)


main()
