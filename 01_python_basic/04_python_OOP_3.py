# <상속>

# 객체지향을 하는 이유는 => 유지보수와 재사용성
# 재사용성을 위한 대표적인 객체지향 기법 => Inheritance (상속)

# 두개의 class를 이용하여 상속을 알아보자.
# Unit class, Marine class
# Unit class => 모든 unit이 공통으로 가지고 있는 속성과 method로 구성
#            => super class, base class로 사용
# Marine => sub class

# class object:
#       ~
#       ~
# python의 모든 class는 object class다!!
# python의 모든 class는 object class를 상속해야 한다.

class Unit(object):     # 모든 class는 object를 상속받는다.
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__    # 클래스 이름 참조
        self.damage = damage
        self.life = life

    def show_status(self):
        print("직업: {}".format(self.utype))
        print("공격력: {}".format(self.damage))
        print("생명력: {}".format(self.life))


class Marine(Unit):
    # pass
    
    def __init__(self, damage, life, range_upgrade):        # 오버라이딩 - 상속 시 재정의
        super(Marine, self).__init__(damage, life)          # Marine class의 상위 class를 찾아, 두 인자를 넘겨 init 호출
        # self.utype = self.__class__.__name__                # 클래스 이름 참조
        # self.damage = damage
        # self.life = life
        self.range_upgrade = range_upgrade

    def show_status(self):
        super(Marine, self).show_status()
        print("사거리 업그레이드 유무: {}".format(self.range_upgrade))


marine_1 = Marine("100", "100", True)
marine_1.show_status()      # 직업: Marine
                            # 공격력: 100
                            # 생명력: 100
                            # 사거리 업그레이드 유무: True


###########################################################################

# 사용할 유닛들은 Marine, Medic, Valture, Dropship 4 종류
# super class
class Unit(object):
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life

    def show_status(self):
        print("직업: {}".format(self.utype))
        print("공격력: {}".format(self.damage))
        print("생명력: {}".format(self.life))

    def attack(self):
        pass

class Marine(Unit):
    def __init__(self, damage, life, range_upgrade):  # 오버라이딩 - 상속 시 재정의
        super(Marine, self).__init__(damage, life)  # Marine class의 상위 class를 찾아, 두 인자를 넘겨 init 호출
        self.range_upgrade = range_upgrade

    # overriding
    def show_status(self):
        super(Marine, self).show_status()
        print("사거리 업그레이드 유무: {}".format(self.range_upgrade))

    # overriding
    def attack(self):
        print("마린이 총으로 공격합니다. 땅땅!!")

    def stimpack(self):
        if int(self.life) < 20:
            print("체력이 낮아서 스팀팩 수행이 불가능합니다.")
        else:
            # int(self.life) -= 10
            # int(self.damage) += 1.5
            print("마린이 스팀팩을 사용했어요!!")


class Medic(Unit):
    def __init__(self, damage, life):
        super(Medic, self).__init__(damage, life)

    # overriding
    def attack(self):
        print("메딕이 치료합니다. 힐힐!!")


class Vulture(Unit):
    def __init__(self, damage, life, amount_of_mine):
        super(Vulture, self).__init__(damage, life)
        self.amount_of_mine = amount_of_mine

    # overriding
    def attack(self):
        print("벌쳐가 공격합니다~~!")


class Dropship(Unit):
    # def __init__(self, damage, life):
    #     super(Dropship, self).__init__(damage, life)

    # overriding
    def attack(self):
        print("특정 목표 지정으로 이동합니다. 쓩~!")

    def board(self, unit_list):
        self.unit_list = unit_list
        print("유닛들을 드랍쉽에 태워요!!")

    def drop(self):
        print("모든 unit이 드랍쉽에서 내립니다.")
        return self.unit_list



# marine을 생성합니다. 3마리
marine_1 = Marine("100", "100", False)
marine_2 = Marine("100", "100", False)
marine_3 = Marine("100", "100", False)

# marine을 생성합니다. 1마리
medic = Medic("0", "100")

# vulture를 생성합니다. 2마리
vulture_1 = Vulture("200", "100", 3)
vulture_2 = Vulture("200", "100", 3)

# list를 이용해서 여러개의 객체를 저장할거에요!
troop = list()
troop.append(marine_1)
troop.append(marine_2)
troop.append(marine_3)
troop.append(medic)
troop.append(vulture_1)
troop.append(vulture_2)

# Dropship 생성
dropship = Dropship("0", "100")
dropship.board(troop)

# 공격지점으로 이동
dropship.attack()

# 공격지점에서 내리기
my_list = dropship.drop()

# 스팀팩을 쓰고 공격하기
for unit in my_list:
    if isinstance(unit, Marine):        # isinstance() 내장함수
        unit.stimpack()
    unit.attack()


