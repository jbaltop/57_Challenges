#1/usr/local/bin/python3

# 셀프계산대

# 입력: 물건의 가격, 물건의 수량
# 프로세스: 소계 계산, 세금 계산
# 출력: 물건 종류별 수량, 전체 수량, 가격 소계, 세금, 합계 금액

a = price_of_item_1 = float(input("Price of item 1: "))
b = quantity_of_item_1 = int(input("Quantity of item 1: "))
c = price_of_item_2 = float(input("Price of item 2: "))
d = quantity_of_item_2 = int(input("Quantity of item 2: "))
e = price_of_item_3 = float(input("Price of item 3: "))
f = quantity_of_item_3 = int(input("Quantity of item 3: "))

vat = 5.5

g = subtotal = a * b + c * d + e * f
h = tax = round(g * vat / 100, 2)
i = total = g + h
result = "\nSubtotal: " + str(g) + "\nTax: " + str(h) + "\nTotal: " + str(i)

print(result)
