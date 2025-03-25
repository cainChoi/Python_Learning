#집합은 set()로 구분

s1 = set([1, 2, 3, 4, 5])
print(s1)
s2 = set("Python")
print(s2)
s3 = set('banana')
print(s3)

s1 = set([1,2,3,4])
s2 = set([3,4,5,6])

#합집합
print(s1 | s2)
print(s1.union(s2))

#교집합
print(s1 & s2)
print(s1.intersection(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))