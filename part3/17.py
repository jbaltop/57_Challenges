def main():
    a = float(input("alcohol consumption(oz): "))
    w = float(input("weight(lb): "))
    g = input("gender(m/f): ")
    h = float(input("elapsed time to drink alcohol(h): "))
    bac_limit = 0.08

    if g.lower() == "m" or g.lower() == "male":
        r = 0.73
    elif g.lower() == "f" or g.lower() == "female":
        r = 0.6
    else:
        print("please enter a correct gender.")

    bac = (a * 5.14 / w * r) - 0.015 * h

    if bac >= 0:
        message1 = "\nyour blood alcohol content: " + str(bac)
    else:
        message1 = "\nyour blood alcohol content: 0"

    if bac < bac_limit:
        message2 = "\nIt is legal for you to drive."
    else:
        message2 = "\nIt is not legal for you to drive."

    print(message1, message2)


main()
