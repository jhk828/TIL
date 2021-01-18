# python에서 Module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
# 다른 python 파일에서 불러와서 사용할 수 있다.

# module을 사용하는 이유는 코드의 재사용성과 관리목적

# python 모듈은 크게 2가지가 있다.
# - C언어로 구성된 binary module
# - python언어로 구현된 일반 module

# module을 사용하기 위해 사용하는 keyword : import
# module도 파이썬 입장에서는 객체로 관리된다.

import sys

print(sys.path)     # python system library 폴더들 list
sys.path.append("c:/python_data")    # module을 저장할 폴더를 지정
print(sys.path)
#
# # module을 하나 만들어 보자! (python file을 하나 생성)
# # module1.py 파일을 "c:/python_data"에 저장한다.
#
# # module을 만들었으니 가져다가 사용해 보아요!
#
import module1

print(module1.my_pi)                # 3.1414926535
print(module1.my_adder(10, 20))     # 30

import module1 as m1
print(m1.my_pi)                # 3.1414926535
print(m1.my_adder(10, 20))     # 30

from 패키지명
from module1 import my_adder
print(my_adder(10, 20))     # 30

from module1 import *
print(my_pi)                # 3.1414926535

# c:/python_data 안에 module1.py를 저장해 놓았다.
# c:/python_data/test_module/module1.py로 다시 저장하자.

import test_module.module1

print(test_module.module1.my_pi)    # 3.1414926535

import test_module.module1 as my_module

print(my_module.my_pi)              # 3.1414926535j
