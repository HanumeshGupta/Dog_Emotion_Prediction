import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import streamlit as st
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress info & warning logs

# Load Model

ld_model = load_model('D:/Visual Studio Code/ML/Code_Work/Dog Emotion Prediction/dog_emotion_model.h5')


class_name = ['angry', 'happy', 'relaxed', 'sad']

def prediction_model(pil_img):
    img = pil_img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array,axis=0)
    img_array = preprocess_input(img_array)

    prediction = ld_model.predict(img_array)
    predicted_class = class_name[np.argmax(prediction)]
    confidence = np.max(prediction)

    return predicted_class, confidence

def main() :

    # Giving the Title
    st.title("Dog Emotion Prediction")


    upload_image = st.file_uploader("Upload as Image... ", type=['jpg','jpge','png'])


    if upload_image is not None :
        image = Image.open(upload_image)
        col1,col2 = st.columns(2)

        with col1 :
            resize_img = image.resize((100,100))
            st.image(resize_img)

        with col2:
            if st.button("Check Emotion") :

                emotion, confidence = prediction_model(image)

                st.success(f"Predicted Emotion: {emotion} (Confidence: {confidence:.2f})")


    
if __name__ =='__main__':
    main()

