# CAR CLASSIFIER

GOAL

To classify a given car into either Ferrari, Mclaren or Mercedes using Computer Vision

DATASET

The dataset has been downloaded from the DuckDuckGo search API that is available with fastai library

DESCRIPTION

This project uses the fastai library and leverages the abilities of computer vision to accurately differentiate between a Ferrari car, a Mclaren car and a Mercedes car which can be rather difficult to differentiate as many cars have similar structure. This shows the wide capabilities deep learning and computer vision hold!

WHAT I HAD DONE

First I scraped the dataset using DuckDuckGo API, which basically includes around 200 images of each car (Ferrari, Mclaren and Mercedes). Then I used data augmentation on each image to increase the size of dataset and the accuracy of model and then trained it using fastai's vision_learner.

MODELS USED

fastai provides easy to use vision_learner to learn various features of an image and then use those learnings to predict the class of any other given input image.

LIBRARIES NEEDED

fastai and pytorch

VISUALIZATION

Included in the Images📸 folder

ACCURACIES

Neural networks are used using fastai's vision_learner and it provides an accuracy of nearly 88%

CONCLUSION

We simply scraped our data from DuckDuckGo and thus we can not validate the data. Even so we were able to get around 88% accuracy, not to mention that cars can be rather difficult to distinguish between especially only the rear side of the car is visible. Thus this is turns out to be a really good model if trained with proper dataset.

YOUR NAME

Pranshav Patel
https://www.github.com/pranshavpatel
https://www.linkedin.com/in/pranshav-patel-1a80b0231/
https://medium.com/@pranshavpatel