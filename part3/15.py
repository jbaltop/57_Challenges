#!/usr/local/bin/python3

# 암호 검증

# 입력: 이름, 암호(비밀번호)
# 프로세스: 미리 저장된 사용자 이름에 대한 암호를 비교한다
# 출력: 암호의 일치 여부

print("Username: Hello\nPassword: World")

username = input("Username: ")
password = input("Password: ")

if username == "Hello":
	if password == "World":
		message = "\nWelcome, " + username + "!"
	else:
		message = "\nYour password is incorrect."
else:
	message = "\nYour username or password is incorrect."

print(message)
