'''
위키 독스 점프 투 파이썬
https://docs.google.com/presentation/d/17UXm1UVtPfYhZ_UNInZBh4Izqx0dVDxz/edit?usp=sharing&ouid=107162547144128955683&rtpof=true&sd=true
'''
# #내장 함수

# #표준 라이브러리
# import datetime

# day1 = datetime.date(2025,9,8)
# day2 = datetime.date(2025,1,1)
# print(day2-day1)

# print(day1.weekday()) # (0~6 -> 월부터 일요일)
# print(day1.isoweekday()) # (1~7 -> 월부터 일요일)

# import time

# for i in range(10):
#     time.sleep(2)
#     print(i)

# import webbrowser

# webbrowser.open_new('www.google.com')



#외부 라이브러리

#pip

from faker import Faker

faker = Faker()
print(faker.name)


a = 'Life is too short'
b = a.encode('utf-8')
print(b) # byte
print(type(b))

a= '한글'
b = a.encode('euc-kr')
print(b)

#유니코드

#클로저

#데코레이터

#이터레이터

#제너레이터

#파이썬 타입 어노테이션

#인터프리터가 사용하는 언더스코어
if __name__ == '__main__': # 직접 실행시켰을 때만 코드를 실행
  print('hello') # ????