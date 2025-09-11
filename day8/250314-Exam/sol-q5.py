import pandas as pd

a = pd.Series([20, 15, 30, 25, 35], name='age')
b = pd.Series([68.5, 60.3, 53.4, 74.1, 80.7], name='weight')
c = pd.Series([180, 165, 155, 178, 185], name ='height')
human = pd.DataFrame([a,b,c]) # axis=0
print(human,'\n')

def main():
    # loc(), iloc() 함수를 이용하여 특정 행, 열 추출
    print(human.loc['age'],'\n')
    print(human.iloc[0],'\n')

    # loc(), iloc() 함수를 이용하여 데이터의 특정 범위 추출
    print(human.loc['weight':'height'],'\n')
    print(human.iloc[1:3],'\n')

    sex = ['F','M','F','M','F']
    # 새로운 데이터 추가하기
    human.loc['sex'] = sex
    print(human,'\n')

    #원하는 행/열 데이터 삭제하기
    tmp = human.drop(['height'])
    print(tmp,'\n')

if __name__ == "__main__":
    main()