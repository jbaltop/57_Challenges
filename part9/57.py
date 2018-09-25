import random


def read_question():
    with open("../data/57.txt", "rt", encoding="utf-8") as fin:
        questions = fin.read()
        question_list = questions.split("\n")
        question_list.remove("")
        question_list2 = [
            question_list[i : i + 6] for i in range(0, len(question_list), 6)
        ]
    return question_list2


def select_question(length):
    x = random.randint(0, length - 1)
    return x


def play_game(question_list):
    i = 0
    length = len(question_list)
    question_num = select_question(length)
    selected_questions = []
    while True:
        while i < length:
            while question_num in selected_questions:
                question_num = select_question(length)
            selected_questions.append(question_num)
            fmt = "\n{}\n[a] {}\n[b] {}\n[c] {}\n[d] {}"
            print(
                fmt.format(
                    question_list[question_num][0],
                    question_list[question_num][1],
                    question_list[question_num][2],
                    question_list[question_num][3],
                    question_list[question_num][4],
                )
            )
            answer = input("answer [a/b/c/d]: ")
            while check_valid_answer(answer) == False:
                answer = input("answer [a/b/c/d]: ")
            while check_correct_answer(question_list, question_num, answer) == False:
                print("\ngame over. you got {} question(s) correct.".format(i))
                return False
            i += 1
        print("You got all {} questions.".format(i))
        break


def check_valid_answer(answer):
    answer_list = ["a", "b", "c", "d"]
    if answer.lower() in answer_list:
        return True
    return False


def check_correct_answer(question_list, question_num, answer):
    if answer.lower() == question_list[question_num][-1]:
        return True
    return False


def main():
    question_list = read_question()
    play_game(question_list)


main()
