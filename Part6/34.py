#!/usr/local/bin/python3

# 사원 명단 삭제

# 입력: 제거할 사원 이름
# 프로세스: 이름을 명단에서 제거
# 출력: 명단

messages = {
	"m1": "\nThere are {} employees:",
	"m2": "\nEnter an employee name to remove: ",
	"m3": "\nThe name {} is not in the list. Please enter a name in the list: "
	}

employee_list = [ 'John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin' ]

def make_new_list(arg):
	employee_list2 = []

	for employee in employee_list:
		if employee == arg:
			continue
		else:
			employee_list2.append(employee)
	return employee_list2

def print_list(arg):
	print(messages["m1"].format(len(arg)))

	for employee in arg:
		print(employee)

def remove_name():
	print_list(employee_list)
	print(messages["m2"], end = '')
	while True:
		name = input()
		new_list = make_new_list(name)
		if name in employee_list:
			print_list(new_list)
			break
		print(messages["m3"].format(name), end = '')

remove_name()
