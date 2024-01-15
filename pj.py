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

print(filtered_data.head())
print(filtered_data.info())