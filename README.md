# 🩺 Doctor Appointment Booking System

A full-stack appointment booking web app built with **Streamlit** for the frontend and **n8n** for backend automation — no traditional server required.

When a patient submits the form, the data is automatically:
- 📧 Sent as a confirmation email via **Gmail**
- 📊 Logged into a **Google Sheet** for record keeping

**Live Demo:** [doctor-appointment-22602.streamlit.app](https://doctor-appointment-22602.streamlit.app)

---

## ✨ Features

- Clean, modern UI with rich styling
- Patient form with full validation
- Instant email confirmation to patient
- Auto-logging to Google Sheets
- Fully automated via n8n workflow (no code backend)
- Deployable for free on Streamlit Cloud

---

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Frontend | Streamlit (Python) |
| Automation | n8n (self-hosted via Docker) |
| Tunnel | ngrok (exposes local n8n to internet) |
| Email | Gmail via n8n node |
| Database | Google Sheets via n8n node |
| Hosting | Streamlit Community Cloud |

---

## 📋 Form Fields

- **Full Name**
- **Email Address**
- **Contact Number**
- **Medical Problem** (dropdown)
- **Preferred Date**
- **Time Slot** (dropdown)
- **Address**

---

## 🏗️ Architecture

```
Patient fills form (Streamlit)
        │
        │ POST request (JSON)
        ▼
n8n Webhook (receives data)
        │
        ├──▶ Gmail Node → sends confirmation email to patient
        │
        └──▶ Google Sheets Node → logs appointment row
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Docker Desktop (for n8n)
- ngrok account (free tier works)
- Google account (for Gmail + Sheets)
- GitHub account

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
streamlit run doctor_appointment.py
```

App opens at `http://localhost:8501`

---

## ⚙️ n8n Workflow Setup

### Start n8n via Docker

```bash
docker-compose up -d
```

Access n8n at `http://localhost:5678`

### Start ngrok Tunnel

```bash
ngrok http 5678
```

Copy the public URL (e.g. `https://among-harbor-borough.ngrok-free.dev`)

### Create the Workflow in n8n

1. Add a **Webhook** node
   - HTTP Method: `POST`
   - Path: `doctor-form`

2. Add a **Gmail** node
   - Operation: Send
   - To: `{{ $('Webhook').item.json.body.email }}`
   - Subject: `Appointment Confirmed`
   - Body: HTML email with patient details

3. Add a **Google Sheets** node
   - Operation: Append Row
   - Map columns: `name`, `email`, `contact`, `problem`, `date`, `time_slot`, `address`

4. Click **Publish** to activate

### Update Webhook URL in Code

Open `doctor_appointment.py` and update line 6:

```python
N8N_WEBHOOK = "https://among-harbor-borough.ngrok-free.dev/webhook/doctor-form"
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"Create app"**
4. Select:
   - Repository: `mastans22602/Doctor-Appointment`
   - Branch: `main`
   - Main file: `doctor_appointment.py`
5. Click **Deploy**

Your app will be live at:
`https://doctor-appointment-22602.streamlit.app/`

---

## 📁 Project Structure

```
Doctor-Appointment/
│
├── doctor_appointment.py   # Main Streamlit app
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📦 Requirements

```
streamlit
requests
```

---

## 🔧 Environment Notes

- n8n runs locally via Docker and is exposed to the internet using ngrok
- The ngrok free tier provides a **persistent domain** (no URL changes on restart)
- Google Sheets and Gmail are connected via OAuth2 credentials in n8n
- Streamlit Cloud auto-redeploys whenever you push to the `main` branch

---

## 🗺️ n8n Field Mapping Reference

When mapping fields in n8n nodes, use these expressions:

```
Name        →  {{ $('Webhook').item.json.body.name }}
Email       →  {{ $('Webhook').item.json.body.email }}
Contact     →  {{ $('Webhook').item.json.body.contact }}
Problem     →  {{ $('Webhook').item.json.body.problem }}
Date        →  {{ $('Webhook').item.json.body.date }}
Time Slot   →  {{ $('Webhook').item.json.body.time_slot }}
Address     →  {{ $('Webhook').item.json.body.address }}
```

---

## 🙋 Author

**Mastan** — [@mastans22602](https://github.com/mastans22602)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
