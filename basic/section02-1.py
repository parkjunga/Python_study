
# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

# 원하는 출력값을 넣지 않았을 경우 엔터효과가 난다.
print()

# Separator 옵션
print('T', 'E', 'S', 'T', sep='')
print('2019','02','19', sep='-')
print('nicname','gogle.com',sep='@')

# end 옵션 
print('Wellcome To', end ='')
print('the black paradise', end='')

# format 사용 [], {}, () //대괄호, 중괄호, 소괄호순
print('{} and {}'.format('You','Me') )
print("{0} and {1} and {0} " .format('You','Me')) # 인덱스순으로 
print("{a} and {b} ".format(a='You',b='Me'))

# %d = 정수 %s = 문자열 %f = 실수 , 뒤에 formating대신 %넣고 괄호에 앞에값에 들어갈 것 넣는다.
print("%s'a favorite number id %d'" % ('Test', 7)) 

print("Test : %5d, Price : %4.2f" % (1234,1234.123)) # 5자리 정수가 온다. # 4자리 정수 소수점 두자리까지 나오게 지정 
print("Test1 : {0: 5d}, Price :{1: 4.2f}" .format(556,1234.1234)) # 중괄호붙였을때는 %안붙여도됨. 중괄호내에 해당 내용넣을시 중괄호옆에 붙여야됨
print("TEST1 : {a: 5d}, Price :{b: 4.2f}" .format(a= 556, b=1234.1234))# s위와 동일

'''
참고 = 이스케이프 문자 
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스 
\000 : 널 문자
'''

print('\'you\'')
print("'you'")
print('you"')