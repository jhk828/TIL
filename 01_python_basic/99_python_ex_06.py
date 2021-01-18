## 문제 6.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요

# 대칭인지 판단할 때 string 뒤집에서 같은지 비교해도 됨
def is_daching2(a, b):
    tmp_str = str(a*b)
    if list(tmp_str) == list(reversed(tmp_str)):
        return True
    else:
        return False


def is_daching(a, b):
    tmp_str = str(a*b)
    # for i in range(0, int(len(tmp_str)/2)):
    for i in range(0, len(tmp_str)):
        if tmp_str[i] != tmp_str[(-1)*(i+1)]:
            return False
        else:
            pass
    return True

print(''.join(list(reversed("1234"))))  # 문자열 -> 뒤집어서 리스트에 -> 다시 문자열

# print(is_daching2(123, 1))
# print(is_daching2(5555555, 1))
# print(is_daching2(1001, 1))

daching_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_daching2(i, j) == True:
            daching_list.append(i*j)
answer4 = max(daching_list)
print(answer4)              # 906609