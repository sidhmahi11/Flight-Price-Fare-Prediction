# Helpdesk Support Automation System 🛠️

A web-based IT support ticketing system built using Python and Streamlit. The project simulates real-world ITSM workflows like ticket creation, status tracking, and SLA management.

---

## 🔍 Features
- 🎫 Submit new helpdesk tickets with title, description, and priority
- 📊 View and manage all submitted tickets
- 🔄 Update ticket statuses (Open → In Progress → Resolved)
- 💾 Local storage with SQLite for persistence
- 🧠 Simulates basic ITSM functionality for IT Analyst/Support scenarios

---

## 🚀 Live Demo

👉 [Click to View App](https://sidhmahi11-helpdesk-automation-system-app-na2771.streamlit.app)

---


## 🧰 Tech Stack
- Python
- Streamlit
- SQLite
- GitHub
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Folder Structure
```
helpdesk-automation-system/
├── app.py                # Main Streamlit interface
├── ticket_handler.py     # Ticket logic (create, view, update)
├── requirements.txt      # Dependencies (streamlit only)
├── README.md             # Documentation
└── tickets.db            # SQLite file auto-created on first run
```

---

## ✨ Output Example

When a user submits a ticket:
- It is added to a SQLite database with **status: Open**
- Can be tracked in “View Tickets” tab
- Can be updated using Ticket ID to “In Progress” or “Resolved”

```
Ticket ID: 1
Title: Wi-Fi Not Working
Priority: High
Status: Open → In Progress → Resolved
```

---

## 🧑‍💻 Author
**Siddhant Jain**  
📧 siddhantjain261@gmail.com  
🔗 [GitHub](https://github.com/sidhmahi11/helpdesk-automation-system)

---

## 🏆 Why This Project?
This project was built to demonstrate:
- Real-world problem-solving in IT support roles
- Ticketing system logic for an IT Analyst job
- Deployment skills (Streamlit, GitHub)

---

## 📌 Ideal For:
- IT Analyst Resume Projects  
- Technical Support Portfolio  
- Entry-level ITSM Simulations
