import streamlit as st
import math

#create a class StreamlitCalculator with 4 different functions 
#(add, substract, divide,multiply)
class StreamlitCalculator: 

    def add(self,x,y):
        try:
            return x + y
        except ValueError:
            return "Error: Invalid input."
 
    def subtract(self,x,y):
        try:
            return x - y 
        except ValueError:
            return "Error: Invalid input."


    def multiply(self,x,y):
        try:
            return x*y 
    
        except ValueError:
            return "Error: Invalid input."

    def divide(self,x,y):
        try:
            return x/y 
        except ZeroDivisionError:
            return "Cannot divide by zero."
        except ValueError:
            return "Error: Invalid input."
        
    def square(self,x):
            
        return x*x
    
    def exponent(self,x,y):
        try:
            return x**y
        except ValueError:
            return "Error: Invalid input."
    
    def squareroot(self,x):
        try:
            return round(math.sqrt(x),3) #rounding to 3 decimals
        except ValueError:
            return "Error : Invalid input."

    def log(self,x,base=10):
        try:
            return math.log(x,base)
        except ValueError:
            return "Error: Input must be positive"
        


#streamlit user interface

# App starts
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")
st.title("Basic Calculator")

calculator = StreamlitCalculator()

# Input numbers
x = st.number_input("Enter first number", step=1, format="%d")
y = st.number_input("Enter second number", step=1, format="%d")

# Button layout with columns
 
result = None  # to store result

# Row 1: Basic operations
row1 = st.columns(4)
with row1[0]:
    if st.button("➕ Add"):
        result = calculator.add(x, y)
with row1[1]:
    if st.button("➖ Subtract"):
        result = calculator.subtract(x, y)
with row1[2]:
    if st.button("✖ Multiply"):
        result = calculator.multiply(x, y)
with row1[3]:
    if st.button("➗ Divide"):
        result = calculator.divide(x, y)

# Row 2: Extra functions
row2 = st.columns(4)
with row2[0]:
    if st.button("⬆ Exp (x^y)"):
        result = calculator.exponent(x,y)
with row2[1]:
    if st.button("🟰 Square (x²)"):
        result = calculator.square(x)
with row2[2]:
    if st.button("√ Square Root"):
        result = calculator.squareroot(x)
with row2[3]:
    if st.button("🔢 Log10"):
        result = calculator.log(x, 10)

# Show result
if result is not None:
    st.markdown(f"<h4 style='color: green;'>Result: {result}</h4>", unsafe_allow_html=True)