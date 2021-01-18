## 문제 3.
## 알파벳 대소문자로 된 문자열이 주어지면,
## 이 문자열에서 가장 많이 사용된 알파벳이
## 무엇인지 출력하는 프로그램을 작성하시오.
## 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
## 알파벳 순으로 제일 앞에 있는
## 문자를 출력하세요.

## 문자열) "This is a sample Program mississippi river" => i
## 문자열) "abcdabcdababccddcd"    => c

# my_str = "This is a sample Program mississippi river"
my_str = "abcdabcdababccddcd"

new_str = (my_str.lower()).replace(" ", "") # 대소문자 구분x, 중간 공백 제거
print(new_str)

count = {"a" : 0}

for i in range(0, len(new_str)):
    if new_str[i] in count.keys():
        count[new_str[i]] += 1
    else:
        count[new_str[i]] = 1   # 해당 알파벳이 없으면 dict에 추가

maxList = []

key_list = list(count.keys())
val_list = list(count.values())
myMax = max(count.values())   # 7

for z in range(0, len(val_list)):
    if val_list[z] == myMax:
        maxList.append(key_list[z])

# maxList.sort()
print(min(maxList))     # 가장 작은 값이 알파벳 상 앞에 있는 값

print("답: " + min(maxList))