import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

components.html(
    f"""
    <script>window.location.href = 'https://hal9.com/chat'</script>
    """,
    height=800
)

from streamlit.components.v1 import html
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

open_page('https://hal9.com')
