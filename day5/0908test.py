'''
https://leelang7.github.io/python/ml/dl/jumptopython-codinglicenseexam/

1. 문자열 바꾸기 다음과 같은 문자열이 있다.

a:b:c:d

문자열의 split와 join함수를 사용하여 위 문자열을 다음과 같이 고치시오.

a#b#c#d

2. 딕셔너리 값 추출하기 다음은 딕셔너리의 a에서 ‘C’라는 key에 해당하는 value를 출력하는 프로그램이다.

a = {‘A’:90, ‘B’:80} a[‘C’]

a딕셔너리에는 ‘C’라는 key가 없으므로 오류가 발생한다. ‘C’에 해당하는 key값이 없을 경우 오류대신 70을 얻을 수 있도록 수정하시오.

3. 리스트의 더하기와 extend 함수 다음과 같은 리스트가 있다.

a = [1, 2, 3]

리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3] a = a + [4, 5] print(a) >> [1, 2, 3, 4, 5]

리스트 a에 [4, 5]를 extend를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3] a.extend([4, 5]) print(a) >> [1, 2, 3, 4, 5]

+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.

4. 리스트 총합 구하기 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상 점수의 총합을 구하시오.

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

5. 피보나치 함수 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후에 이어지는 항은 이전의 두항을 더한 값으로 이루어지는 수열을 피보나치 수열이라고 한다.

0, 1, 1, 2, 3, 5, 8, 13 …

입력을 정수 n으로 받았을 때, n이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.

6. 숫자의 총합 구하기 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)

65, 45, 2, 3, 45, 8

7. 한 줄 구구단 사용자로부터 2~9까지의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오. 실행 예)

구구단을 출력할 숫자를 입력하세요(2~9): 2 2 4 6 8 10 12 14 16 18

8. 역순 저장

다음과 같은 내용의 파일 abc.txt가 있다.

AAA

BBB

CCC

DDD

EEE

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

EEE

DDD

CCC

BBB

AAA

9. 평균값 구하기

오른쪽 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

70

60

55

75

95

90

80

80

85

100

10. 사칙연산 계산기

다음과 같이 동작하는 클래스 Calculator를 작성하시오.

>>> cal1 = Calculator([1,2,3,4,5])
>>> cal1.sum() # 합계
15
>>> cal1.avg() # 평균
3.0
>>> cal2 = Calculator([6,7,8,9,10])
>>> cal2.sum() # 합계
40
>>> cal2.avg() # 평균
8.0
11. 모듈 사용 방법

C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 차이썬 셸을 열어 이 모듈을 import 해서 사용할 수 있는 방법을 모두 기술하시오.

>>> import mymod
>>>
12. 오류와 예외 처리

다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

result = 0
try:
    [1,2,3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
13. DashInsert 함수

DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되며 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.

입력 예시 : 4546793 출력 예시 : 454*67-9-3

14. 문자열 압축하기 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

입력 예시 : aaabbcccccca 출력 예시 : a3b2c6a1

15. Duplicate Numbers 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

입력 예시 : 0123456789 01234 01234567890 6789012345 012322456789 출력 예시 : true false false true false
'''

#1번 문제
str_list = 'a:b:c:d'
a = str_list.split(':')
print('#'.join(a))


# 2번 문제
a = {'A':90, 'B':80}
'''
try:
    print(a['C'])
except:
    a['C'] = 70
    print(a['C'])
'''
if a.get('C') == None:
    a['C'] = 70

print(a['C'])

# 3번 문제
#append()는 기존 리스트의 주소에 [4, 5]가 들어가고, + 연산자는 새로운 주소에 두 리스트를 합해서 넣음


# 4번 문제
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in A:
    if i >= 50:
        sum += i
print(sum)


# 5번 문제
num = int(input('숫자를 입력해주세요'))
'''
fn = 0
fn2 = 1
fn3 = 0
while fn <= num:
    fn3 = fn2
    fn2 += fn
    print(fn)
    fn = fn3
'''
'''
def fib(n):
    result = []
    a, b = 0,1
    while a <= n:
        result.append(a)
        a, b = b, a+b
    return result

n = int(input('입력: '))
print(fib(n))
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(input):
    print(fib(i))


# 6번 문제
'''
a = input('숫자들을 입력해주세요')
sum = 0
b = a.split(',')
for i in range(len(b)):
    sum += int(b[i])
print(sum)
'''
val = input('입력: ')
a = map(int,val.split(''))
result  = 0

# 7번 문제
a = int(input('구단을 출력할 숫자를 입력하세요(2~9): '))
for i in range(1, 10):
    print(a*i)


# 8번 문제
f = open('C:\ljs\day5\abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()


# 9번 문제
f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

f = open('result.txt', 'w')
f.write(str(average))
f.close


# 10번 문제
'''
class Calculator(list):

    def sum(list):
        result = 0
        for i in range(len(list)):
            result += list[i]
        print(result)

    def avg(list):
        result = 0
        for i in range(len(list)):
            result += list[i]
        print(result/len(list))
'''
class Calculator:
    def __init__(self, val):
        self.val = val

    def sum(self):
        sum = 0
        for i in self.val:
            sum += i
        return sum
        print(sum)

    def avg(self):
        avg = 0
        avg = self.sum() / int(len(self.val))
        print(avg)

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()


# 11번 문제


# 12번 문제
# 정답 : 7
# 인덱스 에러가 나기때문에 3
# 오류 상관없이 실행되는 4
# 3 + 4 = 7