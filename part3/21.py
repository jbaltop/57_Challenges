def main():
    month_number = input("Please enter the number of the month: ")

    number_to_name = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    if month_number in number_to_name:
        month_name = number_to_name[month_number]
        message = "\nThe name of the month is " + month_name + "."
    else:
        message = "\nPlease enter the correct number of month."

    print(message)


main()
