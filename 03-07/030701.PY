farms = ['제일농장', '우리농장', '한국농장']
animals = ['닭', '소', '돼지']

제일농장 = [100, 50, 80]
우리농장 = [50, 10, 20]
한국농장 = [200, 100, 150]

farm_data = {
    '제일농장': 제일농장,
    '우리농장': 우리농장,
    '한국농장': 한국농장
}

for farm in farms :
    print(f"***** {farm} *****")
    for animal, i in zip(animals, farm_data[farm]) :
        print(f"{animal}: {i}마리 입니다.")