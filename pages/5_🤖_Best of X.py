import streamlit as st
import pandas as pd


st.set_page_config(
    page_icon="🤖",
    page_title="Best of X",
    layout="wide",
)
st.header("Best of X")
st.markdown("Best of X falls under **Awareness** category of Automobiles Industry. ",help="[Press Information Bureau Ministry of Information and Broadcasting  Government of India](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2023/feb/doc2023217160601.pdf)")
st.markdown("Every Car is amazing in it's own way some has great mileage or some has great power. Dream Car provides you a platform where you can find which car is suitable for your needs you can compare cars and choose your Dream Car. The below metrices are taken from study from [Automobile application](https://www.auto-data.net/en/)")

feul_types = ["CNG","Electric","Petrol","Diesel"]
feul_type = st.multiselect("What feul type car do you want ",feul_types)

body_types = ["SUV","Sedan","Hatchback","MUV","Minivan","Pickup Truck","Coupe","Convertible","Luxury","Wagon"]
body_type = st.multiselect("What type of body do you want", body_types)

seating_capacities =[2,4,5,6,8]
seating = st.radio("No. of Seats you require",seating_capacities)


min_amount = st.slider("Minimum Amount ",min_value=200000, max_value=1000000)
max_amount = st.slider("Maximum Amount ",min_value= 1000000,max_value=90000000)

mileages =["10 km/l","20 km/l","30 km/l","40 km/kg","300 km/Charge","400 km/Charge","500 km/Charge","600 km/Charge","700 km/Charge","800 km/Charge","900 km/Charge"]
mileage = st.multiselect("Max mileage for the car",mileages)

max_power = st.number_input("Maximum Power ",max_value=800,min_value=0)

transmissions = ["Automatic","Manual"]
transmission = st.multiselect("Transmission types are :",transmissions)

value = st.button("Submit")

sheet_name = "data"
sheet_id = "1IN1YCm8DcLIgxY73ZmakN8m3SplYv8wb"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df = pd.read_csv(url, dtype=str)

def foo():

    filtered_df = df[(df["fuel_type"].isin(feul_type)) & (df["body_type"].isin(body_type)) & (df["transmission_type"].isin(transmission)) & (df.seating_capacity == seating)]
    filtered_df = filtered_df[(filtered_df["max_power_bhp"] < max_power) & (filtered_df["max_power_bhp"] > (max_power - 100))]
    mileages_numeric = [int(mileage.split()[0]) for mileage in mileages]


    filtered_df = filtered_df[filtered_df["fuel_eff"] <= max(mileages_numeric)]
    has_min = filtered_df["starting_price"] >= min_amount
    has_max = filtered_df["ending_price"] <= max_amount
    st.write(filtered_df[has_min & has_max])

    st.area_chart(data=filtered_df)
      
    

if(value):
    foo()


