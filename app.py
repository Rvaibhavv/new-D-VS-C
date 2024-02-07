import streamlit as st
from src.DogvsCatClassifier.pipeline.prediction import PredictionPipeline
import matplotlib.pyplot as plt
# import cv2
# test_img =cv2.imread



# def upload_file(self):
# st.title("photo uploader App")
# uploaded_file = st.file_uploader("choose a photo",type=['png','jpg','jpeg'])
# if uploaded_file is not None:
#     st.image(uploaded_file,caption='uploaded photo',use_column_width=True)
#     predictor=PredictionPipeline(uploaded_file)
#     predictedvalue = predictor.predict()
#     st.subheader(f"this is a {predictedvalue}")

# def predictions(self):
st.title("photo uploader App")
uploaded_file = st.file_uploader("choose a photo",type=['png','jpg','jpeg'])
# plt.imshow(uploaded_file)
if uploaded_file is not None:
    st.image(uploaded_file,caption='uploaded photo',use_column_width=True)
    predictor=PredictionPipeline()
    predictedvalue = predictor.predict(uploaded_file)
    st.subheader(f"this is a {predictedvalue}")


