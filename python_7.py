# 클래스 : 변수와 함수를 묶어놓은 개념
# 변수와 함수가 들어있는 클래스를 선언, 클래스를 객체로 만들어 클래스 안에 선언된 변수와 함수를 사용

from python_5 import plus


class Calculator :
    num1 = 1
    num2 = 2

    def plus(self) :
        return self.num1 + self.num2         # 객체명.num1 + 객체명.num2 와 같음


    def minus(self):
        return self.num1 - self.num2


calc = Calculator()    # Calculator 라는 클래스로 calc 라는 객체를 만듦

# self 의 의미 : 객체 자신을 뜻함
print(calc.plus())      # calc.num1 + calc.num2 가 실행되는것과 같음 

# 객체지향 : 여러명의 개발자가 코드를 효율적으로 작성해서 프로젝트를 완성시키기 위한 방법 설계도 작성(class) -> 실제 물건(object)

# 생성자 : 클래스가 객체로 생성될때 실행되는 함수

class Calculator :
    num1 = 1          # 이 클래스를 이용해 객체를 생성하면, num1 num2 두개의 변수가 생성되고 안에 1,2 가 각자 저장된다.
    num2 = 2          # 객체를 생성하면서, 변수만 생성이 되고 안의 값은 지정하지 않게끔 변수생성 과정만 만들고 싶을때 생성자 사용 

    def plus(self) :
        return self.num1 + self.num2        


    def minus(self):
        return self.num1 - self.num2

class Calculator :
    # 생성자 함수 : 함수명 앞 뒤에 __를 무조건 붙여야 함 
    def __init__(self,num1,num2):    # 이 클래스가 객체를 만드는 순간 자동으로 실행되며, num1 num2 변수를 만들지않으면 바로 에러가 남
        self.num1 = num1
        self.num2 = num2


    def plus(self) :
        return self.num1 + self.num2        

    def minus(self):
        return self.num1 - self.num2

calc2 = Calculator(3,4)     # calc2.num1 = 3, calc2.num2 = 4 가 생성자로 인해 바로 지정됨
print(calc2.plus())         # 함수에서 아규먼트 값으로 3,4를 받은것과 비슷하게 볼 수 있음


# def __init__(self,num1,num2 =10 ):    # 생성자 함수에도 디폴트 파라미터를 지정할수 있음
#        self.num1 = num1
#        self.num2 = num2



# 데코레이터 예제 문제
user_datas = [
    {"id" : "test" , "pw" : "1234", "count" : 0},
    {"id" : "python" , "pw" : "0000", "count" : 0}
]

# user data 를 입력받아서, 아이디와 패스워드를 체크하는 데코레이터 함수를 작성
# 로그인이 될때마다 count 1씩 증가

def need_login(func):
    def wrapper(*args,**kwargs):
       # 아이디 패스워드 입력
        id , pw= tuple(input("input id and pw : ").split(" "))  # id , pw 를 " "로 구분을 해서 튜플로 만듦
        
        # 존재하는 아이디, 패스워드인지 확인
        for idx, user in zip(range(len(user_datas)),user_datas):
            # [0,{"id" : "test" , "pw" : "1234", "count" : 0}],[1,{"id" : "python" , "pw" : "0000", "count" : 0}]
            # 0,1 이 idx 에 해당, 두 개의 딕셔너리 요소가 user 에 해당

            if user["id"]==id and user["pw"]==pw:   # user 가 딕셔너리 형태이므로 user["id"], 랑 user["pw"] 를 구분 
                user_datas[idx]["count"] += 1   # 어떤  id pw 로 로그인 되었는지에 따라 두개의 count 값을 구분해서 +1 해야하니깐 해당하는 idx의 count를 1 증가
                return func(*args,**kwargs)

        return "error"    
        # 카운트 증가 및 함수 실행
    return wrapper


@ need_login
def plus_1(num1,num2):
    return num1 + num2


 