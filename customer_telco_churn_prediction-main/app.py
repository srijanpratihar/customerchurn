import tensorflow as tf
from tensorflow import keras
import streamlit as st
from keras.models import load_model 
import numpy as np 


st.title("Welcome to flower prediction app")
model=load_model('churn.h5')   

gender=st.selectbox('select gender',('Male','Female'))
if(gender=='Male'):
        gender=0
else:
        gender=1
seniorcitizen=st.selectbox('select senior citizen or not',('Yes','No'))
if(seniorcitizen=='Yes'):
        seniorcitizen=1
else:
        seniorcitizen=0
partner=st.selectbox('do you have a partner',('Yes','No'))
if(partner=='Yes'):
        partner=1
else:
        partner=0
dependents=st.selectbox('do you have any dependents',('Yes','No'))
if(dependents=='Yes'):
        dependents=1
else:
        dependents=0
tenure=(float)(st.number_input("enter your tenure"))

phoneservice=st.selectbox('do you have phone service',('Yes','No'))
if(phoneservice=='Yes'):
        phoneservice=1
else:
        phoneservice=0
MultipleLines=st.selectbox('do you have multiple lines',('Yes','No'))
if(MultipleLines=='Yes'):
        MultipleLines=1
else:
        MultipleLines=0
OnlineSecurity=st.selectbox('do you have online security',('Yes','No'))
if(OnlineSecurity=='Yes'):
        OnlineSecurity=1
else:
        OnlineSecurity=0
OnlineBackup=st.selectbox('do you have online backup',('Yes','No'))
if(OnlineBackup=='Yes'):
        OnlineBackup=1
else:
        OnlineBackup=0
DeviceProtection=st.selectbox('do you have Device protection',('Yes','No'))
if(DeviceProtection=='Yes'):
        DeviceProtection=1
else:
        DeviceProtection=0
TechSupport=st.selectbox('do you have tech support',('Yes','No'))
if(TechSupport=='Yes'):
        TechSupport=1
else:
        TechSupport=0
StreamingTV=st.selectbox('do you stream TV',('Yes','No'))
if(StreamingTV=='Yes'):
        StreamingTV=1
else:
        StreamingTV=0
StreamingMovies=st.selectbox('do you stream Movies',('Yes','No'))
if(StreamingMovies=='Yes'):
        StreamingMovies=1
else:
        StreamingMovies=0
InternetService=st.text_input("InternetService")#1
Contract=st.text_input("Contract") #2
PaymentMethod=st.text_input("PaymentMethod")#3
PaperlessBilling=st.selectbox('do you have paperless Billing',('Yes','No'))
if(PaperlessBilling=='Yes'):
        PaperlessBilling=1
else:
        PaperlessBilling=0
MonthlyCharges=(float)(st.number_input("MonthlyCharges"))
TotalCharges=(float)(st.number_input("TotalCharges"))




        
        #1
if(InternetService=="DSL"):
    internet=[1,0,0]
elif(InternetService=="Fiber optic"):
    internet=[0,1,0] 
else:
    internet=[0,0,1]    
#2

if(Contract=="Month-to-month"):
    cont=[1,0,0]
elif(Contract=="One year"):
    cont=[0,1,0] 
else:
    cont=[0,0,1]   
#3
if(PaymentMethod=="Bank transfer (automatic)"):
    transfer=[1,0,0,0]
elif(Contract=="Credit card (automatic)"):
    transfer=[0,1,0,0] 
elif(Contract=="Electronic check"):
    transfer=[0,0,1,0] 
else:
    transfer=[0,0,0,1]  

tenure=(tenure-1)/71
MonthlyCharges=(MonthlyCharges-18.25)/(118.75-18.25)
TotalCharges=(TotalCharges-18.8)/(8684.8-18.8)
btn = st.button("predict")
if btn:
    prediction=model.predict(np.array([[gender,seniorcitizen,partner,dependents,tenure,phoneservice,MultipleLines,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,PaperlessBilling,MonthlyCharges,TotalCharges,internet[0],internet[1],internet[2],cont[0],cont[1],cont[2],transfer[0],transfer[1],transfer[2],transfer[3]]]))      
    if(prediction[0][0]>0.5):
        value="The customer will leave the company"
        st.subheader(value)
    else:
        value="The customer will not leave the company"  
        st.subheader(value)  

    



