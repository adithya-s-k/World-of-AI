# Sentiment-Analysis

<b>Task</b> : Performing sentiment analysis on movie review
<b>Dataset used</b> : IMDB Dataset of 50K Movie Reviews <br>
<b>Source </b>: Kaggle<br>
<b>URL</b> : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

# Dataset metadata :<br>
It consists of 50,000 rows with equal division of positive and negative reviews. There are two rows, namely "Sentiment" and "Review".

# Steps performed
1) Importing Neccessary libraries
2) Performing Exploratory Data Analysis
     -> Showcasing 10 positive and negative sentiments <br>
     -> Dropping Duplicate values<br>
     -> Checking for NULL values<br>
     -> Displaying percentage of positive and negative sentiment<br>
     -> Analysing number of words in each category of sentiment<br>
3) Data Cleaning<br>
     -> Decode HTML encoded characters<br>
     -> Removing Stop words (only those stopwords which arent negative)<br>
     -> Removing URL's<br>
4) Tokenization 
5) Stemming and Lemming
6) Displaying Word Cloud
7) Applying Tf-Idf vectorizer and different models
8) Applying Tf-Idf with bigrams 
9) Applying Word2Vec as word embedding technique
10) Result

# Libraries 
1) Pandas
2) Numpy
3) Sklearn
4) NLTK
5) Wordcloud
6) BeautifulSoup
7) Matplotlib
8) Gensim


# Models
1) Decision Tree Classifier
2) Random Forest Classifier
3) Logisitic Regression
4) KNN
5) Navie Bayes
6) SVM

# Result:<br>
<br>
Using Tf-Idf vectorizer for feature extraction, we obtain highest accuracy of 0.87 using SVM model and using word2vec as word embedding technique highest accuracy is using both SVM and Logistic regression which is 0.88

