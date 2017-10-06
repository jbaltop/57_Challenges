#!/usr/local/bin/python3

# 세금 계산기

# 입력: 가격, 주 이름
# 프로세스: 세금 계산, 총액 계산
# 출력: 세금, 총액

order_amount = float(input("What is the order amount? "))
state = input("What is the state? ")

vat = 5.5

total = order_amount
result = "\nThe total is $" + str(order_amount)

if state.lower() == 'wisconsin' or state.lower() == "wi":
	tax = order_amount * vat / 100
	total = round(order_amount + tax, 2)
	result = "\nThe subtotal is $" + str(order_amount) + "\nThe tax is $" + str(round(tax, 2)) + "\nThe total is $" + str(total)

print(result)
