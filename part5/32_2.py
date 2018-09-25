import random


def random_number(a, b):
    return random.randint(a, b)


def compare_number(a, b):
    if a == b:
        return 0
    else:
        if a < b:
            return 1
        else:
            return 2


def max_number(a):
    return 10 ** a


def is_it_appropriate_number(a, b):
    if a >= 1 and a <= max_number(b):
        return True
    return False


def is_it_appropriate_difficulty(a):
    if a >= 1 and a <= 3:
        return True
    return False


def input_integer(messages, message=""):
    while True:
        result = input(message)
        if result.isdigit():
            return int(result)
        else:
            message = messages["error3"]


def guess_number(difficulty, answer_number, messages):
    guessed_list = []
    while True:
        input_number = input_integer(messages)
        if is_it_appropriate_number(input_number, difficulty) == False:
            print(
                messages["error1"].format("[1, " + str(max_number(difficulty)) + "]"),
                end="",
            )
        a = compare_number(input_number, answer_number)
        if a == 0:
            guessed_list.append(input_number)
            break
        else:
            if input_number in guessed_list:
                print(messages["duplicated"], end="")
            if a == 1:
                print(messages["low"], end="")
            else:
                print(messages["high"], end="")
            guessed_list.append(input_number)
    return len(guessed_list)


def main():
    messages = {
        "start": "\nLet's play Guess the Number.",
        "difficulty": "\nPick a difficulty level. 1 for easy, 2 for normal, and 3 for hard: ",
        "guess": "\nI have my number. What's your guess: ",
        "low": "\nToo low. Guess again: ",
        "high": "\nToo high. Guess again: ",
        "correct": "\nYou got it in {} guesses!",
        "again": "\nPlay again(Y/n): ",
        "bye": "\nGoodbye!",
        "error1": "\nPlease enter a number in range {}: ",
        "error2": "\nYou can only choose from '1', '2', or '3'.",
        "error3": "\nPlease enter a natural number: ",
        "message1": "\nYou're a mind reader!",
        "message2": "\nMost impressive.",
        "message3": "\nYou can do better than that.",
        "message4": "\nBetter luck next time.",
        "duplicated": "\nYou already tried that number.",
    }

    print(messages["start"])

    while True:
        while True:
            difficulty = input_integer(messages, messages["difficulty"])
            if is_it_appropriate_difficulty(difficulty):
                print(messages["guess"], end="")
                break
            print(messages["error2"])
        answer_number = random_number(1, max_number(difficulty))
        tries = guess_number(difficulty, answer_number, messages)
        print(messages["correct"].format(tries))
        if tries == 1:
            print(messages["message1"])
        elif tries >= 2 and tries <= 4:
            print(messages["message2"])
        elif tries >= 5 and tries <= 6:
            print(messages["message3"])
        else:
            print(messages["message4"])

        c = input(messages["again"])
        if c == "n" or c == "N":
            print(messages["bye"])
            break


main()
