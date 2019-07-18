import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

country=pd.read_csv("D:\Downloads\DP_LIVE_17072019162535290.csv",index_col=0)
df=country.head(5)
df=df.set_index(['TIME'])
sd=df.reindex(columns=['SUBJECT','Value'])
#db=sd.diff(axis=1)

sd.plot(kind='bar')
plt.show()
