import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
df = pd.read_excel('C:/Users/sgua0/Downloads/OECD 학생 1인당 공교육비(2020).xlsx')

print(df.head())

# 'x'를 NA로 대체하고 결측치 제거
df = df.replace('x', pd.NA).dropna()

# '구분' 컬럼을 제외하고 각 행의 합계 계산
df['Total'] = df.drop('구분', axis=1).sum(axis=1)

# 합계를 기준으로 데이터프레임 내림차순 정렬
df.sort_values(by='Total', ascending=True, inplace=True)

# 'Total' 컬럼은 그래프에 필요 없으므로 제거
df.drop('Total', axis=1, inplace=True)

# '구분' 컬럼을 인덱스로 설정
df.set_index('구분', inplace=True)

# 가로 막대 그래프 그리기
df.plot(kind='barh', stacked=True, figsize=(10, 6))
plt.title('OECD 학생 1인당 공교육비 (2020)')
plt.xlabel('1인당 공교육비')
plt.ylabel('')

# 그래프 보여주기
plt.show()



