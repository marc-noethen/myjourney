# 🐍 Python Mega Course – Lernstruktur
> Ardit Sulce · Udemy · 20 Real-World Apps & AI Agents  
> Diese Struktur spiegelt den Kursaufbau wider. Jeder Ordner enthält eigene Notizen, Code und Übungen.

---

## 📁 Ordnerstruktur

```
python-mega-course/
│
├── README.md                         ← diese Datei
├── requirements.txt                  ← alle pip-Pakete des Kurses
│
├── 00_setup/
│   ├── notes.md                      ← Installation, VS Code Setup, venv
│   └── hello_world.py
│
├── 01_basics/
│   ├── notes.md
│   ├── variables.py
│   ├── strings.py
│   ├── numbers.py
│   ├── user_input.py
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   ├── sets.py
│   ├── conditionals.py
│   ├── loops.py
│   ├── functions.py
│   └── exercises/
│       ├── exercise_01.py
│       └── exercise_02.py
│
├── 02_intermediate/
│   ├── notes.md
│   ├── oop_classes.py
│   ├── oop_inheritance.py
│   ├── file_handling.py
│   ├── error_handling.py
│   ├── modules_packages.py
│   ├── list_comprehensions.py
│   ├── lambda_functions.py
│   └── exercises/
│
├── 03_libraries/
│   ├── notes.md
│   ├── datetime_example.py
│   ├── os_pathlib.py
│   ├── json_handling.py
│   ├── requests_http.py
│   └── exercises/
│
├── 04_data_science/
│   ├── notes.md
│   ├── numpy_basics.py
│   ├── pandas_basics.py
│   ├── matplotlib_basics.py
│   └── exercises/
│
├── 05_web/
│   ├── notes.md
│   ├── flask_basics.py
│   ├── streamlit_basics.py
│   └── exercises/
│
├── 06_databases/
│   ├── notes.md
│   ├── sqlite_basics.py
│   └── exercises/
│
├── 07_ai_agents/
│   ├── notes.md
│   ├── langchain_basics.py
│   └── exercises/
│
├── projects/
│   ├── app01_todo_desktop/
│   │   ├── README.md
│   │   ├── main.py
│   │   └── requirements.txt
│   │
│   ├── app02_todo_webapp/
│   │   ├── README.md
│   │   ├── app.py
│   │   └── templates/
│   │
│   ├── app03_web_scraper/
│   │   ├── README.md
│   │   └── scraper.py
│   │
│   ├── app04_weather_api/
│   │   ├── README.md
│   │   └── weather.py
│   │
│   ├── app05_data_analysis/
│   │   ├── README.md
│   │   └── analysis.py
│   │
│   ├── app06_desktop_gui/
│   │   ├── README.md
│   │   └── app.py
│   │
│   ├── app07_email_automation/
│   │   ├── README.md
│   │   └── email_bot.py
│   │
│   ├── app08_pdf_tools/
│   │   ├── README.md
│   │   └── pdf_tool.py
│   │
│   ├── app09_data_dashboard/
│   │   ├── README.md
│   │   └── dashboard.py
│   │
│   ├── app10_database_app/
│   │   ├── README.md
│   │   └── db_app.py
│   │
│   ├── app11_image_processing/
│   │   ├── README.md
│   │   └── image_tool.py
│   │
│   ├── app12_portfolio_website/
│   │   ├── README.md
│   │   ├── app.py
│   │   └── templates/
│   │
│   ├── app13_rest_api/
│   │   ├── README.md
│   │   └── api.py
│   │
│   ├── app14_webcam_motion_detector/
│   │   ├── README.md
│   │   └── detector.py
│   │
│   ├── app15_automation_workflow/
│   │   ├── README.md
│   │   └── automation.py
│   │
│   ├── app16_chatbot/
│   │   ├── README.md
│   │   └── chatbot.py
│   │
│   ├── app17_file_organizer/
│   │   ├── README.md
│   │   └── organizer.py
│   │
│   ├── app18_ml_tool/
│   │   ├── README.md
│   │   └── ml_app.py
│   │
│   ├── app19_ai_agent_langchain/
│   │   ├── README.md
│   │   ├── agent.py
│   │   └── .env.example
│   │
│   └── app20_ai_automation_workflow/
│       ├── README.md
│       ├── workflow.py
│       └── .env.example
│
└── resources/
    ├── cheatsheet.md                 ← Python Schnellreferenz
    ├── useful_links.md               ← Kurs-Links, Docs, Tools
    └── progress.md                   ← eigener Fortschritts-Tracker
```

---

## 🚀 Setup

```bash
# Repo klonen
git clone https://github.com/DEIN-USERNAME/python-mega-course.git
cd python-mega-course

# Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Pakete installieren
pip install -r requirements.txt
```

---

## 📦 requirements.txt Inhalt

```
requests
flask
streamlit
pandas
numpy
matplotlib
beautifulsoup4
selenium
pillow
fpdf2
opencv-python
langchain
langchain-openai
python-dotenv
sqlalchemy
```

---

## 📈 Fortschritt

| # | App | Status |
|---|-----|--------|
| 01 | To-Do Desktop App | ⬜ |
| 02 | To-Do Web App | ⬜ |
| 03 | Web Scraper | ⬜ |
| 04 | Weather API App | ⬜ |
| 05 | Data Analysis Tool | ⬜ |
| 06 | Desktop GUI App | ⬜ |
| 07 | Email Automation | ⬜ |
| 08 | PDF Tools | ⬜ |
| 09 | Data Dashboard | ⬜ |
| 10 | Database App | ⬜ |
| 11 | Image Processing | ⬜ |
| 12 | Portfolio Website | ⬜ |
| 13 | REST API | ⬜ |
| 14 | Webcam Motion Detector | ⬜ |
| 15 | Automation Workflow | ⬜ |
| 16 | Chatbot | ⬜ |
| 17 | File Organizer | ⬜ |
| 18 | ML Tool | ⬜ |
| 19 | AI Agent (LangChain) | ⬜ |
| 20 | AI Automation Workflow | ⬜ |

---

*Teil der [KI-Roadmap](../KI-Roadmap.md) · Phase 0*
