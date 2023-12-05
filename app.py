import streamlit as st
from streamlit.components.v1 import html
import pathlib
import shutil
from bs4 import BeautifulSoup

st.title("Redirect")

def inject_redirect():
    SR_ID = "streamlit_redirect"
    SR_JS = """
<script id="streamlit_redirect>
  window.location.href = 'https://hal9.com/';
</script>
"""
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    with open(index_path, 'r') as file:
    	file_contents = file.read()
    if not 'streamlit_redirect' in file_contents:
    	file_contents = file_contents.replace('<body>', '<body>' + SR_JS)
    	with open(index_path, 'w') as file:
    		file.write(file_contents)

inject_redirect()