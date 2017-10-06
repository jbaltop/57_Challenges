#!/usr/local/bin/python3

# 숫자 비교

# 입력: 숫자 세 개
# 프로세스: 숫자 세 개 비교
# 출력: 같은 숫자가 있다면 프로그램을 종료시키고, 그렇지 않다면 가장 큰 수를 출력

a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

if a == b or b == c or c == a:
	message = "\ngood bye"
else:
	if a > b:
		if a > c:
			largest_number = a
		else:
			largest_number = c
	elif b > c:
		if b > a:
			largest_number = b
		else:
			largest_number = a
	elif c > a:
		if c > b:
			largest_number = c
		else:
			largest_number = b
	message = "\nThe largest number is " + str(largest_number) + "."

print(message)
