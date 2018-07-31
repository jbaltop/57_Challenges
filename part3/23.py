#!/usr/local/bin/python3

# 자동차 문제 해결

# 입력: 질문에 대한 답
# 프로세스: 여러 질문들을 하면서 문제 파악
# 출력: 해결책 제시

m0 = message0 = "\n질문에 대한 답이 '예'일 경우에는 '1'을, '아니요'일 경우에는 '0'을 누르시오."
m1 = message1 = "\n단자를 깨끗하게 하고 다시 시도하라."
m2 = message2 = "\n케이블을 교체하고 다시 시도하라."
m3 = message3 = "\n배터리를 교체하고 다시 시도하라."
m4 = message4 = "\n점화플러그 연결 상태를 점검하라."
m5 = message5 = "\n초크가 제대로 여닫히는지 확인하라."
m6 = message6 = "\n서비스센터에 의뢰하라."
m7 = message7 = "\n문제가 없습니다."

q1 = question1 = "\n열쇠를 꽂고 돌렸을 때 차가 조용한가? "
q2 = question2 = "\n배터리 단자가 부식되었는가? "
q3 = question3 = "\n차에서 딸깍거리는 소리가 나는가? "
q4 = question4 = "\n시동이 완전히 걸리지 않는가? "
q5 = question5 = "\n엔진이 동작한 후 바로 꺼지는가? "
q6 = question6 = "\n차에 연료 분사 장치가 있는가? "

print(m0)

a1 = input(q1)
if a1 == '1':
	a2 = input(q2)
	if a2 == '1':
		answer_message = m1
	elif a2 == '0':
		answer_message = m2
elif a1 == '0':
	a3 = input(q3)
	if a3 == '1':
		answer_message = m3
	elif a3 == '0':
		a4 = input(q4)
		if a4 == '1':
			answer_message = m4
		elif a4 == '0':
			a5 = input(q5)
			if a5 == '1':
				a6 = input(q6)
				if a6 == '1':
					answer_message = m5
				elif a6 == '0':
					answer_message = m6
			elif a5 == '0':
				answer_message = m7

print(answer_message)
