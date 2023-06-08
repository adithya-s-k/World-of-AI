import streamlit as st
import torch
from PIL import Image
import albumentations as A
from io import BytesIO
import numpy as np  
import model
gen = model.Generator()

checkpoint = torch.load("World-of-AI\deep_learning\ESRGAN\Model\Pretrainedgen.pth" , map_location='cpu')
gen.load_state_dict(checkpoint["state_dict"])
st.title("Enhanced Image Resolution 😊")
image = st.file_uploader(" " , ['jpg' , 'png' , 'gif'])
if image is not None:
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = Image.open(BytesIO(file_bytes))
    img = img.resize((120 , 150))  
    st.image(img, channels="RGB" , width=400)
    img = model.highres(image = np.array(img))["image"]
    highres = gen(img.unsqueeze(0))
    hr = torch.permute(highres[0] , ( 1 ,2 , 0))
    st.image(np.array(hr.detach().numpy()) , clamp = True , channels='RGB' , width=400)
