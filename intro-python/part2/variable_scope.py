#!/usr/bin/env python


# 모듈 변수 생성
module_variable = "I am a module variable."


# 매개 변수를 받는 함수 생성
def my_function(argument_variable):
    """사용된 모듈/매개/지역변수를 출력하는 함수"""
    # 자역 변수 생성
    local_variable = "I am a local variable."

    print(module_variable, "...and I can be accessed inside a function.")
    print(argument_variable, "...and I can be passed to a function.")
    print(local_variable, "...and I can ONLY be accessed inside a function.")


# my_function함수에 매개변수를 넘겨 호출
my_function(argument_variable="I am a argument variable.")


# 지역변수를 module scope에서 호출
print("\nTrying to access local_variable outside of its function...")
try:
    print(local_variable)
except NameError as error:
    print(error)
