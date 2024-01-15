import pandas as pd 
et = pd.read_csv("C:/Users/pjh74/OneDrive/바탕 화면/4-5. 학습시간.csv", header=2)
et= et.iloc[5:10, 0:8]
et.reset_index(drop=True, inplace=True)
et["1시간 이상"] = et["1~2시간"] + et["2~3시간"]
et["3시간 이상"] = et["3~4시간"] + et["4~5시간"]
et["5시간 이상"] = et["5~6시간"] + et["6시간 이상"]
et.drop(["1~2시간", "2~3시간", "3~4시간", "4~5시간", "5~6시간", "6시간 이상"], axis=1, inplace=True)
print(et)
et_2022 = et.iloc[4]
print(et_2022)

import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

# et_2022에서 값과 라벨 추출
values = et_2022[1:].values  # 첫 번째 열(연도)를 제외한 나머지 값들
labels = et_2022.index[1:]  # 첫 번째 열(연도)를 제외한 나머지 라벨들

# 파이 차트 생성
plt.pie(values, labels=labels, autopct='%1.1f%%')

# 동그란 모양 유지
plt.axis('equal')

# 차트 제목 설정
plt.title('2022년 학습 시간')

# 차트 보여주기
plt.show()
