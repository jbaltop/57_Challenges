#!/usr/local/bin/python3

# Magic 8 Ball

# 입력: 질문
# 프로세스: 무작위로 답변 설정
# 출력: 답변

import random

messages = {
	"question": "\nWhat's your question? ",
	"1": "\nYes.",
	"2": "\nNo.",
	"3": "\nMaybe.",
	"4": "\nAsk again later.",
	}

input(messages["question"])

random_number = random.randint(1, 4)
print(messages[str(random_number)])
