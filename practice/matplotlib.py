import matplotlib as plt
import numpy as np

x = np.linspace(0, 10, 100)  # 0부터 10까지 범위에서 100개의 점 생성
y = np.sin(x)  # 사인 함수를 사용하여 y값 생성

# 그래프 생성
plt.figure(figsize=(8, 4))  # 그래프 크기 지정
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-', linewidth=2)  # 선 그래프 생성

# 그래프에 제목과 라벨 추가
plt.title('사인 그래프')
plt.xlabel('x 축')
plt.ylabel('y 축')

# 범례 추가
plt.legend()

# 그래프 표시
plt.grid(True)  # 그리드 추가
plt.show()