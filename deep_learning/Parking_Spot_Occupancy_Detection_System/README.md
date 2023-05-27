### Parking Spot Occupany Detection System

## GOAL

To develop an automated system to detect the empty parking spaces in a parking lot, to provide effective management of car parking to the users which can help in reducing the queues, improving scalability and the time required to find parking spaces

## DATASET

The dataset has been obtained from the following websites:
http://cnrpark.it/
https://public.roboflow.com/object-detection/pklot
You can also refer to other dataset inluding the required attributes.

## DESCRIPTION

In this project, a method for classifying parking spaces in real-time using Convolutional Neural Networks (CNN) and OpenCV is shown. Convolutional Neural Networks are useful because they automatically extract and utilise the characteristics from the dataset, which simplifies the classification process. The suggested approach is also resistant to unusual parking habits, such as vehicles parking in various locations. This technique is anticipated to provide extremely high accuracy, even in the presence of noise brought on by changing lighting conditions, shadows, and partial occlusions. Last but not least, this example demonstrates how car slot recognition may be used to track parking lot capacity over time without the cost of hardware like GPUs or the labour of parking lot managers patrolling at regular intervals.
First parking spot is detected, after which occupancy of that spot is predicted.

## WHAT I HAD DONE

![image](https://github.com/PrathmeshN99/World-of-AI/assets/90515944/86607386-3649-4b93-9cba-b8eca221433b)


The step by step procedure of how project works:
1. Data Cleaning
2. EDA perform
3. Data Visualization
4. Data Processing
5. Slot Detection using OpenCV
6. Data Modeling
7. Slot Occupancy Prediction
8. Data Evaluation

## MODELS USED

Algorithm used:
* Convoulutional Neural Networks(CNN)
* Computer Vision(CV) technology
* AlexNet Architecture 
* Canny Edge Detection

## LIBRARIES NEEDED

Libraries required:
* Numpy
* Matplotlib
* Seaborn
* Tensorflow
* CV2

## VISUALIZATION

![image](https://github.com/PrathmeshN99/World-of-AI/assets/90515944/4ea0edb3-b971-44ca-97e6-e4d301abf08d)
![image](https://github.com/PrathmeshN99/World-of-AI/assets/90515944/59980c0f-68d7-4807-81e3-b230f0822bd1)

## ACCURACY

The AlexNet model was found accurate in terms of validation data. The model produced an validation accuracy of 96.25% and loss of 15.55% as depicted. Thus, the AlexNet model can accurately detect the empty parking slots.

![image](https://github.com/PrathmeshN99/World-of-AI/assets/90515944/06523351-fc10-4bc5-b491-4a6b986e8aa8)
![image](https://github.com/PrathmeshN99/World-of-AI/assets/90515944/e8f16ea0-89d3-41ac-bb4e-5250a5e1dc38)

