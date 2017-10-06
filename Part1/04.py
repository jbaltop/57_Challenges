#!/usr/local/bin/python3

# Mad Libs

# 입력: 단어
# 프로세스: 단어를 이용해 문장 완성
# 출력: 문장

exclamation = input("Enter an exclamation: ")
adverb = input("Enter an adverb: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")

speech = '\n"' + exclamation + "! he said " + adverb + " as he jumped into his convertible " + noun + " and drove off with his " + adjective + " wife." + '"'

print(speech)
