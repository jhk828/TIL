class Student(object):
    scholarship_rate = 3.0      # class variable - 모든 instance가 공유하는 변수

    # instance가 class로 부터 생성될 때 호출되어 초기화 담당
    def __init__(self, name, dept, num, grade):     # initializer/ 생성자/ constructor
        self.name = name                            # instance variable을
        self.dept = dept                            # 선언하고 초기화
        self.num = num
        self.grade = grade

    def __repr__(self):                             # 원래는 호출 시 메모리 주소가 출력되지만
        return self.name                            # 재정의 가능

    @classmethod                                    # Class Method Decorator
    def change_scholarship(cls, rate):                  # class method
        cls.scholarship_rate = rate                 # class variable 변경
        print("장학금 기준이 변경되었어요!")

    @staticmethod
    def is_valid_scholarship(rate):
        if rate < 0:
            print("장학금 기준 학점은 음수가 될 수 없습니다.")


    def is_scholarship(self):                        # instance method
        if self.grade > self.scholarship_rate:       # error(x): instance namespace에 없으면 -> class namespace 가서 찾음
                                                     # instance namespcae에 변수 추가 된 이후에는 instance variable과 비교
        # if self.grade > Student.scholarship_rate:
            return True
        else:
            return False


student = Student("홍길동", "심리학과", "20203311", 4.0)
print(student)
print(student.__repr__())         # <__main__.Student object at 0x00000165AF5D1E88> - 재정의 아닐 시
print(student.is_scholarship())   # True

#####################################################################

## namespace cf) scope
# 객체들을 나누어서 관리하는 공간
# 1. instance namespace
# 2. class namespace
# 3. superclass namespace
# instance namespace < class namespace < superclass namespace

## Python은 동적으로 속성이나 method를 추가할 수 있다.
student.depts = "컴퓨터"                # instance 생성 후에도 새로 추가 가능
print(student.depts)                # 컴퓨터

student.scholarship_rate = 4.5      # class variable을 변경하는 것이 아니라/ instance namespace에 새로 추가
print(Student.scholarship_rate)     # 3.0
print(student.scholarship_rate)     # 4.5
print(student.is_scholarship())     # False

# instance method (self인자를 가지고 있는 method)는 하나의 인스턴스에 한정된 데이터를
# 생성, 변경, 참조하기 위해서 사용된다.

change_rate = -3.0

# class method는 클래스를 인자로 받아서 class variable을 생성, 변경, 참조하기 위해서
# student.change_scholarship(3.7)
Student.change_scholarship(change_rate)     # class method 사용
                                            # 장학금 기준이 변경되었어요!

### static method
Student.is_valid_scholarship(change_rate )  # static method 사용
                                            # 장학금 기준 학점은 음수가 될 수 없습니다.


## Information Hiding (정보은닉)
# instance가 가지는 속성은 매우 매우 중요한 데이터이기 때문에
# 외부에서 직접적으로 access하는 것은 좋지 않다.

# 외부에서 직접적으로 access하는 것을 막는 방법은? 프로그램 언어마다 다르다.
# Java => access modifier(접근제어자)
#         public vs private

# Python => __변수명 -> private

# private로 처리된 속성이 있으면 외부에서 직접적인 access 불가 => method로 처리
# private 속성 값 알아내는 method => getter
# private 속성 값을 설정해주는 method => setter

class Student(object):
    scholarship_rate = 3.0  # class variable

    def __init__(self, name, dept, num, grade):  # initializer
        self.name = name  # instance variable
        self.__dept = dept  # private variable
        self.num = num
        self.grade = grade

    ## getter method
    def get_dept(self):
        return self.__dept

    ## setter method
    def set_dept(self, dept):
        self.__dept = dept

    # private method
    def __print_date(self):
        return self.name


student = Student("홍길동", "심리학과", "20203311", 4.0)
# print(student.__dept)       # private 처리 - error
# 'Student' object has no attribute '__dept'

# student.__dept = "컴퓨터"    # error
print(student.get_dept())  # 심리학과
student.set_dept("컴퓨터")
print(student.get_dept())  # 컴퓨터

### 여기까지가 단일 class의 이론 내용