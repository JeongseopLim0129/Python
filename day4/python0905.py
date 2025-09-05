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
