import streamlit as st
import pandas as pd
 
my_js = """
alert("Hello World");
"""

my_html = f"<script>{my_js}</script>"

html(my_html)
