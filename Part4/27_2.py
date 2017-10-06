#!/usr/local/bin/python3

# 입력 값 검증

# 입력: 이름과 성, 사번, 우편번호, 우편번호
# 프로세스: 입력 받은 것이 규칙에 맞는지 점검
# 출력: 잘못된 데이터의 여부

# TODO: 현재는 list 2개를 사용 --> 향후 list 1개로 줄여야 함

question_messages = [ "\nfirst name: ", "last name: ", "ZIP code: ", "employee ID(AA-0000): " ]

error_message_template = [ "\nThere were no errors found.", "\n'{f1}' is not a valid {f2}.", "\nThe '{f1}' must be filled in.", " It is too short.", "\nThe ZIP code must be numeric." ]

def validate_notnull(arg):
	if arg != '':
		return True
	else:
		return False

def validate_name(arg):
	if len(arg) >= 2:
		return True
	else:
		return False

def validate_zip_code(arg):
	return arg.isdigit()

def validate_employee_id(arg):
	if len(arg) == 7 and arg[0:1].isalpha() == True and arg[2] == '-' and arg[3:-1].isdigit() == True:
		return True
	else:
		return False

def validate_input(first_name, last_name, zip_code, employee_id):
	result = 4
	error_ids = [] 
	error_formats = []
	if validate_notnull(first_name) == False:
		error_ids.append(2)
		error_formats.append({'f1': "first name"})
		result -= 1
	elif validate_name(first_name) == False:
		result -= 1
		error_ids.append(1)
		error_formats.append({'f1': first_name, 'f2': "first name"})
		error_ids.append(3)
		error_formats.append({})

	if validate_notnull(last_name) == False:
		error_ids.append(2)
		error_formats.append({'f1': "last name"})
		result -= 1
	elif validate_name(last_name) == False:
		result -= 1
		error_ids.append(1)
		error_formats.append({'f1': last_name, 'f2': "last name"})
		error_ids.append(3)
		error_formats.append({})

	if validate_notnull(zip_code) == False:
		error_ids.append(2)
		error_formats.append({'f1': "ZIP code"})
		result -= 1
	elif validate_zip_code(zip_code) == False:
		result -= 1
		error_ids.append(4)
		error_formats.append({})

	if validate_notnull(employee_id) == False:
		error_ids.append(2)
		error_formats.append({'f1': "employee ID"})
		result -= 1
	elif validate_employee_id(employee_id) == False:
		result -= 1
		error_ids.append(1)
		error_formats.append({'f1': "employee ID", 'f2': "ID"})

	if error_ids == []:
		error_ids.append(0)
		error_formats.append({})

	for index, error_id in enumerate(error_ids):
		error_format = error_formats[index]
		print(error_message_template[error_id].format(**error_format), end='')

	return result

result = 0

while result < 4:
	answers = []
	for question_message in question_messages:
		answers.append(input(question_message))

	result = validate_input(answers[0], answers[1], answers[2], answers[3])
	if result < 4:
		print("\nPlease try again.")
	else:
		print("\n")
		break
