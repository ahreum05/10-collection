# {'key':데이터}
# key : 정수, 실수 또는 문자열 
dic1 = {'a': 1, 'b': 2, 'c': 'hello', 'd': '파이썬'}
dic2 = {1: 1, 2: 2, 3: 'hello', 4: '파이썬'}
dic3 = {1.1: 1, 2.2: 2, 3.3: 'hello', 4.4: '파이썬'}

print(dic1)
print(dic2)
print(dic3)
print('-' * 20)

# 개별 데이터 확인
print(dic1['b'])
print(dic2[2])
print(dic3[3.3])
print('-' * 20)

# 데이터 추가
# => 기존에 키가 존재하지않으면 추가
dic1['e'] = 'big data'
print(dic1)
print('-' * 20)

# 데이터 수정
# => 기존에 키가 존재하면 수정
dic1['e'] = 'deep learning'
print(dic1)
print('-' * 20)

# 데이터 삭제 : 1개
del(dic1['e'])
print(dic1)
print('-' * 20)

# 데이터 삭제 : 전체 데이터
dic1.clear()
print(dic1)
print('-' * 20)

# 응용
# 고객 1명 데이터 저장
# => 딕셔너리에 저장
people = {}
people['name'] = '홍길동'
people['tel'] = '010-1234-5678'
people['address'] = '서울시 동작구'

print(people)
print('-' * 20)

# 고객 여러명 데이터 저장
# => 리스트에 딕셔너리 저장
members = []
members.append(people)
print(members)
print('-' * 20)

people = {}
people['name'] = '김철수'
people['tel'] = '010-5555-5678'
people['address'] = '서울시 종로구'

print(people)
print('-' * 20)

members.append(people)
print(members)
print('-' * 20)

for p in members :
    print('{} {} {}'.format(p['name'], p['tel'], p['address']))





