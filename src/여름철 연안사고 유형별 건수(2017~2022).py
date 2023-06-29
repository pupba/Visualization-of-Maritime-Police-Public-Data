import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = 'C:/Users/정광원/AppData/Local/Microsoft/Windows/Fonts/SCDream5.otf'
font = fm.FontProperties(fname=font_path)
plt.rc('font',family=font.get_name())

import pandas as pd

path = './해양경찰청_연안사고 이력_20220630.csv'

df = pd.read_csv(path, encoding='cp949')
df = df.loc[:,['발생일자','사고유형']]
df['발생일자'] = pd.to_datetime(df['발생일자'], format='%Y-%m-%d')
dfm = df['발생일자'].dt.month
df_filtered = df[(dfm >= 6) & (dfm <= 9)]

# 사고유형을 묶어서 집계
grouped_categories = {
    '고립': ['고립', '고립익수'],
    '기타': ['기타', '기타익수'],
    '수상': ['수상레저익수', '수상산업익수'],
    '수중': ['수중레저익수', '수중산업익수'],
    '추락': ['추락', '추락익수'],
    '표류': ['표류']
}

# 사고유형을 묶어서 새로운 카테고리 열 생성
df_filtered['사고유형_묶음'] = df_filtered['사고유형'].apply(
    lambda x: next((key for key, values in grouped_categories.items() if x in values), x))
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e']
df_agg = df_filtered.groupby('사고유형_묶음').size()
df_new = pd.DataFrame({"사고유형": df_agg.index, "사고건수": df_agg.values})
plt.bar(df_new['사고유형'],df_new['사고건수'],color=colors)
plt.title("여름철 연안사고 유형별 건수(2017~2022)")
plt.xlabel("사고유형")
plt.ylabel("건수")

for i in range(6):
        plt.text(df_new['사고유형'][i], df_new['사고건수'][i], str(df_new['사고건수'][i]), ha='center', va='bottom')
plt.show()