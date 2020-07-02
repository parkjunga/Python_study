# section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서가있다. 수정도 가능하다. 삭제도 가능하다.) 중요!
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10,100,'pen','banana']
e = [10,100, ['pen','banana','Orange']]

# 인덱싱
print(d[3]) # banana
print(d[-1]) # banana
print(e[2][1]) # banana
print(e[-1][-2])

# 슬라이싱
print(d[0:2]) # [10,100]
print(e[2][1:3]) # ['banana', 'Orange']

# 연산
print(c + d) # [1,2,3,4,10,100,'pen','banana']
print(c * 3) # [1,2,3,4,1,2,3,4,1,2,3,4]
print(str(c[0]) + 'hi') #1hi

# 리스트 수정
c[0] = 77
print(c)
c[1] = ['a','b','c']
print(c)

# 리스트 삭제
del c[1]
print(c)

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7) # 2번 인덱스에 7넣는다.
print(y)
y.remove(2) # y에 2번째 인덱스를 지운다
y.remove(7)
print(y)
y.pop() # 맨 마지막 값을 꺼내는것
ex = [88,77]
y.extend(ex) # y에 연장
print(y)

# 삭제: del, remove, pop


# 튜플 (1. 순서가있다. 2. 중복허용한다. 3. 수정안된다. 4. 삭제도 안된다.) 주로 키값이나 계좌같이 변경이 불필요한 중요한것들에 사용함
a = ()
b = (1,) # 마지막을 ,로 끝내줌
c = (1, 2, 3, 4)
d = (10,100,('a','b','c'))

print(type(c))
print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][1])

print(c + d)
print(c * 3)

# 튜플 함수

z = (5, 2, 1, 3, 4,)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))