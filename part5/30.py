#!/usr/local/bin/python3

# 곱셈표

# 입력: (없음)
# 프로세스: 0부터 12까지 곱셈표 만듦
# 출력: 곱셈표 출력

def print_result(a, b):
	print("{} * {} = {}".format(a, b, a*b))

def make_list():
	a = 0
	while a <= 12:
		b = 0
		while b <= 12:
			print_result(a, b)
			b += 1
		a += 1

make_list()
