import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/sgua0/Downloads/학업성취도.xlsx', header=0)
df.drop(['구분'], axis=1, inplace=True)

print(df.head())

# 필요한 열 선택
df = df[['영역', '평균', 'PISA 2018']]

# '영역' 열에서 결측값 채우기
df['영역'].fillna(method='ffill', inplace=True)

# '읽기', '수학', '과학' 행만 선택
df = df[df['영역'].isin(['읽기', '수학', '과학'])]

# 막대그래프를 위한 데이터 재구성
df_pivot = df.pivot(index='영역', columns='평균', values='PISA 2018')

plt.rc('font', family='Malgun Gothic')


# 데이터 확인
print(df_pivot)

# 막대그래프 그리기
df_pivot.plot(kind='bar', figsize=(10, 6))


plt.title('영역별 OECD 평균과 한국 평균 비교 (PISA 2018)')
plt.xlabel('영역')
plt.ylabel('PISA 점수')
plt.xticks(rotation=0)
plt.legend(title='평균')
plt.show()