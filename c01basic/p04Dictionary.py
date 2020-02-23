# Dictionary 

dic1 = {1:"a"}
print(dic1)
dic1[2] = "ab"
print(dic1)

del dic1[1]
print(dic1)


# 딕셔너리 주의사항 
# 1. key-value 
# 2. key 는 항상 고유한 값 - 따라서 list 는 key 가 될 수 없고, tuple 은 key 값이 될 수 있다.
# ex) dic={[1,2]:"value"} X , dic={(1,2):"value"} O

dic2 = {"토요일":"청소", "일요일":"카페투어"}
print(dic2.keys())
for k in dic2.keys():
    print("키 모음 : {0}".format(k))

values = dic2.values()
print(values)
for v in values:
    print("values : {0}".format(v))

items = dic2.items()
print(items)

# dic2.clear()
# print(dic2)

print(dic2.get("토요일"))
# dic2["토요일"] == dic2.get("토요일")
# 없는 key 값으로 조회하려고 하면 리스트 인덱스 형은 error를, get() 는 None 을 반환 
print(dic2.get('foo', 'bar'))   # get(key, default:key가 없을 경우 default)   

# 해당 key 가 dictionary 안에 있는지 조사하기 : in
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('ph' in a)

