
print(hash(1000))
# print(hash([1,2]))
a = [1,['a']]
b = [1,['a']]
# mutable (list) changeable -- does not
# immutable (tuple) not-changeable -- hash

# everything is an object in python
x = 1  # pointer to object 1
x = 2  # pointer to object 2

# mutable
a = [1, 2, 3]
a[0] = 5

print(a == b)
print(hash(tuple([1, 2])))
print(hash(tuple([1, 2, 3])))
print(hash(frozenset([1, 2, 3])))

print(set([1, 1, 1, 3]))


class A:
    pass

a = A()
print(hash(a))
print(hex(hash(a)))
print(a)

d = dict({1099: 'hi', 2123: 'bye'})

print(d[2123])

print(set([1, 1, a, 3, 3, a]))

print("hash((1, 'hello'))", hash((1, 'hello')))

dict({ (1,2): 'hi'})