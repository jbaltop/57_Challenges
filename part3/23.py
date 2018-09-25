def main():
    m0 = "\nIf the answer is 'yes' enter '1', if 'no' enter '0'."
    m1 = "\nClean terminals and try starting again."
    m2 = "\nReplace cables and try again."
    m3 = "\nReplace battery."
    m4 = "\nCheck spark plug connections."
    m5 = "\nCheck to ensure the choke is opening and closing."
    m6 = "\nGet it in for service."
    m7 = "\nThere is no question."

    q1 = "\nIs the car silent when you turn the key? "
    q2 = "\nAre the battery terminals corroded? "
    q3 = "\nDoes the car make a clicking noise? "
    q4 = "\nDoes the car crank up but fail to start? "
    q5 = "\nDoes the engine start and then die? "
    q6 = "\nDoes your car have fuel injection? "

    print(m0)

    a1 = input(q1)
    if a1 == "1":
        a2 = input(q2)
        if a2 == "1":
            answer_message = m1
        elif a2 == "0":
            answer_message = m2
    elif a1 == "0":
        a3 = input(q3)
        if a3 == "1":
            answer_message = m3
        elif a3 == "0":
            a4 = input(q4)
            if a4 == "1":
                answer_message = m4
            elif a4 == "0":
                a5 = input(q5)
                if a5 == "1":
                    a6 = input(q6)
                    if a6 == "1":
                        answer_message = m5
                    elif a6 == "0":
                        answer_message = m6
                elif a5 == "0":
                    answer_message = m7

    print(answer_message)


main()
