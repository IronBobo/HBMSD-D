#此文件也属于第一问，配合checkmytraindata.py使用
import numpy as np
import pandas as pd

st2 = ['1.csv','2.csv','3.csv','4.csv','5.csv','6.csv','7.csv','8.csv','9.csv','10.csv','11.csv','12.csv','13.csv','14.csv','15.csv','16.csv','17.csv','18.csv','19.csv','20.csv','21.csv','22.csv','23.csv','24.csv','25.csv','26.csv','27.csv','28.csv','29.csv','30.csv']
st3=['speedok1.csv','speedok2.csv','speedok3.csv','speedok4.csv','speedok5.csv','speedok6.csv','speedok7.csv','speedok8.csv','speedok9.csv','speedok10.csv','speedok11.csv','speedok12.csv','speedok13.csv','speedok14.csv','speedok15.csv','speedok16.csv','speedok17.csv','speedok18.csv','speedok19.csv','speedok20.csv','speedok21.csv','speedok22.csv','speedok23.csv','speedok24.csv','speedok25.csv','speedok26.csv','speedok27.csv','speedok28.csv','speedok29.csv','speedok30.csv',]

for i in range(0,30):  
    data = pd.read_csv(st2[i])
    df=data.set_index('starttime',drop=True)
    df.loc[df.speed>=120,'speed'] = 120
    print(df)
    df.to_csv(st3[i])


#errorspeed = data[data.speed>120]
#df=data.set_index('starttime',drop=True)
