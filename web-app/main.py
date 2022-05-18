import numpy as np
import pickle
import streamlit as st
from PIL import Image



# loading the saved model
loaded_model = pickle.load(open("C:/Users/ilham/Notebook/Used car price prediction/Web App/model/lr_model.sav", 'rb'))


# creating a function for Prediction
def used_car_price_prediction_with_sav(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return f"The price will be around ${round(prediction[0],2)}" 

# def used_car_price_prediction_with_pmml(input_data):
#     input_data = np.asarray(input_data)
#     prediction = loaded_model.predict({
#       "km_driven" : input_data[0],
#       "mileage" : input_data[1],
#       "engine" : input_data[2],
#       "max_power" : input_data[3],
#       "seats" : input_data[4],
#       "age" : input_data[5],
#       "fuel_CNG" : input_data[6],
#       "fuel_Diesel" : input_data[7],
#       "fuel_LPG" : input_data[8],
#       "fuel_Petrol" : input_data[9],
#       "seller_type_Dealer" : input_data[10],
#       "seller_type_Individual" : input_data[11],
#       "transmission_Automatic" : input_data[12],
#       "transmission_Manual" : input_data[13],
#       "owner_First.Owner" : input_data[14],
#       "owner_Fourth...Above.Owner" : input_data[15],
#       "owner_Second.Owner" : input_data[16],
#       "owner_Third.Owner" : input_data[17]
#     })
#     print(prediction)
#     return f"The price will be around ${round(prediction[0],2)}"  
    
  
def main():
    
    st.set_page_config(layout='wide', page_title="INPO MASZEEHHH", page_icon="🚗")

    # giving a title
    header = Image.open('web-app/images/header2.png')
  
    st.image(header)
    st.title('Used Car Price Prediction Web App')
    
    # getting the input data from the user
        
    km_driven = st.text_input("KM Driven")
    mileage = st.slider('Mile Age (Kilometres per Litre)', min_value=10, max_value=40,value=13,step=1)
    engine = st.slider('Engine (CC)', min_value=800, max_value=2700,value=1200,step=100)
    max_power = st.slider('Max Power (Brake Horse Power)', min_value=45, max_value=180,value=80,step=5)
    seats = st.select_slider("Seats", [2,4,5,6,7,8,9,10,14], value=5)
    year = st.slider('Year', min_value=1997, max_value=2022,value=2007,step=1)
    fuel = st.selectbox('Fuel', ('Diesel','LPG','Petrol','CNG'))
    seller_type = st.selectbox("Type of Seller",('Dealer', 'Individual'))
    transmission = st.selectbox("Transmission",("Automatic","Manual"))
    owner = st.selectbox("Type Owner",("First Owner","Second Owner","Third Owner","Fourth and Above Owner"))

    
    # code for Prediction
    price = 'In Data We Believe...'
    
    # transforming data
    if year!="":
      age = 2022 - int(float(year))

    fuel_Diesel = 0
    fuel_LPG = 0
    fuel_Petrol = 0
    fuel_CNG = 0
    if fuel=='Diesel':
      fuel_Diesel = 1
    elif fuel=="LPG":
      fuel_LPG = 1
    elif fuel=="Petrol":
      fuel_Petrol = 1
    elif fuel == "CNG":
      fuel_CNG = 1

    seller_type_Individual = 0
    seller_type_Dealer = 0
    if seller_type=="Individual":
      seller_type_Individual = 1
    elif seller_type=="Dealer":
      seller_type_Dealer = 1

    transmission_Manual = 0
    transmission_Automatic = 0
    if transmission=="Manual":
      transmission_Manual = 1
    elif transmission=="Automatic":
      transmission_Automatic = 1

    owner4th = 0
    owner3rd = 0
    owner2nd = 0
    owner1st = 0
    if owner=="Fourth and Above Owner":
      owner4th = 1
    elif owner=="Third Owner":
      owner3rd = 1
    elif owner=="Second Owner":
      owner2nd = 1
    elif owner == "First Owner":
      owner1st = 1

    


    # creating a button for Prediction
    
    if st.button('Price Prediction'):
        price = used_car_price_prediction_with_sav([km_driven, mileage, engine, max_power, seats, age, fuel_CNG, fuel_Diesel, fuel_LPG, seller_type_Dealer, transmission_Automatic, owner1st, owner4th, owner2nd])
        # price = used_car_price_prediction_with_pmml([km_driven, mileage, engine, max_power, seats, age,fuel_CNG, fuel_Diesel, fuel_LPG, fuel_Petrol, seller_type_Dealer, seller_type_Individual, transmission_Automatic, transmission_Manual, owner1st, owner4th, owner2nd, owner3rd])
        
        
    st.success(price)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
