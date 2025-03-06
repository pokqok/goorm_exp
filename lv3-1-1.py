import numpy as np

# 계수 행렬 A
A = np.array([[2, 3], 
              [5, 7]])

# 상수 벡터 B
B = np.array([8, 19])

# 선형 방정식의 해 구하기
solution = np.linalg.solve(A, B)

# solution의 데이터 타입과 값 확인
print(type(solution))   # 배열 타입 확인
print(solution)         # 배열 내용 출력
