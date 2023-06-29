import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = 'C:/Users/정광원/AppData/Local/Microsoft/Windows/Fonts/SCDream5.otf'
font = fm.FontProperties(fname=font_path)
plt.rc('font',family=font.get_name())

import pandas as pd

path = './해양경찰청_연안사고 이력_20220630.csv'
df = pd.read_csv(path, encoding='cp949')
df_ = df.loc[:,['발생일자','사고유형','사고원인']]
# 추락사고만 모으기
df_ = df_[df_['사고유형'].str.contains('추락')]
df_['발생일자'] = pd.to_datetime(df_['발생일자'], format='%Y-%m-%d')
dfm = df_['발생일자'].dt.month
df_filtered = df_[(dfm >= 6) & (dfm <= 9)]
df_agg = df_filtered.groupby('사고원인')['사고원인'].size()
df_new = pd.DataFrame({"사고원인": df_agg.index, "사고건수": df_agg.values})

colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e', '#e377c2', '#17becf', '#f7b6d2', '#8c564b', '#7f7f7f']
plt.bar(df_new['사고원인'],df_new['사고건수'],color=colors)
plt.title("여름철 연안 추락사고 원인별 건수(2017~2022)")
plt.xlabel("사고원인")
plt.xticks(rotation=45) 
plt.ylabel("건수")

for i in range(10):
        plt.text(df_new['사고원인'][i], df_new['사고건수'][i], str(df_new['사고건수'][i]), ha='center', va='bottom')
plt.show()