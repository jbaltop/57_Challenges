#!/usr/local/bin/python3

# 숫자 추가

# 입력: 여러 개의 숫자
# 프로세스: 합계 계산
# 출력: 합계

messages = [ "\nEnter a number(type 'q' or press <enter> to quit): ", "\nThe total is {}" ]

total = 0

while True:
	n = input(messages[0])
	if n.lower() == 'q' or n.lower() == "'q'" or n == '':
		break
	total = total + int(n)

answer = messages[1].format(total)

print(answer)
