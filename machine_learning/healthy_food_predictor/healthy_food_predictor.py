
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
sns.set()

from scipy.stats import skew
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score, mean_squared_error

data = pd.read_csv("C:\\Users\\barkha arora\\OneDrive\\Desktop\\python\\ml\\nutrition ml\\dataset.csv")


data_final=data.dropna().copy()
d=data_final.head()
data_final=data_final.drop('name ',axis=1)
sugar=20
calories=300
totalfat=7
carbohydrates=60
t=data_final.columns.to_list()
#print(t)
data_final['healthy']=(data_final['sugars']<sugar) & (data_final['calories']<calories) & (data_final['carbohydrate']<carbohydrates) & (data_final['fat']<totalfat)
data_final['healthy']=data_final['healthy'].astype(int)

sns.pairplot(data_final.head(30),hue='healthy')
plt.show()




from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier


scaler = MinMaxScaler()
value=pd.DataFrame(scaler.fit_transform(data_final),columns=data_final.columns,index=data_final.index)
x=value[['total_fat','carbohydrate', 'fiber', 'sugars', 'fat']]
y=value['healthy']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
model = RandomForestClassifier()
model.fit(x_train, y_train)


predictions = model.predict(x_test)

from sklearn import metrics
t=metrics.mean_squared_error(y_test, predictions)
print(t)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print(rmse)
print(r2)

