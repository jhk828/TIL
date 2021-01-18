### 문제 2.
### 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다.
### 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

### 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
### 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까? => 4613732

tmp1 = 1
tmp2 = 2
newTmp = 0
total = 2
idx = 3
while newTmp < 4000000:
    newTmp = tmp1 + tmp2
    if newTmp % 2 == 0: # 짝수라면
        total += newTmp
    tmp1 = tmp2
    tmp2 = newTmp
    idx += 1

print("문제 2 - 답: {}".format(total))
print("idx =  {}".format(idx))
print("total =  {}".format(total))