## 문제 13.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로 왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어 왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)

number = input()
# number = 123456

while len(str(number)) != 1:
    print("number = {}".format(number))
    mid = int(float(len(str(number))/2))    # 5=>2, 4=>2
    print("mid = {}".format(mid))
    if len(str(number)) % 2 == 0:
        tmp_l = int(str(number)[0:mid])
        tmp_r = int(str(number)[mid:])

    else:  # 홀수
        tmp_l = int(str(number)[0:mid])
        tmp_r = int(str(number)[mid+1:])

    number = max(tmp_l, tmp_r)
    print("new number = {}".format(number))

print(number)
