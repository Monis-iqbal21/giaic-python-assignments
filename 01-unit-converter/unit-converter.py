import streamlit as st

st.title("Unit Converter")

categories = st.selectbox("",
    ("Length", "Weight", "Temperature", "Area", "Volume", "Time")
)

units = {
    "Length": ["centimeter", "meter", "kilometer"],
    "Weight": ["gram", "kilogram", "ton"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["square meter", "square kilometer", "hectare"],
    "Volume": ["millilitre", "litre", "cubic meter"],
    "Time": ["second", "minute", "hour"]
}

user_unit = st.selectbox("From Unit", units[categories])
convert_to = st.selectbox("To Unit", units[categories])
value = st.number_input("Enter Value")


def convert(category, value, user_unit, convert_to):
    if category == "Length":
        factor = {
            "centimeter": 0.01,
            "meter": 1,
            "kilometer": 1000
        }
        return value * factor[user_unit] / factor[convert_to]

    elif category == "Weight":
        factor = {
            "gram": 0.001,
            "kilogram": 1,
            "ton": 1000
        }
        return value * factor[user_unit] / factor[convert_to]

    elif category == "Area":
        factor = {
            "square meter": 1,
            "square kilometer": 1_000_000,
            "hectare": 10_000
        }
        return value * factor[user_unit] / factor[convert_to]

    elif category == "Volume":
        factor = {
            "millilitre": 0.001,
            "litre": 1,
            "cubic meter": 1000
        }
        return value * factor[user_unit] / factor[convert_to]

    elif category == "Time":
        factor = {
            "second": 1,
            "minute": 60,
            "hour": 3600
        }
        return value * factor[user_unit] / factor[convert_to]

    elif category == "Temperature":
        if user_unit == convert_to:
            return value

        if user_unit == "Celsius":
            if convert_to == "Fahrenheit":
                return (value * 9/5) + 32
            elif convert_to == "Kelvin":
                return value + 273.15

        elif user_unit == "Fahrenheit":
            if convert_to == "Celsius":
                return (value - 32) * 5/9
            elif convert_to == "Kelvin":
                return (value - 32) * 5/9 + 273.15

        elif user_unit == "Kelvin":
            if convert_to == "Celsius":
                return value - 273.15
            elif convert_to == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    return None


if st.button("Convert"):
    result = convert(categories, value, user_unit, convert_to)
    if result is not None:
        st.success(f"{value} {user_unit}  =  {result:.2f} {convert_to}")
    else:
        st.error("Error while Conversion")
