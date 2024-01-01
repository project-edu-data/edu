import pandas as pd
df = pd.read_excel('C:/Users/sgua0/Downloads/GDP 대비 공교육비 비율(2020).xlsx')


df.drop(['고등교육', '고등교육.1', '고등교육.2'], axis=1, inplace=True)

print(df.head())


