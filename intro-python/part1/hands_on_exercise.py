"""Intro to Python - Part 1 - Hands-On Exercise."""


import math   #수학 관련 함수를 모아놓은 라이브러리
import random #난수 발생을 위한 라이브러리


# TODO: 원주율 값을 갖고있는 변수 pi를 print함수를 이용하여 출력하세요
pi = math.pi



# TODO: 0에서 100사이로 랜덤하게 생성되는 변수 i를  50보다 작거나 (<50) 혹은 50보다 클때만 출력하고, 그 외의 경우(i=50일때)에는 본인의 이름이 출력될 수 있도록 하세요
i = random.randint(0, 100)


# TODO: 아래 세가지 과일이름을 갖는 변수 picked_fruit의 값에 따라 해당 과일의 색깔을 출력하게 만들어보세요
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])


# TODO: 두 수의 곱을 반환하는 함수를 만들어보세요 함수의 이름은 multi로 지정합니다.
# 아래에 함수를 작성하세요.


# TODO: 두 수의 곱을 반환하는 함수를 호출하여 아래 곱셈의 값을 출력하세요

print("12 x 96 =",)

print("48 x 17 =",)

print("196523 x 87323 =",)
