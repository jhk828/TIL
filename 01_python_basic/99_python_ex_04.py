## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개, 4등 몇개, 꽝 몇개로 출력

## 쉬운버전을 해결했다면
## 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

import random

cash = 0

# while True:
# 로또 번호 입력
input_list = []
print("로또 번호 구매 시작")
for i in range(5):
    print("{}번째 구매입니다.: ".format(i + 1), end='')
    tmp_list = []
    for j in range(7):
        # tmp_list += [int(input())]
        tmp_list += [random.randint(1, 100)]
    print(tmp_list)
    input_list.append(tmp_list)
# print("입력한 번호는 {} 입니다.".format(input_list))

# 임의의 숫자 6개 생성

num_list = [random.randint(1, 100) for i in range(7)]
print("이번 주 로또 번호는 {} 입니다.".format(num_list))

lotto_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, "꽝": 0}

cnt_for_csh = 0
flag = False  # 보너스 숫자
for lst in input_list:
    # print(i)      # [34, 24, 80, 28, 19, 25]
    cnt = 0
    for j in lst:
        # 보너스 숫자 먼저 확인
        if lst[-1] == num_list[-1]:
            flag = True
            cnt += 1  # 보너스 숫자 일치

        for z in range(0, 6):
            if j == num_list[z]:
                # print("j= {}, num_list[z]={}, flag= {}".format(j, num_list[z], flag))
                cnt += 1

    # print("cnt= {}, flag= {} ".format(cnt, flag))

    if cnt == 7:
        lotto_dict[1] += 1  # 보너스 숫자와 모든 숫자가 일치면 1등
    elif cnt == 6:
        if flag:  # 보너스 숫자 포함 6개는 2등:
            lotto_dict[2] += 1
        else:
            lotto_dict[1] += 1  # 미포함 6개는 1등
    elif cnt == 5:
        if flag:  # 보너스 숫자 포함 5개는 3등
            lotto_dict[3] += 1
        else:  # 미포함 5개는 2등
            lotto_dict[2] += 1
    elif cnt == 4:
        if flag:  # 보너스 숫자 포함 4개는 4등:
            lotto_dict[4] += 1
        else:
            lotto_dict[3] += 1  # 미포함 4개는 3등
    elif cnt == 3:
        if flag:  # 보너스 숫자 포함 3개는 5등:
            lotto_dict[5] += 1
        else:
            lotto_dict[4] += 1  # 미포함 3개는 4등
    else:
        lotto_dict["꽝"] += 1

print(lotto_dict)
# tmp = [34, 24, 80, 28, 19, 25]
# print(tmp.find(50))
