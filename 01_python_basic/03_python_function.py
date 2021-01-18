# python의 함수

# python의 함수는 크게 2가지 분류가 있어요!
# 1. 내장함수
# 2. 사용자 정의 함수 (user define function) V

# 함수 => 특정 작업을 수행하는 일정량의 코드 모음
# 함수를 만드려면 어떻게 해야 하나요?

# 내장함수와 이름이 겹치면 재정의된 함수로 대체됨
# 관용적으로 함수 이름에 대문자 사용x, 소문자와 밑줄로
# 파이썬은 함수 인자에도 data type을 명시하지 않는다


### <사용자 정의 함수>

## 일반적인 함수의 정의와 사용


def my_sum(a, b, c):
    return a + b + c


result = my_sum(10, 20, 30)
print("함수 호출의 결과는 : {}".format(result))		# 함수 호출의 결과는 : 60



## 함수를 호출하는데 인자가 가변적일 경우에는 어떻게 하나요? => *args


def my_sum2(*args):             # 전달되는 인자를 tuple로 받아요
    tmp = 0
    for k in args:
        tmp += k
    return tmp


result = my_sum2(1, 2, 3, 4, 5, 6)
print("결과값은 : {}".format(result))   # 결과값은 : 21




## python은 함수의 결과값이 (리턴값이) 2개 이상일 수 있다는데요? => 사실 튜플임


def my_operator(a, b):
    result1 = a + b
    result2 = a * b
    return result1, result2         # 괄호를 생략한 tuple로 리턴함


result = my_operator(10, 20)
print(type(result))                  # <class 'tuple'>

# tuple을 각각 받아올 수 있다
# (tmp1, tmp2)
tmp1, tmp2 = my_operator(10, 20)
print(tmp1)     # 30
print(tmp2)     # 200




## default parameter
# python의 함수는 default parameter를 쓸 수 있어요!! => 맨 마지막 인자에만 사용 가능!!
# def my_default(a, b=10, c):   => error


def my_default(a, b, c=True):			#  가변인자 (formal parameter)
    data = a + b
    if data > 10 and c:
        return data
    else:
        return 0


result1 = my_default(10, 20, False)
result2 = my_default(10, 20)			# 실인자 (real parameter)



## python 함수의 인자는 mutable , immutable 둘 중 하나에요.

# call-by-value & call-by-reference 와 비슷
# Python에서 함수에 인자를 전달하고 함수는 전달된 인자를 받아요!

# 실인자의 데이터가 변하는 경우가 있어요  =>  mutable (list, dict)
# 실인자의 데이터가 변하지 않는 경우가 있어요!  =>  immutable (숫자, 문자열, Tuple)


def my_func(tmp_number, tmp_list):      # 리턴값이 없는 함수
    tmp_number = tmp_number + 100
    tmp_list.append(100)


data_x = 10         # Numeric
data_list = [10]    # list

my_func(data_x, data_list)

print(data_x)       # 10         변화X    =>  immutable (숫자, 문자열, Tuple)
print(data_list)    # [10, 100]  변화O    =>  mutable (list, dict)



### <내장 함수>

## id()라는 함수는 알아둘 필요가 있어요!
# id() : 객체의 고유 주소값을 return하는 함수
# 숫자인 경우 0 ~256까지는 너무나 많이 사용하는 객체(값)

my_list1 = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

print(id(my_list1))      # 1660836073992
print(id(my_list2))      # 1660836073992    => 내용이 같을 지라도 다른 주소값을 갖는다

my_num1 = 100
my_num2 = 100
print(id(my_num1))      # 140709997743472
print(id(my_num2))      # 140709997743472   => 숫자는 같은 주소값을 가질 수 있다


## 내장함수는 너무 많고, 주요한 함수는 알아둬야 하지만
## 일반적으로 코드를 작성해 나가면서 하나씩 알아가는 방법이 가장 좋아요



######################################################################

### <lambda expression>
# 함수와는 다르지만 함수의 역할을 수행하는 lambda expression (람다 표현식)
# lambda : 한 줄로 함수를 정의하는 방법
#          함수의 이름이 없어요!! (= annonymous function)
#          이름이 없는데 어떻게 사용하나요?
#          이름이 없기 때문에 - 변수에 저장, 함수의 인자로 사용,
#                             함수의 결과값 (리턴값)으로 함수를 리턴
#                             => first class


# def my_func(tmp_number, tmp_list):      # 리턴값이 없는 함수
#     tmp_number = tmp_number + 100
#     tmp_list.append(100)

my_lambda = lambda x1, x2, x3: x1 + x2 + x3

my_lambda(10, 20, 30)       # => 10 + 20 + 30

# 람다가 함수와 결정적으로 다른 점은.. 람다는 대체식이다!!