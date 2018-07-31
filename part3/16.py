#!/usr/local/bin/python3

# 합법적으로 운전 가능한 연령

# 입력: 나이
# 프로세스: 운전 가능한 나이인지 계산
# 출력: 운전 가능 여부

age = int(input("What is your age? "))

m = minimum_age_to_drive = 16

if age >= m:
	message = "\nYou are old enough to legally drive."
else:
	message = "\nYou are not old enough to legally drive."

print(message)
