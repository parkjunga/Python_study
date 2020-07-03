# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모디렉토리
# .  : 현재디렉토리

# 사용1(클래스) pkg패키지 하위 fibonaci 파일에서 Fibonaci를 가져옴

from pkg.fibonaci import Fibonacci

Fibonacci.fib(300)
print("ex2 : ", Fibonacci.fib(400))
print("ex3 : ", Fibonacci().title)

# 사용2 권장X 메모리 많이 차지함
# from pkg.fibonaci import * 

# 사용3 

from pkg.fibonaci import Fibonacci as fb
fb.fib(500)
print("테스트4 : ", fb.fib(1500))
print("테스트4.title ", fb().title)

# 사용4(함수)

import pkg.calculations as c

print("TEST4 :",  c.add(10,100))
print("TEST% : ", c.mul(10,1000))


# 사용5(함수)
from pkg.calculations import div  as d
print("ex 5 : ", int(d(100,1000)))


# 사용6
import pkg.prints as p
import builtins # 기본임폴트임
p.print1()
p.print2()
print(dir(builtins))