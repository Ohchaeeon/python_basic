# 예시문제 1 번 : 문장을 입력받아서 그를 문법에 맞게 출력함

# python IS the best Language ---> 를 Python is the best language. 
# 처럼 첫 문자는 대문자로 , 끝에는 점을 찍도록 한다.


# 1. 문자열 입력받기.
sentence = input("Input sentence : ")

# 2. 전체 문장 소문자로 바꾸기
result = sentence.lower()

# 3. 첫 글자만 대문자로 바꾸기.
result = result[0].upper() + result[1:]

# 4. 마지막에 마침표 찍기.
if result[-1] != "." :
    result += "."

print(result)

# 예시 문제 2 번 : 1-45 까지 숫자 중 로또 번호를 랜덤 6개 받고 중복되지 않도록 출력.
# for 문 이용
import random

from python_4 import cal
lotto = []

for b in range(10):        # 넉넉하게 10 번 랜덤 숫자를 뽑으면서 중복 제외하고 6개를 찾아보기 위해
    a = random.randint(1,45)
    if a not in lotto:     # a 가 로또 안에 없을 경우에만 추가함으로 중복 방지
        lotto.append(a)
    
    if len(lotto) == 6:    # 로또 숫자의 개수가 6개가 되면 바로 for 문 종료
        break

print(lotto)          # 많은 반복안에서 중복을 제외하면서 for 문으로 해결하기보다는 while 문이 나음

# while 문 이용

import random

Lotto = []

while True:
    num = random.randint(1,45)
    if num not in Lotto:
        Lotto.append(num)

    if len(Lotto) == 6:
        break
print(Lotto)

# global (전역 )local (지역) 차이 

# global

gv = 10    # global 변수 함수 외에서도 적용됨

def echo():
    print(gv)

echo()
print(gv)

# ---------------------------------------------
# local

gv = 10

def echo():
    global gv # 이걸 쓰게되면, 전역함수의 gv 의 주소값에 지역변수의 gv 값인 200 이 들어가게됨. 그래서 전역변수 값이 지역변수 값과 동일해짐
    # global gv 를 쓰지 않으면, 함수 내에서만 gv 값이 200 이고 그 밖에서는 그대로 gv 값은 10 으로 유지됨.
    gv = 200 # local 변수 - 함수 내에서만 적용 됨
    print(gv)

echo()    # 함수 내에서 변수가 선언되면 그 변수를 사용, 함수 내에서 선언되지 않은 경우에 전역변수를 사용

# Inner Function : 함수가 지역영역에 선언, 함수 안에 함수가 선언

def outer (a,b):

    def inner(c,d):
        return c + d

    return inner(a,b)    

outer(1,2) # 3 이 출력 , outer를 호출함으로서 inner 가 return 되고 그 안의 함수를 돌아 3이 출력됨.
# inner (2,3) 은 지역함수 이므로 전역에서 호출 할수가 없음.


def outer (a,b):

    def inner(c,d):
        return c + d

    return inner

outer(1,2) (3,4) # 7이 출력, outer(1,2)의 값으로 inner 함수 자체가 return 되고, 거기에 (3,4)가 들어가는거니깐 7이 나옴

# callback function : 함수 자체를 아규먼트 파라미터로 설정해서 사용

def calc(func,a,b): # 함수를 아규먼트로 받아서 그 함수가 실행되도록 함
    a **= 4
    b **= 3
    return func(a,b)  # calc 함수안의 파라미터로 func 가 들어가는데 이 함수가 callback function 임

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b 

print(calc(plus,2,4))  

# lambda funtion : 파라미터를 간단한 계산으로 리턴되는 함수 (ex. 삼항연산)

def plus(a,b):
    return a + b

# 이 plus 함수를 간단하게 람다함수를 이용해서 표현하면,

plus2 = lambda a,b : a + b    # lambda  (파라미터) : (리턴값) 간단하게 표현가능

# calc(plus,a,b) = calc(lambda a,b : a + b ,a,b) 함수 자리에 바로 람다를 넣음으로서 plus 함수 선언 안해도 되니깐 메모리 줄일 수 있음.

# map() = 순서가 있는 데이터 집합에서 모든 값에 함수를 적용시킨 결과를 출력

list = [1,2,3,4]
def odd_even(num):
    return "odd" if num %2 else "even" # 삼항 연산 / 나머지 1 이면 홀수 2면 짝수

odd_even(1),odd_even(2),odd_even(3),odd_even(4)

print(map(odd_even,list)) # map(function,#iterable) 파라미터에 함수와 순서있는 값 넣음, 위 처럼 하나하나 할 필요 없이 간단

# 간단한 예
# 숫자 여러개를 입력받고, str.split() 으로 리스트로 만든 다음,리스트의 값들을 int 로 형변환

datas = input ("insert numbers : ") 
result = datas.split(" ")
result = list(map(int,result))


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