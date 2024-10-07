a = [1, 2, 3, 4, 5]
b = (6, 7, 8, 9, 10)
c = {11, 12, 13}

print(a, type(a))
print(b, type(b))
print(c, type(c))
print('-' * 20)

ba = tuple(a)
bc = tuple(c)
print(ba, type(ba))
print(bc, type(bc))
print('-' * 20)

ca = set(a)
cb = set(b)
print(ca, type(ca))
print(cb, type(cb))
print('-' * 20)

ab = list(b)
ac = list(c)
print(ab, type(ab))
print(ac, type(ac))
print('-' * 20)

