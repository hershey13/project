import streamlit as st
from utils.api import send_otp, log_input

st.set_page_config(page_title="🔐 Message Input", layout="centered")
st.title("🔐 Step 1: Enter Details")

email = st.text_input("📧 Email")
message = st.text_area("💬 Message")
password = st.text_input("🔑 Password", type="password")

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Submit"):
        if email and message and password:
            log_result = log_input(email, message, password)
            otp_result = send_otp(email)
            if log_result["success"] and otp_result["success"]:
                st.session_state["email"] = email
                st.session_state["message"] = message
                st.session_state["password"] = password
                st.success("OTP sent to your email.")
                st.switch_page("1_Encrypt")
            else:
                st.error(log_result.get("error") or otp_result.get("error"))
        else:
            st.warning("Please fill in all fields.")
with col2:
    if st.button("🧹 Clear All"):
        st.experimental_rerun()
