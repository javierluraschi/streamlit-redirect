import streamlit as st
from streamlit.components.v1 import html
 
st.title("Redirect")

my_js = """
alert("Hello World");
"""

my_html = f"<script>{my_js}</script>"

html(my_html)
