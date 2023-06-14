import numpy as np
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Data cleaning
# ...


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


# Train, test datasets
X = df.drop("Outcome", axis=1)
Y = df["Outcome"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Prepare the data in the format compatible with XGBoost
dtrain = xgb.DMatrix(X_train, label=Y_train)
dtest = xgb.DMatrix(X_test)

# Set the parameters for XGBoost classifier
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'eta': 0.1,
    'max_depth': 3
}

# Train the XGBoost model
model = xgb.train(params, dtrain)

# Make predictions using the trained model
y_pred = model.predict(dtest)
y_pred_binary = (y_pred > 0.5).astype(int)

# Print classification report
print(classification_report(Y_test, y_pred_binary))

# Scatter plot
plt.scatter(Y_test, y_pred_binary, color="blue", linewidth=3)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()

print("XGBoost done.")
