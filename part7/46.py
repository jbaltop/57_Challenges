import re
from collections import Counter


def read_file(filename):
    fin = open(filename, "rt", encoding="utf-8")
    contents = fin.read()
    fin.close()
    return contents


def count_words(contents):
    word_list = re.split("\W", contents)
    word_counter = Counter(word_list)
    return word_counter.most_common()


def print_frequency_histogram(items):
    messages = {"1": "{}: {}"}

    for item in items:
        a, b = item
        if a == "":
            continue
        else:
            print(messages["1"].format(a, "*" * b))


def main():
    contents = read_file("../data/46.txt")
    word_frequency = count_words(contents)
    print_frequency_histogram(word_frequency)


main()
