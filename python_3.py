#  반복문 : 반복되는 코드를 실행할때 사용
# while

from typing import List


data = 3
while data : # data 조건 부분이 False가 될때까지 반복
    #반복되는 코드 , False 되면 빠져나옴
    print(data)
    data -= 1

# while 예시 문제 
# 국어 80점 영어 90점 수학 100 점 인 학생의 총점, 평균 구하고 dict 또는 list 쓸것
# 해결책 1 
score = [80, 90, 100]
c = len(score)
a = 0
x = 0

while  score :
   
    a = a + score.pop()
    x += 1

print(int(a)/c)

# 해결책 2
score = [80, 90, 100]
count = len(score)
while count : 
    count -= 1

# 해결책 2 
score = [80, 90, 100]
a = 0
data = score.copy() # pop 을 쓸거기 때문에 미리 하나 복사를 해둠

while score : 
    a = a + score.pop()

print(a, a/len(data))    

# 무한 루프 
# break : 반복문을 중단시킬때 쓰는 예약어

result = 1
while result : 

    if result >= 10:
        break   # result 값이 10이 되는 순간 while문 빠져나옴

    result += 1

print(result)

# for 문
# iterble 한 값을 꺼내서 value에 대입시킨 후, 코드를 iterable 변수 개수만큼 실행
# continue : 다음으로 넘어가지 않고 다시 조건부문으로 올라가서 코드 실행
list = [0, 1, 2, 3, 4]

for a in list:
    if a % 2:  # 홀수이면 continue 실행돼서 다시 올라감
        continue # 짝수이면 실행안되고 바로 print로 내려감

    print(a)

# for 를 이용하여 코드를 100 번 실행 - range 함수 이용

sum  = 0
for b in range(100) : # 0 ~ 99 까지 실행함
    sum += b # 0 - 99 까지의 합을 출력

print(sum)      

# for 문에서 dict 자료형의 값을 사용할 때 dict.items()
# for 문에서 iterable 데이터가 tuple 로 나오면 여러개의 변수로 받을 수 있다.
a_dict = {'a' : 50, 'b' : 30 , 'c' : 40} 

for s,n in a_dict.items():   # s,n 에 차례로 각 key 와 value 값이 들어가게 됨 / 튜플 형태로 출력
    print(s,n)

# 구구단 출력
# 이중 for 문 사용

for a in range(1,10) :
    for b in range(2,10) :
        print("{} * {} = {} ".format(b,a,b*a), end = '\t') # 가로 세로로 잘 맞추기 위해 print 문 순서 잘 활용
    print()

# List comprhention
# 리스트 데이터를 만들어주는 방법, for 문 보다 빠르게 동작함.

# 리스트 내의 각 값을 제곱하여 출력
# 1.for 문 사용

list = [1,2,3,4]
result = []
for a in list:
    result.append(a ** 2)
print(result)    

# 2. list comprehention 사용 (간단, 빠름)
result = [a ** 2 for a in list ]

# 홀수와 짝수를 출력하는 코드, 삼항연산 사용

list = [1,2,3,4]
# result = ["홀","짝","홀","짝"]
result = [
"홀" if a % 2 else "짝"
for a in list
]
print(result)

# 1 - 10 까지중 홀수만 뽑을 때 , 컴프리헨션 안에 if 조건문 넣을 수 있음.

odd = [a for a in range(1,11) if a % 2 == 1]
print(odd)

# 컴프리헨션 활용 예

print(dir(list)) 
# 결과
# ['__add__', '__class__', '__class_getitem__', '__contains__', 
#'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
#'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', 
#'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
#'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', 
#'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 
#'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# dir(list) 에서 시작이 __ 가 아닌 값들만 뽑을때
result=[a for a in dir(list) if a[:2] != '__']
print(result)


