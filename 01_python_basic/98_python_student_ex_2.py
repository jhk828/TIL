class Student(object):

    def __init__(self, name, kor, eng, math):
        self.__name__ = name
        self.__kor__ = kor
        self.__eng__ = eng
        self.__math__ = math
        self.avg = round((kor + eng + math) / 3, 1) # 반올림하여 소수점 1자리까지 나타내라

    def __repr__(self):
        return "{} {}".format(self.__name__, self.avg)

## txt 읽어오기
file = open("C:/python_data/student_score.txt", "r") # 읽기 모드로 열기
students = list()

while True:
    line = file.readline()      # 홍길동,18,7,19 + 한줄띄라는 것 까지 같이 읽음
    if not line:                # empty string => False
        break
    stu_data = line.split(",")  # ["홍길동", "18", "7", "19"]
    students.append(Student(stu_data[0],
                            int(stu_data[1]),
                            int(stu_data[2]),
                            int(stu_data[3]) ))
file.close()

# sorted(정렬할 리스트, key = lambda stu: stu.avg 객체가 가지고 있는 평균값)
# key : 무엇을 기준으로 정렬할지

result = reversed(sorted(students, key = lambda stu: stu.avg))      #  정렬 후 뒤집기

idx = 1
for tmp in result:
    print("{}등 {}".format(idx, tmp))
    idx += 1


# result = sorted(students, key = lambda stu: stu.avg, reverse = True)    # 객체의 평균을 기준으로 정렬됨
# for tmp in result:
#     print(tmp)

# for idx, tmp in enumerate(result):
#     print("{}등".format(idx+1), end = ' ')
#     print(tmp)