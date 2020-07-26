#使用knn进行补全
import numpy as np
import pandas as pd
from fancyimpute import KNN

data = pd.read_csv('data 2.csv')

data = pd.DataFrame(KNN(k=6).fit_transform(data)) 
data.columns = ['speed','volume','occupancy']  # fancyimpute填补缺失值时会自动删除列名
print(data)
