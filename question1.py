#第一问将数据按照日期进行分割
import numpy as np
import pandas as pd


st = ['2009-01-01','2009-01-02','2009-01-03','2009-01-04','2009-01-05','2009-01-06','2009-01-07','2009-01-08','2009-01-09','2009-01-10','2009-01-11','2009-01-12','2009-01-13','2009-01-14','2009-01-15','2009-01-16','2009-01-17','2009-01-18','2009-01-19','2009-01-20','2009-01-21','2009-01-22','2009-01-23','2009-01-24','2009-01-25','2009-01-26','2009-01-27','2009-01-28','2009-01-29','2009-01-30']
st2 = ['1.csv','2.csv','3.csv','4.csv','5.csv','6.csv','7.csv','8.csv','9.csv','10.csv','11.csv','12.csv','13.csv','14.csv','15.csv','16.csv','17.csv','18.csv','19.csv','20.csv','21.csv','22.csv','23.csv','24.csv','25.csv','26.csv','27.csv','28.csv','29.csv','30.csv']
data = pd.read_csv('data 1.csv')
df=data.set_index('starttime',drop=True)
#df.to_csv('time.csv')


#cols = data.columns
#m = data.loc[0, 'speed']
#error = data[data.speed>120]
#data.drop_duplicates('starttime', 'first', inplace=True)


#frame = pd.DataFrame(df)


for i in range(0,30):
    time = df.filter(like=st[i], axis=0)
    print(time)
    time.to_csv(st2[i])
    print(time.shape[0] )
    
    





