#!/usr/local/bin/python3

# 복리 계산

# 입력: 원금, 투자 기간, 연이율, 연간 수익이 지급되는 횟수
# 프로세스: 원리금 계산
# 출력: 원리금

import math

p = principal = int(input("principal($): "))
r = rate = float(input("rate of interest(%): "))
t = number_of_years = int(input("number of years: "))
n = number_of_times_the_interest_is_compounded_per_year = int(input("number of times the interest is compounded per year: "))

a = principal_and_interest = math.ceil((p * (1 + r / 100 / n) ** (n * t)) * 100) / 100
result = "\n" + str(p) + " invested at " + str(r) + "% for " + str(t) + " years compounded " + str(n) + " times per years is $" + str(a) 

print(result)
