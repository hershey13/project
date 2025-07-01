import streamlit as st
from utils.crypto_utils import encrypt_message

st.set_page_config(page_title="🔒 Encrypt", layout="centered")

st.title("🔒 Enter Private Key & OTP to Encrypt")

private_key = st.text_area("🔏 Private Key")
otp = st.text_input("📨 OTP")

if st.button("🔐 Encrypt"):
    if private_key and otp:
        encrypted = encrypt_message(
            st.session_state.get("message", ""),
            st.session_state.get("password", ""),
            private_key,
            otp
        )
        st.success("Message Encrypted:")
        st.code(encrypted, language="text")
    else:
        st.warning("Please enter both Private Key and OTP")

if st.button("🔙 Back"):
    st.switch_page("Home")
