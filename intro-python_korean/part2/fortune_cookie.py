#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script flow and debugging. Print your own fortune cookie!"""

import random


FORTUNES = [
    "이 코드도 언젠간 잘 동작할 거에요",
    "오늘 날씨 너무 좋아요!",
    "미래에는 Devnet과 함께해요",
]


def generate_fortune() -> str:
    """행운을 생성해주는 함수"""
    return random.choice(FORTUNES)


def generate_lucky_numbers(how_many: int) -> list:
    """입력된 개수만큼 행운의 번호를 생성해주는 함수"""
    lucky_numbers = []
    for _ in range(how_many):
        lucky_numbers.append(random.randint(0, 99))
    return lucky_numbers


def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    """행운의 메세지를 생성하고 반환하는 함수
    메세지는 사용자의 행운번호 또한 포함해야합니다
    """
    # TODO: generate_fortune() 과 generate_lucky_numbers() 를 이용하여
    # 행운 메세지를 생성하고 해당 메세지를 반환하는 함수를 만들어보세요
    message = generate_fortune()
    numbers = str(generate_lucky_numbers(how_many_lucky_numbers))
    return f'{message} \nAnd your lucky number: " {numbers}'


def main():
    """포춘쿠키 생성 및 출력하는 Main문"""
    print("Get your fortune cookie!")

    # 필요한 행운번호의 개수를 물어보는 코드
    qty_lucky_numbers = input("How many lucky numbers would you like?  ")
    qty_lucky_numbers = int(qty_lucky_numbers.strip())

    # 행운 생성 및 출력하는 코드
    fortune_cookie_message = create_fortune_cookie_message(qty_lucky_numbers)
    print("\nHere is your fortune:\n")
    print(fortune_cookie_message)


if __name__ == '__main__':
    main()
