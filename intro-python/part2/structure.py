#!/usr/bin/env python

# Import문
import os
import sys


# Module Constants
START_MESSAGE = "CLI Inspection Script"


# Module "Global" Variables
location = os.path.abspath(__file__)


# Module Functions and Classes
def main(*args):
    """
    아래 함수는 실행된 파일의 위치와 입력된 인자를 출력하는 함수입니다.
    예) python structure.py 1 2 3 실행
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)


# 파일이 실행 시, main함수 실행
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)
