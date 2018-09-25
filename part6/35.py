import random


def main():
    messages = {
        "m1": "Enter a name: ",
        "m2": "\nThe winner is... ",
        "m3": "\nThere is no participant.",
    }

    participant_list = []

    while True:
        name = input(messages["m1"])
        if name == "":
            break
        participant_list.append(name)

    if participant_list == []:
        answer_message = messages["m3"]
    else:
        winner_id = random.randint(1, len(participant_list)) - 1
        answer_message = messages["m2"] + participant_list[winner_id]

    print(answer_message)


main()
