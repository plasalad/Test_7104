# -*- coding: utf-8 -*-
"""pages/1_Registration

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jk_wbQ56j592xfRJB-zKd6qwuBu2v0SY
"""

import streamlit as st

st.set_page_config(page_title="User Registration", layout="wide")

if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {
        'name': '',
        'surname': '',
        'telephone': '',
        'location': '',
        'skills': ''
    }

st.markdown("<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True)

with st.form("registration_form"):
    st.session_state['user_data']['name'] = st.text_input("Name", value=st.session_state['user_data']['name'])
    st.session_state['user_data']['surname'] = st.text_input("Surname", value=st.session_state['user_data']['surname'])
    st.session_state['user_data']['telephone'] = st.text_input("Telephone number", value=st.session_state['user_data']['telephone'])
    st.session_state['user_data']['location'] = st.text_input("Location (Work Area)", value=st.session_state['user_data']['location'])
    st.session_state['user_data']['skills'] = st.text_area("Skills", value=st.session_state['user_data']['skills'])

    submitted = st.form_submit_button("Continue to Document Upload")
    if submitted:
        st.page_link("pages/2_Documents.py", label="Continue to Document Upload", icon="📂")