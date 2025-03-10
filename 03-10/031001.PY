def unique_words(sentences: list) -> set:
    result = {}
    
    for day, word_list in sentences.items(): #입력받은 sentences의 day마다 반복을 돌린다
        wordset= set()
        for word in word_list:
            words = word.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split() #문장부호 제거, 공백 제거, 단어를 소문자로 바꾸는 작업을 한다
            wordset.update(words)
            result[day] = wordset
    
    return result

sentences = {
    'day1': [
        "Hello world, welcome to Python.",
        "Python is fun and Python is powerful.",
        "Hello everyone, have a great day!"
    ],
    'day2': [
        "How was your day?",
        "What's the weather like?",
        "I'm not busy. Take your time, please."
    ],
    'day3' : [
        "3",
        "3",
        "3"
    ]
}

word_results = unique_words(sentences)     #함수를 실행하고 day를 출력한다
for day, words in word_results.items():
    print(f"{day}:")
    print(f"{words}\n")