#클래스 (설계도) (인스턴스는 객체(물건)))
'''
class 클래스명:
    정의

변수 = 클래스명() # 객체
'''
class BlackBox:
    def __init__(self, name, price): # 객체를 생성할때 자동으로 호출됨
        self.name = name # self는 객체 자기 자신
        self.price = price # name, price는 맴버변수 라고함

    def set_travel_mode(self, min):
        print(str(min) + '분 여행모드 on')

b1 = BlackBox('까망이', 200000) # b1 BlackBox 객체
b2 = BlackBox('하양이', 100000) # b2 BlackBox 객체
#b1.name = '까망이' # . 으로 접근
#b2.name = '하양이'

print(b1.name, b1.price)
print(b2.name, b2.price)
print(isinstance(b1,BlackBox)) # b1객체가 BlackBox클래스의 객체가 맞는지 확인
'''
__func__ : 특정 조건이 만족되면 호출됨 (더블 언더 스코어)
매직메소드, 던더메소드 라고함
'''

b1.set_travel_mode(30)
b2.set_travel_mode(10)



#상속
class TravelBlackBox(BlackBox):
    def set_travel_mone(self, min):
        print(str(min) + '분 여행모드 on')



#super
'''class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        BlackBox.__init__(self, name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
'''
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        super().__init__(name, price) # BlackBox.__init__(self, name, price) 이걸 super()로 대체 가능
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')


#다중 상속
class BlackBox:
    def __init__(self, name, price): # 객체를 생성할때 자동으로 호출됨
        self.name = name # self는 객체 자기 자신
        self.price = price # name, price는 맴버변수 라고함

    def set_travel_mode(self, min):
        print(str(min) + '분 여행모드 on')

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')
      
class TravelBlackBox(BlackBox, VideoMaker, MailSender): # 여러개의 클래스를 상속 받을 수 있음
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

b1 = TravelBlackBox('하양이', 100000, 64)
b1.make() # > 결과 : 추억용 여행 영상 제작 (VideoMaker클래스의 make)
b1.send() # > 결과 : 메일 발송 (MailSender의 send)



#메소드 오버라이딩
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make() # 추억용 여행 영상 제작
        self.send() # 메일 발송
'''
자식 클래스에서 같은 메소드를 새로 정의하지 않으면
부모 클래스의 메소드를 사용하고
자식 클래스에서 같은 메소드를 새로 정의하면
자식 클래스의 메소드를 사용함
'''



#예외처리
'''
try:
    수행 문장 (에러가 발생할 가능성이 있는 문장)
except:
    에러 발생 시 수행 문장 (에러 상황이 발생했을 때만 수행할 문장)
else:
    정상 동작 시 수행 문장 (에러가 발생하지 않았을 때만 수행할 문장) (없어도됨)
finally:
    마지막으로 수행할 문장 (에러 여부 상관 없이 항상 수행되는 문장)
'''

try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다')

except ZeroDivisionError:
    print('0 으로 나눌 수 없어요')

except Exception as err:
    print('에러가 발생했어요 : ', err)
'''
num2 가 정수 0 이라면 > 실행 결과 : 0 으로 나눌 수 없어요

num2 가 문자열 '0' 이라면 > 실행 결과 : 값의 형태가 이상해요
'''