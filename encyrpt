import streamlit as st

st.set_page_config(page_title="Enter Key and OTP")

st.title("🔐 Encryption Inputs")

private_key = st.text_area("🔏 Private Key")
otp = st.text_input("📨 OTP")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔒 Encrypt"):
        st.success("Message Encrypted (simulate here)")
with col2:
    if st.button("🔙 Back"):
        st.switch_page("Home.py")
