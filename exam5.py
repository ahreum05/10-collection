str_list = ['국어','영어', '수학','사회','한국사']
print(str_list)
print('-' * 20)

print(str_list[::-1])
print('-' * 20)

# 데이터 뒤집기
str_list.reverse()
print(str_list)
print('-' * 20)

# count()
print(str_list.count('영어'))
print('-' * 20)

# 항목 변경하기
str_list[3] = '과학'
print(str_list)
print('-' * 20)

# 항목 추가 : 제일 끝에
str_list.append('세계사')
print(str_list)
print('-' * 20)

# 항목 추가 : 중간에
str_list.insert(2, '일본어')
print(str_list)
print('-' * 20)

# 정렬1 : 내장 함수
# => 원본은 안건드리고 결과를 리턴함
sort_list = sorted(str_list)  # 오름차순
print(sort_list)
print('-' * 20)

sort_list = sorted(str_list, reverse=True)  # 내림차순
print(sort_list)
print('-' * 20)

# 정렬2 : 리스트 함수
# => 리스트의 내용이 변경됨
str_list.sort()  # 오름 차순
print(str_list)
print('-' * 20)

str_list.sort(reverse=True)  # 내림 차순
print(str_list)
print('-' * 20)

# 데이터 삭제1
del(str_list[4])
print(str_list)
print('-' * 20)

del(str_list[1:3])
print(str_list)
print('-' * 20)

# 데이터 삭제2
str_list.remove('국어')
print(str_list)
print('-' * 20)

# 없는 데이터를 삭제할 경우, 에러 발생
# => 데이터 유무 검사후 삭제해야함
if '영어' in str_list :
    str_list.remove('영어')
ele : print('삭제할 데이터가 없습니다.')

print(str_list)
print('-' * 20)

# 데이터 삭제3
# => 전체 데이터 삭제
str_list.clear()
print(str_list)
print('-' * 20)




