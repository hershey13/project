import streamlit as st

st.set_page_config(page_title="Encrypt Message")

st.title("🔐 Message Input")

if "email" not in st.session_state:
    st.session_state["email"] = ""
if "message" not in st.session_state:
    st.session_state["message"] = ""
if "password" not in st.session_state:
    st.session_state["password"] = ""

def clear_field(field):
    st.session_state[field] = ""

st.text_input("📧 Email", key="email")
st.button("Clear Email", on_click=clear_field, args=["email"])

st.text_area("💬 Message", key="message")
st.button("Clear Message", on_click=clear_field, args=["message"])

st.text_input("🔑 Message Password", type="password", key="password")
st.button("Clear Password", on_click=clear_field, args=["password"])

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Submit"):
        st.switch_page("Encrypt.py")
with col2:
    if st.button("🧹 Clear All"):
        for key in ["email", "message", "password"]:
            st.session_state[key] = ""
