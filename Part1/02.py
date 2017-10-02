#!/usr/local/bin/python3

string = input("Type something to calculate string length.\n")

length = len(string)
speech = '\n"' + string + '"' +  " has " + str(length) + " character(s)."

print(speech)
