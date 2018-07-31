#!/usr/local/bin/python3

# 암호 길이 점검

# 입력: 암호(비밀번호)
# 프로세스: 암호의 복잡도 계산
# 출력: 암호의 복잡도

password = input("\npassword: ")

m1 = "\nThe password '" + password + "' is a "
m2 = " password."

password_power = [ 'very weak', 'weak', 'strong', 'very strong', 'normal' ]

numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
symbols = {'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'}

def is_it_included(string, type_of_data):
	for i in string:
		if i.lower() in type_of_data:
			return True
	return False

def password_validator(arg):
	if len(arg) < 8:
		if arg.isdigit():
			return 0
		elif arg.isalpha():
			return 1
	else:
		if is_it_included(arg, numbers) and is_it_included(arg, alphabets):
			if is_it_included(arg, symbols):
				return 3
			else:
				return 2
	return 4

answer = password_validator(password)

message = m1 + password_power[answer] + m2
print(message)
