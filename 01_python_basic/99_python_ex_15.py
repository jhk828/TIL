## 문제 15.
## 각 부품의 생산정보가 문자열로 제공된다.
## [부품생산정보] : A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8

## 각 부품정보는 부품명과 품질데이터로 구성된다.
## - A,B,C 3개의 부품이 있으며 품질은 1이상 10미만의 정수.
##   예) A7 : A부품, 품질 7

## 생산정보에서 품질이 7이상인 부품만을 순서대로 선택한다.
## [생산정보] A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8
## [품질이 7이상인 부품 목록] A7A8B9A8B9C7C7B9A7B8C9A8

## 품질이 7이상인 부품들을 조립해 완성품을 만든다.
## A, B, C 세 부품이 순서대로 있을 때만 부품을 조립한다.
## A7A8B9A8B9C7C7B9A7B8C9A8 => A8B9C7, A7B8C9 2개 조립
## 조립한 부품의 목록과 전체 조립한 개수를 출력

my_str = "A7B5C4A1A8B9B3A5A8B9B1C7C1A1B3C7B9B3A7B8A1C9A8"

cnt = 0
my_lst = list()
tmp_str = ""
answer = []

for i in range(0, len(my_str), 2):
    if my_str[i] == 'A' or 'B' or 'C':
        if int(my_str[i+1]) >= 7:
            tmp_str += my_str[i:i+2]

# print(tmp_str)  # A7A8B9A8B9C7C7B9A7B8C9A8

for j in range(0, len(tmp_str)-6, 2):
    if tmp_str[j] == 'A' and tmp_str[j+2] == 'B' and tmp_str[j+4] == 'C':
        cnt += 1
        answer.append(tmp_str[j:j+6])

print("조립한 부품 목록 : {}". format(answer))
print("조립한 개수 : {}".format(cnt))

# 조립한 부품 목록 : ['A8B9C7', 'A7B8C9']
# 조립한 개수 : 2


