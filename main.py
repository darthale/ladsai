import streamlit as st
from home import home
from knowledge_graph import your_knowledge_graph


st.set_page_config(page_title="LADS", layout="wide")
col1, col2 = st.columns([1, 5])

with col1:
    st.image("img/logo.png", width=100)

with col2:
    st.title("LADS")
    st.subheader("Your network. Reimagined.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Your Knowledge Graph"))

# Display the selected page
if page == "Home":
    home()
elif page == "Your Knowledge Graph":
    your_knowledge_graph()