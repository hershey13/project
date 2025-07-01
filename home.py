import streamlit as st

st.set_page_config(page_title="🔐 Message Input", layout="centered")

st.title("🔐 Enter Message Details")

# Initialize session state
for key in ["email", "message", "password"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# Input fields
st.text_input("📧 Email", key="email")
st.text_area("💬 Message", key="message")
st.text_input("🔑 Password", type="password", key="password")

# Individual clear buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🧹 Clear Email"):
        st.session_state.email = ""
with col2:
    if st.button("🧹 Clear Message"):
        st.session_state.message = ""
with col3:
    if st.button("🧹 Clear Password"):
        st.session_state.password = ""

# Submit or Clear All
colA, colB = st.columns(2)
with colA:
    if st.button("✅ Submit"):
        if st.session_state.email and st.session_state.message and st.session_state.password:
            st.switch_page("1_encrypt")
        else:
            st.warning("Please fill in all fields.")
with colB:
    if st.button("❌ Clear All"):
        st.session_state.email = ""
        st.session_state.message = ""
        st.session_state.password = ""
