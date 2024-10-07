list1 = []  # 비어있는 리스트
# 제일뒤에 추가
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
# 있는 그대로 추가
list1.append([10, 20, 30])

print(list1)
print('-' * 20)

list2 = []  # 비어있는 리스트
# 리스트만 추가
# 제일 뒤에
# list2.extend(1)  # error, 1개씩 추가안됨
list2.extend([1])
list2.extend([2])
list2.extend([3])
list2.extend([4])
list2.extend([5])
list2.extend([10, 20, 30])
print(list2)
print('-' * 20)

# 데이터 개수 확인
print(len(list1))
print('-' * 20)

# 중간에 삽입 
# insert(index, 데이터)
list1.insert(2, 100)
print(list1)
print('-' * 20)


