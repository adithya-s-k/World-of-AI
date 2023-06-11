# Deep Learning Projects
# Deep Learning Projects
Video Caption Generator 
GOAL
The main purpose of this Project is to help the people with Deaf and hard of hearing individuals to watch videos helps people to focus on and remember the information more easily, to build the feature extraction using the convolutional neural network (VGG 16), to examine how LSTM is used for encoding and decoding the features and to explore how the greedy search algorithm predict the efficient caption.


DATASET
The Microsoft Research Video Description Corpus (MSVD) dataset consists of about 1970 
short video snippets downloaded from YouTube. Each video snippet is annotated with 
around 40 textual description collected via crowdsourcing. This results in 80839 sentences. 
In the project, the data is split into train, validation and test sets, containing 1200, 100 and 
670 video snippets respectively. Each video has a unique ID, and each ID includes 
approximately 15–20 captions. There are two directories in the dataset: training_data and 
testing_data. Each folder has a video subfolder that contains the videos that will be used 
for both training and testing. There is also a feat subfolder in these folders, which stands 
for features. The video’s features are contained in the feat folders.

DESCRIPTION
Video understanding has become increasingly important as surveillance, social, and 
informational videos weave themselves into everyday lives. Video captioning offers a 
simple way to summarize, index, and search the data. In recent years, automatically 
generating natural language descriptions for videos has created a lot of focus in computer 
vision and natural language processing research. Video captioning is the quite challenging 
because of the complex and diverse nature of video content. However, the understanding 
between video content and natural language sentence remains an open problem to create 
several methodology to better understand the video and generate the sentence 
automatically. Video Captioning is a task of automatic captioning a video by understanding 
the action and event in the video which can help in the retrieval of the video efficiently 
through text. Video Captioning is an encoder decoder mode based on sequence to sequence 
learning. Automated video caption generator helps searching of videos in websites better 
and make content easier. The video information is considered as a sequence of images with 
10 to 12 seconds short video clips. In the proposed system, Convolutional Neural Networks 
(VGG 16) is used for feature extraction and LSTM is used for encoding and decoding the 
features. Greedy search algorithm is used for predicting the efficient caption and gives 
speedy word extraction. Finally, the language converter is used for specific people 
language to understand the captions

WHAT I HAD DONE
The step by step procedure of how project works:

Feature Extraction 
Preprocessing of Captions
LSTM for sequence generation
Model Building
Generating Caption using Greedy search
MODELS USED
Algorithm used:

CNN
RNN
LSTM

LIBRARIES NEEDED
Libraries required:

opencv
pillow
keras
fpdf
py_edamam
joblif
anaconda


ACCURACIES
Accuracies and results of Algorithms used The accuracy score achieved is 0.87 and the loss score less than 1.

CONCLUSION
The most accurate model found to be CNN-RNN  for video caption generation.

email- nehavish006@gmail.com