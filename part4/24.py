#!/usr/local/bin/python3

# 애너그램 점검

# 입력: 두 문자열
# 프로세스: 두 문자열이 애너그램인지 검사
# 출력: 애너그램 여부

def is_anagram(a, b):
	if len(a) == len(b):
		c = sorted(list(a))
		d = sorted(list(b))
		if c == d:
			return 1
		else:
			return 0
	else:
		return -1

result = -1

while result < 0:
	message = "\nEnter two strings and I'll tell you if they are anagrams."
	print(message)

	string1 = input("first string: ")
	string2 = input("second string: ")
	result = is_anagram(string1, string2)

	answer = "\n" + '"' + string1 + '"' + " and " + '"' + string2 + '"'
	if result == 1:
		answer = answer + " are anagrams."
	elif result == 0:
		answer = answer + " aren't anagrams."
	else:
		answer = answer + "have different length."
		answer = answer + "\nPlease enter two strings with the same length."

	print(answer)
