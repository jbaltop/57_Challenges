def main():
    string = input("Type something to calculate string length.\n")

    length = len(string)
    speech = '\n"' + string + '"' + " has " + str(length) + " character(s)."

    print(speech)


main()
