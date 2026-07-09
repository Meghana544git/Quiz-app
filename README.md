# QuizMaster Pro 🧠

A **modern, full-featured Quiz App** built with Python Flask and a polished Bootstrap 5 dark-mode frontend.

---

## ✨ Features

| Feature | Details |
|---|---|
| **Category selection** | Science, History, Geography, Technology, Mathematics, General Knowledge, Sports |
| **Difficulty levels** | Easy (20s), Medium (25s), Hard (30s) — or All |
| **Per-question timer** | Animated SVG ring countdown; auto-submits on time-out |
| **Randomised order** | Questions and answer options shuffled every run |
| **Instant feedback** | Correct / incorrect colour + explanation banner |
| **Score calculation** | Running score shown throughout the quiz |
| **Final result screen** | Animated score ring, grade label, per-answer review |
| **Retry quiz** | One-click retry with the same category + difficulty |
| **Question navigator** | Dot grid shows answered / current / upcoming questions |
| **Quiz history** | Last 20 sessions stored in server-side session, table view |
| **Search / filter** | Live search bar on the category grid |
| **EN / हिं labels** | Toggle between English and Hindi UI labels |
| **Confetti** | Fires on scores ≥ 80% |
| **Mobile responsive** | Bootstrap 5 grid + custom media queries |
| **Dark mode** | Full dark palette, no external theme required |

---

## 🗂️ Project Structure

```
Quiz/
├── app.py               ← Flask app + all routes
├── questions.py         ← Question bank (37 questions, 7 categories)
├── requirements.txt     ← Python dependencies
├── .env.example         ← Sample environment variables
├── templates/
│   ├── base.html        ← Navbar, footer, Bootstrap/JS includes
│   ├── index.html       ← Home: category + difficulty selector
│   ├── quiz.html        ← Quiz: timer, options, navigator, feedback
│   └── result.html      ← Results: score ring, review, history
└── static/
    ├── css/style.css    ← Custom dark theme + animations
    └── js/app.js        ← Timer, answer fetch, confetti, search
```

---

## 🚀 Quick Start (Local)

### 1. Create & activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment (optional)

```bash
copy .env.example .env   # Windows
cp  .env.example .env    # macOS/Linux
# Edit SECRET_KEY in .env
```

### 4. Run the app

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## 🌐 Deployment

### Heroku

```bash
# Add a Procfile
echo "web: python app.py" > Procfile
heroku create quizmaster-pro
heroku config:set SECRET_KEY=your_secret FLASK_DEBUG=0
git push heroku main
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
docker build -t quizmaster-pro .
docker run -p 5000:5000 quizmaster-pro
```

### Render / Railway / Fly.io

Set the start command to `python app.py` and add `SECRET_KEY` + `FLASK_DEBUG=0` as environment variables.

---

## 🔧 Configuration

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `quiz_secret_2024_ibmbob` | Flask session signing key |
| `FLASK_DEBUG` | `1` | Set `0` in production |
| `PORT` | `5000` | HTTP port |

---

## 📚 Adding Questions

Open [`questions.py`](questions.py) and add a new dict to `QUESTIONS`:

```python
{
    "id": 38,
    "category": "Science",          # must match an existing CATEGORIES value
    "difficulty": "medium",          # easy | medium | hard
    "question": "Your question EN",
    "question_hi": "आपका प्रश्न HI",
    "options": ["A", "B", "C", "D"],
    "options_hi": ["अ", "ब", "क", "ड"],
    "correct_index": 0,              # 0-based index into options
    "explanation": "Why A is correct.",
}
```

---

## 📄 License

MIT — free to use, modify, and distribute.

---

*Made with ❤️ by IBM Bob*
