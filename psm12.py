import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    strength = sum(criteria.values())

    if strength == 5:
        return "Very Strong 🔐", criteria
    elif strength == 4:
        return "Strong ✅", criteria
    elif strength == 3:
        return "Moderate ⚠️", criteria
    elif strength == 2:
        return "Weak ❌", criteria
    else:
        return "Very Weak 🚫", criteria

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter a password", type="password")

if password:
    strength_msg, details = check_password_strength(password)
    st.subheader(f"Strength: {strength_msg}")
    
    with st.expander("🔍 Check Details"):
        for criterion, passed in details.items():
            status = "✅" if passed else "❌"
            st.write(f"{status} {criterion.capitalize()}")

