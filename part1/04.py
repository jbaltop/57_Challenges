def main():
    exclamation = input("Enter an exclamation: ")
    adverb = input("Enter an adverb: ")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")

    speech = (
        '\n"'
        + exclamation
        + "! he said "
        + adverb
        + " as he jumped into his convertible "
        + noun
        + " and drove off with his "
        + adjective
        + " wife."
        + '"'
    )

    print(speech)


main()
