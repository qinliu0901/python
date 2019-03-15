import pandas as pd
import numpy as np

train_data = pd.read_csv("happiness_train_clean.csv",index_col='id')
test_data = pd.read_csv("happiness_test_clean.csv",index_col='id')
# 删除无关的特征
list = ['survey_time','work_yr','work_type','work_manage']
for i in list:
	del train_data[i]
	del test_data[i]
test_index = test_data.index

""" 主成分分析，数据降维
降维是对数据高维度特征的一种预处理方法。
降维是将高维度的数据保留下最重要的一些特征，去除噪声和不重要的特征实现提升数据处理速度的目的。"""
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
# np.isnan()多用于单个值的检验，pd.isnull()用于对一个DataFrame或Series（整体）的检验。
train_data_y = train_data['happiness']
del train_data['happiness']
# 先将空值填充为0
def data_deal(train_data):
	for i in train_data.columns: 
		for j in train_data.index:
			if np.isnan(train_data[i][j]):
				train_data[i][j] = 0
	pca = PCA(n_components=10)
	re = pca.fit_transform(train_data)
	return re 
train_data_x = data_deal(train_data)
test_data = data_deal(test_data)


#建立神经网络模型，进行幸福感预测
from keras.models import Sequential
from keras.layers.core import Dense,Activation
# 初始化一个神经网络
model = Sequential()
# 添加一层神经网，输入层
model.add(Dense(input_dim=20,output_dim=10))
# 设置激活函数
model.add(Activation('relu'))
# 添加输出层
model.add(Dense(input_dim=10,output_dim=1))
# 模型设置：optimizer选择优化函数，loss损失函数的评价方法
model.compile(loss='mean_squared_error',optimizer='adam')
# batch_size: 每一次迭代的样本数目. nb_epoch训练代数
model.fit(train_data_x,train_data_y,nb_epoch=1000,batch_size=20)
model.predict(test_data)
r = pd.DataFrame(model.predict(test_data),index=test_index)
r.to_csv("forcast.csv")