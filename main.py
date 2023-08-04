import streamlit as st

NAME = "Eunice Patrina J"

description = """ Enthusiastic engineering graduate seeking for an opportunity in the field of software engineering 
to enhance my knowledge and skill while contributing to the growth of the company """

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpg")

with col2:
    st.title(NAME)
    st.write(description)
