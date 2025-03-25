#딕셔너리는 {}로 구분
d = {'class' : 1, 'number' : 5, 'class' : 2}
print(d)
print(d['class'])
print(d['number'])

d['name'] = 'minho'
print(d)

del d['class']
print(d)

d['number'] = 10
print(d)

#특정 키가 있는지 확인
print('number' in d)
print('class' in d)

print(d.keys())
print(d.values())

print(list(d.keys()))
print(list(d.values()))