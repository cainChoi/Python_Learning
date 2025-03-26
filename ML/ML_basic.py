import numpy as np
from sklearn.linear_model import LinearRegression

# 샘플 데이터 생성
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# 모델 훈련
model = LinearRegression()
for idx in range(100000):
    model.fit(X, y)

# 예측
predictions = model.predict([[3, 5], [4, 4]])
print(predictions) # 출력: [16. 15.]
