NEURALFOLIO AI PORTFOLIO — QUICK START (Windows)

1. Install Python 3.13 from python.org if it is not already installed.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Run:
   py -m venv .venv
   .venv\Scripts\activate
   python -m pip install -r requirements.txt
   python app.py
5. Hold Ctrl and click the local URL shown in the terminal, usually:
   http://127.0.0.1:5000

The portfolio is a fictional demo. Replace Alex Morgan and the project details with your own.
The contact form is a demo: it validates and responds, but does not send or store email messages.

To publish publicly, deploy this Flask project on a Python-capable host such as Render.
Create a web service from your GitHub repository, use build command:
   pip install -r requirements.txt
and start command:
   gunicorn app:app
Add gunicorn to requirements.txt before deployment (or change it to include Flask and gunicorn).
