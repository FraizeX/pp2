import math

a = int(input("Input degree: "))
answer = a * math.pi / 180
answer = round(answer, 6)

print("Output radian: " + str(answer))