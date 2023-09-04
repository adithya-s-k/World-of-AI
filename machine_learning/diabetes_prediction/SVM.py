import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = np.loadtxt("/content/airfoil_self_noise.dat")
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

from sklearn.metrics import classification_report
from sklearn.svm import SVC

# Create an instance of the SVM classifier
model = SVC()

# Fit the model on the training data
model.fit(X_train, Y_train)

# Predict values for the test data
y_pred = model.predict(X_test)
print(y_pred)
print(classification_report(Y_test, y_pred))
plt.scatter(Y_test,model.predict(X_test),color= "blue",linewidth=3)
plt.show()
print("SVM CLASSIFIER DONE")

