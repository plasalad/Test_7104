# -*- coding: utf-8 -*-
"""pages/4_Profile

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/122w_tMmtFz2OAWl04w8r4xNLDVyCwDnc
"""

import streamlit as st

st.set_page_config(page_title="User Profile", layout="wide")

st.markdown("<h1 style='text-align: center;'>User Profile</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Profile Information")
    st.write(f"**Name:** {st.session_state['user_data']['name']}")
    st.write(f"**Surname:** {st.session_state['user_data']['surname']}")
    st.write(f"**Telephone:** {st.session_state['user_data']['telephone']}")
    st.write(f"**Location:** {st.session_state['user_data']['location']}")
    st.write(f"**Skills:** {st.session_state['user_data']['skills']}")

with col2:
    st.subheader("Verification Status")
    if st.session_state['verification_status'] == 'approved':
        st.success("Your documents have been verified successfully!")
    else:
        st.warning("Verification pending.")

    st.write("**Uploaded Documents:**")
    for doc_type, doc_name in st.session_state['documents'].items():
        if doc_name:
            st.write(f"- {doc_type.replace('_', ' ').title()}: {doc_name}")

if st.button("Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.page_link("Home.py", label="Return to Home", icon="🏠")