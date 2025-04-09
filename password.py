import streamlit as st
import re

# --- Password Strength Evaluation Function ---
def check_password_strength(password: str) -> dict:
    score = 0
    remarks = []

    # Length check
    if len(password) < 6:
        remarks.append("Password is too short (min 6 characters).")
    elif 6 <= len(password) < 10:
        remarks.append("Good, but try to make it 10+ characters.")
        score += 1
    else:
        score += 2

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters.")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    # Digits
    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add digits (0-9).")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Include special characters (!@#$...).")

    # Final strength label
    if score <= 3:
        strength = "Weak"
        color = "red"
    elif 4 <= score <= 6:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return {"score": score, "strength": strength, "color": color, "remarks": remarks}

# --- Streamlit App UI ---
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")

st.title("🔐 Password Strength Checker")
st.markdown("Check how strong your password is in real time!")

password = st.text_input("Enter your password", type="password")

if password:
    result = check_password_strength(password)

    st.markdown(f"**Strength:** :{result['color']}[{result['strength']}]")
    st.progress(min(result["score"], 7) / 7)

    if result["remarks"]:
        st.markdown("### 🔍 Suggestions to improve:")
        for remark in result["remarks"]:
            st.markdown(f"- {remark}")
else:
    st.info("Enter a password above to check its strength.")
