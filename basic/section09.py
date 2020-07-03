# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로

# 예제1
txt  = './resource/review.txt'
f = open(txt, 'r')
content = f.read()
print(content)
# 반드시 close 리소스 반환
f.close()
print ('-------------------------')

# 예제2 , close문 생략가능
with open(txt, 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print ('-------------------------')
print ('-------------------------')
# 에제3
with open(txt,'r') as f:
    for c in f: # f자체가 iter
        print(c.strip()) # strip 양쪽공백제거해줌
print ('-------------------------')
print ('-------------------------')

# 예제4
with open(txt,'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 한번에 읽었기때문에 내용이 없음
    print(">",content) # 한번읽었기때문에         

print ('-------------------------')
print ('-------------------------')

# 예제5 (라인별로)
with open(txt, 'r') as f:
    line = f.readline() # 한줄 읽어옴
    # print(line)
    while line: # 값이 없을떄까지 
        print(line, end=' #### ')
        line = f.readline()

# 예제6 
with open(txt,'r') as f:
    contents = f.readlines()
    print(contents) # 줄바꿈까지 리스트형태로 가지고 있음
    for c in contents:
        print(c, end= ' ****** ')


print ('-------------------------')
print ('-------------------------')

# 예제7 평균구하기
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line)) 
    print(score) 

# 6자리고 소숫점 셋째짜리까지 나오도록
print('Avg : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('NiceMan\n')

# 예제2
with open('./resource/text1.txt','w') as f:
    f.write('GoodMan\n')    

# 예제3
from random import randint
with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))    
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['kim\n','Park\n','Cho\n']
    f.writelines(list)       


# 예제5 파일로 로그성 찍을때 가끔사용
with open('./resource/text4.txt','w') as f:
    print('TEST CONTENTS', file=f) # 파일 연결시 