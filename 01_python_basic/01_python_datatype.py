# 4. Python의 데이터 타입 (data type) : 6개
#  python의 built-in data type (이미 정의되있는 데이터 타입)
# - Numeric (숫자) (int, float, complex)
# - Sequence (순서가 있음) - list, tuple, range
# - Text Sequence Type (str) : 문자열
# - Mapping : dictionary
# - Bool

##################################################################################
# 4-1. Numeric Data Type (숫자형)
# - 다른 언어는 정수와 실수로 구분, 파이썬은 구분 안하지만 처리 시에는 floating 실수형으로 처리
# int (정수)
# float (실수)
# complex (복소수)

a = 100               # 정수
b = 3.14159265358979  # 실수
c = 1 + 2j            # 복소수
d = 0o34              # int 8진수
e = 0xAB              # int 16진수

# 데이터 타입을 알고싶어요! -> type()
print(type(a))    # <class 'int'> (integer class의 instance다)
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>

# Python은 나누기 연산자가 다르다
my_result = 3 / 4
print(my_result) # 다른 언어: 0, Python: 0.75

my_result = 10 % 3  # 나머지 (modular) 연산자
my_result = 10 // 3  # 몫 연산자


##################################################################################

# 4-2. Text Sequence Type (str)
# 다른 언어는 문자와 문자열을 구분 : 문자 '' 한글자, 문자열 ""
# Python은 문자열을 표현할 때 ('', "") 둘 다 같음

a = "Hello"
b = "K"
c = 'python'

# 문자열 연산
first = "haha"
second = "hoho"

print(first + second)   # hahahoho
print(first + str(10))  # haha10
print(first * 3)        # hahahahahaha


##################################################################################

# Indexing
my_var = "Hello"
print(my_var[0])    # H
print(my_var[-1])   # o

# Slicing
my_var = "이것은소리없는아우성!"
print(my_var[0:3])      # Hel 0<= x < 3
print(my_var[0:-1])     # 이것은소리없는아우성 - 처음부터 끝까지, 맨 마지막은 빼고
print(my_var[:3])       # 이것은 0<= x < 3
print(my_var[:])        # 처음부터 끝까지

# in, not in 연산자
myStr = "This is a sample Text"
print("sample" in myStr)        # True
print("Sample" not in myStr)    # 대소문자 구분, True

# Formatting
num_of_apple = 10
myStr = "나는 사과를 %d개 가지고 있어요!" % num_of_apple
print(myStr)    # 나는 사과를 10개 가지고 있어요!

# 문자열 formatting은 아래의 표현을 주로 사용해요!
myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요!".format(num_of_apple, 20)
            # 나는 사과를 10개, 바나나 20개 가지고 있어요!
myStr = "나는 사과를 {1}개, 바나나 {0}개 가지고 있어요!".format(num_of_apple, 20)
            # 나는 사과를 20개, 바나나 10개 가지고 있어요!
print(myStr)

# 문자열 method를 이용해서 문자열 처리를 할 수 있어요!
myStr = "cocacola"

print(len(myStr))           # 문자열 길이 : len() 함수를 이용
print(myStr.count('c'))     # 3, str의 method인 count()를 이용
print(myStr.find('o'))      # 1, 위치 반환

myStr = "   my Hobby"   # 공백도 문자열에 포함됨
print(myStr.upper())    #   MY HOBBY
print(myStr.lower())    #   my hobby
print(myStr.strip())    # 앞의 공백 날림, my Hobby


##################################################################################

# 4-3. Sequence type
# list [], tuple (), dict {}
# 시퀀스 타입은 Indexing, Slicing 가능
    # 인덱싱은 해당 위치의 값 추출만 함
    # 슬라이싱의 결과값은 무조건 리스트

# 1) list : 임의의 객체(데이터)를 순서대로 저장하는 집합 자료형
# Java의 ArrayList와 유사.
# list는 literal로 표현할 때 (코드상에서 코드로 표현할 때), [] (대괄호로 표현)

my_list = []
print(type(my_list))
my_list = list()
my_list = [1, 2, 3.14, "Hello"]                     # 리스트는 다른 자료형끼리도 쓸 수 있음
my_list = [1, 2, 3.14, "Hello", [5, 6, 7], 100]     # 중첩 리스트 : 리스트의 원소로 리스트 사용 가능

# indexing과 slicing을 할 수 있어요!
print(my_list[1])       # 2
print(my_list[-2])      # [5, 6, 7] => indexing은 해당 위치 요소 추출만 함!
print(my_list[4:5])     # [[5, 6, 7]] => slicing은 결과값이 무조건 리스트!
print(my_list[4][1])    # 6 - 슬라이싱한 리스트의 인덱싱
print(my_list[4][0:3])  # [5, 6, 7] - 슬라이싱한 리스트의 슬라이싱 (리스트)
print(my_list[0:2])     # [1, 2] (슬라이싱이니까 결과값 리스트)

# list 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)    # [1, 2, 3, 4, 5, 6]
print(a * 3)    # [1, 2, 3, 1, 2, 3, 1, 2, 3]

a = [1, 2, 3]
a[0] = 5
print(a)                # [5, 2, 3]
a[0] = [7, 8, 9]
print(a)                # [[7, 8, 9], 2, 3]
print(a[0:1])           # [[7, 8, 9]]
a[0] = 5
a[0:1] = [7, 8, 9]      # 슬라이싱 해서 대체
print(a)                # [7, 8, 9, 2, 3]

