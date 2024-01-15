import pandas as pd

df = pd.read_excel('C:/Users/sgua0/Downloads/학생수.xlsx', skiprows=1)

print(df.head())



import matplotlib.pyplot as plt




df['연도'] = df['연도'].astype(str)

df.set_index('연도', inplace=True)

plt.figure(figsize=(15, 5))  

plt.rc('font', family='Malgun Gothic')


for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)


plt.title('학급당 학생수')
plt.xlabel('연도')
plt.ylabel('학생수')


plt.legend()


plt.grid(True)


plt.tight_layout()
plt.show()

