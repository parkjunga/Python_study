# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형 

# 딕셔너리(Dictionary) : 순서가없다., 중복안됨, 수정o

# key, value (Json) -> MongoDB
# 선언

a = {'name':'kim', 'Phone':'010-1234-1234','birth': 870212}
b = {0: 'Hello Python', 1: 'Hello Coding'} # 보통 숫자로 키값 사용하지않음
c = {'arr' : [1,2,3,4,5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name')) # 이 방식을 좀 더 추천, 더 안전하게 조회됨
print(a.get('address')) # 조회시 없을경우 None으로 표시됨
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
a['rank1'] = [1,2,3,4]
a['rank2'] = (1,2,3)
print(a)

# keys, values, items
print(a.keys()) # 키에서 인덱싱 접근은 불가능 ex) a.key()[0] (x)

# 위와같은 상황때문에 list로 형변환
print(list(a.keys()))
temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items()) # 전체를 가져옴
print(2 in b)
print('name2' not in a)

# 집합 (머신러닝이나 이러경우 주로쓰임)
# 순서가없고 중복을 허용하지않음
a = set()
b = set([1,2,3,4])
c = set([1,2,3,4,6,6])
print(type(a))
print(c)

t = tuple(b) 
print(type(t))
l  = list(b)
print(l)

print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([5,6,4,1,2,32])

# 교집합 출력
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7,8,10,15])
s3.add(18)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))