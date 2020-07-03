# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if q1.get('가을'):
    print("1 : ", q1.get('가을'))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q2.values():
    if v == '사과':
        print('2 : ','사과포함됨')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
jumsu = input("점수 : ")

if 100 >= int(jumsu)and int(jumsu) >= 81:
    print("A학점")
elif 80 >= int(jumsu) and int(jumsu) >= 61:
    print("B학점") 
elif 61 >= int(jumsu) >= 40:
    print("c학점")    
elif 40 >= int(jumsu) >= 21:
    print("D학점")
elif 20 >= int(jumsu) >= 0:
    print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

test = [12, 6, 18]
print("4 :", max(test))
a,b,c = 12,6,18
best = a

if b > a :
    best = b
if c > b:
    best = c     
print('best : ', best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for q in q3:
    if q != '정':
        print("6 : ", q)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for odd in range(1,101):
    if odd % 2 != 0:
        print("7 : " ,odd)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for q in q4:
    if len(q) >=5:
        print("8 : ",q)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for q in q5:
    if q.islower():
        print("9 : ", q)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for q in q6:
    if q.islower():
        print("10 : ", q.upper())
    else:
        print("10 : ", q.lower())    