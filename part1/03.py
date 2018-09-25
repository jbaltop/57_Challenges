def main():
    quote = input("What is the quote?\n")
    person = input("Who said it?\n")

    speech = "\n" + person + " says, " + '"' + quote + '"'

    print(speech)


main()
