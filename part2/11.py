#!/usr/local/bin/python3

# 환율 변환

# 입력: 유로 금액, 유로 환율
# 프로세스: 유로에 해당하는 미국 달러 값 계산
# 출력: 유로에 해당하는 미국 달러 값

import math

euro = float(input("How many Euros are you exchanging? "))
exchange_rate = float(input("What is the exchange rate? "))

dollar = math.ceil((euro * exchange_rate / 100) * 100) / 100
result = "\n" + str(euro) + " euros at an exchange rate of " + str(exchange_rate) + " is " + str(dollar) + " dollars."

print(result)
