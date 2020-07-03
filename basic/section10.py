# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드실행프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 

# SyntaxError : 잘못된 문법

# print('TEst)
# if True
#     pass

# NameError : 참조변수
a = 10
b = 15

# print(c)

#ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버 
x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외발생

# KeyError

dic = {'name' : 'Kim' , 'Age' : 33, 'City' : 'Seoul'}

#print(dic['hobby']) 직접접근보다는
print(dic.get('hobby')) #없다면 반환값은 None이라 if로 처리 가능

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러

import time
print(time.time())
# print(time.month())

# ValueError : 참조값이 없을때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('test.txt','r') # 없는파일 실행시 예외

# TypeError

x = [1,2]
y = (1,2)
z = 'test'
# print(x + y) # 다른타입끼리 더하니까 에러 

# 정리 : 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩 
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAEP 코딩 스타일)

# 예외 처리 기본
# try : 예외가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 예외가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name =['kim', 'Lee', 'Park']

try:
    z = 'kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError : # 어떤 에러가 날지모를때는 그냥 except:
     print("에러발생!!") 
else:
    print('에러없음')      

print('-------------------------------------')

# 예제3

try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it ! in name'.format(z, x+1))
except:
    print("뭔지모름") 
else: 
    print("에러아니야") 
finally:
    print('ok')

print('-------------------------------------')
print('-------------------------------------')

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok Finally')

print('-------------------------------------')
print('-------------------------------------')

# 예제5 (에러가 발생될만한게 추측되는 except를 미리 앞에 적고 그래도 아니다 싶을때 최후 Exception을 마지막에)

try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it ! ' .format(z, x+1))
except ValueError as l:
    print(l)
except IndexError:
    print("IndexError")
except Exception:
    print("뭔에러인지..") 
else:
    print("무사통과")       
finally:
    print("무조건 실행")   

# 예제6
# 예외 발생 : raise 
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == "No":
        print("ok")
    else:
        raise ValueError        
except ValueError:
    print("문제발생")
except Exception as f:
    print(f)
else:
    print("ok !")    