#1

import math

degree = float(input())
radian = degree * math.pi / 180
print(radian)


#2

height = float(input())
base1 = float(input())
base2 = float(input())

area = 0.5 * (base1 + base2) * height
print(area)


#3

import math

num_sides = int(input())
length_side = float(input())

area = (num_sides * length_side ** 2) / (4 * math.tan(math.pi / num_sides))
print(area)


#4

base_length = float(input())
height = float(input())

area = base_length * height
print(area)
