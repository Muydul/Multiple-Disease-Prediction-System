# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

heart_model = pickle.load(open('F:/3-2/1903136/3200/Multiple Disease Prediction System/model/heart_modell.sav','rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['heart'],
                           default_index=0)

#Heart Disease Prediction page

if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction using ML")
    
    #getting the input data
    #column for input data
    col1,col2,col3 = st.columns(3)
    
    age = st.text_input('Age of patient')
    sex = st.text_input('sex')
    chest_of_pain = st.text_input('Chest of pain type')
    Resting_BP = st.text_input('Trestbps')
    serum_chol = st.text_input('Cholesterol(mg/dL)')
    Fasting_blood_sugar = st.text_input('Fbs')
    Resting_electrocardiographic_result = st.text_input('Resting electrocardiographic result(Restecg)')
    Maximum_heart_rate = st.text_input(' Maximum heart rate(Thalach)')
    Exercise_induced_angina = st.text_input('Exercise induced angina(Exang)')
    Oldpeak = st.text_input('Oldpeak')
    slope = st.text_input('The slope of the peak exercise(slope)')
    num_of_vessels = st.text_input('Ca')
    Thalassemia = st.text_input('Thalassemia(Thal)')
    
    
    #code for prediction
    heart_diagnosis=''
    
    #created a button for prediction
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([ [age, sex,chest_of_pain,Resting_BP,serum_chol,Fasting_blood_sugar,Resting_electrocardiographic_result,Maximum_heart_rate,Exercise_induced_angina,Oldpeak,slope,num_of_vessels,Thalassemia] ])
    
        if heart_prediction[0] == 1 :
            heart_diagnosis= 'The Person have a heart Disease'
        else :
            heart_diagnosis= 'The Person does not have a heart Disease'
    st.success(heart_diagnosis)
    

    
