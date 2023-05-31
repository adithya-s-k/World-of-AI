from flask import Flask, render_template, request
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import joblib

# Load the k-means model and vectorizer
kmeans = joblib.load('kmeans_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Load the abstracts
abstracts = pd.read_csv('abstracts.csv')

# Initialize Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home_1.html')

# Cluster abstracts from uploaded CSV file
@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file)
    # Use the loaded vectorizer to transform the new abstracts
    new_abstracts = vectorizer.transform(data['abstract'])
    terms = vectorizer.get_feature_names_out()
    cluster_names = []
    for i in range(4):
        center = kmeans.cluster_centers_[i]
        top_indexes = center.argsort()[::-1][:3]  # change 2 to the number of relevant words you want to extract
        top_terms = [terms[index] for index in top_indexes]
        cluster_name = ' '.join(top_terms)
        cluster_names.append(cluster_name)
    clusters = kmeans.predict(new_abstracts)
    data['kmeans.labels_'] = kmeans.labels_
    data['cluster_name'] = [cluster_names[label] for label in kmeans.labels_]
    # data['cluster'] = clusters
    return render_template('home_1.html', data=data.to_html())

# Cluster text string
@app.route('/cluster', methods=['POST'])
def cluster():
    text = request.form['text']
    data = pd.DataFrame({'abstract': [text]})
    # Use the loaded vectorizer to transform the new abstract
    new_abstract = vectorizer.transform(data['abstract'])
    data['tokens'] = data['abstract'].apply(word_tokenize)
    data['tokens'] = data['tokens'].apply(lambda x: [word.lower() for word in x])
    stop_words = set(stopwords.words('english'))
    data['tokens'] = data['tokens'].apply(lambda x: [word for word in x if word not in stop_words])
    terms = vectorizer.get_feature_names_out()
    lemmatizer = WordNetLemmatizer()
    data['tokens'] = data['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
    data['processed'] = data['tokens'].apply(lambda x: ' '.join(x))
    X = vectorizer.fit_transform(data['processed'])

    cluster_names = []
    for i in range(4):
        center = kmeans.cluster_centers_[i]
        top_indexes = center.argsort()[::-1][:3]  # change 2 to the number of relevant words you want to extract
        top_terms = [terms[index] for index in top_indexes]
        cluster_name = ' '.join(top_terms)
        cluster_names.append(cluster_name)
    clusters = kmeans.predict(new_abstract)
    data['cluster'] = clusters
    print(data)
    return render_template('home_1.html', data=data.to_html())

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True)
