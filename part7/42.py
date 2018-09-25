def file_to_list(filename):
    lines = []
    fin = open(filename, "rt", encoding="utf-8")
    lines = fin.readlines()
    fin.close()
    return lines


def print_table(lines):
    template = {
        "1": "+" + "-" * 11 + "+" + "-" * 11 + "+" + "-" * 8 + "+",
        "2": "| {:<10.9}| {:<10.9}| {:<7.6}|",
    }

    print(template["1"])
    print(template["2"].format("Last", "First", "Salary"))
    print(template["1"])
    for line in lines:
        field = line.rstrip().split(",")
        print(template["2"].format(field[0], field[1], field[2]))
    print(template["1"])


def main():
    lines = file_to_list("../data/42.txt")
    print_table(lines)


main()
