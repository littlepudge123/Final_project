import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs('plots/boston_pairplot', exist_ok=True)

sns.set(style='darkgrid', palette='coolwarm')

boston_df = pd.read_csv('data/boston/housing.data',
                        sep='\s+',
                        header=None)
boston_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                     'MEDV']
sns.pairplot(boston_df, hue='CHAS', diag_kind='hist')
plt.savefig('plots/boston_pairplot.png')
plt.clf()
plt.close()