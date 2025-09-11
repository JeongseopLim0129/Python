import numpy as np

x = [[1,2,3], 
    [4,5,6], 
    [7,8,9]]

def solution(self):
    #리스트 x를 Numpy 배열로 출력합니다.
    array1 = np.array(x)
    #모든 원소가 0인 3×3의 배열을 출력합니다.
    array2 = np.zeros([3, 3])
    #모든 원소가 1인 2×5의 배열을 출력합니다.
    array3 = np.ones([2, 5])
    #모든 원소가 초기화되지 않은 임의의 값을 가진 5×3의 배열을 출력합니다.
    array4 = np.random.random([5, 3])
    # 0부터 9까지의 값을 원소로 하는 1×10 배열을 출력합니다.
    array5 = np.arange(10)
  
    return array1, array2, array3, array4, array5

def print_answer(**kwargs): # 딕션어리 전용 매개변수 전달값
    for key in kwargs.keys():
        print(key,"\n", kwargs[key], "\n")

array1, array2, array3, array4, array5 = solution(x)
print_answer(array1=array1, array2=array2, array3=array3, array4=array4, array5=array5)
