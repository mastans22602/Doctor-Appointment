import streamlit as st
import requests
from datetime import date

# ── n8n Webhook URL ───────────────────────────────────────────────────────────
N8N_WEBHOOK = "https://among-harbor-borough.ngrok-free.dev/webhook/doctor-form"

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Doctor Appointment", page_icon="🩺", layout="centered")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

/* ── Root reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
.stApp {
    background: linear-gradient(135deg, #f0f4ff 0%, #fdf0f0 50%, #f0f8ff 100%);
    min-height: 100vh;
}

/* ── Card wrapper ── */
.card {
    background: #ffffff;
    border-radius: 24px;
    padding: 48px 44px 44px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.08), 0 2px 12px rgba(235,100,80,0.06);
    max-width: 560px;
    margin: 40px auto 0;
    border: 1px solid rgba(255,255,255,0.9);
}

/* ── Header area ── */
.header-icon {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 6px;
}
.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #1a1a2e;
    text-align: center;
    margin: 0;
    letter-spacing: -0.5px;
}
.header-sub {
    font-size: 0.9rem;
    color: #8a8fa8;
    text-align: center;
    margin: 6px 0 32px;
    font-weight: 400;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #e8ecf8, transparent);
    margin: 0 0 28px;
}

/* ── Section label ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #eb6450;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin: 24px 0 14px;
}

/* ── Field labels ── */
label[data-testid="stWidgetLabel"] p,
.stTextInput label, .stSelectbox label,
.stDateInput label, .stTextArea label {
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    color: #3d4168 !important;
    letter-spacing: 0.3px;
    margin-bottom: 4px !important;
}

/* ── Input fields ── */
.stTextInput input, .stTextArea textarea {
    border: 1.5px solid #e2e6f3 !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 0.92rem !important;
    color: #1a1a2e !important;
    background: #fafbff !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #eb6450 !important;
    box-shadow: 0 0 0 3px rgba(235,100,80,0.12) !important;
    background: #ffffff !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    border: 1.5px solid #e2e6f3 !important;
    border-radius: 12px !important;
    background: #fafbff !important;
    font-size: 0.92rem !important;
}
.stSelectbox > div > div:focus-within {
    border-color: #eb6450 !important;
    box-shadow: 0 0 0 3px rgba(235,100,80,0.12) !important;
}

/* ── Date input ── */
.stDateInput input {
    border: 1.5px solid #e2e6f3 !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    font-size: 0.92rem !important;
    background: #fafbff !important;
}
.stDateInput input:focus {
    border-color: #eb6450 !important;
    box-shadow: 0 0 0 3px rgba(235,100,80,0.12) !important;
}

/* ── Submit button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #eb6450 0%, #d94f3a 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 16px 24px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    cursor: pointer !important;
    margin-top: 10px !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 4px 18px rgba(235,100,80,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(235,100,80,0.45) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Success / Error banner ── */
.stAlert {
    border-radius: 12px !important;
}

/* ── Two-column row spacing ── */
[data-testid="column"] {
    padding: 0 6px !important;
}

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── Card open ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)

# Header
st.markdown('<div class="header-icon">🩺</div>', unsafe_allow_html=True)
st.markdown('<h1 class="header-title">Doctor Appointment</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-sub">Please fill the form with your details</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Personal Info section ─────────────────────────────────────────────────────
st.markdown('<div class="section-label">Personal Info</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", placeholder="e.g. John Doe")
with col2:
    email = st.text_input("Email Address", placeholder="you@email.com")

contact = st.text_input("Contact Number", placeholder="+91 98765 43210")

# ── Appointment Details section ───────────────────────────────────────────────
st.markdown('<div class="section-label">Appointment Details</div>', unsafe_allow_html=True)

problem = st.selectbox("Medical Problem", [
    "Select an option ...",
    "General Checkup",
    "Fever / Cold",
    "Chest Pain",
    "Back / Joint Pain",
    "Skin Issue",
    "Mental Health",
    "Diabetes / Blood Sugar",
    "Blood Pressure",
    "Eye / ENT",
    "Other",
])

col3, col4 = st.columns(2)
with col3:
    appt_date = st.date_input("Preferred Date", min_value=date.today())
with col4:
    time_slot = st.selectbox("Time Slot", [
        "Select a slot ...",
        "09:00 AM", "10:00 AM", "11:00 AM",
        "12:00 PM", "02:00 PM", "03:00 PM",
        "04:00 PM", "05:00 PM",
    ])

address = st.text_area("Address", placeholder="House No, Street, City, State", height=90)

# ── Submit ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
submitted = st.button("Book Appointment →")

if submitted:
    errors = []
    if not name.strip():
        errors.append("Full Name is required.")
    if not email.strip() or "@" not in email:
        errors.append("A valid Email is required.")
    if not contact.strip():
        errors.append("Contact Number is required.")
    if problem == "Select an option ...":
        errors.append("Please select a Medical Problem.")
    if time_slot == "Select a slot ...":
        errors.append("Please choose a Time Slot.")
    if not address.strip():
        errors.append("Address is required.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        payload = {
            "name": name,
            "email": email,
            "contact": contact,
            "problem": problem,
            "date": str(appt_date),
            "time_slot": time_slot,
            "address": address,
        }
        try:
            response = requests.post(N8N_WEBHOOK, json=payload, timeout=10)
            if response.status_code == 200:
                st.success(
                    f"✅ Appointment booked for **{name}** on **{appt_date.strftime('%d %b %Y')}** "
                    f"at **{time_slot}**. A confirmation will be sent to **{email}**."
                )
            else:
                st.error(f"⚠️ Submission failed. Server returned status: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Could not reach server: {e}")

st.markdown('</div>', unsafe_allow_html=True)
