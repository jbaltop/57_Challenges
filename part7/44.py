#!/usr/local/bin/python3
# coding=UTF-8

# 제품 검색

# 입력: 제품 이름
# 프로세스: 제품에 해당하는 현재 가격과 수량 조회
# 출력: 제품 이름, 가격, 수량

import json

messages = {
	"product": "\nWhat is the product name? ",
	"sorry": "\nSorry, that product was not found in our inventory.",
	"name": "\nName: {}",
	"price": "Price: {}",
	"quantity": "Quantity on hand: {}",
	}

fin = open('44.json', 'rt')
product_json = fin.read()
fin.close()

product_dictionary = json.loads(product_json)

def make_new_dictionary(products_list):
	new_dictionary = {}
	for item in products_list:
		new_dictionary[item['name']] = [item['price'], item['quantity']]
	return new_dictionary

new_dictionary = make_new_dictionary(product_dictionary['products'])

while True:
	product_name = input(messages["product"])
	if product_name in new_dictionary:
		print(messages["name"].format(product_name))
		print(messages["price"].format(new_dictionary[product_name][0]))
		print(messages["price"].format(new_dictionary[product_name][1]))
		break
	print(messages["sorry"])
