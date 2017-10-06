#!/usr/local/bin/python3

# 암호 길이 점검

# 입력: 암호(비밀번호)
# 프로세스: 암호의 복잡도 계산
# 출력: 암호의 복잡도

password = input("\npassword: ")

m1 = "\nThe password '" + password + "' is a "
m2 = " password."
message1 = m1 + "very weak" + m2
message2 = m1 + "weak" + m2
message3 = m1 + "strong"  + m2
message4 = m1 + "very strong" + m2
message5 = m1 + "normal" + m2

numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
symbols = {'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'}

def is_it_included(string, type_of_data):
	character_list = []
	for i in string:
		if i.lower() in type_of_data:
			character_list.append(i)
	if character_list == []:
		return False
	else:
		return True

def password_validator(arg):
	if len(arg) < 8:
		if arg.isdigit() == True:
			return message1
		elif arg.isalpha() == True:
			return message2
	else:
		if is_it_included(arg, numbers) and is_it_included(arg, alphabets):
			if is_it_included(arg, symbols):
				return message4
			else:
				return message3

answer = password_validator(password)

if answer == None:
	answer = message5

print(answer)
