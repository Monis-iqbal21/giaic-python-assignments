import streamlit as st
import re
import random

blacklist = ["password", "12345678", "hello123", "abc123", "password123", "admin", "monis123"]

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This is a commonly used and insecure password.")
        return 1, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is and get suggestions to improve it!")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.subheader("🔍 Password Analysis")
    for item in feedback:
        st.write(item)

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password - Try to make it stronger.")

    if score < 4:
        st.subheader("💡 Suggested Strong Password")
        st.code(generate_strong_password(), language="text")
