import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path

st.title("Streamlit Redirect")

def inject_redirect():
    SR_ID = "streamlit_redirect"
    SR_JS = """
<script id="streamlit_redirect>
  window.location.href = 'https://hal9.com/';
</script>
"""

    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="lxml")
    if not soup.find(id=SR_ID):
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)
        else:
            shutil.copy(index_path, bck_index)
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + SR_JS)
        index_path.write_text(new_html)

inject_redirect()