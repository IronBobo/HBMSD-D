#生成训练数据集（代码中有将npy文件变为csv文件的代码）
import numpy as np
import pandas as pd

data = pd.read_csv('mytraindataofcheck.csv')
print(data.shape)
data2 = np.array(data)
data5 = data2.reshape(-1,170,3)
print(data5)
print(data5.shape)
np.save('mytraindataofcheck.npy',data5)
#data3 = data2.transpose([0,2,3,1]) 
#data4 = np.load('mytraindataofcheck.npy')
#data5 = data4.reshape(-1,2,3)

#print(data2)
#np.savez('pems08.npz',data5=data)


#input_data = np.load(r"data.npy")
#print(input_data.shape)
#data = input_data.reshape(-1,3)
#print(data.shape)
#print(data)
#df = pd.DataFrame(data)
#print(df)
#df.to_csv('traindata.csv')
#np.savetxt(r"test1111.txt",data,delimiter=',')
