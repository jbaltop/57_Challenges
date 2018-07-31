#!/usr/local/bin/python3

# 단어 빈도 검색

# 입력: 파일
# 프로세스: 파일에서 단어 빈도 측정
# 출력: 단어의 빈도(히스토그램 형태)

import re
from collections import Counter

messages = {
	"1": "{}: {}",
	}

def read_file(filename):
	fin = open(filename, 'rt')
	contents = fin.read()
	fin.close()
	return contents

def count_words(contents):
	word_list = re.split('\W', contents)
	word_counter = Counter(word_list)
	return word_counter.most_common()

def print_frequency_histogram(items):
	for item in items:
		a, b = item
		if a == '':
			continue
		else:
			print(messages["1"].format(a, '*' * b))

contents = read_file('46.txt')
word_frequency = count_words(contents)
print_frequency_histogram(word_frequency)
