#!/usr/local/bin/python3

# 카드 대금 상환 기간

# 입력: 총 대금(b), 연이율(apr, annual percentage rate), 월 상환 금액(p)
# 프로세스: 상환에 소요되는 개월 수 계산
# 출력: 상환에 소요되는 개월 수

import math

q1 = "What is your principal? "
q2 = "What is your Annual Percentage Rate on the card as a percent? "
q3 = "What is the monthly payment you can make? "

def calculate_months_until_paid_off(p, r, m):
	r = r / 100
	n = (math.log(m/p)-math.log(m/p-r/12))/(12*math.log(1+r/12))*12 # http://www.cnusd.k12.ca.us/cms/lib/CA01001152/Centricity/Domain/255/05_Financial_Algebra_AIE_ch04.pdf
	return math.ceil(n)

answer = "\nIt will take you " + str(calculate_months_until_paid_off(float(input(q1)), float(input(q2)), float(input(q3)))) + " months to pay off this card."

print(answer)
