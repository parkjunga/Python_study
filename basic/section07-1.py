# section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수
#     함수



# 에제1 클래스명 -> 첫글자는 대문자
class UserInfo:
    def __init__(self, name,height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        print("초기화")
    def user_info_p(self):
        print("Name : ", self.name)    


user1 = UserInfo("kim",150,10) 

print(user1.user_info_p())
print(user1.__dict__)       

# 예제2
# self의 이해
class SelfTest:
    def function1(): # 클래스메소드 클래스에서 직접
        print("function1 called")
    def function2(self): # 인스턴스메소드   
        print("function2 called")
self_test = SelfTest()
SelfTest.function1()
self_test.function2()

# 예제3
# 클래스 벼수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 모두공유하기때문에 3
    stock_num = 0
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('jim')
user2 = WareHouse('park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스 

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 자기네임스페이스에 없으면 클래스 네임스페이스에서 찾고 없을경우 에러발생