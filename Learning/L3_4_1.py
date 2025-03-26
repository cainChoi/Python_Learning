#판다스는 자료 정리를 위한 라이브러리
import pandas as pd

balls = pd.Series([20,40,10])
print(balls)

balls = pd.Series([20,40,10], ['red', 'blue', 'black'])
print(balls)