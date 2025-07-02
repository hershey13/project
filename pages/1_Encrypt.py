import streamlit as st
from utils.api import verify_otp

st.set_page_config(page_title="🔒 Verify OTP", layout="centered")
st.title("🔒 Step 2: Enter OTP and Private Key")

if "email" not in st.session_state:
    st.warning("Please complete Step 1 first.")
    st.switch_page("Home")

private_key = st.text_area("🔐 Your Private Key")
otp = st.text_input("📨 OTP")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔐 Verify & Encrypt"):
        if private_key and otp:
            result = verify_otp(st.session_state["email"], otp)
            if result["success"]:
                st.success("OTP verified successfully.")
                st.code("🔒 [Simulated encryption done]", language="text")
            else:
                st.error(result["error"])
        else:
            st.warning("Please enter Private Key and OTP")
with col2:
    if st.button("🔙 Back"):
        st.switch_page("Home")
