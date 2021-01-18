## Python의 입출력

# 입력 받고 싶어요!
# console 입력을 받으려면 input()을 이용하면 되요

my_input = input("입력값을 넣으세요!! : ")
print(type(my_input), end=" - ")  # <class 'str'>, 줄바꿈 하지 않고 - 출력
print(my_input)

# 기본적으로 print() 함수는 한줄을 출력한 후 line feed (줄바꿈)를 수행
# 줄바꿈 대신 다른 문자를 출력하려면 end 속성을 이용


####################################################################################


### Control Statement (제어문)

# 1. if문
# python의 조건문 (if)은 두 가지 방식으로 사용이 가능

## 전통적인 if~elif~else 구문
a = 15

if a % 3 == 0:
    pass  # 빈칸으로 두면 에러 발생
elif a % 5 == 0:
    print("5의 배수입니다.")
else:
    print("3의 배수도 5의 배수도 아닙니다.")

## in을 이용한 구문이 있어요
my_list = ["서울", "인천", "부산"]

if "수원" in my_list:
    pass
else:
    print("수원은 지역 안에 없어요!")

########################################################################################

# 2. for문 -> 반복문
# for문은 두가지 형태로 사용을 해요
# for ~ in range() => 반복횟수를 지정할 경우
# for ~ in list, tuple, dict, .. => 가지고 있는 데이터만큼 반복할 경우

## 1부터 100까지의 합을 구해보아요!
my_sum = 0

for tmp in range(1, 101, 1):
    my_sum += tmp

# print("누적값은 : {}".format(my_sum))   # 누적값은 : 5050


## 집합 자료형을 이용해서 for문을 수행
my_list = ["서울", "인천", "부산"]

for tmp in my_list:
    print(tmp)

## tuple
total = 0
my_data = [(1, 2), (3, 4), (5, 6)]

for (tmp1, tmp2) in my_data:
    total += (tmp1 + tmp2)

############################################################

# python은 특이하게 list comprehension이라는게 있어요!
# 하나의 자료형으로 다른 list를 쉽게 생성하는 방법 중 하나

myList = [1, 2, 3, 4, 5]

goal = []
for tmp in myList:
    goal.append(tmp * 2)

print(goal)  # [2, 4, 6, 8, 10]

#########################################################

myList = [1, 2, 3, 4, 5]
goal = [tmp * 2 for tmp in myList]
print(goal)  # [2, 4, 6, 8, 10]

## 짝수만 뽑아내보아요!!
goal = [tmp for tmp in myList if tmp % 2 == 0]
print(goal)  # [2, 4]

##############################################################

# 3. while

idx = 0
while idx < 10:
    print("현재 idx의 값은 : {}".format(idx))
    idx += 1