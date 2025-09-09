'''
https://drive.google.com/drive/folders/1a4P85aQsDoKFsjfzEnoMba6Ivm-44KeI?usp=sharing
'''
#변수
a = 10000
b = 20000
c = '안녕하세요'

print(a)
print(b)
print(c)

name = 10
_name = 123
name1= 20
# 변수는 숫자로 시작할 수 없음
# 공백이나 특수문자 사용 안됨
# 대소문자 구분함


#타입 변환
test = int(float('2.5'))
print(test)


#연산자
print(5+2)
print(5/2)
print(5%2) # 나머지
print(5//2) # 몫
print(5**2) # 제곱
print(5>2)
print(5>+2)
print(5<2)
print(5<=2)
print(5==2)
print(5!=2)
print(3<5 and 7<5)
print(3<5 or 7<5)
print(not 3<5)
print('c' in 'cat')
print('c' not in 'cat')


#주석처리
print('hello1')
#print('hello2') # 주석처리된 곳은 실행했을때 나오지 않음
print('hello3')

'''
print('hello1')
print('hello2')
'''
print('hello3')


#인덱스
lang = 'PYTHON'
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])
print(lang[-1]) # -1은 마지막 인덱스
print(lang[-3]) # -3은 마지막에서 3번째 인젝스


#슬라이싱
print(lang[1:3]) #[start:end] (end의 바로 전 인덱스 까지)
print(lang[:3]) #아무것도 안넣으면 start에는 처음부터 end에는 마지막 까지



#문자열 처리
snack = '꿀꽈배기'
two = '2개' # 문자와 정수는 더할 수 없다
juseyo = snack + two
juseyo += ' 주세요' # juseyo += '주세요' = juseyo = juseyo + '주세요'
print(juseyo + ' 더주세요')

print(len(snack)) # len은 길이를 알려주는 함수

a = '''꿀꽈배기는
너무
맛있어요
'''
print(a)

print('-' * 10)
print('반가워요')
print('-' * 10)



#메소드 (클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음)
letter = 'how are YOU?'
print(letter.lower()) # lower()는 소문자로 바꿔주는 함수 //함수뒤에는 ()를 붙여줘야함
print(letter.upper()) # upper()는 대문자로 바꿔주는 함수
print(letter.capitalize()) # capitalize는 첫 글자만 대문자로 바꿔주는 함수
print(letter.title()) # 각 단어들의 첫 글자만 대문자로 바꿔주는 함수
print(letter.swapcase()) # 대소문자를 서로 바꿔주는 함수
print(letter.split()) # 문자열을 나눠서 리스트에 저장 (공백을 기준으로 나눔)
print(letter.count('how')) # 해당 문자열이 몇번 쓰였는지 알려주는 함수

s = '나도 고등학교'
print(s.startswith('나도')) # 해당 문자로 시작을 하는지 알려주는 함수
print(s.endswith('초등학교')) # 해당 문자로 끝나는지 알려주는 함수
d = '...나도 고등학교...'
print(d.strip('.')) # 문자열 앞, 뒤에 해당 문자들를 제거하는 함수
print(d.lstrip('.')) # 문자열 왼쪽에 해당 문자들을 제거하는 함수
print(d.rstrip('.')) # 문자열 오른쪽에 해당 문자들을 제거하는 함수
print(s.replace('고등학교', '고교')) # 앞의 문자열을 뒤에 문자열로 교체하는 함수
print(s.find('학교')) # 해당 문자열이 몇번 인덱스에 있는지 알려주는 함수
print(s.center(20, '-')) # 20의 공간안에 s의 문자열을 가운데로하고 앞, 뒤로 -를 채움



#문자열 포멧
python = '파이썬'
java = '자바'
print(python+' '+java) # =print(python, java) (,를 사용하면 공백이 하나 생김)

print('개발언어에는 {},  {}'.format(python, java))
print('개발언어에는 {1},  {0}'.format(python, java)) # 인덱스를 정할 수 있음

print(f'개발언어에는 {python}, {java}가 있어요') # (f-string)



#탈출문자
print('친구가 "파이썬 배우기 쉬워?" 하고 물었다') # ' '안에는 " "를 쓸 수 있다 (반대로 " "안에 ' '도 쓸 수 있음) (안에 있는것이 문자열로 출력됨)

#print('나는 속으로 '엄청 어려운데...'라고 생각했다') # 같으면 안됨 (' '안에 ' '라거나 " " 안에 " "는 안됨)
print('나는 속으로 \'엄청 어려운데...\'라고 생각했다') # \'를 사용하면 가능함

print('\\') # \\를 쓰면 \를 출력 가능

print(r'C:\ljs\day1\python0902.py') # 주소 경로의 경우 앞에 r을 써서 주소를 출력 가능 (raw string)

print('꿀꽈배기는\n너무\n맛있어요') # \n 는 줄바꿈
print('''꿀꽈배기는
너무
맛있어요''') # 이렇게도 됨