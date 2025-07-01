import streamlit as st
from utils.crypto_utils import decrypt_message

st.set_page_config(page_title="🔓 Decrypt", layout="centered")

st.title("🔓 Decrypt Message")

email = st.text_input("📧 Email")
private_key = st.text_area("🔏 Private Key")
otp = st.text_input("📨 OTP")

if st.button("🧩 Decrypt"):
    if email and private_key and otp:
        decrypted = decrypt_message("SIMULATED_ENCRYPTED_MESSAGE", private_key, otp)
        st.success("Decrypted Message:")
        st.code(decrypted, language="text")
    else:
        st.warning("Please fill in all fields.")
