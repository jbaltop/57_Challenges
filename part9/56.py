#!/usr/local/bin/python3

# 상품 목록 추적

# 입력: 상품 이름, 시리얼 번호, 추정 가격
# 프로세스: 입력을 표로 만든다
# 출력: 표

def get_info():
	info_list = []
	while True:
		stop = input("Do you want to stop? [Y/n] ")
		if stop.lower() == 'y':
			break
		item = input("item: ")
		serial_num = input("serial number: ")
		while True:
			price = input("price($): ")
			try:
				price_float = float(price)
				break
			except ValueError:
				print("\nprice must be float")
		info_list.append([item, serial_num, price])
	return info_list

def make_json_file(info_list):
	n = len(info_list)
	with open('56.json', 'wt') as fout:
		fout.write('{"products": [')
		i = 0
		while i < n-1:
			fout.write('{"name": "' + info_list[i][0] + '", "serial_num": "' + info_list[i][1] + '", "price": "' + info_list[i][2] + '"}, ')
			i += 1
		fout.write('{"name": "' + info_list[i][0] + '", "serial_num": "' + info_list[i][1] + '", "price": "' + info_list[i][2] + '"}')
		fout.write(']}')

def make_html_file(product_list):
	with open('56.html', 'wt') as fout:
		fout.write('<html>\n\t<body>\n\t\t<table border>\n')
		fout.write('\t\t\t<tr>\n\t\t\t\t<th>Name</th>\n\t\t\t\t<th>Serial Number</th>\n\t\t\t\t<th>Price($)</th>\n\t\t\t</tr>\n')
		for product in product_list:
			fout.write('\t\t\t<tr>\n')
			for value in product:
				fout.write('\t\t\t\t<td>{}</td>\n'.format(value))
			fout.write('\t\t\t</tr>\n')
		fout.write('\t\t</table>\n\t</body>\n</html>')

def main():
	info_list = get_info()
	make_json_file(info_list)
	make_html_file(info_list)

if __name__ == '__main__':
	main()
