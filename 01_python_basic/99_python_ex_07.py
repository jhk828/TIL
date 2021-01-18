## 문제 7.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

def is_prime(number):
    if number != 1:
        for i in range(2, number):  # 2부터 나누어보며 소수 판별
            if number % i == 0:
                return False
    else:
        return False    # 1은 소수가 아니다

    return True

answer = 1
prime_list = []

for j in range(2, 21):      # 20이하의 소수 구하기
    if is_prime(j) == True:
        prime_list.append(j)
    else:
        pass
print(prime_list)

tmp = 1

another_list = []

# 소수끼리만 곱해도 표현되지 않는 수가 있다.
# ex) 20 = 2 * 2 * 5
# => 20 이하일 때 까지 소수를 제곱해나가면서 정답에 곱한다.
for p in prime_list:
    tmp = 1
    while tmp < 20:
        tmp *= p
        # print(tmp/p)
    another_list.append(tmp/p)
    answer *= (tmp/p)

answer = int(answer)
print(another_list)
print("answer : {}".format(answer))      # 232792560
