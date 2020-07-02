# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))
# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('apple','orange','banana','lemon' ,sep=';')

# 3. 화면에 * 기호 100개를 표시하세요.
ver = '*'
print( ver * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
str_1 = '30'
int_1 = int(str_1)
float_1 = float(int_1)
com_1 = complex(int_1)

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
test2 = 'Niceman'
print(test2[4:len((test2))]) # 4다음부터 


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry" list에 담아서 출력
str_2 = 'Strawberry'
#print(list(reversed(str_2)))
print(str_2[::-1]) #슬라이싱해서 거꾸로 


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
str_3 = "010-7777-9999"
#print(str_3.replace('-',''))
print(str_3[0:3] + str_3[4:8] + str_3[9:13])

# 정규표현식

import re
print("7", re.sub('[^0-9]','',str_3)) # 정규표현식

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
str_4 = "http://daum.net"
print(str_4.replace("http://",''))

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
str_5 = 'NiceMan'
print(str_5.upper())
print(str_5.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
str_6 = 'abcdefghijklmn'
print(str_6[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
list_1 = ["Banana", "Apple", "Orange"]
del list_1[1]
print(list_1)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
set_1 = {1,2,3,4}
print(list(set_1))

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dic_1 = {'성인':100000,'청소년':7000, '아동':3000}
print(dic_1)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dic_1['소아'] = 0
print(dic_1)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(dic_1.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(dic_1.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
