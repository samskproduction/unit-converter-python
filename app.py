import streamlit as st
import os

class UnitConverter:
    def __init__(self):
        self.length_units = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }
        
        self.weight_units = {
            'mg': 0.000001,
            'g': 0.001,
            'kg': 1.0,
            'oz': 0.0283495,
            'lb': 0.453592,
            'ton': 907.185
        }
        
        self.volume_units = {
            'ml': 0.001,
            'l': 1.0,
            'gal': 3.78541,
            'qt': 0.946353,
            'pt': 0.473176,
            'fl_oz': 0.0295735
        }
    
    def convert(self, value, from_unit, to_unit, measurement_type):
        if measurement_type == 'length':
            return value * self.length_units[from_unit] / self.length_units[to_unit]
        elif measurement_type == 'weight':
            return value * self.weight_units[from_unit] / self.weight_units[to_unit]
        elif measurement_type == 'volume':
            return value * self.volume_units[from_unit] / self.volume_units[to_unit]
        return value

def format_number(value):
    return f"{value:,.4f}" if value >= 1 else f"{value:.4f}"

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")
    converter = UnitConverter()
    
    st.title("📏 Unit Converter")
    
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=0.1, format="%.4f")
    from_unit = st.selectbox("From:", list(converter.length_units.keys()))
    to_unit = st.selectbox("To:", list(converter.length_units.keys()))
    
    result = converter.convert(value, from_unit, to_unit, 'length')
    
    st.markdown(f"### Result: {format_number(value)} {from_unit} = {format_number(result)} {to_unit}")

if __name__ == "__main__":
    main()
