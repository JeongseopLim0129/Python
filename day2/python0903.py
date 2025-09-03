# #리스트
# my_list = ['a', 'b', 'c']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

# my_list[1] = 'bbb' # 해당 인덱스의 값 변경
# print(my_list)
# my_list.append('eee') # 리스트 마지막에 해당 값 추가
# print(my_list)
# my_list.remove('eee') # 해당 값을 리스트에서 제거
# print(my_list)
# your_list = [4,5]
# my_list.extend(your_list) #리스트에 해당 리스트를 더함
# print(my_list)



# #튜플 (추가, 삭제, 수정이 불가함 (패킹돼있다)) (읽기 전용 리스트)
# my_tuple = ('a', 'b', 'c') # 차원(가로, 세로, 높이)에서 많이 씀
# print(my_tuple)
# (pie1, pie2, pie3) = my_tuple # 언패킹
# print(pie1)
# print(pie2)
# print(pie3)

# numbers = (1,2,3,4,5,6,7,8,9,10)
# (one, two, *others) = numbers # *를 사용한 others는 리스트로 생성됨
# print(one)
# print(two)
# print(others)
# (one, *others, ten) = numbers
# print(one)
# print(others)
# print(ten)



# #세트 (중복x, 순서x, 접근x)
# a = {1,2,3}
# b = {3,4,5}
# print(a.intersection(b)) # 교집합 출력
# print(a.union(b)) # 합집합 출력
# print(a.difference(b)) # 차집합 출력

# a.add(4) # 세트 마지막에 해당 값 추가
# print(a)
# a.remove('3') # 해당 값을 세트에서 삭제
# print(a)
# a.clear() # 세트내의 모든 값 삭제
# print(a)
# del a # 해당 세트 자체를 삭제함


# #딕셔너리 (키, 밸류가 있음, 중복x)
# person = {'이름':'홍길동', '나이':20, '키':180}
# print(person['이름'])
# print(person['나이'])
# print(person['키'])

# print(person.get('별명')) # 해당 키의 밸류가 있으면 출력, 없으면 None
# person['별명'] = '바보' # 딕셔너리 마지막에 해당 값 추가
# print(person)
# person['키'] = 130 # 값 변경
# print(person)
# person.update({'키':130, '나이':30}) # 여러 값을 한번에 바꿀 수 있음
# print(person)
# person.pop('이름') # 해당 키와 밸류를 삭제
# print(person)
# person.clear() # 딕셔너리 내의 모든 키와 밸류를 삭제
# print(person)
# print(person.keys()) # 어떤 키들이 있는지 출력
# print(person.values()) # 어떤 밸류들이 있는지 출력
# print(person.items()) # 어떤 키와 밸류들이 있는지 출력


my_list = ['a', 'b', 'c', 'd', 'd']
# my_set = set(my_list) # 중복을 제거할 수 있음
# my_list = list(my_set)
# print(my_list)

my_dic = dict.fromkeys(my_list) # 중복도 제거하고 순서도 그대로임
my_list = list(my_dic)
print(my_list)
