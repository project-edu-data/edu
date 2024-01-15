import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
# CSV 파일 불러오기
df = pd.read_csv('C:/Users/pjh74/OneDrive/바탕 화면/969fe518ad1fe87f.csv', encoding='cp949')

# 컬럼명 변경
df.rename(columns={'Unnamed: 0': 'Category'}, inplace=True)

# '평생직업교육'과 '교육일반'의 수치 합치기
other_sum = df[df['Category'].isin(['평생직업교육', '교육일반'])]['2023'].sum()

# '기타'로 묶어 새 행 추가
df = pd.concat([df, pd.DataFrame([{'Category': '기타', '2023': other_sum}])], ignore_index=True)

# 원래 '평생직업교육'과 '교육일반' 행 제거
df = df[~df['Category'].isin(['평생직업교육', '교육일반'])]

print(df.head())

categories = df['Category']
sizes = df['2023']

# 파이 차트 생성
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

# 타이틀 추가
plt.title('2023년 교육 예산 분포', fontdict={'fontname': 'Malgun Gothic'})

# 차트 보여주기
plt.show()
