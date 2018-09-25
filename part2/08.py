def main():
    a = int(input("How many people? "))
    b = int(input("How many pizzas do you have? "))
    c = int(input("How many pieces are in a pizza? "))

    if a == 0:
        result = "\nnumber of people can't be 0"
    else:
        d = (b * c) // a
        e = b * c - a * d
        result = (
            "\nEach Person gets "
            + str(d)
            + " piece(s) of pizza."
            + "\nThere are "
            + str(e)
            + " leftover piece(s)."
        )

    print(result)


main()
