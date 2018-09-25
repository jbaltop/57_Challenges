def main():
    a = int(input("first number: "))
    b = int(input("second number: "))
    c = int(input("third number: "))

    if a == b or b == c or c == a:
        message = "\ngood bye"
    else:
        if a > b:
            if a > c:
                largest_number = a
            else:
                largest_number = c
        elif b > c:
            if b > a:
                largest_number = b
            else:
                largest_number = a
        elif c > a:
            if c > b:
                largest_number = c
            else:
                largest_number = b
        message = "\nThe largest number is " + str(largest_number) + "."

    print(message)


main()
