num = input("당신의 나이는?: ")

num = int(num)

if(num == 19) :
    print("[1] 당신은 올해 성년이 되셨군요!")
if(num != 19) :
    print("[2] 당신은 19세가 아닙니다.")
if(num >= 19) :
    print("[3] 당신은 19세 이상입니다.")
if(num > 19) :
    print("[4] 당신은 20세 이상입니다.")
if(num > 19 & num<30) :
    print("[5] 당신은 20대 입니다.")