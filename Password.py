
import streamlit as st
import string

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2563EB;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #64748B;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Application heading
st.markdown(
    '<div class="main-title">🔐 Password Strength Checker</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Check your password security in seconds!</div>',
    unsafe_allow_html=True
)

st.write("")
st.info("Enter a password below to analyze its strength.")

# Password input (characters are hidden)
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type your password here"
)

if password:
    # Check password criteria
    checks = {
        "Minimum 8 characters": len(password) >= 8,
        "Uppercase letter (A-Z)": any(
            char.isupper() for char in password
        ),
        "Lowercase letter (a-z)": any(
            char.islower() for char in password
        ),
        "Number (0-9)": any(
            char.isdigit() for char in password
        ),
        "Special character (!@#$ etc.)": any(
            char in string.punctuation for char in password
        )
    }

    # Calculate score out of 5
    score = sum(checks.values())

    # Determine password strength
    if score <= 2:
        strength = "Weak"
        color = "red"
        progress_color = 0.25
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
        progress_color = 0.65
    else:
        strength = "Strong"
        color = "green"
        progress_color = 1.0

    # Display analysis
    st.subheader("📊 Password Strength Analysis")

    st.markdown(
        f"### Strength: :{color}[{strength}]"
    )

    st.metric("Password Strength Score", f"{score}/5")

    # Progress bar
    st.write("Strength Progress")
    st.progress(progress_color)

    # Checklist
    st.subheader("✅ Criteria Checklist")

    for criterion, passed in checks.items():
        if passed:
            st.success(f"✓ {criterion}")
        else:
            st.error(f"✗ {criterion}")

    # Suggestions for improvement
    failed_checks = [
        criterion for criterion, passed in checks.items()
        if not passed
    ]

    st.subheader("💡 Suggestions for Improvement")

    if not failed_checks:
        st.success(
            "Excellent! Your password meets all five criteria."
        )
        st.write(
            "For better security, use a unique password "
            "that is difficult to guess."
        )
    else:
        st.warning("Consider the following improvements:")
        for suggestion in failed_checks:
            st.write(f"• Add or satisfy: {suggestion}")

    # Final message
    if strength == "Weak":
        st.error("Your password is weak. Improve it before use.")
    elif strength == "Moderate":
        st.warning(
            "Your password is moderately strong. "
            "Try satisfying all five criteria."
        )
    else:
        st.success(
            "Your password satisfies all five strength criteria!"
        )

else:
    st.caption(
        "Your analysis will appear here after you enter a password."
    )

# Footer
st.divider()
st.caption("Created with Python and Streamlit | Project 4")
