import sqlite3
import sys


def main():
    def printf(format, *args):
        sys.stdout.write(format % args)

    messages = {"keyword": "Enter a search string: "}

    keyword = input(messages["keyword"])

    db = sqlite3.connect("../data/39_40.sqlite3")

    cursor = db.cursor()

    cursor.execute(
        '''SELECT PRINTF("%-25s| %-25s| %-25s", FIRSTNAME || ' ' || LASTNAME, POSITION, SEPARATIONDATE) FROM EMPLOYEE WHERE FIRSTNAME LIKE "%{}%" OR LASTNAME LIKE "%{}%"'''.format(
            keyword, keyword
        )
    )

    printf("%-25s| %-25s| %-25s\n", "Name", "Position", "Separation Date")
    print("-" * 25 + "+" + "-" * 26 + "+" + "-" * 16)

    for row in cursor:
        print(row[0])

    db.close()


main()
