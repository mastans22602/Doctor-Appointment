# 🩺 Doctor Appointment Booking System

A full-stack automated appointment booking system built with **Streamlit** (frontend) and **n8n** (backend automation). Patients fill out a form, receive an instant email confirmation, and their details are logged to Google Sheets — all without any manual intervention.

---

## 🚀 Live Demo

👉 **[doctor-appointment-22602.streamlit.app](https://doctor-appointment-22602.streamlit.app)**

---

## ✨ Features

- **Instant Email Confirmation** — Patients receive a rich HTML email with their full appointment summary
- **Google Sheets Logging** — Every booking is automatically appended to a shared sheet
- **No Account Required** — Patients just fill the form and go
- **Responsive UI** — Clean dark UI with no scrolling, works on mobile and desktop
- **Real-time Webhook** — Streamlit POSTs to n8n webhook; automation handles the rest

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit (Python) |
| Automation | n8n (self-hosted via Docker + ngrok) |
| Email | Gmail via n8n Gmail node |
| Database | Google Sheets |
| Deployment | Streamlit Community Cloud |
| Tunnel | ngrok (free tier) |

---

## 📐 Architecture

```
Patient fills form (Streamlit)
        │
        ▼ POST /webhook/doctor-form
  n8n Webhook Node
        │
        ▼
  Code Node (JavaScript)
  └─ Extracts & structures form data
  └─ Builds HTML email body
        │
        ├──▶ Gmail Node
        │     └─ Sends confirmation email to patient
        │
        └──▶ Google Sheets Node
              └─ Appends row to "Appointment Details" sheet
```

---

## 📁 Project Structure

```
Doctor-Appointment/
├── app.py                  # Streamlit frontend
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── workflow/
    └── doctor_appointment_workflow.json   # n8n workflow export
```

---

## ⚙️ Setup & Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/mastans22602/Doctor-Appointment.git
cd Doctor-Appointment
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Locally

```bash
streamlit run app.py
```

### 4. Configure the Webhook URL

In `app.py`, update the webhook URL to your n8n instance:

```python
WEBHOOK_URL = "https://your-ngrok-domain.ngrok-free.app/webhook/doctor-form"
```

### 5. Set Up n8n Workflow

1. Open your n8n instance
2. Import `workflow/doctor_appointment_workflow.json`
3. Configure credentials:
   - **Gmail** — connect your Google account via OAuth
   - **Google Sheets** — connect your Google account via OAuth
4. Update the Google Sheets document ID to your own sheet
5. Activate the workflow

### 6. Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set `app.py` as the entry point
4. Deploy

---

## 🔧 n8n Workflow Nodes

| Node | Purpose |
|---|---|
| **Webhook** | Receives POST from Streamlit (`/webhook/doctor-form`) |
| **Code (JavaScript)** | Extracts form fields, builds HTML email body |
| **Gmail** | Sends confirmation email to patient |
| **Google Sheets** | Appends booking row to tracking sheet |

---

## 📧 Email Confirmation

Patients automatically receive an HTML email with:

- Appointment date & time slot
- Full contact details summary
- Address and problem description

---

## 📊 Google Sheets Schema

The workflow appends one row per booking with these columns:

| Name | Email | Contact | Problem | Appointment Date | Time Slot | Address |
|---|---|---|---|---|---|---|

---

## 🐳 n8n Self-Hosting (Docker + ngrok)

```bash
# Start n8n
docker compose up -d

# Start ngrok tunnel
ngrok http 5678
```

Update `WEBHOOK_URL` in `app.py` with your ngrok domain whenever it changes.

---

## 📦 Requirements

```
streamlit
requests
```

---

## 👤 Author

**Mastan**
- GitHub: [@mastans22602](https://github.com/mastans22602)
- Project: [Doctor-Appointment](https://github.com/mastans22602/Doctor-Appointment)

---

## 📄 License

MIT License — feel free to fork and adapt for your own use.
