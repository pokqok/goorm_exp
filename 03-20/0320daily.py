# -*- coding: utf-8 -*-
"""0320daily.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YMJAZWY9lnAcAy5gYo_0W6BO5xAmkIOX
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 폰트 설치 및 시스템 업데이트
!apt-get install fonts-nanum -qq > /dev/null
!apt-get install fontconfig -qq > /dev/null
!fc-cache -fv > /dev/null

# 폰트 경로 직접 지정
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'

# 폰트 매니저에 명시적으로 등록
fontprop = fm.FontProperties(fname=font_path, size=12)
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

products = ["노트북", "태블릿", "스마트폰", "스마트워치", "헤드폰"]
sales = [150, 80, 300, 120, 180]

plt.figure(figsize=(10,6))
plt.bar(products, sales, color='green')

plt.title("전자제품 판매량 비교", fontsize=15)
plt.xlabel("제품명", fontsize=12)
plt.ylabel("판매량", fontsize=12)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

companies = ["A사", "B사", "C사", "D사","E사", "F사"]
market_share = [40, 25, 15, 8, 7, 5]

# 가장 큰 값의 인덱스 찾기
max_index = market_share.index(max(market_share))

# 동적으로 explode 생성
explode = [0.1 if i == max_index else 0 for i in range(len(companies))]

# 10% 미만은 빈 문자열로 처리
def autopct_format(pct):
    return f'{pct:.1f}%' if pct >= 10 else ''

plt.figure(figsize=(10,7))
plt.pie(market_share,
        labels=companies,
        explode=explode,
        autopct=autopct_format,
        startangle=90)

plt.title("IT 기업 시장 점유율", fontsize=15)
plt.axis('equal')
plt.tight_layout()
plt.show()