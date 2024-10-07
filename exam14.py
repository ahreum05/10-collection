dic1 = {'a': 1, 'b': 2, 'c': 'hello', 'd': '파이썬'}
print(dic1)
print('-' * 20)

# key값 유무 확인
if 'c' in dic1 : print('키가 존재함')
else : print('키가 존재하지 않음')
print('-' * 20)

# key 값 확인 1
for k in dic1 :
    print(k, end=', ')

print()
print('-' * 20)

# key 값 확인 2
print(dic1.keys())
print('-' * 20)
# 리스트로 변경
print(list(dic1.keys()))
print('-' * 20)

# value 값 확인
print(dic1.values())
print('-' * 20)
# 리스트로 변경
print(list(dic1.values()))
print('-' * 20)

# key, value 둘다 확인
print(dic1.items())
print('-' * 20)
# 리스트로 변경
print(list(dic1.items()))
print('-' * 20)

# 개별 데이터 확인 1
print(dic1['a'])
print('-' * 20)
#print(dic1['f'])  # error, 없는 키 사용안됨
print('-' * 20)

# 개별 데이터 확인 2
print(dic1.get('a'))
print('-' * 20)
print(dic1.get('f'))
print('-' * 20)

# for문 사용 : key
for key in dic1.keys() :
    print(key, dic1[key])
    
print('-' * 20)    

# for문 사용 : value
for value in dic1.values() :
    print(value)
    
print('-' * 20)  

# for문 사용 : key, value
for k, v in dic1.items() :
    print(k, v)

print('-' * 20) 

# 딕셔너리를 다른 딕셔너리에 추가
dic2 = {'e': '빅데이터', 'f': '딥러닝'}

# 추가방법1
dic1.update(dic2)
print(dic1)
print('-' * 20) 

# 추가방법2
dic1['g'] = dic2
print(dic1)
print('-' * 20) 







