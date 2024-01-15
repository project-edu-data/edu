import pandas as pd 
en = pd.read_csv("C:/Users/pjh74/OneDrive/바탕 화면/진학률.csv", encoding="utf-8", header=1)
en= en.iloc[0:13, 0:4]
en.drop([0,1,2,3,4,5,6,7], axis=0, inplace=True)
en.drop(["Unnamed: 1"], axis=1, inplace=True)
en.reset_index(drop=True, inplace=True)
en.rename(columns={'Unnamed: 0': '연도', 'Unnamed: 2': '남자', 'Unnamed: 3': '여자'}, inplace=True)
print(en)

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 이미 적용된 열 이름을 사용하여 그래프를 그립니다.
plt.figure(figsize=(10,5))

# 선 그래프 그리기
plt.plot(en['연도'], en['남자'], marker='o', label='남자')
plt.plot(en['연도'], en['여자'], marker='s', label='여자')

# 그래프 제목 및 축 레이블 설정
plt.title('연도별 남녀 진학률 추세')
plt.xlabel('연도')
plt.ylabel('진학률 (%)')

# 범례 표시
plt.legend()

# 그래프에 격자 표시
plt.grid(True)

# 그래프 보여주기
plt.show()
