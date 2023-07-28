### Cricket Score Prediction

## GOAL

The goal of this code is to build and evaluate regression models, including XGBoost and Linear Regression, for predicting the target variable in a cricket dataset. The code aims to provide insights into the performance and predictive accuracy of these models for estimating the runs scored in a cricket match.

By training and evaluating the models on the given dataset, this code facilitates the comparison of different regression techniques and helps in understanding their strengths and limitations in the context of cricket run prediction.

## DATASET

The dataset for the given model is in the form of CSV file.  

**Link for the dataset - https://drive.google.com/file/d/1vvTqJ8OK77_D0iculp_fANTVe0netYhy/view?usp=sharing**

## DESCRIPTION

The project helps in cricket score prediction using T20 world cup data. 

## WHAT I HAD DONE

The step-by-step procedure of how the project works:

**1. Data Preprocessing:**
   - Load the cricket dataset into a pandas DataFrame.
   - Perform any necessary data cleaning, such as handling missing values or data type conversions.
   - Encode categorical variables using one-hot encoding to prepare the data for modeling.

**2. Exploratory Data Analysis (EDA):**
   - Conduct exploratory data analysis to gain insights into the dataset.
   - Create visualizations, such as bar charts, histograms, and scatter plots, to understand the distribution and relationships between variables.
   - Analyze key metrics and patterns related to batting teams, powerplay runs, death overs, run rates, and other relevant factors.

**3. Model Training and Evaluation:**
   - Split the dataset into training and testing sets.
   - Train different regression models, such as XGBoost and Linear Regression, on the training data.
   - Use the trained models to make predictions on the testing data.
   - Evaluate the performance of the models using various evaluation metrics, such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared score (R2).

**4. Comparison of Models:**
   - Compare the evaluation metrics of the different models to assess their performance.
   - Analyze the strengths and weaknesses of each model in predicting the runs scored in a cricket match.
   - Determine which model performs better based on the chosen evaluation metrics.

**5. Additional Analysis and Visualization:**
   - Explore additional analysis and visualizations to gain deeper insights into the model predictions and the relationship between variables.
   - Create visualizations, such as scatter plots or residual plots, to understand the correlation between actual and predicted values.

## LIBRARIES NEEDED

1) Numpy
2) Pandas
3) Matplotlib
4) Sciket-Learn
5) xgboost
6) LinearRegressiom
7) DecisionTreeRegressor

## VISUALIZATION

Visualization with the help of Residual Plots for all the 3 models. (Decision Tree, XGBoost, Linear Regression).

## CONCLUSION

The Decision Tree Model predicts the model with the highest accuracy. 

Mean Absolute Error (MAE): 0.5904828065300451

Mean Squared Error (MSE): 21.003820771101076

Root Mean Squared Error (RMSE): 4.582992556299986

R-squared Score (R2): 0.9797796972256891



