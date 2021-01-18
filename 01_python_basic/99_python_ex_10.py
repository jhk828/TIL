## 문제 10.
## 세 자연수 a, b, c 가 피타고라스 정리 a**2 + b**2 = c**2 를 만족하면
## 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
## 예를 들면 3**2 + 4**2 = 9 + 16 = 25 = 5**2이므로
## 3, 4, 5는 피타고라스 수입니다.

## a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다.
## 이 때, a × b × c 는 얼마입니까?      # 31875000

breaker = False
for i in range(1, 1000):
    for j in range(1, 1000):
        if breaker == True:
            break

        if (1000 - (i + j)) > 0:
            z = 1000 - (i + j)
            my_list = []
            my_list = sorted([i, j, z])
            if pow(my_list[2], 2) == pow(my_list[0], 2) + pow(my_list[1], 2):
                # print(my_list)
                breaker = True
                break
        else:
            pass

print(my_list)      # [200, 375, 425]

print(my_list[0]*my_list[1]*my_list[2])     # 31875000
