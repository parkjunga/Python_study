# 데이터 타입

v_str1 = 'Niceman'
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "kim",
    "age" : 25
}

v_list =[3, 5, 7] # 배열과 비슷
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_list))
print(type(v_set))
print(type(v_tuple))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999
big_int2 = 11223214141515151515155511515151
f1 = 1.234
f2 = 3.456
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1* f2)
print(f3 + f2)

result = f3 + i2
print(result,type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b 
print(result2)

# 형변환 
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int('3'))

y = 100
y *= 100
print(y)

# 수치 연산 함수 

# 절대값을 알려줌 결과값 : 7 
print(abs(-7)) 
n, m = divmod(100,8)
print(n,m) # 100을 8로 나누면 12가 몫, 4가 나머지

import math

# 5.1보다 크면서 가장 작은 정수
print(math.ceil(5.1)) 

# 3.874보다 작으면서 가장 큰 정수 
print(math.floor(3.874))
