# 1. 주석
# python의 주석은 1줄 주석은 => #
# 여러 줄 주석은 """ """, ''' '''
# 여러 블록 + ctrl _ / => 한꺼번에 주석 처리

# 2. Python의 keyword
import keyword
print (keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 3. 변수의 생성과 삭제
my_var = 100
print(my_var)

del my_var
# print(my_var) -> 삭제되어 에러 발생