## 문제 14.
## 2**15 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

## 2**1000의 각 자리수를 모두 더하면 얼마입니까?

# num = 123
# tmp_lst = list(str(123)) # ['1', '2', '3']
# tmp_lst2 = [int(i) for i in tmp_lst]
# print(tmp_lst2) # [1, 2, 3]

num = pow(2, 1000)
tmp_lst = list(str(num))
tmp_lst2 = [int(i) for i in tmp_lst]
print(tmp_lst2)
answer = sum(tmp_lst2)
print("answer = {}".format(answer))     # 1366