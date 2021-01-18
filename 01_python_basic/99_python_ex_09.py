## 문제 9.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.
# 함수 써서 풀면 엄청 오래 걸림

def is_prime(number):
    if number != 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else :
        return False    # 1은 소수가 아님

    return True

# prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43]
prime_list = [2]

i = 1
# while len(prime_list) != 20:
while len(prime_list) != 10001:
    if is_prime(prime_list[-1]+i) == False:
        i += 1      # 소수가 아니라면 1 증가시킨다
    else:
        prime_list.append(prime_list[-1]+i)
        i = 1

print(prime_list)
print("{}개의 소수 ".format(len(prime_list)))
print("답은 {}".format(prime_list[-1]))

# 10001개의 소수
# 답은 104743