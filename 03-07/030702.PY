menu = [     ("Pizza", 12000),     ("Burger", 8000),     ("Pasta", 15000),     ("Sushi", 20000),     ("Salad", 6000) ]
print(f"메뉴판: ") #메뉴판 출력
for i , (name, price) in enumerate(menu) :
    print(f"{i+1}. {name} - {price:,}원") 

user_menu = input("메뉴를 입력하세요(,로 구별)\n").split(",") # 메뉴 입력받기
user_menu = [item.strip().capitalize() for  item in user_menu] # input에 바로 strip을 쓰면 적용이 안된다. 따로 strip과 capitalize

ok_menu = [item for item in user_menu if item in [m[0] for m in menu]] # 가능한 메뉴와 안되는 메뉴를 따로 만든다
no_menu = [item for item in user_menu if item not in [m[0] for m in menu]]

if no_menu : # 없는 메뉴 모아서 출력
    print(f"{', '. join(no_menu)}은(는) 없는 메뉴입니다.")

total_price = 0
print("\n 주문 내역: \n") # 주문내역을 ok_menu에서 출력하고 menu와 비교해서 총 가격을 계산
for item in ok_menu :
    for name, price in menu:
        if item == name :
            print(f"{name}: {price:,}원")
            total_price += price

print(f"총 가격은 {total_price:,}원 입니다.")