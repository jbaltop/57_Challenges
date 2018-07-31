#!/usr/local/bin/python3

# 데이터 파일 파싱

# 입력: csv로 된 리스트
# 프로세스: 입력을 표 형식으로 만든다
# 출력: 표

template = {
	"1": '+' + '-' * 11 + '+' + '-' * 11 + '+' + '-' * 8 + '+',
	"2": '| {:<10.9}| {:<10.9}| {:<7.6}|',
	}

def file_to_list(filename):
	lines = []
	fin = open(filename, 'rt')
	lines = fin.readlines()
	fin.close()
	return lines

def print_table(lines):
	print(template["1"])
	print(template["2"].format('Last', 'First', 'Salary'))
	print(template["1"])
	for line in lines:
		field = line.rstrip().split(',')
		print(template["2"].format(field[0], field[1], field[2]))
	print(template["1"])

lines = file_to_list('42.txt')
print_table(lines)