a = [1, 2, 3]
a.append(4)
print(a)           # [1, 2, 3, 4]
a.append([5, 6, 7])
print(a)          # [1, 2, 3, 4, [5, 6, 7]] 리스트 통째로 넣는다

my_list = ["홍길동", "아이유", "강감찬", "신사임당", "Kim"]
result = my_list.sort()     # 리스트를 오름차순으로 정렬
print(result)               # None : sort()는 리턴값이 없음, 자기 자신을 정렬해서 바꿈
print(my_list)              # ['Kim', '강감찬', '신사임당', '아이유', '홍길동'], 오름차순 정렬 시 영어가 더 빠르다. 유니코드 순서가 영어가 앞임


##################################################################################

# 2) Sequence type - tuple
# list는 []로 표현, tuple은 ()로 표현
# tuple은 일단 만들어지면 내용 변경이 불가능!!
a = (1, 2, 3)   # tuple
# a[0] = 100    # 에러 발생

a = (1)     # tuple의 원소가 하나만 있으면 연산자 우선순위랑 구분히 안되어 애매하다
a = (3, )   # 요소가 1개만 존재하는 tuple

a = (1, 2, 3)   # 일반적인 tuple
b = 1, 2, 3     # tuple은 괄호 생략 가능!
print(a==b)     # True
print(type(b))  # <class 'tuple'>

a = (1, 2, 3)
b = (5, 6, 7)
print(a + b)    # (1, 2, 3, 5, 6, 7) => tuple이 변하지 않는 것은 자기 자신이지, 연결하는 것은 가능

# list <-> tuple 변환 가능
a = (1, 2, 3)
my_list = list(a)
print(my_list)      # [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)     # (1, 2, 3)


##################################################################################

# 3) Sequence type - range
# 주로 for문에서 사용
# 같은 데이터를 적은 양의 데이터로 표현 가능
my_range = range(10)    # 0<= x < 10, 증감치 생략, 표현만 하고 실제 값 저장은 아님
print(my_range)         # range(0, 10)
print(7 in my_range)    # True

# sequence타입은 다 인덱싱, 슬라이싱 가능
print(my_range[0])      # 0
print(my_range[1:4])    # range(1, 4)

my_range = range(1, 10, 3)  # 3씩 증가
print(my_range) # range(1, 10, 3)


##################################################################################

# 4-4. Mapping( dict ) - Java의 HashMap
# 순서가 없었는데 새로운 버전에서는 순서가 생겼다.

# Dictionary는 key와 value로 데이터를 저장하는 구조
# [] 리스트, () 튜플, { } 딕셔너리
a = {"name" : "홍길동", "age" : 40}    # JSON 표현 방식
print(type(a))          # <class 'dict'>
print(a["name"])        # 홍길동, key값으로 인덱싱하여 value값을 추출
a["address"] = "서울"    # key 값이 없으면 추가함!
print(a)                # {'name': '홍길동', 'age': 40, 'address': '서울'}
print(a.get("age"))     # 40, get method로도 접근 가능

# dict에서 많이 사용하는 대표적인 method 3개 : keys(), values(), items()
a = {'name': '홍길동', 'age': 40, 'address': '서울'}
print(a.keys())         # dict_keys(['name', 'age', 'address']),
print(type(a.keys()))   # <class 'dict_keys'>, 리스트처럼 생겼지만 리스트는 아님
print(list(a.keys()))   # ['name', 'age', 'address'], 이제 진짜 리스트

print(a.values())       # dict_values(['홍길동', 40, '서울'])
print(list(a.values())) # ['홍길동', 40, '서울']

print(a.items())        # dict_items([('name', '홍길동'), ('age', 40), ('address', '서울')]) => 튜플의 리스트


##################################################################################

# 4-5. Bool data type => Boolean (True, False)
# 사용하는 연산자 => and, or, not 연산자를 사용할 수 있어요
#                   & , |  , ~  비트 연산자

# 다음의 경우 Python은 False로 간주
# 1. 빈 문자열은 False로 간주 => "", ''
# 2. 빈 리스트는 False로 간주 => []
# 3. 빈 tuple도 False로 간주 => ()
# 4. 빈 dict도 False로 간주 => {}
# 5. 숫자 0은 False, 다른 숫자는 모두 True (= C, =! JAVA)
#   True -> 1, False -> 0
# 6. None은 False로 간주

a = 5
b = 0
print(a and b)  # 0
print(a & b)    # & : bitwise 연산
                # 0101 & 0000 => 0000 , 0
print(a | b)    # | : bitwise 연산
                # 0101 | 0000 => 0101 , 5


###############################################################################

# 4-6. Set data type
# 집합 자료형이고 중복을 허용하지 않아요
# 순서가 존재하지 않는 자료형

# {} => dict => {"key" : "value"}
# {} => set  => {1, 2, 3}

my_set = {1, 2, 3, 4, 1, 2}
print(my_set)           # {1, 2, 3, 4}

my_list = [1, 2, 3, 4, 1, 2]
my_set = set(my_list)
print(my_set)           # {1, 2, 3, 4}

my_str = "Hello"        #  Text Sequence는 list
my_set = set(my_str)
print(my_set)           # {'o', 'e', 'l', 'H'}

# set에서 사용하는 연산자
# 합집합 (union : |), 교집합 (intersection : &), 차집합 (difference : -)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 | s2)        # {1, 2, 3, 4, 5, 6} union
print(s1 & s2)        # {3, 4} intersection
print(s1 - s2)        # {1, 2} difference