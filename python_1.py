# %reset : 현재까지 선언된 모든 변수들 리셋해줌 
# %whos : 현재 선언되어 있는 변수들 뭐 있는지 출력해줌



a = "123456789"

b = a[::-2]

print(b)
# 단축키 
# shift + tap : docstring
# 자동완성 : tap 
# 실행 : shift + enter


#컬렉션 데이터 타입 : list tuple dict
#  list [] : 순서가 있는 수정이 가능한 데이터 타입 
#  tupple () : 순서가 있는 수정이 불가능한 데이터 타입
# dict {} : 순서가 없고 , 키:값 으로 구성되어 있는 데이터 타입

# list 

ls = [ 1, 2, 3, "four", [5,6], True, 1.2]
print(type(ls))
print(ls)

#offset index 사용 가능
print(ls[3],ls[1:3],ls[::-1])

#list 함수

#append() : 가장 뒤에 값을 추가
#sort() : 오름차순으로 정렬, 바뀐 순서를 리스트에 저장
#pop() : 가장 마지막 데이터를 출력, 리스트에서 그 데이터를 삭제

ls = [1,5,2,4]
ls.append(3)
print(ls)

ls.sort() # 오름차순
lsdown = ls[::-1] # 내림차순
print(ls)
print(lsdown)

num = ls.pop()
print(num,ls)

# 리스트의 복사
ls1 = [1,2,3]
ls2 = ls1
print(ls1,ls2)  # [1,2,3],[1,2,3] 
ls1[2] = 5
print(ls1,ls2)  # [1,2,5],[1,2,5] 으로 두 개 같음 (주소값이 같기 때문에)

# 해결방안
ls3 = ls1.copy() # copy 함수 이용
print(ls1,ls3)

ls1[2]= 4
print(ls1,ls3) #[1,2,4] , [1,2,5] 로 ls3은 변하지 않음 


#tuple 은 같은 데이터를 가진 list보다 저장공간이 적게 사용된다.

a = (1,2,3)
b,c = (4.,5) # 함수에서 여러 개의 값을 반환받도록 튜플로 지정 할 수 있음 (변수로 여러개의 값 지정가능 b,c 통째가 튜플)

# list와 tuple 의 저장공간 크기 비교
import sys
ls = [1, 2, 3]
tp = (1, 2, 3)
print(sys.getsizeof(ls),sys.getsizeof(tp))

# dict 의 키 값은 정수와 문자열만 사용 가능
# 인덱스 대신 키를 사용
dic = {
    1 : "one",
    "two" : 2,
    "three" : [1,2,3]
}
print(type(dic),dic)   # 결과 : <class 'dict'> {1: 'one', 'two': 2, 'three': [1, 2, 3]}
print(dic[1],dic["three"]) # 결과 : one [1, 2, 3]


# 도시 : 부산 서울 대구
# 인구 : 340 970 240 
lst_a = ["부산","서울","대구"]
lst_b = [340,970,240]

dic = {"부산" : 340,
"서울" : 970,
"대구" : 240}

print(sum(lst_b),sum(dic.values())) # sum 함수 이용 합 구하기 , dict 는 values() 써서 값 추출한다음 sum 이용

# 데이터 타입 변환
a = 1 
b = '2'
a + int(b) # str 변수 앞에 int() 를 붙여서 형 변환가능

# zip : 같은 인덱스 끼리 묶어주는 함수
print(list(zip(lst_a,lst_b))) # lst_a 랑 b 를 각 인덱스에 맞게 맵핑하고 list 형태로 출력
result = dict(zip(lst_a,lst_b))
print(result)

data1 = list(result.keys())
data2 = list(result.values()) # 딕셔너리 형태의 값에서 keys 와 valuse 를 따로 뽑아서 리스트 형태로 만들수 있음.

print(data1, data2)

# 연산자 : 산술 , 할당(a += 10), 비교(>,< 이고 결과는 True False), 논리(or : 둘중에 하나 True 면 True, and : 둘다 True 여야 True), 멤버
# 멤버 연산 
list = ['a','b','c']

print('a' in list , 'd' in list, 'c' not in list)  # 맞는지 아닌지 - 결과 : True False False

# 랜덤함수 
import random
a = random.randint(0, 20)  # 0 - 19 사이의 정수 중 랜덤으로 하나 출력
print(a)

# 랜덤함수 , input() 이용한 간단한 해결의 책 예시
# 1. 솔루션을 리스트로 작성
# 2. 질문을 입력받음
# 3. 솔루션 개수에 맞게 랜덤 index 값 생성
# 4. index에 해당하는 리스트의 값을 출력

solutions = ["모든일이 잘 해결될 것입니다.",
"조금 조심해야합니다.",
"안좋은 일이 있을 수 있습니다."]

question = input("질문을 적으세요 : ")

result = random.randint(0 , len(solutions)-1)

print(solutions[result])  # 질문을 적으세요 : 저 오늘 행복한가요 ? /n 모든일이 잘 해결될 것입니다.