#!/usr/local/bin/python3

# 따옴표 출력

# 입력: 인용구, 그 말을 한 사람
# 프로세스: 메시지에 인용구와 그 말을 한 사람 추가
# 출력: 메시지

quote = input("What is the quote?\n")
person = input("Who said it?\n")

speech = "\n" +  person + " says, " + '"' + quote + '"'

print(speech)
