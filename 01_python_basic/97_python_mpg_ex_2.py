import operator

cty_dict = dict() #  문제2
hwy_dict = dict()  #  문제3
audi_list = list()  # 문제4

class Car(object):

    def __init__(self, manufacturer, model, displ, year, cyl,
                 trans, drv, cty, hwy, fl, car_class):  # 11개 인자
        self.manufacturer = manufacturer
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.car_class = car_class
        self.avg_fuel = round((cty + hwy) / 2, 2)

        if manufacturer in ["audi", "toyota"]:     # 문제 2
            if manufacturer in cty_dict.keys():
                cty_dict[manufacturer][0] += 1
                cty_dict[manufacturer][1] += hwy
            else:
                cty_dict[manufacturer] = [0, 0]
                cty_dict[manufacturer][0] += 1
                cty_dict[manufacturer][1] += hwy
            if manufacturer == "audi":
                audi_list.append(self)


        elif manufacturer in ["chevrolet", "ford", "honda"]:  # 문제 3
            if manufacturer in hwy_dict.keys():
                hwy_dict[manufacturer][0] += 1
                hwy_dict[manufacturer][1] += hwy
            else:
                hwy_dict[manufacturer] = [0, 0]
                hwy_dict[manufacturer][0] += 1
                hwy_dict[manufacturer][1] += hwy

    def __repr__(self):
        return "{} {} {} {} {} {} {} {} {} {}".format(self.manufacturer,
                                                      self.model, self.displ, self.year,
                                                      self.cyl, self.trans, self.drv,
                                                      self.cty, self.hwy, self.fl, self.car_class)


f1 = open("C:/python_data/mpg.txt", "r")

car_list = list()

idx = 1
while True:
    line = f1.readline()
    if not line:
        break

    if idx == 1:
        idx += 1
        pass
    else:
        my_car = line.split(',')

        car_list.append(Car(my_car[0], my_car[1], float(my_car[2]), my_car[3], my_car[4], my_car[5], my_car[6],
                            float(my_car[7]), float(my_car[8]), my_car[9], my_car[10][0:-1]))
    # print(my_car)

f1.close()

displ_4 = [0, 0]     #  문제1
displ_5 = [0, 0]

for tmp in car_list:
    # 문제1
    if tmp.displ <= 4:
        displ_4[0] += 1
        displ_4[1] += tmp.hwy
    elif tmp.displ > 5:
        displ_5[0] += 1
        displ_5[1] += tmp.hwy


# 문제 1
print("\n-------문제1------------------------------")
if displ_4[1]/displ_4[0] > displ_5[1]/displ_5[0]:
    print("배기량 4 이하의 고속도로 연비가 더 높습니다.")
else:
    print("배기량 5 이상인 자동차의 고속도로 연비가 더 높습니다.")


# 문제 2
print("\n-------문제2------------------------------")

if cty_dict["audi"][1]/cty_dict["audi"][0] > cty_dict["toyota"][1]/cty_dict["toyota"][0]:
    print("audi의 도시 연비가 더 높습니다.")
else:
    print("toyota의 도시 연비가 더 높습니다.")



# 문제 3
print("\n-------문제3------------------------------")
print("chevrolet의 평균 고속도로 연비는 {}입니다.".
      format(round(hwy_dict["chevrolet"][1]/hwy_dict["chevrolet"][0], 2)))
print("ford의 평균 고속도로 연비는 {}입니다.".
      format(round(hwy_dict["ford"][1]/hwy_dict["ford"][0], 2)))
print("honda의 평균 고속도로 연비는 {}입니다.".
      format(round(hwy_dict["honda"][1]/hwy_dict["honda"][0], 2)))


## 문제4
audi_list = sorted(audi_list, key=lambda car: car.hwy, reverse=True)
print("\n-------문제4------------------------------")
idx = 0
for tmp_a in audi_list:
    if idx < 5:
        print(tmp_a)
        idx += 1


## 문제 5
print("\n-------문제5------------------------------")
suv_dict = dict()   # 문제5
for tmp in car_list:
    if tmp.car_class == "suv":
        if tmp.manufacturer in suv_dict.keys():
            suv_dict[tmp.manufacturer][0] += 1
            suv_dict[tmp.manufacturer][1] += tmp.avg_fuel
        else:
            suv_dict[tmp.manufacturer] = [1, 0, 0]
            suv_dict[tmp.manufacturer][1] += tmp.avg_fuel

for tmp in suv_dict:
    suv_dict[tmp][2] += round(suv_dict[tmp][1]/suv_dict[tmp][0], 2)

suv_dict = sorted(suv_dict, key=lambda car: suv_dict[car][2], reverse=True)

print(suv_dict)

## 문제6
class_dict = dict()
for tmp in car_list:
    if tmp.car_class in class_dict.keys():
        class_dict[tmp.car_class][0] += 1
        class_dict[tmp.car_class][1] += tmp.cty
    else:
        class_dict[tmp.car_class] = [0, tmp.cty]

for car in class_dict:
    avg = round(class_dict[car][1]/class_dict[car][0], 1)
    class_dict[car].append(avg)

class_dict = sorted(class_dict, key=lambda car:class_dict[car][2], reverse=True)

print("\n-------문제6------------------------------")
print(class_dict)

## 문제 7 - hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력
hwy_dict = dict()
for tmp in car_list:
    if tmp.manufacturer in hwy_dict.keys():
        hwy_dict[tmp.manufacturer][0] += 1
        hwy_dict[tmp.manufacturer][1] += tmp.hwy
    else:
        hwy_dict[tmp.manufacturer] = [0, tmp.hwy]

print("\n-------문제7------------------------------")
for car in hwy_dict:
    avg = round(hwy_dict[car][1]/hwy_dict[car][0], 1)
    hwy_dict[car].append(avg)

hwy_dict = sorted(hwy_dict, key=lambda car: hwy_dict[car][2], reverse=True)
for idx, tmp in enumerate(hwy_dict):
    if idx < 3:
        print(hwy_dict[idx])


## 문제 8 - 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력
compact_dict = dict()

for tmp in car_list:
    if tmp.car_class == "compact":
        if tmp.manufacturer in compact_dict.keys():
            if tmp.model in compact_dict[tmp.manufacturer]:
                pass
            else:
                compact_dict[tmp.manufacturer].append(tmp.model)
        else:
            compact_dict[tmp.manufacturer] = [tmp.model]

tuple_lst = list()

print("\n-------문제8------------------------------")
# print(compact_dict)     # {'audi': ['a4', 'a4 quattro'], 'nissan': ['altima'], 'subaru': ['impreza awd'],
for k in compact_dict:
    print(k)
    tuple_lst.append((k, len(compact_dict[k])))

tuple_lst = sorted(tuple_lst, key=lambda v: v[1], reverse=True)

for tmp in tuple_lst:
    print("회사 : {} 차종 수 : {}개".format(tmp[0], tmp[1]))