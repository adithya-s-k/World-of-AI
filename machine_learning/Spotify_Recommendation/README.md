# Spotify Recommendation

## GOAL

This implementation helps in recommending the top 5 songs, on the basis of the input provided.

## DATASET

The data is in the form of a CSV file.  

## DESCRIPTION

With input as a song name, the implementation will be able to recommend the top 5 songs. It has used Manhattan distance formulae on the numerical values, 
to select the top 5 songs. 

## WHAT I HAD DONE

The step-by-step procedure of how the project works:

This code provides a Spotify song recommender system based on a given dataset. The recommender system uses the KMeans clustering algorithm and the Manhattan distance metric to find songs with similar characteristics.

**1. Data Loading and Preprocessing:** The dataset is loaded from a CSV file and preprocessed to handle missing values and normalize the numerical columns.

**2. Exploratory Data Analysis:** Data visualization is performed to understand the trends and changes in music over time.

**3. Correlation Analysis:** The correlation between different features of the dataset is analyzed using a heatmap.

**4. Feature Engineering:** Additional features are created, such as clustering songs into different groups using KMeans.

**5. SpotifyRecommender Class:** A class is implemented to encapsulate the recommender system logic. It calculates the Manhattan distance between songs and provides recommendations based on the smallest distances.

**6. Usage Example:** Several examples are given to demonstrate how to use the recommender system on different songs.

## Recommendation Algorithm

The recommendation algorithm in this code utilizes the concept of Manhattan distance to measure the similarity between songs. The Manhattan distance, also known as the city block distance or L1 distance, calculates the total difference between corresponding feature values of two songs. By comparing the Manhattan distances of songs, the algorithm identifies the top 5 closest songs to a given input song.

## Requirements

To run this code, you need the following dependencies:

- NumPy
- pandas
- matplotlib
- seaborn
- tqdm
- sci-kit-learn

## VISUALIZATION

Added a result folder, which has the screenshots. 

## CONCLUSION

The recommender system uses the KMeans clustering algorithm and the Manhattan distance metric to find songs with similar characteristics.




