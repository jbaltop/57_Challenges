#!/usr/local/bin/python3

# 필터링 레코드

# 입력: 키워드
# 프로세스: FirstName이나 LastName에 키워드가 들어있는 레코드 선택
# 출력: 표

import sqlite3
import sys

def printf(format, *args):
	sys.stdout.write(format % args)

messages = {
	"keyword": "Enter a search string: ",
	}

keyword = input(messages["keyword"])

db = sqlite3.connect('database/sample')

cursor = db.cursor()

cursor.execute('''SELECT PRINTF("%-25s| %-25s| %-25s", FIRSTNAME || ' ' || LASTNAME, POSITION, SEPARATIONDATE) FROM EMPLOYEE WHERE FIRSTNAME LIKE "%{}%" OR LASTNAME LIKE "%{}%"'''.format(keyword, keyword))

printf("%-25s| %-25s| %-25s\n", "Name", "Position", "Separation Date")
print("-"*25+'+'+"-"*26+"+"+"-"*16)

for row in cursor:
	print(row[0])

db.close()
