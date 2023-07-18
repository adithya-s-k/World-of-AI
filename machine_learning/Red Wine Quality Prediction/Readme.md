# Red_Wine_Quality_Prediction
Predict the Quality of the red wine given the physiochemical data of the wine. Improved the accuracy of the model using EDA and features selection using correlations.


### DESCRIPTION

The dataset is related to the red variant of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).
These datasets can be viewed as regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).

### [Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) 



### OBJECTIVE
To predict the quality of the red wine.

### APPROACH
- Import the modules and dependencies and load the dataset.
- Clean the data, check the null values with imputation if any.
- Perform EDA on the dataset.
   - Label is quality, do the target analysis with features.
   - Do Features engineering.
- Split the data into training and testing dataset.
- Apply Regression techniques and compare the models.

### ACCURACY
With applying correlations to select non-redundant features

- Gradient Descent in Multiple Linear Regression :       52.5%
- Linear Regression                              :       57.8%
- Random Forest Regression                       :       72.18%

### CONCLUSION

Applied different regression techniques to predict the quality of wine and observed that Random Forest Regressor provided comparatively high accuracy score ( 72.18 % ) than other regression algorithms.
