from random import uniform
import streamlit as st

def unit_converter(value, unit_form, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }
    
    key = f"{unit_form}_{unit_to}"  # Generate a unique key for the conversion
    
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not available"

def main():
    st.title("Unit Converter")
    
    value = st.number_input("Enter the value to convert", min_value=0.0, format="%.4f")
    unit_form = st.selectbox("From", ["meter", "kilometer", "gram", "kilogram"])
    unit_to = st.selectbox("To", ["meter", "kilometer", "gram", "kilogram"])

    if st.button("Convert"):
        result = unit_converter(value, unit_form, unit_to)
        st.write(f"Converted Value: {result}")

if __name__ == "__main__":
    main()
