import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

st.title('Concrete Strength Prediction App using ANN')
st.markdown('**Input your Concrete Compostition**')

data = pd.read_csv('concrete_data.csv')

scaler = MinMaxScaler()
scaler.fit(data.drop(columns=['Strength']))

def collect_data(scaler):
    cement = st.number_input('Cement (kg/m^3)', value=None, placeholder="Type a number...")
    blast_furnace_slag= st.number_input('Blast Furnace Slag (kg/m^3)',value=None,placeholder="Type a number...")
    ash = st.number_input('Fly Ash (kg/m^3)', value=None,placeholder="Type a number...")
    water = st.number_input('Water (kg/m^3)',value=None,placeholder="Type a number...")
    superplasticizer = st.number_input('Superplasticizer (kg/m^3)', value=None,placeholder="Type a number...")
    coarse_aggregate = st.number_input('Coarse Aggregate (kg/m^3)', value=None,placeholder="Type a number...")
    fine_aggregate = st.number_input('Fine Aggregate (kg/m^3)',value=None,placeholder="Type a number...")
    age = st.number_input('Age (days)', value=None,placeholder="Type a number...")
    user_input=pd.DataFrame([[cement,blast_furnace_slag,ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]],
                columns=["Cement",'Blast Furnace Slag','Fly Ash','Water','Superplasticizer','Coarse Aggregate','Fine Aggregate','Age'])
    # Scale the user input
    scaled_input = pd.DataFrame(scaler.transform(user_input), columns=user_input.columns)
    
    return scaled_input

# Load the saved model
model = tf.keras.models.load_model('concrete_model.h5')

# Predict concrete strength
input_data =  collect_data(scaler)
if st.button('Predict'):
    with st.spinner('Calculating prediction...'):
        prediction = model.predict(input_data)
        result = (prediction[0])
        st.success(f'Your cement strength is {result} MPa.')