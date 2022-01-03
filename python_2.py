# boolean 에서 int , float = 0, 0.0 외에 전부 True / str = "" 외 전부 True, list tuple dict = [] 외에 전부 True
# if 문 간단한 예

# 1. 돈이 10000원 이상 있으면 택시를 탄다.

money = 12000

if money > 10000:
    print("택시를 탄다.")
if money < 10000: 
    print("걸어간다.")   

# 조건문 두개가 아닌 한번에 하는 간단한 방법
money = 7000
if money >= 10000:
    print("택시를 탄다.")
else :
    print("걸어간다.")


# 돈이 10000원 이상 있으면 택시, 5000 이상이면 버스 , 그 이하면 걸음.

money = 3000
if money >= 10000:
    print("택시를 탄다.")
elif money >= 5000:
    print("버스를 타다.")
else :
    print("걷는다.")


# 2.
# - 계좌에 10000 원이 들어있다.
# - 인출금액을 입력받는다.
# - 인출 금액이 계좌 금액보다 크면 "인출불가"
# - 인출 금액이 계좌 금액보다 작으면 "인출가능"
# - 인출 후 남은 금액 출력

account = 10000

money = int(input("draw money : "))

if money > account :
    print("인출 불가합니다" + str(money - account)+ "원이 부족합니다.")
    print("현재 잔액은" + str(account)+"원입니다.")

else :
    print("인출가능")
    print(str(money) + "원이 출금되었습니다.")
    print("현재 잔액은" + str(account-money)+"원입니다.")  # 첫 번째 방법

    

account = 10000

money = int(input("draw money : "))

if money <= account :
    account -= money
    print(str(money) + "원이 출금되었습니다.")


else :
    print(str(money-account) + "원이 부족하여 출금불가합니다.")

print("현재 잔액은" + str(account)+ "입니다." )   # 두번째 방법

# string 데이터 타입에서 간단한 .format(변수명) 사용방법
print(str(account) + "원하는 출금액과" + str(money)+ "처음 계좌 잔액입니다.")
# = print("{} 원하는 출금액과 {} 처음 계좌 잔액입니다.".format(account,money))

# 삼항 연산자
# (True) if (condition) else (False)

# num 이 0이면 , "zero"  아니면 "not zero" 를 출력
num = 1

if num :
    print("not zero")

else :
    print("zero")

# 삼항 연산자로 나타내면, 
num = 0

"not zero" if num else "zero"

