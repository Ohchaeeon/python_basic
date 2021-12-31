# 함수 선언 

def score(point):
    result =""
    if point >= 90:
        reuslt ="A"
    elif point >= 70:
        reuslt ="B"
    else:
        reuslt ="C"
    return result        

# 함수 호출
point = 90
a = score(point)

print(a)
# 파라미터 : 함수를 선언할때, 호출하는 부분에서 보내주는 데이터를 받는 변수
# 아규먼트 : 함수를 호출할때 함수에 보내주는 데이터
     # num1,2,3 이 파라미터, 디폴트 파라미터로 num2에 300이 들어감

def cal(num1,num2=300,num3=20):
    return num1 + num2 + num3

# 함수 선언 할 때 , 
cal(30,40,20) # 파라미터에 들어가는 값 : 아규먼트 
cal(20,num3=40) # num1 30 num2 300 num3 에 40 이 들어가고, num3 은 키워드 파라미터가 됨

# return : 함수를 실행한 결과를 저장하고 싶을때 사용


def echo(msg):
    if msg == 'quit':
        return          # 함수에서 return 코드가 실행되면 무조건 실행 종료 
    print(msg)    

# *args , **kwargs : 함수를 호출할때 아규먼트와 키워드 아규먼트의 개수를 지정할 수 없을경우 사용
# args 는 기본적으로 튜플로, kwargs 는 딕셔너리로 받아짐
def plus(*args,**kwargs) :
    print(type(args),args)    # plus 함수에서 아규먼트를 10개 받게될지 100개 받게될지 모를경우 
    print(type(kwargs),kwargs)   # plus 함수에 키워드 아규먼트를 10개 받게될지 100개 받게될지 모를경우 
    return sum(args), sum(list(kwargs.values())) 


spek = plus (1,2,3,4,5,a=100,b=49)
print(spek)

# *args **kwargs 의 응용
def func(num1,num2=30,num3=40):
    return num1 + num2 + num3

data = [24,35,67]
func(*data)  # list 형태의 data 값이 각각의 아규먼트 값으로 24, 35, 67 들어간다.
# func(data) 이렇게 쓰면, data 값의 리스트 형태가 그대로 num1 값에 들어가면서 에러가 남.

data = {
    'num2' : 10,
    'num3' : 50
}

func(1,**data) # func(1,num2=10,num3=50) 을 한것과 같음.