import pandas as pd

# CSV 파일을 읽어들임
file_path = 'C:/Users/pjh74/OneDrive/바탕 화면/quit.csv'
data = pd.read_csv(file_path)

# 첫 5개 열만 유지하고, 필요없는 행을 제거
cleaned_data = data.iloc[2:, :5]

# 열 이름을 지정
cleaned_data.columns = ['연도', '전체', '초등학교', '중학교', '고등학교']

# '연도' 열을 숫자형으로 변환
cleaned_data['연도'] = pd.to_numeric(cleaned_data['연도'], errors='coerce')

# 2017년부터 2021년까지의 데이터 필터링
filtered_data = cleaned_data[(cleaned_data['연도'] >= 2017) & (cleaned_data['연도'] <= 2021)]
filtered_data['연도'] = filtered_data['연도'].astype(int)

# 인덱스 재설정
filtered_data.reset_index(drop=True, inplace=True)




import matplotlib.pyplot as plt


# 'Overall' 열을 제외하고 'Year'를 인덱스로 설정합니다.
visualization_data = filtered_data.drop(columns=['전체']).set_index('연도')

# 그래프를 그리기 위한 한글 폰트 설정 (여기서는 기본적으로 있는 한글 폰트를 사용합니다.)
plt.rc('font', family='Malgun Gothic')

visualization_data['초등학교'] = pd.to_numeric(visualization_data['초등학교'], errors='coerce')
visualization_data['중학교'] = pd.to_numeric(visualization_data['중학교'], errors='coerce')
visualization_data['고등학교'] = pd.to_numeric(visualization_data['고등학교'], errors='coerce')

# 막대 그래프를 그립니다.
visualization_data.plot(kind='bar', figsize=(10, 6), width=0.8)
# 그래프의 제목과 레이블을 설정합니다.
plt.title('연도별 초등학교, 중학교, 고등학교 학업 중단율 비교', fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('(%)', fontsize=14, rotation = 0)
plt.legend(title='학교 유형')
# colors = ['red', 'orange', 'green']

# for idx, column in enumerate(visualization_data.columns):
#     plt.bar(visualization_data.index, visualization_data[column], label=column, color=colors[idx])

# x축 레이블을 0도 회전하여 표시합니다.
plt.xticks(rotation=0)


# 그래프를 화면에 표시합니다.
plt.tight_layout()
plt.show()
