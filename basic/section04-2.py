# section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = 'NiceMan'
str3 = ' '
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have \'bing collection\'"
print(escape_str1)
escape_str2 = "Tab\tTab\t"
print(escape_str2)

# Rav String (중요), 경로표시시 많이 사용
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인 변수뒤에 \를 쓰고 나서야 해야 문자로 인식하고 제대로 출력됨  
multi = \
""" 
문자열 
멀티라인 
테스트 
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)

# a라는 연산자가 str_o4에 포함했는지를 물어보는 예제
print('a' in str_o4) 
print('f' in str_o4)
print('z' not in str_o4)


# 문자열 형 변환
print(str(77) + 'a') # 형변환해서 덧셈이 가능
print(str(10.4))

# 문자열 함수

a = 'niceman'
b = 'orange'

print(a.islower())
print(b.endswith('e')) # 끝이 e로 끝나는지 true/false로 반환
print(a.capitalize()) # 첫글자만 대문자로 변경해줌
print(a.replace('nice','good')) # 첫번째 : 찾고자하는거 두번째는 바꿀값
print(list(reversed(b))) # orange 라는 단어가 역순으로 거꾸로 리스트 형태로 담겨서 반환됨

# 슬라이싱  중요 **
print(a[0:3]) # nic 3이전까지
print(a[2:3]) # c 3이전까지 출력
print(a[0:len(a)]) # 끝까지
print(b[0:4:2])
print(b[1:-2]) # ran -1이 e고 -2가 g니까
print(b[::-1]) # 역방향