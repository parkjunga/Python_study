# section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello", world)

hello("Python")
hello(777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python! ! !")
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100) 
print(type(val1),val2,val3)   

# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))


# 예제4
# *args, *kwargs (다양한 매개변수 형태를 받아서)

def args_func(*args):
    print(args)
    # 튜플에서 인덱스를 확인하고자할때 
    for i, v in enumerate(args):
        print(i, v)
    for t in args:
        print(t)

args_func('kim')
args_func('kim','park')


# kwargs (키워드줄임말) 별표가 하나일때 *args는 튜플 **kwargs 두개일때 딕셔너리
def kwargs_fun(**kwargs):
    print(kwargs)
    for k, v  in kwargs.items():
        print(k,v)

kwargs_fun(name=1,name2=2,name3=3)    

# 전체 혼합 (다양한 형태의 매개변수받으려고 뒤에 두개는 가변인자)
def example_mul(args1, args2, *args, **kwargs):
    print(args1,args2, args, kwargs)

example_mul(10,20)
example_mul(10,20,'park','kim')

example_mul(10,20,'park','kim',age=24,age2=40)

# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)        

# 예제6(hint)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1,y2,y3]

print(func_mul3(5))


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 게시판 전체 내용 바꾸거나 새로운문자열사용할때 좋음 람다사용시

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func) # 함수생성해서 변수에 할당


lambda_mul_10 = lambda num: num * 10

print(lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10,10, lambda_mul_10)    

print(func_final(10,10,lambda x : x * 1000))