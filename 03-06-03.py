animals = ['닭', '소', '돼지']

find = input("찾는 가축을 입력하세요: ") 

if find in animals:
    print("{}, 있습니다!".format(find))
else:
    print("{}.. 없습니다...".format(find))
