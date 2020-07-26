#将多个csv文件连接成一个文件
import pandas as pd

df1 = pd.read_csv('mytraindataofcheck1.csv')
df2 = pd.read_csv('mytraindataofcheck2.csv')
df3 = pd.read_csv('mytraindataofcheck3.csv')
df4 = pd.read_csv('mytraindataofcheck4.csv')
df5 = pd.read_csv('mytraindataofcheck5.csv')
df6 = pd.read_csv('mytraindataofcheck6.csv')

print(pd.concat([df1,df2,df3,df4,df5,df6],axis=0))
data = pd.concat([df1,df2,df3,df4,df5,df6],axis=0)
data.to_csv('mytraindataofcheck.csv',index=False)


