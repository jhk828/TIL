## 문제 5.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.  => 6857

my_num = 600851475143
# my_num = 106
prime_list = []
result = []     # (소수, 갯수)


def is_prime(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True


tmp = my_num
for j in range(2, my_num):
    if is_prime(j):
        prime_list.append(j)
        count = 0
        while tmp % j == 0:
            count += 1
            tmp = int(tmp/j)
        if count != 0:
            result.append((j, count))
        if tmp == 1:
            break

# print(prime_list)
print(result)

# 소인수 중에서 가장 큰 수
print("소인수 중에서 가장 큰 수는 {}입니다.".format(result[-1][0]))