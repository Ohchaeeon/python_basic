# 클래스 상속 예제 문제
# 클래스 아이폰 1 : calling 기능만
# 클래스 아이폰 2 : calling + send msg 기능 
# 클래스 아이폰 3 : calling + send msg + internet 기능


class Iphone_1 :
    def calling(self):
        print("calling")

class Iphone_2(Iphone_1) :
    def send_msg(self):    # iphone1 을 상속받아 calling 의 기능이 들어가도록 함
        print("send msg")

class Iphone_3(Iphone_2) :
    def internet(self):         # iphone 3 에 calling 의 기능이 있는 iphone2 를 상속받아 세가지 기능이 다 들어가도록함
        print("internet")

iphone = Iphone_3()
print(iphone.calling(), iphone.send_msg(), iphone.internet())


# 클래스 예제 문제
# 스타크래프트의 마린을 클래스로 설계
# 체력 : 40 / 공격력 : 5 / 
# 마린 클래스로 마린 객체를 두개 생성,마린 1이 마린 2를 공격하도록 설계
# attack(self,unit)

class Marine:
    def __init__(self,health=40,attack_pow=5):
        self.health = health
        self.attack_pow = attack_pow     # 체력과 공격력을 각자 생성자로 미리 지정

    def attack(self,unit):
        unit.health -= self.attack_pow   # marine 2의 체력에서 marine 1의 공격력만큼 뺌
        if unit.health <= 0:            # marine 2 의 체력이 0보다 작으면 0인것, 사망으로 출력
            unit.health = 0
            print("사망")

Marine_1 = Marine()
Marine_2 = Marine()

print(Marine_1.attack(Marine_2))
print(Marine_1.health , Marine_2.health)


# 상속 : 클래스의 기능을 가져다가 그를 수정하거나 추가할때 사용하는 방법

class Calculator :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self) :
        return self.num1 + self.num2         # 객체명.num1 + 객체명.num2 와 같음


# 상속을 통해, plus 함수와 minus 함수를 한번에 쓸수 있는 객체를 만들수있음
# 즉, calculaotr 에 minus 함수를 추가하는것과 같음        

class Calculator2(Calculator) :
    def minus(self):
        return self.num1 - self.num2

# calculator 2 와 calculator 3은 같은 기능을 함 

class Calculator3 :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self) :
        return self.num1 + self.num2         

    def minus(self):
        return self.num1 - self.num2

# 메소드 오버라이딩 : 원래 클래스에 있는 같은명의 함수를 수정하고 싶을때 덮어쓰는 것

# calculator 4 라는 새로운 클래스는, calculator 2 안의 함수들을 그대로 상속받고, 거기서 plus 함수만 수정 시킴
class Calculator4(Calculator2) :
    def plus(self):
        return self.num1 **2  + self.num2 ** 2 # 그냥 덧셈이던 plus 함수를 각 숫자를 제곱해서 더하도록 함수의 기능을 바꿈


# 멀티 상속 예제 

class Iphone_1 :
    def calling(self):
        print("calling")

class Iphone_2(Iphone_1) :
    def send_msg(self):    # iphone1 을 상속받아 calling 의 기능이 들어가도록 함
        print("send msg")

class Iphone_3(Iphone_2) :
    def internet(self):         # iphone 3 에 calling 의 기능이 있는 iphone2 를 상속받아 세가지 기능이 다 들어가도록함
        print("internet")

class Galaxy :
    def show_img(self):
        print("show_img")

class LG(Iphone_3,Galaxy):
    def camera(self):
        print("camera")        


New_phone = LG()   # show_img + Iphone3 의 세가지 기능, Galaxy 의 기능까지 전부 들어있는 객체가 생성됨


# super : 부모 클래스에서 사용한 함수의 코드를 가져다가 자식 클래스의 함수에서 재사용할때 사용

# class A :
#    def plus(self):
#        code 1 

# class B(A) :
#    def minus(self):      
#        code 1        # 부모 클래스의 코드1 이 똑같이 사용될때, super를 이용해 반복을 막을수 있음  
                       # super().plus() 를 쓰면됨
#        code 2


# super(). 사용 예시
class Marine:
    def __init__(self):
        self.health = 40
        self.attack_pow = 5    # 체력과 공격력을 각자 생성자로 미리 지정

    def attack(self,unit):
        unit.health -= self.attack_pow   # marine 2의 체력에서 marine 1의 공격력만큼 뺌
        if unit.health <= 0:            # marine 2 의 체력이 0보다 작으면 0인것, 사망으로 출력
            unit.health = 0
            print("사망")


class Marine2(Marine):
        def __init__(self):
            super().__init__()   # __init__ 함수는 Marine 에서 그대로 가져오고 
            self.max_health = 40   # 이 한줄만 추가된것과 같음


# class 의 getter setter 사용
# 객체의 내부 변수에 접근할때 특정 로직을 거쳐서 접근시키는 방법

class User :
    def __init__(self, first_name):
        self.first_name = first_name

    def disp(self):
        print(self.first_name)

user1 = User()

# user1.first_name = 123 으로 지정한후, user1.disp 를 실행하면 12 이 나오는데, 
# first_name 에 세글자 이상이어야 들어갈수 있도록 설정하기 위해 getter setter 로직을 거지도록 한다.

def setter(self,first_name):
    if len(first_name) >= 3:               # 세글자 이상인지 거치는 로직
        self.first_name = first_name
    else :
        print("error") 

def getter(self):
    print("getter")                      # 거쳐져서 통과했다면, 저장된 데이터를 출력하는 과정
    return self.first_name.upper()


name = property(getter,setter)       # property : name 이라는 변수에, getter setter 로 접근할수 있도록 하는 함수


user1.name = "team"     # setter 실행

print(user1.name)      # getter 실행
print(user1.first_name)    