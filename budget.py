import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv('C:/Users/sgua0/Downloads/연도별 교육예산 추이.csv', encoding='utf-8')
df = pd.read_csv('C:/Users/sgua0/Downloads/연도별 교육예산 추이.csv', encoding='cp949')

# '평생직업교육'과 '교육일반'의 수치 합치기
other_sum = df[df['Unnamed: 0'].isin(['평생직업교육', '교육일반'])]['2023'].sum()

# '기타'로 묶어 새 행 추가
df = df.append({'Unnamed: 0': '기타', '2023': other_sum}, ignore_index=True)

# 원래 '평생직업교육'과 '교육일반' 행 제거
df = df[~df['Unnamed: 0'].isin(['평생직업교육', '교육일반'])]

print(df.head())

categories = df['Unnamed: 0']
sizes = df['2023']

plt.rc('font', family='Malgun Gothic')


# 파이 차트 생성
plt.figure(figsize=(8, 8))  # 차트의 크기 설정
plt.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # 차트를 원형으로 만듭니다.

# 타이틀 추가
plt.title('2023년 교육 예산 분포')

# 차트 보여주기
plt.show()
