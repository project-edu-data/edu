import pandas as pd

data = pd.read_excel('C:/Users/sgua0/Downloads/OECD_1_2021.xlsx', header=0)

print(data.head())

import matplotlib.pyplot as plt


data = data.replace('x', pd.NA).dropna()

oecd_avg = data[data['Unnamed: 0'] == 'OECD 평균']
countries = data[data['Unnamed: 0'] != 'OECD 평균']

countries[['초등학교 과정', '중학교 과정', '고등학교 과정']] = countries[['초등학교 과정', '중학교 과정', '고등학교 과정']].apply(pd.to_numeric)

plt.figure(figsize=(15, 8))

plt.rc('font', family='Malgun Gothic')

for i, column in enumerate(['초등학교 과정', '중학교 과정', '고등학교 과정'], 1):
    plt.subplot(1, 3, i)
    bar_colors = ['navy' if country == '한국' else 'skyblue' for country in countries['Unnamed: 0']]
    plt.bar(countries['Unnamed: 0'], countries[column], color=bar_colors)
    plt.axhline(y=oecd_avg[column].values[0], color='r', linestyle='--')
    plt.title(column)
  

plt.tight_layout()

plt.show()