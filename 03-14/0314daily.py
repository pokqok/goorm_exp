# -*- coding: utf-8 -*-
"""0314daily.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MawzWLU0tXQAVwE3s0k3Jt0NMH7txvfe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression

# 1. 데이터 생성
np.random.seed(42)  # 시드 입력
temperature = np.random.randint(15, 35, (30,))
humidity = np.random.randint(10, 50, (30,))
soil_moisture = np.random.randint(5, 40, (30,))
dates = pd.date_range(start="2024-02-01", periods=30, freq="D")

# 2. 데이터프레임 생성
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature,
    "Humidity": humidity,
    "Soil Moisture": soil_moisture
})

# 3. 모든 값이 25 이상인 날짜 찾기
valid_indices = np.where((temperature >= 25) & (humidity >= 25) & (soil_moisture >= 25))[0]
valid_days = df.iloc[valid_indices]

# 4. 시각화 (Matplotlib)
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Temperature"], label="Temperature (°C)", marker="o")
plt.plot(df["Date"], df["Humidity"], label="Humidity (%)", marker="s")
plt.plot(df["Date"], df["Soil Moisture"], label="Soil Moisture", marker="^")

plt.scatter(valid_days_df["Date"], valid_days_df["Temperature"], color="red", label="Valid Days", zorder=3) # valid days 강조하기

plt.xlabel("Date")
plt.ylabel("Sensor Values")
plt.title("Smart Farm Sensor Data Over 30 Days")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()

#  5. Plotly
fig = px.line(df, x="Date", y=["Temperature", "Humidity", "Soil Moisture"],
              title="Smart Farm Sensor Data (Interactive)", markers=True)
fig.add_scatter(x=valid_days_df["Date"], y=valid_days_df["Temperature"], mode="markers",
                marker=dict(color="red", size=10), name="Valid Days")
fig.show()

