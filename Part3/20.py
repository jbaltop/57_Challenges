#!/usr/local/bin/python3

# 입력: 주문 가격, 주, 카운티
# 프로세스: 세금 계산, 총계 계산
# 출력: 세금, 총계

order_amount = float(input("What is the order amount? "))
state = input("What state do you live in? ")
if state.lower() == "wisconsin":
	county = input("what county do you live in? ")

wisconsin_state_tax = 5.5
eau_claire_county_tax = 0.5
dunn_county_tax = 0.4
illinois_state_tax = 8

total = order_amount
result = "\nThe total is $" + str(total)

if state.lower() == "wisconsin":
	if county.lower() == "eau claire":
		state_tax = order_amount * wisconsin_state_tax / 100
		county_tax = order_amount * eau_claire_county_tax / 100
		tax = state_tax + county_tax
		total = round(order_amount + tax, 2)
		result = "\nThe state tax is $" + str(round(state_tax, 2)) + "\nThe county tax is $" + str(round(county_tax, 2)) + "\nThe total tax is $" + str(round(tax, 2)) + "\nThe total is $" + str(total)
	elif county.lower() == "dunn":
		state_tax = order_amount * wisconsin_state_tax / 100
		county_tax = order_amount * dunn_county_tax / 100
		tax = state_tax + county_tax
		total = round(order_amount + tax, 2)
		result = "\nThe state tax is $" + str(round(state_tax, 2)) + "\nThe county tax is $" + str(round(county_tax, 2)) +  "\nThe total tax is $" + str(round(tax, 2)) + "\nThe total is $" + str(total)
elif state.lower() == "illinois":
	tax = state_tax = order_amount * illinois_state_tax / 100
	total = round(order_amount + tax, 2)
	result = "\nThe state tax is $" + str(round(state_tax, 2)) + "\nThe total is $" + str(total)

print(result)
