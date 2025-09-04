# Q1. 홍길동의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수는?

# 국어 - 80, 영어 -75, 수학 - 55

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법?

# Q3. 홍길동의 주민등록번호는 881120-1068234이다. 홍길동의 주민등록번호를 연원일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.

# Q4. 주민등록번호 뒷자리(Q3의 주민등록번호 사용)의 맨 첫 번째 숫자는 성별을 나타낸다. 성별을 나타내는 숫자를 출력해보자.

# Q5. 다음과 같은 문자열 a:b:c:d:가 있다. 문자열의 replace함수를 이용하여 a#b#c#d로 바꿔보자.

# Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.(Hint : sort() 함수와 reverse() 함수)

# Q7. [‘Life’, ‘is’, ‘too’, ‘short’] 리스트를 Life is too short 문자열로 만들어 출력해 보자.(Hint : join()함수)

# Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

# Q9. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.

# a[‘name’] = ‘python’

# a[(‘a’,)] = ‘python’

# a[[1]] = ‘python’

# a[250] = ‘python’

# Q10. 딕셔너리 a에서 ‘B’에 해당되는 값을 추출해 보자.

# >>> a = {'A':90, 'B':80, 'C':70}
# Q11. a 리스트에서 중복 숫자를 제거해 보자.

# >>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

# >>> a = b = [1, 2, 3]
# >>> a[1] = 4
# >>> print(b)

#  [1, 4, 3]



#1번 문제
kildong_score = {'국어':80, '영어':75, '수학':55}
avg = (kildong_score['국어'] + kildong_score['영어'] + kildong_score['수학'])/len(kildong_score)
print(f'평균: {avg}')

#2번 문제
if 13 % 2 == 0:
    print('짝수')
else:
    print('홀수')

#3번 문제
kildong_num = '881120-1068234'
print(f'앞자리: {kildong_num[:6]}')
print(f'뒷자리: {kildong_num[7:]}')
'''
print(kildong_num.split('-'))
'''

#4번 문제
print(f'뒷자리 첫번째: {kildong_num[7]}')

#5번 문제
abcd_str = 'a:b:c:d'
print(abcd_str.replace(':', '#'))

#6번 문제
num_list = [1,3,5,4,2]
num_list.sort()
num_list.reverse()
print(num_list)

#7번 문제
str_list = ['Life', 'is', 'too', 'short']
print(' '.join(str_list))

#8번 문제
num_tuple = (1,2,3)
num_list = list(num_tuple)
num_list.append(4)
num_tuple = tuple(num_list)
print(num_tuple)
'''
num_tuple = (1,2,3)
num_tuple2 = (4,)
priny(num_tuple + num_tuple2)
'''

#9번 문제
a = {}
a['name'] = 'python'

a[('a',)] = 'python'

#a[[1]] = 'python' # 딕셔너리의 키는 변경 불가능 해야하는데 리스트는 변경 가능한 자료형이기 때문에

a[250] = 'python'
print(a.items())

#10번 문제
a = {'A':90, 'B':80, 'C':70}
print(a['B'])

#11번 문제
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
dic_a = dict.fromkeys(a)
a = list(dic_a)
print(a)
'''
print(set(a))
'''

#12번 문제
a = b = [1, 2, 3]
a[1] = 4
print(b)
#a와 b는 같은 객체를 참조하기 때문에 (메모리 주소가 같기 때문에)