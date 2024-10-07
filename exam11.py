tup1 = (1, 2, 3, 4, 5)
tup2 = ('c언어', 'Python', 'Java', 'JSP', 'Python')

print(tup1)
print(tup2)
print('-' * 20)

tup3 = tup1 + tup2
tup4 = tup1 * 3
print(tup3)
print(tup4)
print('-' * 20)

print(tup1.count(30))
print(tup1.count(3))
print('-' * 20)

print(tup1.index(3))
print(tup2.index('Python'))
print(tup2.index('Python', 2))
print('-' * 20)

print('len :', len(tup1))
print('max :', max(tup1))
print('min :', min(tup1))
print('sum :', sum(tup1))
print('오름차순 :', sorted(tup1))
print('내림차순 :', sorted(tup1, reverse=True))
print('-' * 20)

print('len :', len(tup2))
print('max :', max(tup2))
print('min :', min(tup2))
print('오름차순 :', sorted(tup2))
print('내림차순 :', sorted(tup2, reverse=True))
print('-' * 20)





