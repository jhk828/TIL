## 문제 9.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.

# 함수 써서 풀면 엄청 오래 걸림

# 10001개의 소수
# 답은 104743

#### 소수 20개 구하기 다르게 구현하는 중
# 소수 20개 구하기
prime_list = [2]
num = 3

# while len(prime_list) < 20:
while len(prime_list) < 10001:
    flag = True
    for i in prime_list:
        # print(prime_list)
        if num % i == 0:  # 4는 2로 나누어 떨어져서 소수가 아님
            flag = False
            break

    if flag == True:
        prime_list.append(num)

    # print("num {}".format(num))
    num += 1

print(prime_list[-1])       # 104743

