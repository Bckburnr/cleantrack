# CleanTrack

CleanTrack is a lightweight GMP-compliant equipment calibration tracker built using Flask. It allows users to log, track, and manage calibration activities across pharmaceutical and biotech facilities.

---

## 🚀 Features

- Log equipment with due calibration dates
- View all calibration tasks in a simple dashboard
- Flask-based web app (easy to deploy internally)
- SQLite backend for lightweight tracking
- Built with GMP, 21 CFR Part 11, and audit-readiness in mind

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Jinja2 Templates
- SQLite
- HTML/CSS (Bootstrap Ready)

---

## 📸 Screenshot

![screenshot](https://via.placeholder.com/800x400.png?text=CleanTrack+Calibration+Dashboard)

_(Update this with your actual screenshot or leave it out)_

---

## 🧪 Use Case

Originally developed as a mock internal tool for use in FDA-regulated environments (pharma, biotech, labs). Could be extended to include:

- User login and permissions
- Audit trail (logging updates/deletions)
- Email reminders for upcoming or overdue calibrations
- PDF report generator for validation documentation

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Bckburnr/cleantrack.git
cd cleantrack
pip install -r requirements.txt
python app.py
