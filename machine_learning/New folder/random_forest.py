
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
sns.set()

from scipy.stats import skew
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score, mean_squared_error
from sklearn.preprocessing import LabelEncoder, StandardScaler
# data = pandas.read_csv("C:\Users\barkha arora\OneDrive\Desktop\python\ml\nutrition ml\nutrition.csv")
data = pd.read_csv("C:\\Users\\barkha arora\\OneDrive\\Desktop\\python\\ml\\nutrition ml\\dataset.csv")

# data=pandas.read_csv("C:\Users\barkha arora\OneDrive\Desktop\python\ml\nutrition ml\dataset.csv")
# d=data.head()
# print(d)
data_final=data.dropna().copy()
d=data_final.head()
data_final=data_final.drop('name ',axis=1)
sugar=20
calories=300
totalfat=7
carbohydrates=60
t=data_final.columns.to_list()
print(t)
data_final['healthy']=(data_final['sugars']<sugar) & (data_final['calories']<calories) & (data_final['carbohydrate']<carbohydrates) & (data_final['fat']<totalfat)
data_final['healthy']=data_final['healthy'].astype(int)

# print(data_final.describe())
# print(data_final.info())
# number=data_final['healthy'].value_counts()
# print(number)
# plt.pie(data_final['healthy'].value_counts(),labels=['not healthy','healthy'],autopct = '%0.2f %%')
# print(data_final)
# sum1=data_final.isnull().sum()
# print(sum1)
sns.pairplot(data_final.head(30),hue='healthy')
plt.show()
# print("working")
# sns.histplot(data_final['calories'],kde=False,bins=40)
# sns.histplot(data_final['sugars'],kde=True,bins=30)
# plt.figure(figsize=(50,20))
# sns.heatmap(data_final.corr(),annot=True,cmap='YlGnBu')
# plt.show()



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
# print(model.coef_)
# u=pd.DataFrame(model.coef_, x.columns, columns = ['Coeff'])
# print(u)

predictions = model.predict(x_test)

from sklearn import metrics
t=metrics.mean_squared_error(y_test, predictions)
print(t)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print(rmse)
print(r2)

