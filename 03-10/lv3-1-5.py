import re

# 추출할 이메일
text = "아이우에오 example123@gmail.com"

# 정규표현식
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# findall을 사용한 이메일 주소 추출
emails = re.findall(email_pattern, text)
print(emails)
