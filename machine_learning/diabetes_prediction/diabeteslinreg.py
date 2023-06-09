import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow.keras import layers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
# data = np.loadtxt("/content/airfoil_self_noise.dat")
df = pd.read_csv("diabetes.csv")
df.head()
#visuaize data

# Print the result
X_train= df.drop("Outcome",axis=1)
Y_train= df["Outcome"]

#Data Cleaning skin thickness can never be zero
# Calculate the mean of non-zero values in the "SkinThickness" column
# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome


mean_skin_thickness = df.loc[df["SkinThickness"] != 0, "SkinThickness"].mean()
# Replace the zero values with the calculated mean
df.loc[df["SkinThickness"] == 0, "SkinThickness"] = mean_skin_thickness

mean_bp = df.loc[df["BloodPressure"] != 0, "BloodPressure"].mean()
# Replace the zero values with the calculated mean
df.loc[df["BloodPressure"] == 0, "BloodPressure"] = mean_bp


mean_insulin = df.loc[df["Insulin"] != 0, "Insulin"].mean()
# Replace the zero values with the calculated mean
df.loc[df["Insulin"] == 0, "Insulin"] = mean_insulin

mean_glucose = df.loc[df["Glucose"] != 0, "Glucose"].mean()
# Replace the zero values with the calculated mean
df.loc[df["Glucose"] == 0, "Glucose"] = mean_glucose

mean_bmi = df.loc[df["BMI"] != 0, "BMI"].mean()
# Replace the zero values with the calculated mean
df.loc[df["BMI"] == 0, "BMI"] = mean_bmi


mean_dpf = df.loc[df["DiabetesPedigreeFunction"] != 0, "DiabetesPedigreeFunction"].mean()
# Replace the zero values with the calculated mean
df.loc[df["DiabetesPedigreeFunction"] == 0, "DiabetesPedigreeFunction"] = mean_dpf


mean_age = df.loc[df["Age"] != 0, "Age"].mean()
# Replace the zero values with the calculated mean
df.loc[df["Age"] == 0, "Age"] = mean_age

for label in df.columns[:-1]:
  plt.hist(df[df["Outcome"]==1][label], color='blue', label='gamma', alpha=0.7, density=True)
  plt.hist(df[df["Outcome"]==0][label], color='red', label='hadron', alpha=0.7, density=True)
  plt.title(label)
  plt.ylabel("Probability")
  plt.xlabel(label)
  plt.legend()
  plt.show()

#data cleaning done

#Train, validation, test datasets
train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

def scale_dataset(dataframe, oversample=False):
  X = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(X)

  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y
train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)



#apply log regression


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, y_train)
y_pred = lg_model.predict(X_test)
print(classification_report(y_test, y_pred))

# Number of zeroes in the 'Outcome' column: 500
print(df.head())

plt.scatter(y_test,lg_model.predict(X_test),color= "blue",linewidth=3)
plt.show()


print("Logistic Regression Done")


