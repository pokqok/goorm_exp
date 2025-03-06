scores_data = '''
학생1: 홍길동, 성적: 85
학생2: 김철수, 성적: 90
학생3: 이영희, 성적: 78
학생4: 박민지, 성적: 92
학생5: 최준호, 성적: 88
'''
students = []
scores = []

for person in scores_data.strip().split("\n") :
    parts = person.split(", ")
    name = parts[0].split(": ")[1]
    score = int(parts[1].split(": ")[1])

    students.append((name, score))
    scores.append(score)

print(students)

avg = sum(scores) / len(scores)
print(f"평균은 {avg}")