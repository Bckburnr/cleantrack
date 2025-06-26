# CleanTrack

![Flask App](https://img.shields.io/badge/built%20with-Flask-blue)
![License](https://img.shields.io/badge/license-MIT-green)

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

![CleanTrack Screenshot](https://github.com/Bckburnr/cleantrack/blob/main/Calibration%20tracker.png?raw=true)

---

## 🧪 Use Case

Originally developed as a mock internal tool for use in FDA-regulated environments (pharma, biotech, labs). Could be extended to include:

- User login and permissions
- Audit trail (logging updates/deletions)
- Email reminders for upcoming or overdue calibrations
- PDF report generator for validation documentation

---

## ✍️ Author

**Charles Kwena**  
Systems Validation | Quality | Python Dev-in-Progress  
🔗 [LinkedIn](https://www.linkedin.com/in/charles-k-a198b9137/)  
📍 Based in NJ | Open to Remote & Hybrid Roles  

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Bckburnr/cleantrack.git
cd cleantrack
pip install -r requirements.txt
python app.py
