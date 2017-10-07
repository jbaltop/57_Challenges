#!/usr/local/bin/python3

# 승자 선택

# 입력: 대회 참가자
# 프로세스: 무작위로 수상자 선정
# 출력: 수상자

import random

messages = {
	"m1": "Enter a name: ",
	"m2": "\nThe winner is... ",
	"m3": "\nThere is no participant.",
	}

participant_list = []

while True:
	name = input(messages["m1"])
	if name == '':
		break
	participant_list.append(name)

if participant_list == []:
	answer_message = messages["m3"]
else:
	winner_id = random.randint(1, len(participant_list)) - 1
	answer_message = messages["m2"] + participant_list[winner_id]

print(answer_message)
