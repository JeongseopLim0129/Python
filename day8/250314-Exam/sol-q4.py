import pandas as pd

# Series()를 사용하여 1차원 데이터를 만들어보세요.
# 5개의 age 데이터와 이름을 age로 선언해보세요.

age = pd.Series([15,20,25,30,35], name= 'age')


# Python Dictionary 형태의 데이터가 있습니다.
# class_name 데이터를 Series로 만들어보세요.
class_name = {'국어' : 90, '영어' : 70, '수학' : 100, '과학' : 80}
class_series = pd.Series(class_name)
print(class_series,'\n')


# DataFrame 만들기
# DataFrame()을 사용하여 2차원 데이터를 생성해보세요.
df = pd.DataFrame([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(df,'\n')