#!/usr/bin/env python3


# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

# creat plot file for image
os.makedirs('plots', exist_ok=True)

# load dataset from sklearn, set value as target
from sklearn.datasets import load_boston
boston= load_boston()


bos = pd.DataFrame(boston.data, columns=boston.feature_names)
bos['MEDV']= boston.target
# check the value, find relations, price is even
sns.set(rc={'figure.figsize':(10,10)})
sns.distplot(bos['MEDV'], bins=30)
plt.savefig('plots/check_price_range.png', dpi=300)

# find correlation on LSTAT & RM  compare with MEDV
sns.heatmap(data=bos.corr().round(2), cmap='coolwarm', annot=True, annot_kws={"size":8})
plt.tight_layout()
plt.savefig('plots/check_corrolation.png')


# make plots to show relations
plt.figure(figsize=(10, 5))

features = ['LSTAT', 'RM']
target = bos['MEDV']

for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = bos[col]
    y = target
    plt.scatter(x, y, marker='*',s=2)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('MEDV')
    plt.show()
plt.close()

# prepare for modeling
X = pd.DataFrame(np.c_[bos['LSTAT'], bos['RM']],columns = ['LSTAT','RM'])
Y = bos['MEDV']

# build train and test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state=5)
# print(X_train.shape)
# print(X_test)
# print(Y_train)
# print(Y_test)
# traning Linear Regression model with fit()
from sklearn.linear_model import LinearRegression
from sklearn import metrics
lm = LinearRegression()
lm.fit(X_train, Y_train)

# predicting training: training results
y_train_predict = lm.predict(X_train)

for (real, predicted) in list(zip(Y_test, y_train_predict)):
    print(f"Value: {real:.2f}, pred: {predicted:.2f}, diff: {(real - predicted):.2f}")

# check predict errors and r2-score
rmse = (np.sqrt(metrics.mean_squared_error(Y_train, y_train_predict)))
r2 = metrics.r2_score(Y_train, y_train_predict)
print("model performance for training:")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")

y_test_predict = lm.predict(X_test)
rmse = (np.sqrt(metrics.mean_squared_error(Y_test, y_test_predict)))
r2 = metrics.r2_score(Y_test, y_test_predict)

print("The model performance for testing:")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

plt.scatter(Y_test, y_test_predict)
plt.savefig('plots/prediciton_accurate.png',dpi=300)
plt.show()