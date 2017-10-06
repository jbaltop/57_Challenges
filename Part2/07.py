#!/usr/local/bin/python3

# 직사각형 방의 면적

# 입력: 방의 길이, 방의 폭
# 프로세스: 방의 면적을 제곱 피트와 제곱 미터로 계산
# 출력: 방의 면적

length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))

square_feet = length * width
square_meter = square_feet * 0.09290304
result = "\nThe area is\n" + str(square_feet) + " square feet\n" + str(square_meter) + " square meter(s)."

print(result)
