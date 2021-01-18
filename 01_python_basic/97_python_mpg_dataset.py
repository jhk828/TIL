#
#
# mpg data set을 이용한 문제 8개 구현
#
class Car(object):
    def __init__(self, car_data):
        car_data = car_data.split(",")
        self.manufacturer = car_data[0]
        self.model = car_data[1]
        self.displ = float(car_data[2])
        self.year = int(car_data[3])
        self.cyl = int(car_data[4])
        self.trans = car_data[5]
        self.drv = car_data[6]
        self.cty = int(car_data[7])
        self.hwy = int(car_data[8])
        self.fl = car_data[9]
        self.car_class = car_data[10]

    def __repr__(self):
        return self.manufacturer + ", " + self.model \
               + "," + self.displ + ", " + self.year \
               + self.trans + ", " + self.drv \
               + self.cty + ", " + self.hwy




file = open("C:/python_data/mpg.txt","r")
car_list = list()

line = file.readline()

while True:
    line = file.readline()
    if not line:
        break
    car_list.append(Car(line.strip()))

file.close()

# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
#    어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

displ_4_lower = []
displ_5_upper = []

for tmp in car_list:
    if tmp.displ <=4:
        displ_4_lower.append(tmp.hwy)
    elif tmp.displ >= 5:
        displ_5_upper.append(tmp.hwy)

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## List Comprehension

displ_4_lower = [tmp.hwy for tmp in car_list if tmp.displ <= 4]
displ_5_upper = [tmp.hwy for tmp in car_list if tmp.displ >= 5]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## filter 함수 이용

def filter_displ_4_lower(tmp):
        return tmp.displ <= 4

def filter_displ_5_upper(tmp):
    return tmp.displ >= 5

displ_4_lower_list = list(filter(filter_displ_4_lower,car_list))
displ_5_upper_list = list(filter(filter_displ_5_upper,car_list))

displ_4_lower = [tmp.hwy for tmp in displ_4_lower_list]
displ_5_upper = [tmp.hwy for tmp in displ_5_upper_list]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

## lambda 이용
displ_4_lower_list = list(filter(lambda tmp:tmp.displ <= 4,car_list))
displ_5_upper_list = list(filter(lambda tmp:tmp.displ >= 5,car_list))

displ_4_lower = [tmp.hwy for tmp in displ_4_lower_list]
displ_5_upper = [tmp.hwy for tmp in displ_5_upper_list]

avg_hwy_4_lower = sum(displ_4_lower) / len(displ_4_lower)
avg_hwy_5_upper = sum(displ_5_upper) / len(displ_5_upper)

print("배기량 4 이하인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_4_lower))
print("배기량 5 이상인 자동차의 고속도로 평균 연비 : {}".format(avg_hwy_5_upper))

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# # "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# # 평균적으로 더 높은지 확인하세요.
cty_audi_list = [tmp.cty for tmp in car_list if tmp.manufacturer == "audi"]
cty_toyota_list = [tmp.cty for tmp in car_list if tmp.manufacturer == "toyota"]

cty_audi = sum(cty_audi_list) / len(cty_audi_list)
cty_toyota = sum(cty_toyota_list) / len(cty_toyota_list)

print("audi의 평균 cty : {}".format(cty_audi))
print("toyota의 평균 cty : {}".format(cty_toyota))



# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# # 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# # class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

mpg_class = [tmp.car_class for tmp in car_list]
mpg_class_set = set(mpg_class)awsd

def make_car_dict(car_class):
    result = [tmp.cty for tmp in car_list if tmp.car_class == car_class]
    avg = sum(result) / len(result)
    return (car_class, avg)

my_result = []
for tmp in mpg_class_set:
    my_result.append(make_car_dict(tmp))
kk = reversed(sorted(my_result, key=lambda t : t[1]))
for i in kk:
    print("class : {}, cty평균 : {}".format(i[0],i[1]))

