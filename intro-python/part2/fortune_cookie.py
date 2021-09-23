#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script flow and debugging. Print your own fortune cookie!"""


import random


FORTUNES = [
    "There is a good chance your code will work, eventually.",
    "The weather will be hot, cold or just right today.",
    "I see Network DevOps in your future.",
]


def generate_fortune() -> str:
    """랜덤한 FORTUNES 메세지를 반환하는 함수"""
    return random.choice(FORTUNES)


def generate_lucky_numbers(how_many: int) -> list:
    """사용자가 입력한 숫자를 개수로하는 행운번호를 반환하는 함수"""
    lucky_numbers = []
    for _ in range(how_many):
        lucky_numbers.append(random.randint(0, 99))
    return lucky_numbers


def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    """
    FORTUNES 메세지를 출력하는 함수 +해당 메세지에 행운번호도 함께 포함시키세요
    """
    # TODO: generate_fortune()함수와 generate_lucky_numbers()함수를 호출하여
    # FORTUNES 메세지와 행운번호를 생성하고 해당 값을 반환하도록 하세요
    raise NotImplementedError()


def main():
    """포춘쿠키 생성 및 출력하는 main함수"""
    print("Get your fortune cookie!")

    # 행운번호의 개수를 입력받아 qty_lucky_numbers변수에 저장
    qty_lucky_numbers = input("How many lucky numbers would you like?  ")
    qty_lucky_numbers = int(qty_lucky_numbers.strip())

    # qty_lucky_numbers를 create_foutune_cookie_message의 인자로 전달하여 생성될 행운번호 개수 지정 및 행운메세지 출력
    fortune_cookie_message = create_fortune_cookie_message(qty_lucky_numbers)
    print("\nHere is your fortune:\n")
    print(fortune_cookie_message)


if __name__ == '__main__':
    main()
