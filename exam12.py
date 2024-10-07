tup1 = (1, 2, 3, 4, 5)
print(tup1)
print('-' * 20)

# 문자열 만들기 1
st1 = '%d %d %d %d %d'\
      %(tup1[0], tup1[1], tup1[2], tup1[3], tup1[4])
print(st1)
print('-' * 20)

# 문자열 만들기 2
st2 = '{} {} {} {} {}'\
      .format(tup1[0], tup1[1], tup1[2], tup1[3], tup1[4])
print(st2)
print('-' * 20)

st2 = '{0} {1} {2} {3} {4}'\
      .format(tup1[0], tup1[1], tup1[2], tup1[3], tup1[4])
print(st2)
print('-' * 20)

st2 = '{0} {3} {4} {1} {2}'\
      .format(tup1[0], tup1[1], tup1[2], tup1[3], tup1[4])
print(st2)
print('-' * 20)

st2 = '{0} {3} {4} {1} {2} {3} {4}'\
      .format(tup1[0], tup1[1], tup1[2], tup1[3], tup1[4])
print(st2)
print('-' * 20)

st2 = '{0} {1} {2} {3} {4}'.format(*tup1)
print(st2)
print('-' * 20)

st2 = '{0} {1} {2} {3} {4} {2} {3}'.format(*tup1)
print(st2)
print('-' * 20)

st2 = '{0} {1} {4}'.format(*tup1)
print(st2)
print('-' * 20)

st2 = '{} {} {} {} {}'.format(*tup1)
print(st2)
print('-' * 20)

st2 = '{} {} {}'.format(*tup1)
print(st2)
print('-' * 20)

st3 = '{}'.format(3.141592)
print(st3)
print('-' * 20)

# 소수점 2자리 설정
st3 = '{:.2f}'.format(3.141592)
print(st3)
print('-' * 20)

# unpacking
a, b, c, d, e = tup1
print(a, b, c, d, e)
print('-' * 20)

a, b, c = tup1[1:4]
print(a, b, c)
print('-' * 20)

list1 = [1, 2, 3, 4, 5]
print(list1)
print('-' * 20)

st2 = '{} {} {} {} {}'.format(*list1)
print(st2)
print('-' * 20)

st2 = '{} {} {}'.format(*list1)
print(st2)
print('-' * 20)

st2 = '{1} {2} {3}'.format(*list1)
print(st2)
print('-' * 20)