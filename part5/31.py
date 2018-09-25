def calculate_target_heart_rate(age, resting_pulse):
    intensity = 55
    intensity_and_rate_lists = []
    while intensity <= 95:
        thr = round((((220 - age) - resting_pulse) * intensity / 100) + resting_pulse)
        intensity_and_rate_list = [intensity, thr]
        intensity_and_rate_lists.append(intensity_and_rate_list)
        intensity += 5
    return intensity_and_rate_lists


def print_chart(arg):
    print("\n intensity |   rate    \n-----------+-----------")
    chart = ""
    for pair in arg:
        chart = chart + "    {}%    | {}  bpm  \n".format(str(pair[0]), str(pair[1]))
    print(chart)


def main():
    messages = ["\nage: ", "resting pulse: "]

    result = calculate_target_heart_rate(
        int(input(messages[0])), int(input(messages[1]))
    )

    print_chart(result)


main()
