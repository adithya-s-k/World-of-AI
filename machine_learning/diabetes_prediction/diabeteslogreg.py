import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")
df.head()
#visuaize data


# Data Cleaning skin thickness can never be zero
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



#data cleaning done

#Train, validation, test datasets
train,  test = df.sample(frac = 0.8), df.sample(frac=0.2)
train, test = df.sample(frac=0.8), df.sample(frac=0.2)

X_train, Y_train = train.drop("Outcome", axis=1), train["Outcome"]
X_test, Y_test = test.drop("Outcome", axis=1), test["Outcome"]

# #apply log regression


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, Y_train)
y_pred = lg_model.predict(X_test)
print(classification_report(Y_test, y_pred))

# # Number of zeroes in the 'Outcome' column: 500p
print(df.head())

plt.scatter(Y_test,lg_model.predict(X_test),color= "blue",linewidth=3)
plt.show()
print("Logistic Regression Done")


