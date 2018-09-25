import datetime


def main():
    current_age = int(input("What is your current age? "))
    retire_age = int(input("At what age would you like to retire? "))

    years_left = retire_age - current_age
    current_year = int(datetime.datetime.now().strftime("%Y"))
    retire_year = current_year + years_left
    speech = (
        "\nYou have "
        + str(years_left)
        + " years left until you can retire."
        + "\nIt's "
        + str(current_year)
        + ", so you can retire in "
        + str(retire_year)
        + "."
    )

    print(speech)


main()
