import pandas as pd 
pe = pd.read_csv("C:/Users/pjh74/OneDrive/바탕 화면/사교육데이터.csv", encoding="utf-8", header=1)
pe= pe.iloc[2:18, 0:9]

pe.drop(["Unnamed: 1", "Unnamed: 2"], axis=1, inplace=True)
pe.rename(columns={'Unnamed: 0': '연도', 'Unnamed: 3': '초등참여율', 'Unnamed: 4': '초등참여시간', 'Unnamed: 5': '중등참여율', 'Unnamed: 6': '중등참여시간',
                     'Unnamed: 7': '고등참여율', 'Unnamed: 8': '고등참여시간'}, inplace=True)

pe.reset_index(drop=True, inplace=True)
pe.drop([0,1,2,3,4,5,6,7,8,9,10], axis=0, inplace=True)
pe.reset_index(drop=True, inplace=True)


# print(pe)
pe_1 = pe[["연도", "초등참여율", "중등참여율", "고등참여율"]]
pe_2 = pe[["연도", "초등참여시간", "중등참여시간", "고등참여시간"]]

pe_2['초등참여시간'] = pd.to_numeric(pe_2['초등참여시간'], errors='coerce')
pe_2['중등참여시간'] = pd.to_numeric(pe_2['중등참여시간'], errors='coerce')
pe_2['고등참여시간'] = pd.to_numeric(pe_2['고등참여시간'], errors='coerce')

pe_1['초등참여율'] = pd.to_numeric(pe_1['초등참여율'], errors='coerce')
pe_1['중등참여율'] = pd.to_numeric(pe_1['중등참여율'], errors='coerce')
pe_1['고등참여율'] = pd.to_numeric(pe_1['고등참여율'], errors='coerce')

# print(pe_1)
# print(pe_2)

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

# 이미 적용된 열 이름을 사용하여 그래프를 그립니다.
plt.figure(figsize=(10,5))

# 선 그래프 그리기
plt.plot(pe_1['연도'], pe_1['초등참여율'], marker='o', label='초등참여율')
plt.plot(pe_1['연도'], pe_1['중등참여율'], marker='s', label='중등참여율')
plt.plot(pe_1['연도'], pe_1['고등참여율'], marker='^', label='고등참여율')

# 그래프 제목 및 축 레이블 설정
plt.title('연도별 사교육 참여율')
plt.xlabel('연도')
plt.ylabel('참여율 (%)')

# 범례 표시
plt.legend()

# 그래프에 격자 표시
plt.grid(True)

# 그래프 보여주기
plt.show()



# plt.figure(figsize=(10,5))

# # 선 그래프 그리기
# plt.plot(pe_2['연도'], pe_2['초등참여시간'], marker='o', label='초등참여시간')
# plt.plot(pe_2['연도'], pe_2['중등참여시간'], marker='s', label='중등참여시간')
# plt.plot(pe_2['연도'], pe_2['고등참여시간'], marker='^', label='고등참여시간')

# # 그래프 제목 및 축 레이블 설정
# plt.title('연도별 사교육 참여시간')
# plt.xlabel('연도')
# plt.ylabel('참여시간')

# # 범례 표시
# plt.legend()

# # 그래프에 격자 표시
# plt.grid(True)

# # 그래프 보여주기
# plt.show()