# student_score.txt
# 각 사람에 대한 데이터를 읽어서
# 성적순으로 출력하기
# 출력 양식
# 1등 아이유 95.6
# 2등 홍길동 89.3 ,,,

avg_list = []

class Student(object):
    def __init__(self, line):
        self.line = line
        self.my_list = line.split(',')
        self.name = self.my_list[0]
        self.avg = (int(self.my_list[1]) + int(self.my_list[2]) + int(self.my_list[3]))/3
        self.push_avgs()

    def push_avgs(self):
         avg_list.append([self.avg, self.name])

stu_list = list()

## txt 읽어오기
file = open("C:/python_data/student_score.txt", "r") # 읽기 모드로 열기
while True:
    line = file.readline()      # 홍길동,18,7,19 + 한줄띄라는 것 까지 같이 읽음
    if not line:                # empty string => False
        break
    stu_list.append(Student(line))
    # print(line, end="")
file.close()
# print(avg_list)

avg_list = sorted(avg_list, reverse=True)

for rank, stu in enumerate(avg_list):
    print(str((rank+1)) + "등", end = " ")
    print(stu[1], end = " ")
    print(stu[0])