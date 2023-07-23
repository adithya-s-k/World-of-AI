# **Enhancing Single-Image Resolution**

**GOAL**

The goal of the is to implement ESRGAN to Improve the resolution of Images.

**DATASET**

The dataset used to train the model was the [Celebrity Dataset](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset) from kaggle, the well trained Pretrained Weights(trained on larger datasets) are provided in the Model folder.

**DESCRIPTION**

***The Project aims to implement the ESRGAN or Enhanced Super Resolution Generative Adverserial Network. ESRGAN is a generative adversarial network for single image super-resolution. It uses a perceptual loss function which consists of an adversarial loss and a content loss. The adversarial loss pushes the solution to the natural image manifold using a discriminator network that is trained to differentiate between the super-resolved images and original photo-realistic images. 
Generating Images with better higher resolutions.***

**Implementation**

The ESRGAN is implemented using PyTorch. 
The project envolves training the model on the celebrity dataset, Initialy it is only trained on celbrity faces, but you can use the Pretrained weights as they are more sophisticated and authentic.


**LIBRARIES NEEDED**

torch, matplotlib, PIL, numpy, os etc.



**VISUALIZATION**

Below are some results of the model taking a Low Resolution image (Left) and producing a high resolution image (right)

![image1](https://github.com/sam5658/World-of-AI/assets/101457916/cc990684-7909-4d49-a4e8-a140d92ddfd7) ![image1](https://github.com/sam5658/World-of-AI/assets/101457916/0479637e-b793-4198-9bd6-8e88a2633c38)
![image2](https://github.com/sam5658/World-of-AI/assets/101457916/1bfc40e2-18b1-4754-8271-701e2c2adade) ![image2](https://github.com/sam5658/World-of-AI/assets/101457916/ce9ce1be-17d3-46d8-8cdb-b346b8ebf2dd)
![image0](https://github.com/sam5658/World-of-AI/assets/101457916/85e140c7-be18-4c07-9648-4ba19d2550d7) ![image0](https://github.com/sam5658/World-of-AI/assets/101457916/a34795b1-b0ad-4a35-a1fa-fb738e78db36)   



**ACCURACIES**

| Metrics     | Loss |
| :---        |    :----:   | 
| gp      | 0.2343       | 
| vgg  | 0.1935        |
| adversarial      | 0.0074      | 



**Conclusion**

The ESRGAN was successfully implemented and deployed on streamlit.

**Shubham Mishra**

[Linkedn](https://www.linkedin.com/in/shubhammishra1234/) ![702300](https://github.com/sam5658/World-of-AI/assets/101457916/00e21b1a-4865-4caf-b889-25a5e33f8602)
