import numpy as np
import streamlit as st
from PIL import Image
import rpy2
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

r = robjects.r('dir.create(Sys.getenv("R_LIBS_USER"), recursive = TRUE)')  # create personal library
r = robjects.r('.libPaths(Sys.getenv("R_LIBS_USER"))')

# r = robjects.r('install.packages("https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-14.tar.gz", repos=NULL, type="source")')
r = robjects.r('library(randomForest)')


# loading the saved model

loaded_model = robjects.r('model = readRDS(".//web-app//model//rf_model.rda")')


# creating a function for Prediction

def used_car_price_prediction(km_driven, mileage, engine, max_power, seats, year, fuel, seller_type, transmission, owner):
    # transforming data
    if year!="":
      age = 2022 - int(float(year))

    fuel_Diesel = 0
    fuel_LPG = 0
    fuel_CNG = 0
    if fuel=='Diesel':
      fuel_Diesel = 1
    elif fuel=="LPG":
      fuel_LPG = 1
    elif fuel == "CNG":
      fuel_CNG = 1

    
    seller_type_Dealer = 0
    if seller_type=="Dealer":
      seller_type_Dealer = 1

    
    transmission_Automatic = 0
    if transmission=="Automatic":
      transmission_Automatic = 1

    owner4th = 0
    owner2nd = 0
    owner1st = 0
    if owner=="Fourth and Above Owner":
      owner4th = 1
    elif owner=="Second Owner":
      owner2nd = 1
    elif owner == "First Owner":
      owner1st = 1
    
    data = f"new_data = data.frame(km_driven={km_driven},mileage={mileage},engine={engine},max_power={max_power},seats={seats},age={age},fuel_CNG={fuel_CNG},fuel_Diesel={fuel_Diesel},fuel_LPG={fuel_LPG},seller_type_Dealer={seller_type_Dealer},transmission_Automatic={transmission_Automatic},owner_First.Owner={owner1st},owner_Fourth...Above.Owner={owner4th},owner_Second.Owner={owner2nd})"
    robjects.r(data)
    result = robjects.r(f'predict(model, new_data)')
    amount = int(result[0])
    price = "IDR {:,.2f}".format(amount)
    return (f"The price will be around {price}")
    
  
def main():
    
    st.set_page_config(layout='wide', page_title="INPO MOBIL", page_icon="👀")

    # giving a title
    header = Image.open("./web-app/images/header2.png")
  
    st.image(header)
    st.title('Used Car Price Prediction Web App')
    
    # getting the input data from the user
        
    
    mileage = st.slider('Mile Age (Kilometres per Litre)', min_value=10, max_value=40,value=13,step=1)
    engine = st.slider('Engine (CC)', min_value=800, max_value=2700,value=1200,step=100)
    max_power = st.slider('Max Power (Brake Horse Power)', min_value=45, max_value=180,value=80,step=5)
    seats = st.select_slider("Seats", [2,4,5,6,7,8,9,10,14], value=5)
    year = st.slider('Year', min_value=1997, max_value=2022,value=2007,step=1)
    fuel = st.selectbox('Fuel', ('Diesel','Petrol','LPG','CNG'))
    seller_type = st.selectbox("Type of Seller",('Dealer', 'Individual'))
    transmission = st.selectbox("Transmission",("Automatic","Manual"))
    owner = st.selectbox("Type Owner",("First Owner","Second Owner","Third Owner","Fourth and Above Owner"))
    km_driven = st.text_input("KM Driven",0)
   
    # code for Prediction
    price = 'Make sure the input value is correct'
    
    # creating a button for Prediction

    if st.button('Price Prediction'):

        price = used_car_price_prediction(km_driven, mileage, engine, max_power, seats, year, fuel, seller_type, transmission, owner)
        
    st.success(price)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
