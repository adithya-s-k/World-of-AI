# Image Captioning

## GOAL

The main goal of this project is to develop a system that can generate descriptive captions for images from the Flickr8k dataset. The purpose of this project is to explore the field of image captioning and develop an algorithm that can accurately generate meaningful captions for a given image.

## DATASET

The dataset used in this project is the [Flickr8k dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k), which is a collection of 8,000 images sourced from the Flickr platform. Each image in the dataset is accompanied by five different captions provided by human annotators.

## DESCRIPTION

This project focuses on the task of automatically generating captions for images. The algorithm takes an image as input and produces a descriptive caption that accurately describes the image's content. The generated captions aim to capture both the objects and the relationships between them in the image.

## WHAT I HAD DONE

The project follows the following steps:

1. Data preprocessing:
   - Load the Flickr8k dataset.
   - Split the dataset into training and testing sets.

2. Feature extraction:
   - Extract image features using a pre-trained convolutional neural network (CNN) -- Xception.
   - Preprocess the images and pass them through the CNN to obtain feature vectors.

3. Caption generation:
  - Download the pre-trained GloVe word embeddings from [here](https://www.kaggle.com/datasets/watts2/glove6b50dtxt).
  - Load the GloVe embeddings and use them to initialize the word embedding layer in the caption generation model.

## MODELS USED

The following models/algorithms were utilized in this project:

- Convolutional Neural Network (CNN): Used for feature extraction from images. Specifically, the pre-trained Xception model was employed due to its excellent performance on image classification tasks.
- LSTM (Long Short-Term Memory): The embedded caption vectors are then passed through an LSTM layer, which is a type of RNN designed to capture long-term dependencies in sequential data. The LSTM layer learns to generate informative captions based on the input embeddings.

## LIBRARIES NEEDED

The following libraries are required to run this project:

- TensorFlow
- Keras
- NumPy
- NLTK (Natural Language Toolkit)
- Pandas
- Matplotlib

## ACCURACIES

The accuracy results for the models used in this project are as follows:
- LOSS - 2.0033
- <br>
![](https://tinyurl.com/54sar2v5)
![](https://tinyurl.com/e5fj3vhf)

## CONCLUSION

In conclusion, this project successfully implemented an image captioning system using the Flickr8k dataset. Further improvements could be made by exploring more advanced models or incorporating additional data sources.

AMAN KUMAR
