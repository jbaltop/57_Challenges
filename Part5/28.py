#!/usr/local/bin/python3

# 숫자 추가

# 입력: 5개의 숫자
# 프로세스: 합계 계산
# 출력: 합계

messages = [ "\nEnter a number: ", "\nThe total is {}" ]

i = 0
total = 0

while i < 5:
	total = total + int(input(messages[0]))
	i += 1

answer = messages[1].format(total)

print(answer)
