import streamlit as st

name = "Eunice Patrina J"

description = """ Enthusiastic engineering graduate seeking for an opportunity in the field of software engineering 
to enhance my knowledge and skill while contributing to the growth of the company """

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(1.5, 0.5, 1.5)

with col1:
    st.image("images/profile.images")

with col2:
    st.header(NAME)
    st.write(description)
