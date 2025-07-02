import streamlit as st
from utils.api import verify_otp

st.set_page_config(page_title="🔓 Decrypt Message", layout="centered")
st.title("🔓 Step 3: Decrypt Message")

email = st.text_input("📧 Email")
private_key = st.text_area("🔐 Private Key")
otp = st.text_input("📨 OTP")

if st.button("🔓 Decrypt"):
    if email and private_key and otp:
        result = verify_otp(email, otp)
        if result["success"]:
            st.success("Decryption successful.")
            st.code("📩 [Simulated original message]", language="text")
        else:
            st.error(result["error"])
    else:
        st.warning("All fields required.")

