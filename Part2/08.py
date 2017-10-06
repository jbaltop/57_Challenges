#!/usr/local/bin/python3

# 피자 파티

# 입력: 사람 수, 피자 개수, 조각 개수
# 프로세스: 한 사람이 받게 되는 피자 조각 개수 계산, 남는 조각의 개수 계산
# 출력: 한 사람이 받게 되는 피자 조각 개수, 남는 조각 개수 

a = number_of_people = int(input("How many people? "))
b = number_of_pizzas = int(input("How many pizzas do you have? "))
c = number_of_pieces_in_a_pizza = int(input("How many pieces are in a pizza? "))

if a == 0:
	result = "\nnumber of people can't be 0"
else:
	d = number_of_pieces_each_person_gets = (b * c) // a
	e = number_of_remain_pieces = b * c - a * d
	result = "\nEach Person gets " + str(d) + " piece(s) of pizza." + "\nThere are " + str(e) + " leftover piece(s)."

print(result)
