import numpy as np

#1번 문제
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]
array1 = np.array(x)
print(array1)

array2 = np.zeros((3,3))
print(array2)

array3 = np.ones((2,5))
print(array3)

array4 = np.random.random((5,3))
print(array4)

array5 = np.arange(0, 10, 1)
print(array5)

#2번 문제
array2 = array1[:, 0] + array1[:, 1]
print(array2)

array3 = array1[0, :] + array1[1, :]
print(array3)

array4 = array2 * array3
print(array4)

array5 = np.c_[array2, array3, array4] # np.c_ 컬럼 방향
print(array5)

array6 = array1 / array5
print(array6)

#3번 문제
x = np.array([1,2,3,4,5,6,7,8,9])
array1 = x.reshape((3,3))
print(array1)

array2 = array1[:, 1].reshape(3,1) # 2차원
print(array2)

array3 = np.c_[array1, array2]
print(array3)

array4 = array3.reshape((3,2,2))
print(array4)

array5 = array4[1,0,:] # 3차원 인덱싱
print(array5)

import pandas as pd

age = pd.Series([15,20,25,30,35]), name= 'age'

class_name = {'숫어': 90, '영어': 70, '수학':100, '과학': 80}
class_series = pd.Series(class_name)
print(class_series)

df = pd.DataFrame([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
