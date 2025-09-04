#함수
'''
def 함수명(매개변수): # 매개변수로 사용된 변수는 함수 내에서만 사용 가능 (로컬 변수)
    수행할 문장
    return 반환값 # 리턴이 없어도 됨 # 반환 즉시 함수 탈출
'''
def show_price(customer):
    print(f'{customer} 고객님')
    print('커트 가격은 10000원 입니다')

cus1 = '나장발'
show_price(cus1)

cus2 = '나수염'
show_price(cus2)

def get_price(is_vip): # 함수 정의
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price(True) #함수 호출
print(f'고객님의 커트 가격은 {price}원 입니다')



#기본값 (전달값에 기본으로 사용되는 값)
def get_price(is_vip=False): #기본값이 flase (매개변수를 받지않고 호출되면 false가 됨)
    if is_vip == True:
        return 10000
    else:
        return 15000

price = get_price()
print(f'고객님의 커트 가격은 {price}원 입니다')



#키워드 값
'''
def get_price(is_vip=False,
is_birthday=False,
is_membership=False,
card=False,
review=False,
first_time=False):
...
price = get_price(review=True, is_birthday=True)
'''
#값이 다르게 출력되는 호출문을 고르세요
def order(shot=2, size='Regular', takeout=True): # 커피 주문
    print(f'아메리카노 {size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료 되었습니다')

# order()
# order(2, takeout=True)
# order(size=“Regular”)
# order(“Regular”, takeout=True) 이것만 다름 shot에 Reguler값이 들어감



#가변인자 (개수가 바뀔 수 있는 인자)
def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)
visit('2022년 6월 10일', '나장발') # 1명 방문
visit('2022년 6월 10일', '나장발', '나수염') # 2명 방문
visit('2022년 6월 10일', '나장발', '나수염', '나김리') # 3명 방문



#지역변수
message = '하이' # 전역변수 (global 변수)

def secret():
    message = '이건 나만의 비밀' # 지역 변수 (함수 내에 정의된 변수), (함수 밖에서 접근 불가능)
print(message) # secret 함수 내의 message와 다른 변수임 (함수 밖에 정의된 message변수임)

def no_secert():
    message = '비밀 아님' # 다른 함수내에 같은이름의 변수가 정의 될 수 있고 서로 다른 변수임
    print(message)

def no_secert2():
    global message # 함수밖에서 정의된 전역변수를 사용할 수 있음
    message = '하이2'
no_secert2()
print(message)



#사용자 입력 (입력받은 값은 항상 string으로 받아짐)
num = int(input('몇 명이세요?'))
if num > 4:
    print('죄송합니다 저희 식당은 4명까지만 예약 가능합니다')
else:
    print(f'{num}명 예약완료되었습니다')



#파일 입출력
'''
open(파일명, 열기 모드, encoding=“인코딩”)

r : read (읽기)
w : write (쓰기)
a : append (이어서 쓰기)
'''
f = open('test.txt', 'w', encoding='utf-8')
f.write('하이\n')
f.write('하이\n')
f.write('하이\n')
f.close() # 파일 닫기

f = open('test.txt', 'r', encoding='utf-8')
contents = f.read() # 파일 내용 다 읽어오는 함수
print(contents)

for line in f:
    print(line, end = '') # 기본값은 줄바꿈임
f.close()


#with
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('ddd')
f.close()