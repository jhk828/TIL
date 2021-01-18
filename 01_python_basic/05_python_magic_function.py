### Magic Function, First Class, Closure

## Magic function
# 1. method의 이름 앞뒤에 더블 언더 스코어 (__)가 붙어있는 method를 지칭
#  - 대표적인 magic function  => __init__ (생성자)
# 2. class안에 정의되어 있는 특수한 형태의 method
# 3. 특수한 상황에서 그에 맞는 magic funcion이 callback/ 호출된다.

class Student(object):

    def __init__(self, name, dept):     # 생성자, constructor, initializer
        self.name = name
        self.dept = dept
        print("{}학과 {} 학생이 생성되었습니다.".format(self.dept, self.name))

    def __del__(self):
        print("소멸자가 호출되었습니다!")


stu1 = Student("홍길동", "심리")     # 심리학과 홍길동 학생이 생성되었습니다.
                                   # 소멸자가 호출되었습니다!

del stu1                           # 객체를 메모리에서 삭제. __del__ 호출된다.

#################################################################

a = 100
print(type(a))                  # class 'int'가 존재한다.

class MyInt(int):
    pass

my_num = MyInt(100)
print(my_num + 200)             # 300
print(my_num.__add__(200))      # 300

#################################################################

class Student(object):

    def __init__(self, name, dept):     # 생성자, constructor, initializer
        self.name = name
        self.dept = dept
        print("{}학과 {} 학생이 생성되었습니다.".format(self.dept, self.name))

    def __repr__(self):
        return self.name


stu1 = Student("홍길동", "심리")     # 심리학과 홍길동 학생이 생성되었습니다.

print(stu1)                         # <__main__.Student object at 0x000001A2ED42E248> => 홍길동
                                    # instance의 class 정보와 저장되어 있는 메모리 주소가 출력. stu1는 메모리값을 가르킨다.

#################################################################

class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __lt__(self, other):   # car_4=>self, car_5=>other
        if self.price < other.price:
            return "{} 가격이 더 낮아요!!".format(self.model)
        else:
            return "{} 가격이 더 높아요!!".format(self.model)

car1 = Car("G70", 5000)
car2 = Car("Sonata", 3000)

print(car1.price < car2.price)      # False
print(car1 < car2)                  # __lt__ 오버라이딩
                                    # G70 가격이 더 높아요!!