# filter() : 리스트 데이터에서 특정 조건에 맞는 value만 남기는 함수

# 홀수만 출력하는 경우

list_1 = [1,2,3,4,5]  

# list_1 내의 값중에서 람다 함수에 True 로 나오는 값들만 출력
print(list(filter(lambda data : True if data %2 else False,list_1)))

# reduce() : 리스트 데이터를 처음부터 순서대로 특정 함수를 실행하여 결과를 누적시켜 주는 함수

from functools import reduce

ls = [2,4,6,7,9]
result = reduce(lambda x,y : x+y,ls)  # ls 내의 값들을 차례로 x,y 에 넣고 결과가 다시 x 에 다음 값은 y 에 들어가면서 누적 실행됨
print(result)

# decorlator : 함수에서 코드를 바꾸지 않고 기능을 추가하거나 수정하고 싶을때 쓰는 문법

# def a():
#     code 1 
#     code 2
#     code 3 


# def b():
#     code 1 
#     code 4
#     code 3               # a, b 함수 모두 code 1,3이 실행되고 중간만 다른 코드가 들어가는 같은 구조의 함수, 이 반복을 줄이기 위해 데코레이터 c 를 만들어줌

# def c(func):
#      def wrapper(*args,**kwargs):
#           code 1 
#           func(*args,**kwargs)
#           code 3
#           return wrapper            # code 1,3 의 순서 그대로 두고, 가운데만 func 로 둔다음, c 함수에 func 자체(b나 a같은)를 파라미터로 받아 넣음.

# --------------------------------------------
# 데코레이터를 사용할 때, @를 붙여 위에 적는다

# @c
# def a() : 
#      code 2

# @c
# def b() : 
#      code 4


def plus(x,y):
    print("start")                       # code 1
    result = x + y                       # code 2
    print("result : {} ".format(result)) # code 3 
    return result

def minus(x,y):
    print("start")                       # code 1
    result = x - y                       # code 4
    print("result : {} ".format(result)) # code 3 
    return result

# 이런 Plus minus 함수가 있을 경우, 데코레이터를 사용하면, 

def deco(func):
    def inner(*args,**kwargs):
        print("start")                       # code 1
        result = func(*args,**kwargs)        # 함수 plus or minus 가 들어올 자리
        print("result : {} ".format(result)) # code 3 
        return result
    return inner    

# @deco를 사용한뒤, 그에 들어갈 각 함수는 간단하게 만들 수 있다.
@deco
def plus_1(x,y):
    result = x + y
    return result

@deco
def minus_1(x,y):
    result = x - y
    return result
#-------------------------------------------------
# 데코레이터 사용 예제
# 패스워드를 입력받아야 함수가 실행되도록하는 데코레이터 작성
def check_password(func):
    def check(*args,**kwargs):
        pw = "abcd" # 패스워드가 맞는지 체크한다
        input_pw = input("nput pw : ")    
        if input_pw == pw:
            result = func(*args,**kwargs) 
        else :
            result = "error" 
        return result 
    return check    
   
import random  

@check_password         # 비번 입력받고, 맞으면 로또번호 출력 틀렸으면 아예 실행안도록 할수있음
def lottofunc() :
    Lotto = []
    while True:
        num = random.randint(1,45)
        if num not in Lotto:
            Lotto.append(num)
        if len(Lotto) == 6:
            break
    return(Lotto)

lottofunc()
   
