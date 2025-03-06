animals = ['닭', '소', '돼지']

legs = int(input("다리는 몇 개입니까?: "))
childs = input("새끼가 2마리 이상입니까?(True/False): ") == "True"
foods = input("초식입니까, 잡식입니까?(초식/잡식): ")

if legs == 2:
    print("닭")

elif legs == 4 and childs and foods == "잡식":
    print("돼지가 분명합니다") 

elif legs == 4 and childs and foods == "초식":
    print("소가 분명합니다") 

elif legs == 4 and childs:
    print("소 또는 돼지입니다")
