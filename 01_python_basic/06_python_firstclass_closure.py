## first class
# first-class citizen (1급 시민)
# 프로그램의 구성 요소(개체-값, 객체, 함수)가 다음의 조건을 만족하면 first-class citizen

# 1. 구성요소가 변수나 데이터 구조의 속성으로 저장될 수 있다.
# 2. 함수의 인자로 전달될 수 있다.
# 3. 함수의 결과로 리턴될 수 있다.

# 즉, 우리가 사용하는 일반 숫자 타입의 데이터 => 변수에 저장도 가능하고
#   함수의 인자로 넘겨줄 수 있고 함수의 결과로 리턴될 수 있다.
#   - 일반 숫자는 일급 시민이다.

# 우리가 사용하는 객체 (class로부터 파생된 instance)
# python에서 사용되는 객체는 1급 시민의 조건을 만족해요 => 1급 객체

# python의 함수는 어떻게 될까요?
# 만약 1급 시민의 조건을 만족한다면 일급 함수 (first class function)
# Python은 1급 시민 지원, JAVA는 미지원
# => 함수를 runtime(실시간)으로 생성할 수 있다.

# 1급 시민 조건들
# 1. 함수를 변수에 저장할 수 있다.

def my_add(x, y):
    return x + y

print(my_add)       # <function my_add at 0x00000195179D45E8>

f = my_add          # 변수 안에 저장된 메모리주소를 변수 f에 저장
print(f)            # <function my_add at 0x00000263A7C945E8> => f도 같은 함수 pointing
print(f(100, 200))  # 300

# 2. 함수를 다른 함수의 인자로 전달할 수 있다.

def my_add(x, y):
    return x + y

def my_sub(x, y):
    return x - y


def my_operation(func, arg_list):
    result = []

    for (tmp1, tmp2) in arg_list:
        result.append(func(tmp1, tmp2))

    return result

data = [(1, 2), (3, 4), (5, 6)]

print(my_operation(my_add, data))       # [3, 7, 11]
print(my_operation(my_sub, data))       # [-1, -1, -1]

# 3. 함수를 다른 함수의 리턴값으로 사용할 수 있다. => cf) Closure

def addMaker():

    def my_add_maker():
        return 100

    return my_add_maker     # 실행 코드 자체를 리턴

print(addMaker()())         # addMaker() 리턴=> 함수코드 (의 리턴)
                            # return 100

print(addMaker())           # <function addMaker.<locals>.my_add_maker at 0x0000021BF6914708>

tmp1 = 100

def my_func():
    tmp2 = 200      # local variable - 함수 내에서 생성되어, 함수가 종료되면 생명주기 X
    return tmp2

def my_func2(x):    # 매개변수도 지역변수
    tmp2 = 300
    return x

print(tmp1)         # 100
my_func()
# print(tmp2)       # 200 X
my_func2(1000)
# print(x)          # error - parameter 도 지역변수

def addMaker(x):      # x는 지역변수로 함수가 호출되면 생성되고 함수가 종료되면 없어짐
    def my_add_maker(y):
        return x + y    # 지역변수 x가 사라지지 않고 실행됨
    return my_add_maker

add_5 = addMaker(5)
add_10 = addMaker(10)   # 함수를 동적으로 사용 가능 - runtime시 새로운 기능을 생성

print(add_5(100))      # 105
print(add_10(100))     # 110

#################################################################

## Closure
# first class function (일급함수)의 개념을 이용하여
# 스코프에 묶인 변수를 바인딩 하기 위한 기술을 의미한다.

# 클로저는 데이터를 저장한 레코드다.
# 스코프안의 변수가 소멸되어도, 클로저를 통해 그에 대한 접근을 할 수 있다.

# => 클로져의 도움을 받아 런타임시에 내가 필요한 함수를 만들어 낼 수 있다.