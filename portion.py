# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_excel('C:/Users/pjh74/OneDrive/바탕 화면/GDP_2020.xlsx')


# print(df.head())

# # 모든 컬럼의 합을 새로운 컬럼으로 추가
# df['Total'] = df.sum(axis=1)

# # 새로운 컬럼 'Total'을 기준으로 내림차순 정렬
# df.sort_values(by='Total', ascending=True, inplace=True)

# # 'Total' 컬럼은 그래프에 필요 없으므로 제거
# df.drop('Total', axis=1, inplace=True)

# # 데이터프레임의 인덱스를 설정 (가정: 첫 번째 컬럼이 인덱스에 해당)
# df.set_index('Unnamed: 0', inplace=True)

# # 가로 막대 그래프 그리기
# plt.figure(figsize=(15, 8))
# plt.rc('font', family='Malgun Gothic')
# df.plot(kind='barh', stacked=True)
# plt.title('공교육비 비율')
# plt.ylabel('')

# # 범례 설정
# legend_labels = ['초등·중등·중등후비고등교육', '고등교육']
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# # 그래프 보여주기
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
# Excel 파일 불러오기
df = pd.read_excel('C:/Users/pjh74/OneDrive/바탕 화면/GDP_2020.xlsx')

# 첫 번째 컬럼의 이름 변경
df.rename(columns={df.columns[0]: 'Country'}, inplace=True)

# 모든 숫자 컬럼의 합을 새로운 컬럼으로 추가
df['Total'] = df.select_dtypes(include=['number']).sum(axis=1)

# 'Total' 컬럼을 기준으로 내림차순 정렬
df.sort_values(by='Total', ascending=False, inplace=True)

# 'Total' 컬럼 제거
df.drop('Total', axis=1, inplace=True)

# 'Country' 컬럼을 인덱스로 설정
df.set_index('Country', inplace=True)

# 가로 막대 그래프 그리기
plt.figure(figsize=(15, 8))
df.plot(kind='barh', stacked=True, ax=plt.gca())
plt.gca().set_title('공교육비 비율', fontdict={'fontname': 'Malgun Gothic'})
plt.gca().set_ylabel('')

# 범례 설정
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# 그래프 보여주기
plt.show()
