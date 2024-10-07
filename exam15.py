dic1 = {'a': 1, 'b': 2, 'c': 'hello', 'd': '파이썬'}
print(dic1)
print('-' * 20)

# key만
st1 = '{} {} {} {}'.format(*dic1)
print(st1)
print('-' * 20)

# value만
st1 = '{} {} {} {}'.format(dic1['a'],dic1['b'],dic1['c'],dic1['d'])
print(st1)
print('-' * 20)

st1 = '{a} {b} {c} {d}'.format(**dic1)
print(st1)
print('-' * 20)

# key, value 
st1 = '{0} {a}, {1} {b}, {2} {c}, {3} {d}'.format(*dic1, **dic1)
print(st1)
print('-' * 20)

st1 = '{} {a}, {} {b}, {} {c}, {} {d}'.format(*dic1, **dic1)
print(st1)
print('-' * 20)