from flask import Flask, render_template, request
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Load the k-means model and vectorizer
kmeans = joblib.load('kmeans_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
hierarchical = AgglomerativeClustering(n_clusters=4)

# Load the abstracts
data = pd.read_csv('abstracts.csv')

# Initialize Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Cluster abstracts from uploaded CSV file
@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    data = pd.read_csv(file)
    # Use the loaded vectorizer to transform the new abstracts
    new_abstracts = vectorizer.transform(data['abstract'])
    terms = vectorizer.get_feature_names_out()
    cluster_names_for_k = []
    for i in range(4):
        center = kmeans.cluster_centers_[i]
        top_indexes = center.argsort()[::-1][:3]  # change 2 to the number of relevant words you want to extract
        top_terms = [terms[index] for index in top_indexes]
        cluster_name = ' '.join(top_terms)
        cluster_names_for_k.append(cluster_name)

    cluster_names_for_hc = []
    for i in range(4):
        center = kmeans.cluster_centers_[i]
        top_indexes = center.argsort()[::-1][:4]
        top_terms = [terms[index] for index in top_indexes]
        cluster_name = ' '.join(top_terms)
        cluster_names_for_hc.append(cluster_name)
    hierarchical_clusters = hierarchical.fit_predict(new_abstracts.toarray())
    data['kmeans.labels_'] = kmeans.labels_
    data['hierarchical.labels_'] = hierarchical_clusters
    data['cluster_name_for_k_means'] = [cluster_names_for_k[label] for label in kmeans.labels_]
    data['cluster_name_for_hc'] = [cluster_names_for_hc[label] for label in kmeans.labels_]
    # data['cluster'] = clusters
    data = data.drop('id', axis=1)


    return render_template('index.html', data=data.to_html(), heading_1 = "KEYWORD EXTRACTION")

# Cluster text string
@app.route('/cluster', methods=['POST'])
def cluster():
    if request.method == 'POST':
        abstract = request.form['text']
        new_data = pd.DataFrame({'abstract': [abstract]})
        data = pd.read_csv('abstracts.csv')
        data = pd.concat([data, new_data])
        data['tokens'] = data['abstract'].apply(word_tokenize)
        data['tokens'] = data['tokens'].apply(lambda x: [word.lower() for word in x])
        stop_words = set(stopwords.words('english'))
        data['tokens'] = data['tokens'].apply(lambda x: [word for word in x if word not in stop_words])
        terms = vectorizer.get_feature_names_out()
        lemmatizer = WordNetLemmatizer()
        data['tokens'] = data['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
        data['processed'] = data['tokens'].apply(lambda x: ' '.join(x))
        X = vectorizer.fit_transform(data['processed'])

        if data.shape[0] == 1:  # if only one sample is present in the data
            return render_template('index.html', heading_1='Error',
                                   data='Please enter more than one sample to perform clustering.')
        else:
            clustering = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
            clustering.fit(X.toarray())
            kmeans = KMeans(n_clusters=4, random_state=42)
            kmeans.fit(X)
            terms = vectorizer.get_feature_names_out()
            cluster_names = []
            for i in range(4):
                center = kmeans.cluster_centers_[i]
                top_indexes = center.argsort()[::-1][:3]  # change 2 to the number of relevant words you want to extract
                top_terms = [terms[index] for index in top_indexes]
                cluster_name = ' '.join(top_terms)
                cluster_names.append(cluster_name)

            cluster_name_for_hc = []
            for i in range(4):
                center = kmeans.cluster_centers_[i]
                top_indexes = center.argsort()[::-1][:4]  # change 2 to the number of relevant words you want to extract
                top_terms = [terms[index] for index in top_indexes]
                cluster_name = ' '.join(top_terms)
                cluster_name_for_hc.append(cluster_name)

            data['cluster_name_for_k_means'] = [cluster_names[label] for label in kmeans.labels_]
            labels = clustering.labels_
            data['cluster_name_for_hc'] = [cluster_name_for_hc[label] for label in kmeans.labels_]
            data['kmeans.labels_'] = kmeans.labels_
            data['hierarchical.labels_'] = labels
            # Filter out only the new data and the corresponding cluster labels
            new_data_cluster = data.tail(1)
            new_data_cluster = new_data_cluster.drop('tokens', axis=1)
            new_data_cluster = new_data_cluster.drop('processed', axis=1)
            new_data_cluster = new_data_cluster.drop('id', axis=1)
            return render_template('index.html',
                                   heading_1='CLUSTERED DATA',
                                   data=new_data_cluster.to_html(index=False))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True)
