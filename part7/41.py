def file_to_list(filename):
    fin = open(filename, "rt", encoding="utf-8")
    names = fin.readlines()
    fin.close()
    return names


def order_name(names):
    return names.sort()


def list_to_file(names):
    messages = {"total": "Total of {} names"}

    fout = open("41_out.txt", "wt", encoding="utf-8")
    print("\n" + messages["total"].format(len(names)))
    print("-" * 17)
    for name in names:
        print(name, file=fout, end="")
    fout.close()


def read_file(filename):
    content = ""
    fin = open(filename, "rt", encoding="utf-8")
    for line in fin:
        content += line
    fin.close()
    return content


def main():
    names = file_to_list("../data/41.txt")
    order_name(names)
    list_to_file(names)

    print(read_file("41_out.txt"))


main()
