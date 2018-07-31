#!/usr/local/bin/python3

# 레코드 정렬

# 입력: 정렬 기준
# 프로세스: 정렬 기준에 맞는 표 생성
# 출력: 표

import sqlite3
import sys

def printf(format, *args):
	sys.stdout.write(format % args)

messages = {
	"fieldname": "\nField Name(FirstName, LastName, Position, SeparationDate): ",
	}

while True:
	fieldname = input(messages["fieldname"])
	if fieldname.lower() == 'firstname' or fieldname.lower() == 'lastname' or fieldname.lower() == 'position' or fieldname.lower() == 'separationdate':
		break
	else:
		print("error: invalid field name.")
		continue

db = sqlite3.connect('database/sample')

cursor = db.cursor()

cursor.execute('''SELECT PRINTF("%-25s| %-25s| %-25s", FIRSTNAME || ' ' || LASTNAME, POSITION, SEPARATIONDATE) FROM EMPLOYEE ORDER BY {}'''.format(fieldname))

printf("%-25s| %-25s| %-25s\n", "Name", "Position", "Separation Date")
print("-"*25+'+'+"-"*26+"+"+"-"*16)

for row in cursor:
	print(row[0])

db.close()
