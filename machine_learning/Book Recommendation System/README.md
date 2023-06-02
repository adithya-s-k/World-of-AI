**PROJECT TITLE**

<!-- if any of the topics seem irrelavent - please ignore -->

<i>BRS - Find Your Next Great Read!</i>

**GOAL**

The goal of this project is to develop a Book Recommendation System that suggests the best books based on user preferences, helping readers discover new and relevant books.

**DATASET**

Dataset Source: [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

**DESCRIPTION**

Imagine you're an avid reader and want to explore books similar to your favorite ones. This project introduces a collaborative book recommendation system. By entering a book name, users can receive recommendations based on the preferences of other users who enjoyed similar books.

**WHAT I HAD DONE**

1. Data Cleaning
2. Data preprocessing
3. Data Visualization
4. Data Modeling
5. Model Deployment with Falsk
6. Render

**Brief Description**

Before Diving into Model Description I would like to give a brief introduction about types of Recommendation model.

If you want to make any kind of recommendation sysetm then you should one of the mentioned list.

- Popularity Based Recommendar
- Content Based Recommendar
- Collaborative Based Recommendar
- Hybrid Based Recommendar

Out of these options, I have developed a Collaborative Book Recommendation system.

For this project, I found a suitable dataset on Kaggle, which I used for data preprocessing. After processing the data, my goal was to display the top 50 books in the web application interface. To achieve this, I implemented a popularity-based model.

The popularity model is based on a simple formula: the number of ratings for each book divided by the total number of books, giving the average rating for each book. Using this formula, I determined the top 50 books.

In addition to the popularity-based model, I also developed a collaborative book recommendation system. To implement this, I performed data preprocessing and extracted relevant data such as book titles, user IDs, and ratings.

To ensure the reliability of the collaborative model, I focused on books that received a minimum of 50 ratings from users. This helped me extract a substantial amount of data for modeling.

Next, I applied a technique called pivot table, which allowed me to represent the data more intuitively.After that I calculated the cosine similarity between each book and other books. The cosine similarity measures the distance or similarity between items.

By leveraging these techniques and calculations, I was able to build an effective collaborative book recommendation system. This system considers user preferences and provides recommendations based on the similarity between books, enhancing the personalized experience for users.

Overall, I employed a combination of popularity-based and collaborative-based models to deliver top book recommendations to users, making the application more engaging and valuable for book enthusiasts.

**MODEL USED**

Algorithm used:

- Cosine Similarity
- Sorting and Filtering

**LIBRARIES USED**

The project utilizes the following libraries:

- Pandas
- NumPy
- Scikit-learn
- Flask

**Deploy Link**

Live Link: [BRS - Find Your Next Great Read](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

**CONCLUSION**

In conclusion, the Book Recommendation System successfully assists readers in finding their next great read. By leveraging collaborative filtering techniques, it provides personalized book suggestions. It is ensuring users receive tailored recommendations based on their preferences.

**YOUR NAME**

- Name: <b>Sumit Dey</b>
- Social Media Handle: [LinkedIn](https://www.linkedin.com/in/sumit-dey-459426222/), [Gmail](sumitdeyodisha@gmail.com)
