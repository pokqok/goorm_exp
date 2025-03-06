import numpy as np

# 두 개의 벡터 생성
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# 원소별 곱셈 (Element-wise multiplication)
result = vector_a * vector_b

print("벡터 A:", vector_a)
print("벡터 B:", vector_b)
print("원소별 곱셈 결과:", result)

# 내적 (Dot product)
dot_product = np.dot(vector_a, vector_b)

print("벡터 A:", vector_a)
print("벡터 B:", vector_b)
print("내적 결과:", dot_product)