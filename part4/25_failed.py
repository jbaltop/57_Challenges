#!/usr/local/bin/python3

# 암호 길이 점검

# 입력: 암호(비밀번호)
# 프로세스: 암호의 복잡도 계산
# 출력: 암호의 복잡도

# logic bug

password = input("\npassword: ")

message1 = "\nThe password '" + password + "' is a very weak password."
message2 = "\nThe password '" + password + "' is a weak password."
message3 = "\nThe password '" + password + "' is a strong password."
message4 = "\nThe password '" + password + "' is a very strong password."
message5 = "\nThe password '" + password + "' is a normal password."

def password_validator(arg):
	if len(arg) < 8:
		if arg.isdigit() == True:
			answer = message1
		elif arg.isalpha() == True:
			answer = message2
		else:
			answer = message5
	else:
		if arg.isdigit() == True or arg.isalpha() == True:
			answer = message5
		else:
			if arg.isalnum() == True:
				answer = message3
			else:
				answer = message4
	print(answer)

password_validator(password)
