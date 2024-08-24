# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:50:42 2024

@author: Imsu lkr
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('C:/Users/Imsu lkr/Desktop/multiple disease/diabetes.sav','rb'))
parkenson_model = pickle.load(open("C:/Users/Imsu lkr/Desktop\multiple disease/parkinsons_model.sav",'rb'))
heart_model = pickle.load(open("C:/Users/Imsu lkr/Desktop/multiple disease/heart_model.sav", 'rb'))



#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsin Disease Prediction' ],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    

#diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes prediction using ML')
    
    #getting the input data from the user 
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
      
    with col2:
        Glucose = st.text_input('Glucose Level')
       
        
    with col3:
        BloodPressure = st.text_input('BloodPressure Value')
      
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        
    with col2:
        Age = st.text_input('Age')
       
        
    
  
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose, BloodPressure,SkinThickness, Insulin,BMI,
                                            DiabetesPedigreeFunction,Age ]])
        if (diab_pred[0] == 0):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease prediction using ML')
    
    
    age = st.text_input("enter number1")
    sex = st.text_input("enter number2")
    cp = st.text_input("enter number3")
    trestbps = st.text_input("enter number4")
    chol = st.text_input("enter number5")
    fbs = st.text_input("enter number6")
    restecg = st.text_input("enter number7")
    thalach = st.text_input("enter number8")
    exang = st.text_input("enter number9")
    oldpeak = st.text_input("enter number10")
    slope = st.text_input("enter number11")
    ca = st.text_input("enter number12")
    thal = st.text_input("enter number13")
    
    heart_diagnosis = ''
    if st.button('Heart test result'):
        heart_predict = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_predict[0]==0):
            heart_diagnosis = 'The pearson does not have heart disease'
        else:
            heart_diagnosis = 'The person has heart disease'
    st.success(heart_diagnosis)
    
if (selected == 'Parkinsin Disease Prediction'):
    
    #page title
    st.title('Parkinsin prediction using ML')
    
    
    MDVP_Fo = st.text_input('MDVP:FO')
    MDVP_Fhi = st.text_input('MDVP:Fhi')
    MDVP_Flo = st.text_input('MDVP:Flo')
    MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    MDVP_Jitter = st.text_input('MDVP:Jitter(Abs)')
    MDVP_RAP = st.text_input('MDVP:RAP')
    MDVP_PPQ = st.text_input('MDVP:PPQ')
    Jitter_DDP = st.text_input('Jitter:DDP')
    MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    MDVP_Shimmer = st.text_input('MDVP:Shimmer(dB)')
    Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    MDVP_APQ = st.text_input('NDVP:APQ')
    Shimmer_DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')

    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D@')
    PPE = st.text_input('PPE')
    
    park_diagnoses = ''
    if st.button('Parkinsin Result'):
        
        park_pred = parkenson_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter,MDVP_RAP,
                                              MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer,Shimmer_APQ3,
                                              Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,
                                              D2,PPE]])
        if (park_pred[0] == 0):
            park_pred = 'The person does not have Parkinsin'
        else:
            park_pred = 'The person has Parkinsin'
    st.success(park_diagnoses)

    