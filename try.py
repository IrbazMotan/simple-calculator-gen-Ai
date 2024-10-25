import streamlit as st
import numpy as np

# Streamlit App for Scientific Calculator
st.title("Scientific Calculator")

# User Input
expression = st.text_input("Enter your expression (e.g., 2+3*np.sqrt(4))")

# Scientific Operations
st.write("Scientific Functions Available:")
st.write("- np.sqrt(x): Square root")
st.write("- np.log(x): Natural logarithm")
st.write("- np.log10(x): Base 10 logarithm")
st.write("- np.exp(x): Exponential (e^x)")
st.write("- np.sin(x), np.cos(x), np.tan(x): Trigonometric functions (angle in radians)")
st.write("- np.arcsin(x), np.arccos(x), np.arctan(x): Inverse Trigonometric functions (output in radians)")

# Evaluate the Expression
def calculate_expression(expr):
    """Evaluate the expression entered by the user."""
    try:
        # Use eval safely by restricting it to numpy functions
        result = eval(expr, {"__builtins__": None, "np": np})
        return result
    except Exception as e:
        return f"Error: {e}"

# Calculate and Display Result
if expression:
    result = calculate_expression(expression)
    st.write("Result:", result)
