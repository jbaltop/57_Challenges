#!/usr/local/bin/python3

# 글자 수 세기

# 입력: 문자열
# 프로세스: 문자열의 글자 수 계산
# 출력: 문자열, 문자열의 글자 수

string = input("Type something to calculate string length.\n")

length = len(string)
speech = '\n"' + string + '"' +  " has " + str(length) + " character(s)."

print(speech)
