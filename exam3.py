# index : 위치값
# 양수       0      1      2      3      4
# 음수      -5     -4     -3     -2     -1
str_list = ['국어','영어', '수학','사회','한국사']
print(str_list)
print('-' * 20)

# 인덱싱 : 데이터 1개 선택
print(str_list[0])
print(str_list[2])
print(str_list[4])
print(str_list[-4])
print('-' * 20)

# 슬라이싱 : 데이터 여러개 선택
# [start: end: step]
print(str_list[1:4:1])  # 1, 2, 3
print(str_list[1:4])    # 1, 2, 3
print(str_list[1:])     # 1~끝까지
print(str_list[:4])     # 0, 1, 2, 3
print(str_list[:])      # 0~끝까지
print(str_list[::-1])   # 역순서
print('-' * 20)

# 인덱스 값 확인
print(str_list.index('영어'))
print('-' * 20)
if '중국어' in str_list :
    print(str_list.index('중국어'))
else : print('데이터가 없습니다.')
print('-' * 20)

# 데이터 존재 검사
if '수학' in str_list :
    print('데이터가 존재함')
else : print('데이터가 존재하지 않음')
print('-' * 20)

# for문
for subject in str_list :
    print(subject)




