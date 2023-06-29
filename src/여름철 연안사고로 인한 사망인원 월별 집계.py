import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = 'C:/Users/정광원/AppData/Local/Microsoft/Windows/Fonts/SCDream5.otf'
font = fm.FontProperties(fname=font_path)
plt.rc('font',family=font.get_name())

import pandas as pd

path = './연안사고 현황_20211231.xlsx'

df = pd.read_excel(path)
df_ = df.loc[:,["발생일자","사망인원"]]
df_month = df_['발생일자'].dt.month
df_month_ = df_month[(df_month >= 6) & (df_month <= 9)]
df_monthly_death = df.groupby(df_month_)["사망인원"].sum()
df_new = pd.DataFrame({"발생일자": df_monthly_death.index, "사망인원": df_monthly_death.values})
df_monthly_death = df_new.astype('int')

plt.bar(df_monthly_death['발생일자'],df_monthly_death['사망인원'])
plt.title("여름철 연안사고로 인한 사망인원 월별 집계")
plt.xlabel("월")
plt.xticks(range(min(df_monthly_death['발생일자']),max(df_monthly_death['발생일자'])+1))
plt.ylabel("사망인원(명)")
plt.yticks(range(0,max(df_monthly_death['사망인원'])+1))
for i in range(4):
        plt.text(df_monthly_death['발생일자'][i], df_monthly_death['사망인원'][i], str(df_monthly_death['사망인원'][i]), ha='center', va='bottom')
plt.show()
