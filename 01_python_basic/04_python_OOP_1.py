# <구조적 프로그래밍 (절차적 프로그래밍)>
# - 프로그램 작성 시 기능으로 세분화해서 각각의 기능을 모듈화(함수화)해서 구현
# - 가장 대표적인 프로그램 작성 방식
# - 19990년대 이전에 많이 사용
# - 장점 : 프로그램 구조를 이해하기 쉽고 프로그램을 빠르게 만들 수 있다.
# - 단점 : 프로그램 규모가 커지면 유지보수와 코드의 재사용이 어렵다.

# <객체지향 프로그래밍> - Object Oriented Programming (OOP)
# - 현실세계의 해결해야 할 문제를 그대로 프로그램으로 묘사(표현)
# - 프로그램을 구성하는 주체들 (개체, 객체, Object)을 파악하고, 그 객체들간의 데이터 흐름에 초점을 맞추어서 프로그램을 작성
# - 개체들을 파악해서 그 개체들간의 관계를 프로그래밍 하는 방식
# - 단점: 프로그램을 설계하고 작성하는 과정이 상대적으로 어렵다.
# - 장점: 일단 제대로 작성된 객체지향 프로그램은 유지보수와 재사용성에 상당한 이점.

# -> 객체 모델링 : 각각의 객체를 프로그램적으로 묘사
#   - 추상화(Abstraction)을 거쳐서 객체 모델링한다.
#   - 개체들의 [속성 -> 변수, 행위 -> 함수]
#     - 변수 (property, member field, field), 함수(method)
#     - method에 의해 객체의 변수값이 변하는 경우가 일반적
# - Class를 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게 된다.

# * 현실세계의 개체를 프로그래밍적 객체로 나타내기 위한 수단이 클래스

# <Class>
# 1) 객체 모델링의 수단
# 2) ADT다.

# - ex) 사람 객체 모델링
#  class 사람
#       키(변수) height -> float
#       몸무게(변수) weight -> float
#       나이(변수) age -> int
#       이름(변수) name -> str
#       걷는다(메소드)
#       말한다(메소드)
#       잔다(메소드)

# class는 Abstract data type (추상적인 데이터 타입, ADT)
# - class는 data type의 관점에서 봤을 때, 기존 data type을 이용해서 새로운 data type을 만드는 것이다.
# <-> Built-in data type

#############################################################################

# 학생의 이름, 학과, 학번, 평균평점을 저장하는 방법

stu_name = "홍길동"
stu_dept = "심리학과"
stu_num = "20201134"  # 연산 의도 -> 숫자, 데이터 처리 -> 문자열로 나타내는게 편하다..
stu_grade = 3.5

# 만약 3명의 학생이 있으면 어떻게 하나요?

# 방법1> 일일히 만들기

stu1_name = "홍길동"
stu1_dept = "심리학과"
stu1_num = "20201134"
stu1_grade = 3.5

stu2_name = "김길동"
stu2_dept = "컴퓨터"
stu2_num = "20201134"
stu2_grade = 2.0

stu3_name = "심사임당"
stu3_dept = "경영학과"
stu3_num = "20201136"
stu3_grade = 4.0

# => 코드가 너무 불필요하게 반복적이고 확장성이 없다.


# 방법2> 리스트 사용

stu_name = ["홍길동", "김길동", "심사임당"]
stu_dept = ["심리학과", "컴퓨터", "경영학과"]
stu_num = ["20201134", "20201135", "20201136"]
stu_grade = [3.5, 2.0, 4.0]

# => Indexing을 이용해 처리하는게 쉬운 작업은 아니고, 모든 의미가 다 내포되있는게 아닌 문제 발생



# 어떻게 하면 이런 내용을 class를 이용해서 객체지향적으로 표현할 수 있을까?
# 학생이라는 개념을 프로그램적으로 모델링 해 보아요

