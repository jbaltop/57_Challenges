import random


def main():
    messages = {
        "question": "\nWhat's your question? ",
        "1": "\nYes.",
        "2": "\nNo.",
        "3": "\nMaybe.",
        "4": "\nAsk again later.",
    }

    input(messages["question"])

    random_number = random.randint(1, 4)
    print(messages[str(random_number)])


main()
