import pandas as pd

path = './해양경찰청_연안사고 이력_20220630.csv'
df = pd.read_csv(path, encoding='cp949')
# 관할서별 연도별 사고 현황
# 관할서별 정보
df = df.loc[:,['발생일자','광역시도','사고유형']]

# 추락사고만 모으기
df = df[df['사고유형'].str.contains('추락')]

df['발생일자'] = pd.to_datetime(df['발생일자'], format='%Y-%m-%d')
dfm = df['발생일자'].dt.month
dff = df[(dfm >= 6) & (dfm <= 9)]
df_agg = dff.groupby('광역시도')['광역시도'].size()
df_new = pd.DataFrame({"광역시도": df_agg.index, "사고건수": df_agg.values})

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = 'C:/Users/정광원/AppData/Local/Microsoft/Windows/Fonts/SCDream5.otf'
font = fm.FontProperties(fname=font_path)
plt.rc('font',family=font.get_name())

colors = [
    '#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e',
    '#e377c2', '#17becf', '#f7b6d2', '#8c564b', '#7f7f7f',
    '#ff00ff', '#00ff00', '#008080', '#007ba7', '#ff8c00',
    '#ff69b4', '#32cd32', '#ffd700', '#006400'
]
plt.bar(df_new['광역시도'],df_new['사고건수'],color=colors)
plt.title("여름철 연안 추락사고 광역시별 건수(2017~2022)")
plt.xlabel("광역시도")
plt.xticks(rotation=45) 
plt.ylabel("건수")

for i in range(12):
        plt.text(df_new['광역시도'][i], df_new['사고건수'][i], str(df_new['사고건수'][i]), ha='center', va='bottom')
plt.show()