### 클래스와 instance
# 클래스를 기반으로, 내용을 메모리에 저장시키기 위해 instance로 메모리 공간을 만든다.
# 클래스는 하나, 클래스로부터 파생된 공간 (instance)들은 여러개
# instance 하나가 한 사람의 데이터를 뜻함 -> 각각 다른 리스트에 정보를 저장시키는 것 보다 한 인스턴스 안에 모아서 저장하는 것이 관리도 효율적
# -> 따라서 인스턴스 생성에 대한 정보 (인스턴스가 어떤 정보를 저장해야 하는지)가 클래스에 포함되어 있어야 한다.
# ->       인스턴스에 저장할 정보를 받아와야 한다 (= 초기화 필요)

###
# self -> 현재 사용하는 객체에 대한 주소값/reference
# . -> dot operator :
# instance value : self.dept의 dept


# 방법3> 클래스 이용

## class variable - class 자체가 가진 변수
## instance value - 각각의 instance가 개별적으로 가짐

class Student(object):

    scholarship_rate = 3.0      # class variable - 모든 instance가 공유함

    def __init__(self, name, dept, num, grade):   # initializer : instance가 만들어지는 순간 자동으로 호출 -> 초기화 역할
                                                  # - constructor(생성자)와 비슷
        self.name = name  # self가 가지고 있는 name 변수 / self안에 name 공간 생성, parameter로 받아온 name 값 저장
        self.dept = dept  # self.dept의 dept는 -> instance value
        self.num = num
        self.grade = grade

    def is_scholarship(self):
        if self.grade > Student.scholarship_rate:       # class variable
            return True
        else:
            return False

    def __repr__(self):     # represent
        return self.name    # 현재 이 객체가 가지고 있는 name을 돌려주도록 재정의

    def change_dept(self, tmp_dept):
        # tmp_dept가 정상적인 학과인지 check하는 코드
        self.dept = tmp_dept

students = []
students.append(Student("홍길동", "심리학과", "20201134", 3.5))
students.append(Student("김길동", "컴퓨터", "20201135", 2.0))
students.append(Student("심사임당", "경영학과", "20201136", 4.0))


student = Student("홍길동", "심리학과", "20201134", 3.5)
print(student)          # <__main__.Student object at 0x00000196079F44C8>
                        # main 모듈의 Student의 객체이며, 메모리 주소는 ~이다.
                        # repr 함수 재정의 후 홍길동으로 출력됨.

print(student.is_scholarship())     # True

print(student.dept)                 # 심리학과

### <information hiding (정보은닉)>
# student.dept = "경영학과"          # direct access는 좋지 않다. -> method를 통해 접근하도록 한다.
student.change_dept("임상병리학과")   # information hiding (정보은닉)
print(student.dept)                 # 변수값 변경되어 출력됨


#######################################################

## Python은 객체 지향 언어다.
## Python의 모든 것은 다 객체 (instance)다.

a = 10
print(type(a))       # <class 'int'> : int class의 instance다.

my_list = [10]
print(type(my_list))  # <class 'list'>
# my_list.append(xx)    # instance의 method

# class list(object):
#       ,,,
#       ,,,
#       ,,,

# 숫자도 객체(instance)고, 리스트도 객체(instance)고, str도 객체(instance)고, 함수도 객체(instance)다.
# 객체(instance)가 있다는 건 => class가 존재한다는 것
# 객체(instance) => 변수, method
# instance란 속성과 같은 여러가지 데이터 + 메소드를 가지고 있는 데이터 구조를 지칭한다.


#######################################################

### dir()
# - 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려주는 python 내장 함수

student = Student("홍길동", "심리학과", "20201134", 3.5)
print(dir(student))

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'change_dept', 'dept', 'grade', 'name', 'num']

'''
## 앞뒤로 __ 붙은 메소드 => magic function

### 한가지 더 생각해보아요
student.depts = "철학과"      # JAVA, C++은 error 처리
print(student.depts)         # python은 그냥 추가해줌

## python 함수도 객체다!!
def my_func(a,b):
    return a+b

print(dir(my_func))

my_func.myName = "홍길동"

print(dir(my_func))     # 끝에 myName 추가됨 => 함수조차 객체이기 때문