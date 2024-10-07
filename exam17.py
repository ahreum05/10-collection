a = {1, 2, 3}
b = {1, 2, 3, 3, 3}

print(a)
print(b)
print('-' * 20)

# 데이터 추가
a.add(4)
print(a)
print('-' * 20)

# 개별 데이터 확인
#print(a[0])   # error, 인덱싱을 사용못함
print('-' * 20)

# pop() : 데이터 1개를 꺼내고 삭제함
print(a.pop())
print(a)
print('-' * 20)

# for문 사용
for v in a:
    print(v)
    
print('-' * 20)

# 수정 : 개별 데이터 수정은 할수없음
# => 기존 데이터 삭제후 추가를 함

# 삭제 : 1개 데이터 
a.remove(2)
print(a)
print('-' * 20)

# 삭제 : 모든 데이터
a.clear()
print(a)
print('-' * 20)

# 텅 빈 세트 생성
b = set()
print(b, type(b))
print('-' * 20)

# 주용도
# => 리스트의 중복 데이터를 제거할 때 주로 사용
list1 = [1, 2, 3, 3, 3, 4, 5, 5, 1, 2]
print(list1)
print('-' * 20)

list2 = list(set(list1))
print(list2)
print('-' * 20)





    
