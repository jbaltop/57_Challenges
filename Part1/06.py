#!/usr/local/bin/python3

# 퇴직 계산기

# 입력: 현재 나이, 퇴직하고자 하는 나이
# 프로세스: 퇴직하기까지 몇 년 남았는지, 퇴직하는 해는 몇 년이 되는지 계산
# 프로세스: 계산 결과

import datetime

current_age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like to retire? "))

years_left = retire_age - current_age
current_year = int(datetime.datetime.now().strftime('%Y'))
retire_year = current_year + years_left
speech = "\nYou have " + str(years_left) + " years left until you can retire." + "\nIt's " + str(current_year) + ", so you can retire in " + str(retire_year) + "."

print(speech)
