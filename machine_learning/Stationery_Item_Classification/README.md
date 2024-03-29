# Stationery Items Classification

## GOAL

The main purpose of this Project is to classify different stationery based on their images(appearance).

The stationery items are - highlighter, pen, eraser, and scale.

## DATASET

Data has been created from Google Images.

Link for the dataset - https://drive.google.com/drive/folders/1gnXWrEAJJsMSz4u_vuGXKU5DvlGiCu6i?usp=sharing

## DESCRIPTION

The project involves the classification of 4 types of stationery items based on their appearance. The input is in the form of Images. 

## WHAT I HAD DONE

The step-by-step procedure of how the project works:

**1. Import the Required Libraries** - TensorFlow and its Keras module for building and training neural networks.  Matplotlib for visualizing images and plots.

**2. Displaying Sample Images** - The code displays a grid of 12 images from the dataset along with their corresponding labels. This is done using Matplotlib's plt.imshow() and plt.title() functions.

**3. Training Testing Validation** - Dividing the dataset into training(majority), testing and validation categories.

**4. Partitioning the dataset** -  The dataset is split into training, validation, and test sets using the get_dataset_partitions_tf() function. The function takes the dataset and the desired split percentages as parameters. The training set is assigned to train_ds, the validation set to val_ds, and the test set to test_ds

**5. Data Augmentation** - Data augmentation is performed to increase the dataset's diversity and improve model generalization. The data_augmentation sequence applies random flips and rotations to the images.

**6. Model Architecture** - The model is built using the Sequential API of Keras. It consists of a series of convolutional (Conv2D) and max-pooling (MaxPooling2D) layers. The convolutional layers extract features from the input images. The final layers are a flattened layer, a dense layer with ReLU activation, and a dense layer with softmax activation for multi-class classification.

**7. Model Compilation** - The model is compiled with the Adam optimizer, sparse categorical cross-entropy loss, and accuracy metric.

**8. Model Training** - The fit() function is called to train the model on the training data. Parameters include the training data, batch size, validation data, verbosity, and the number of epochs. The training history is stored in the history variable.

**9. Model Evaluation** - The evaluate() function is used to evaluate the model's performance on the test dataset. The evaluation results (loss and accuracy) are stored in the scores variable.

**10. Visualising Predictions** - The code selects a batch of images from the test dataset and visualizes their actual and predicted classes using the predict() function.

## LIBRARIES NEEDED

Libraries required:
* Tensorflow
* Keras
* Matplotlib

## CONCLUSION
The model can predict the fruit, with input as an image. 

The loss and accuracy - loss: 1.0388 - accuracy: 0.5625


