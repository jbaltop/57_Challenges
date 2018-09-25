import urllib.request
import json


def calculate_max_length(people_list):
    name_len_list = [4]
    craft_len_list = [5]
    for person in people_list:
        name_len_list.append(len(person[0]))
        craft_len_list.append(len(person[1]))
    name_len_list.sort(reverse=True)
    craft_len_list.sort(reverse=True)
    name_max_length = name_len_list[0]
    craft_max_length = craft_len_list[0]
    return name_max_length, craft_max_length


def make_table(name_max_length, craft_max_length, people_list):
    table_template = {}
    table_template["1"] = (
        "+" + "-" * (name_max_length + 2) + "+" + "-" * (craft_max_length + 2) + "+"
    )
    table_template_string = (
        "| {:" + str(name_max_length) + "} | {:" + str(craft_max_length) + "} |"
    )
    table_template["2"] = table_template_string
    table = []
    table.append(table_template["1"])
    table.append(table_template["2"].format("Name", "Craft"))
    table.append(table_template["1"])
    for person in people_list:
        table.append(table_template["2"].format(person[0], person[1]))
    table.append(table_template["1"])
    return table


def main():
    messages = {"m1": "\nThere are {} people in space right now: \n"}

    url = "http://api.open-notify.org/astros.json"

    people_json = urllib.request.urlopen(url).read().decode("utf-8")

    people_dictionary = json.loads(people_json)

    people_list = []
    for person in people_dictionary["people"]:
        people_list.append([person["name"], person["craft"]])
    people_list.sort()

    number = people_dictionary["number"]

    print(messages["m1"].format(number))

    length_tuple = calculate_max_length(people_list)
    name_max_length, craft_max_length = length_tuple

    table = make_table(name_max_length, craft_max_length, people_list)

    for row in table:
        print(row)

    print()


main()
