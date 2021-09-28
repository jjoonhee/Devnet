"""Intro to Python - Part 1 - Hands-On Exercise."""
# -*- coding: utf-8 -*-
import math   #수학 관련 함수를 모아놓은 라이브러리
import random #난수 발생을 위한 라이브러리


print("=" * 20) # 구분선입니다 
# TODO: 원주율 값을 갖고있는 변수 pi를 print함수를 이용하여 출력하세요
pi = math.pi
print("{:.3f}".format(pi))

print("=" * 20) # 구분선입니다
# TODO: 0에서 99사이로 랜덤하게 생성되는 변수 i가 50보다 크거나 작은 경우, i값을 출력하고 50인경우  본인의 이름 이니셜을 출력하세요
i = random.randint(0, 100)
if not i =50:
	print(i)
else:
	print("JH")

#i가 50이 나올때까지 반복하는 while문
cnt = 0
while True:
	i = random.randint(0, 100)
	if not i == 100:
		cnt +=1
	else:
		print(f"{cnt}th Try: Finally! {i}")
		break

print("=" * 20) # 구분선입니다
# TODO: 아래 세가지 과일이름을 갖는 변수 picked_fruit의 값에 따라 해당 과일의 색깔을 출력하게 만들어보세요
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
	print("O")
elif picked_fruit == "strawberry":
	print("R")
else:
	print("Y")

# TODO: 두 수의 곱을 반환하는 funtion을 만들어보세요 funtion의 이름은 multi로 지정합니다.
# Define the function here.
def multi(a, b):
	print("{} * {} = {}".format(a,b,a*b))
	#print(f"{a} * {b} = {a*b}")


print("=" * 20) # 구분선입니다
# TODO: 두 수의 곱을 반환하는 funtion을 호출하여 아래 곱셈의 값을 출력하세요

multi(12,96)

multi(48,17)

multi(196523, 87323)

print("=" * 20) # 구분선입니다


