import random


def random_number(a, b):
    return random.randint(a, b)


def compare_number(a, b):
    if int(a) == b:
        return 0
    else:
        if int(a) < b:
            return 1
        else:
            return 2


def max_number(a):
    return 10 ** int(a)


def is_it_duplicated_number(a, guessed_list):
    if a in guessed_list:
        return True
    return False


def how_many_times(guessed_list):
    return len(guessed_list)


def is_it_appropriate_number(a, b):
    if a >= 1 and a <= max_number(b):
        return True
    return False


def is_it_appropriate_difficulty(a):
    if a == "1" or a == "2" or a == "3":
        return True
    return False


def is_it_number(a):
    return a.isdigit()


def guess_number(difficulty, input_number, answer_number, guessed_list):
    guess_result = []
    if is_it_number(input_number) == False:
        guess_result.append("error3")
        return guess_result

    if is_it_appropriate_number(int(input_number), difficulty) == False:
        guess_result.append("error1")
        return guess_result

    a = compare_number(input_number, answer_number)
    if a == 0:
        b = how_many_times(guessed_list)
        if b == 1:
            guess_result.append("message1")
        elif b >= 2 and b <= 4:
            guess_result.append("message2")
        elif b >= 5 and b <= 6:
            guess_result.append("message3")
        else:
            guess_result.append("message4")
        guess_result.append("correct")
        return guess_result
    else:
        if is_it_duplicated_number(input_number, guessed_list):
            guess_result.append("duplicated")
        if a == 1:
            guess_result.append("low")
            return guess_result
        else:
            guess_result.append("high")
            return guess_result


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
        "error3": "\nPlease enter a natural number.",
        "message1": "\nYou're a mind reader!",
        "message2": "\nMost impressive.",
        "message3": "\nYou can do better than that.",
        "message4": "\nBetter luck next time.",
        "duplicated": "\nYou already tried that number.",
    }

    is_play_again = True

    print(messages["start"])

    while is_play_again:
        guessed_list = []
        while True:
            difficulty = input(messages["difficulty"])
            if is_it_appropriate_difficulty(difficulty):
                print(messages["guess"], end="")
                break
            print(messages["error2"])
        answer_number = random_number(1, max_number(difficulty))
        while True:
            input_number = input()
            result = guess_number(difficulty, input_number, answer_number, guessed_list)
            guessed_list.append(input_number)
            if result[0] == "error1":
                print(
                    messages[result[0]].format(
                        "[1, " + str(max_number(difficulty)) + "]"
                    ),
                    end="",
                )
            elif result[0] == "duplicated":
                print(messages[result[0]], end="")
                print(messages[result[1]], end="")
            elif result[0] == "low" or result[0] == "high":
                print(messages[result[0]], end="")
            elif len(result) == 1:
                print(messages[result[0]])
            elif result[1] == "correct":
                print(messages[result[1]].format(how_many_times(guessed_list)))
                print(messages[result[0]])
                c = input(messages["again"])
                if c == "n" or c == "N":
                    print(messages["bye"])
                    is_play_again = False
                    break
                else:
                    break


main()
