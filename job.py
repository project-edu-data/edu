import pandas as pd 
j = pd.read_csv("C:/Users/pjh74/OneDrive/바탕 화면/취업률.csv", encoding="utf-8", header=0)
j.drop([0,1,2,3,4,5,10,12,13], axis=0, inplace=True)

print(j)
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10, 6))
plt.plot(j['연도'], j['고등학교 졸업 후 \n취업률1)'], marker='o', label='고등학교')
plt.plot(j['연도'], j['대학 졸업 후 \n취업률4)'], marker='o', label='대학')
plt.plot(j['연도'], j['전문대학'], marker='o', label='전문대학')

plt.title('연도별 교육 수준에 따른 취업률')
plt.xlabel('연도')
plt.ylabel('취업률 (%)')
plt.ylim(0, 100)  # Y축 범위 설정
plt.legend()
plt.grid(True)
plt.show()

