import streamlit as st
st.title("Unit Convertor App")
st.markdown("# Converts Length, Weight and Time units instantly.")
st.write("Welcome! Select a category, enter a value and get the converted result.")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

def convert_units(category,value,unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084

        

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462    
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        elif unit == "Kilograms to grams":
            return value * 1000
        elif unit == "Grams to kilograms":
            return value / 1000


    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60   
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        


if category == "Length":
    unit = st.selectbox("Select a unit", ["kilometers to miles", "Miles to kilometers", "Meters to feet", "Feet to meters"])       

elif category == "Weight":
    unit = st.selectbox("Select a unit", ["Kilograms to pounds", "Pounds to kilograms", "Kilograms to grams", "Grams to kilograms"])

elif category == "Time":
    unit = st.selectbox("Select a unit", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])    

value = st.number_input("Enter a value to convert")

if st.button("Convert"):
    result = convert_units(category,value,unit)
    st.success(f"The result is {result:.2f}")
