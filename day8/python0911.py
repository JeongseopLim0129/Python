#NumPy
import numpy as np

l =[1,2,3,4,5]
print(type(l))

a = np.array([1,2,3,4,5])
print(type(a))

b = np.array([1,2],
             [3,4], dtype=float) # 2차원 (2x2)

print(b, type(b))

c = b.astype(int)
print(c, type(c))

d = np.zeros((3,3)) # 0행렬 (쉐입은 튜플로)
print(d)

e = np.ones((3,3))
print(e)

f = np.arange(0, 20, 2)
print(f)

g = np.linspace(0, 1, 20) # 0~1을 20개로 균등하게 나눠라
print(g)

h = np.random.random((2,2)) # 0.0 ~ 1.0의 랜덤숫자를 (2,2)의 행렬에 넣어라
print(h)

i = np.random.normal(0, 1, (2,2)) # 표준정규분포 (평균: 0, 표준편차: 1)
print(i)

j = np.random.randint(0, 10, (2,2))
print(j)


#pandas


#matplotlib

#seaborn
