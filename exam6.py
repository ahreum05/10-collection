# 리스트 내포
# => for문을 이용하여 대량의 데이터를 리스트에 저장하는 방법
list1 = [0 for a in range(5)]  # 0 1 2 3 4
print(list1)
print('-' * 20)

list1 = [a for a in range(5)]
print(list1)
print('-' * 20)

list2 = [num*3 for num in range(1, 5) if num%2==0]
print(list2)
print('-' * 20)

# 리스트 내포에 if 삼항 연산식을 함께 사용
list3 = [num*3 if num%2==0 else 0 for num in range(1, 5)]
print(list3)
print('-' * 20)

# unpacking : 리스트나 튜플에 있는 데이터를 개별 변수에
#             저장하는 방법
# => 개별 변수의 개수와 리스트에 저장된 개수가 일치해야 함
list4 = [1, 2, 3]
a, b, c = list4
print(a, b, c)
print('-' * 20)

a, b, c = list1[1:4]
print(a, b, c)
print('-' * 20)

# enumerate() : for문에서 리스트의 인덱스와 데이터를 묶어서 관리
list5 = ['foo', 'bar', 'baz']
for i, v in enumerate(list5) :  # (0, 'foo'), (1, 'bar'), (2, 'baz')
    print(i, v)

print('-' * 20)    
    
# zip(리스트, 리스트) : for문에서 리스트를 동일한 위치값으로 묶어서 관리
list6 = ['one', 'two', 'three']
for a, b in zip(list5, list6) :  #('foo','one'),('bar','two'),('baz','three')
    print(a, b)








