#배열은 []로 구분분
a = [100, 70, 80, 75, 90]
print(a)
print(a[3])

a = [1, 2]
b = [3, 4]
c = ['a', 'b']

print(a + b)
print(a + c)
print(a * 2)
print(c * 3)
#print(a * b) 오류 남

a = [1, 2, 3, 4, 5]
print(a)
del a[2]
print(a)

del a[1:3]
print(a)

a[1] = 2
print(a)

a = [5, 2, 4, 3, 1]
a.sort()
print(a)
