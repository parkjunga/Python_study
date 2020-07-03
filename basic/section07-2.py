# section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본 (코드재사용 및 중복줄일수있음)
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛,면 종류, 이름): 부모

class Car:
    """Parent Class"""
    def __init__(self,tp, color):
        self.tp = tp
        self.color = color

    def show(self):
        return "Car Class Show method"    

class BwmCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "You Car name : %s" % self.car_name 

class BenzCar(Car):
    def __init__(self, car_name,tp,color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car name : %s' % self.car_name

    def show(self):
        print(super().show()) # 부모꺼도 출력
        return 'Car Info : %s %s %s' % (self.car_name, self.tp, self.color)                

# 일반사용
model1 = BwmCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.tp)  # Super
print(model1.car_name) #Sub
print(model1.show()) # Super
print(model1.show_model())
print(model1.__dict__)

# 메소드 오버라이딩
model2 = BenzCar('220d', 'suv','red')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())


# Inheritance Info
print(BenzCar.mro()) # 상속관계 확인가능
print(BwmCar.mro())


# 예제2 
# 다중상속

class x(object):
    pass

class Y():
    pass

class Z():
    pass

class A(x, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())