#!/usr/local/bin/python3

# 온도 변환

# 입력: 화씨 온도 또는 섭씨 온도
# 프로세스: 온도 변환
# 출력: 변환된 온도

c1 = float(input("temperature(c): "))
f1 = float(input("temperature(f): "))

c2 = (f1 - 32) * 5 / 9
f2 = (c1 * 9 / 5) + 32

message = "\n" + str(c1) + " Celsius is " + str(f2) + " Fahrenheit." + "\n" + str(f1) + " in Fahrenheit is " + str(c2) + " Celsius."

print(message)
