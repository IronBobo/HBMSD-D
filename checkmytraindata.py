#去除不符合要求的数据并进行检验（第一问）
import numpy as np
import pandas as pd
from scipy import stats



df = pd.read_csv('mytraindata.csv')
df.drop(df[(df['speed']==0)&(df['occupancy']==0)&(df['volume']!=0)].index, inplace=True)
df.drop(df[(df['speed']==0)&(df['occupancy']!=0)&(df['volume']==0)].index, inplace=True)
df.drop(df[(df['speed']!=0)&(df['occupancy']==0)&(df['volume']==0)].index, inplace=True)
df.drop(df[(df['speed']!=0)&(df['occupancy']!=0)&(df['volume']==0)].index, inplace=True)
df.drop(df[(df['speed']==0)&(df['occupancy']!=0)&(df['volume']!=0)].index, inplace=True)
df.drop(df[(df['speed']!=0)&(df['occupancy']==0)&(df['volume']!=0)].index, inplace=True)
print('速度')
df2 = df['speed'].var()
df3 = df['speed'].mean()
print(df2)
if(df2!=0):
    print('方差不为0')
print('均值')
print(df3)
print('夏皮罗维尔克检验法检验是否正态分布')
print(stats.shapiro(df['speed']))
print('科尔莫戈罗夫检验法检验是否正态分布')
print(stats.kstest(df['speed'],'norm'))
#speed
print('流量')
df4 = df['volume'].var()
df5 = df['volume'].mean()
print(df4)
if(df2!=0):
    print('方差不为0')
print('均值')
print(df5)
print('夏皮罗维尔克检验法检验是否正态分布')
print(stats.shapiro(df['volume']))
print('科尔莫戈罗夫检验法检验是否正态分布')
print(stats.kstest(df['volume'],'norm'))
    #print(data.speed[0])
#volume
print('占用率')
df6 = df['occupancy'].var()
df7 = df['occupancy'].mean()
print(df6)
if(df2!=0):
    print('方差不为0')
print('均值')
print(df7)
print('夏皮罗维尔克检验法检验是否正态分布')
print(stats.shapiro(df['occupancy']))
print('科尔莫戈罗夫检验法检验是否正态分布')
print(stats.kstest(df['occupancy'],'norm'))
#occupancy
print('速度和流量的方差齐性检验')
print(stats.levene(df['speed'], df['volume']))
print('速度和占用率的方差齐性检验')
print(stats.levene(df['speed'], df['occupancy']))
print('流量和占用率的方差齐性检验')
print(stats.levene(df['volume'], df['occupancy']))
df.loc[df.speed>85,'speed'] = 56.8433784
df.loc[df.volume>211,'volume'] = 59.45491658
df.loc[df.occupancy>52.7,'occupancy'] = 8.698326226

#df.to_csv('mytraindataofcheck.csv')
    #print(df)

