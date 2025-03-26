import numpy as np

a = np.arange(5)
b = np.arange(3, 5) # 3~4 아마 3이상 5미만의 숫자가 생성되는듯

c = np.arange(3.1, 5.0, 0.1)

print(a)
print(b)
print(c)

print(np.zeros(5)) #초깃값이 0인 5 배열
print(np.ones(3)) # 초깃값이 1인 3 배열

list = [5,5,3,1,2,2,5]
print(np.bincount(list)) #위의 숫자에서 숫자가 몇개씩 있는지 세주는 함수

list = [5.1,5,3,1,2,2,5] 
print(np.bincount(list)) #정수만 가능한듯?

#통계함수

list = [2,2,3,1,5]
print(np.average(list)) #평균
print(np.median(list))  #중앙값
print(np.argmax(list))  #가장 큰 인덱스값
print(np.argmin(list))  #가장 작은 인덱스값
print(np.var(list))     #분산
print(np.std(list))     #표준 편차

import math
#Math 라이브러리
print(math.pow(2,3))
print(math.sqrt(16))

import matplotlib.pyplot as plt

x = np.arange(0, 6)
plt.plot(x, 2*x)#x축, y축 구성
plt.grid()
plt.show()




