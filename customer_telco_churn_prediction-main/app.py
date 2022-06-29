import tensorflow as tf
from tensorflow import keras
import streamlit as st
from keras.models import load_model 
import numpy as np 


st.title("Welcome to flower prediction app")
model=load_model('churn.h5')   

gender =(int)(st.number_input("enter gender"))
seniorcitizen=(int)(st.number_input("senior citizen"))
partner=(int)(st.number_input("partner"))
dependents=(int)(st.number_input("dependents"))
tenure=(float)(st.number_input("tenure"))
phoneservice=(int)(st.number_input("phoneservice"))
MultipleLines=(int)(st.number_input("MultipleLines"))
OnlineSecurity=(int)(st.number_input("OnlineSecurity"))
OnlineBackup=(int)(st.number_input("OnlineBackup"))
DeviceProtection=(int)(st.number_input("DeviceProtection"))
TechSupport=(int)(st.number_input("TechSupport"))
StreamingTV=(int)(st.number_input("StreamingTV"))
StreamingMovies=(int)(st.number_input("StreamingMovies")) 
InternetService=st.text_input("InternetService")#1
Contract=st.text_input("Contract") #2
PaymentMethod=st.text_input("PaymentMethod")#3
PaperlessBilling=(int)(st.number_input("PaperlessBilling"))
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

    



