"""Minimal Flask app that serves a single-page portfolio site."""
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Ilya Kozakov",
    "tagline": "Python / .NET engineer building reliable trading + data tools",
    "location": "Warsaw, Poland · Remote-friendly",
    "summary": (
        "Motivated to learn, collaborative, and team-oriented. I combine .NET, "
        "Python, and modern frontend habits to ship low-latency systems and clean "
        "internal tools. Comfortable with MSSQL, Redis, RabbitMQ, SignalR, and "
        "browser-side JavaScript/jQuery. Currently diving deeper into Python "
        "product work while exploring Laravel, Flutter (Dart), and Java ecosystems "
        "to keep my frontend intuition sharp."
    ),
    "contact_email": "ikozakov2018@gmail.com",
    "contact_social": "https://www.linkedin.com/in/ilya-kozakov-467648261/",
    "contact_telegram": "https://t.me/Sp0cee",
}

PROJECTS = [
    {
        "title": "Darwin Trading Surfaces",
        "stack": ".NET · SignalR · RabbitMQ",
        "summary": "Low-latency interface stitching Tradeweb, Bloomberg, and internal feeds for Santander traders.",
        "impact": "Improved situational awareness on the desk and kept execution teams confident in positions.",
    },
    {
        "title": "Trader Activity Monitor",
        "stack": ".NET · MSSQL · Redis · JavaScript",
        "summary": "Unified feed that aggregates trader actions, alerts, and health checks for ops teams.",
        "impact": "Cut triage time for anomalies by ~30% thanks to clearer dashboards and alerting.",
    },
    {
        "title": "IQVIA Client Delivery",
        "stack": ".NET Core · ASP.NET MVC · AWS S3",
        "summary": "Reporting suite helping pharma companies act on real sales data and flexible analytics.",
        "impact": "Enabled consultants to ship tailored reports faster after modernizing legacy modules.",
    },
]

SKILLS = [
    "Python & Flask",
    ".NET / C#",
    "SignalR + RabbitMQ",
    "Redis & MSSQL",
    "JavaScript & jQuery",
    "Clean markup & UI polish",
]

EXPERIENCE = [
    {
        "company": "Santander Corporate & Investment Banking",
        "role": "Software Engineer · Team Darwin",
        "dates": "May 2025 – Present",
        "location": "Warsaw, Poland",
        "highlights": [
            "Building high-performance trading tools ingesting Tradeweb and Bloomberg streams.",
            "Strengthened reliability for low-latency event processing with .NET, SignalR, Redis, RabbitMQ.",
            "Collaborating with traders and ops to turn live feedback into production-ready features.",
        ],
    },
    {
        "company": "Talan (External for Santander)",
        "role": "Junior Backend Developer",
        "dates": "Oct 2023 – May 2025",
        "location": "Warsaw, Poland · Remote",
        "highlights": [
            "Delivered backend services for trader activity dashboards with strict latency SLAs.",
            "Extended monitoring and alerting so ops could trust real-time positions.",
            "Shipped features end-to-end: .NET services, API wiring, plus lightweight frontend updates.",
        ],
    },
    {
        "company": "Itransition Group",
        "role": ".NET Developer",
        "dates": "Oct 2022 – Apr 2023",
        "location": "Remote",
        "highlights": [
            "Contributed to IQVIA Client Delivery used by pharma teams for sales intelligence.",
            "Over seven months, migrated modules to new frameworks and modernized reporting flows (ASP.NET MVC, EF Core).",
            "Demoed features, fixed bugs quickly, and kept deployments steady via Bamboo + Git.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Vistula University",
        "degree": "Engineer’s Degree, Computer Science",
        "dates": "Oct 2021 – Dec 2024",
        "notes": (
            "Focused on software engineering fundamentals, distributed systems, and practical web "
            "development. Led study projects that paired .NET services with Python prototypes."
        ),
    }
]

LANGUAGES = [
    "Russian · Native",
    "English · Professional working",
    "Polish · Conversational",
]

LEARNING = [
    "Advanced Python for data-heavy products",
    "Flutter (Dart) for expressive frontends",
    "PHP (Laravel) for rapid internal tools",
    "Java services for trading connectivity",
]


@app.context_processor
def inject_globals():
    """Provide common template variables."""
    return {
        "profile": PROFILE,
        "skills": SKILLS,
        "experience": EXPERIENCE,
        "education": EDUCATION,
        "languages": LANGUAGES,
        "learning": LEARNING,
        "current_year": datetime.now().year,
    }


@app.route("/")
def home():
    """Render the single-page portfolio."""
    return render_template("index.html", projects=PROJECTS)


if __name__ == "__main__":
    app.run(debug=True)

