"""
Quiz App — Flask backend
Session stores only question IDs to stay well under the 4 KB cookie limit.
Full question objects are looked up from the in-memory QUESTIONS bank on demand.
"""
import os, random
from datetime import datetime
from flask import (
    Flask, render_template, request, session,
    redirect, url_for, jsonify
)
from questions import QUESTIONS, CATEGORIES, DIFFICULTIES, CATEGORY_ICONS, DIFFICULTY_INFO

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "quiz_secret_2024_ibmbob")

# ── helpers ──────────────────────────────────────────────────────────────────

# Build a fast id→question lookup once at startup
_Q_BY_ID = {q["id"]: q for q in QUESTIONS}


def _filter_questions(category: str, difficulty: str) -> list:
    """Return a filtered + shuffled list of questions."""
    qs = list(QUESTIONS)
    if category and category != "all":
        qs = [q for q in qs if q["category"] == category]
    if difficulty and difficulty != "all":
        qs = [q for q in qs if q["difficulty"] == difficulty]
    random.shuffle(qs)
    return qs


def _get_history() -> list:
    return session.get("history", [])


def _save_result(result: dict):
    history = _get_history()
    result["timestamp"] = datetime.now().strftime("%d %b %Y, %I:%M %p")
    history.insert(0, result)
    session["history"] = history[:20]   # keep last 20


def _make_quiz_session(questions: list, category: str, difficulty: str) -> dict:
    """Build a compact quiz session — stores only IDs, not full question dicts."""
    return {
        "question_ids": [q["id"] for q in questions],
        "category": category,
        "difficulty": difficulty,
        "current": 0,
        "score": 0,
        "answers": [],   # list of compact answer records
        "lang": session.get("lang", "en"),
        "started_at": datetime.now().isoformat(),
    }


# ── routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    lang = session.get("lang", "en")
    search = request.args.get("search", "").strip().lower()

    cats = CATEGORIES
    if search:
        cats = [c for c in cats if search in c.lower()]

    return render_template(
        "index.html",
        categories=cats,
        difficulties=DIFFICULTIES,
        category_icons=CATEGORY_ICONS,
        difficulty_info=DIFFICULTY_INFO,
        lang=lang,
        history=_get_history(),
        search=search,
    )


@app.route("/set_lang/<lang>")
def set_lang(lang):
    if lang in ("en", "hi"):
        session["lang"] = lang
    return redirect(request.referrer or url_for("index"))


@app.route("/start", methods=["POST"])
def start():
    category   = request.form.get("category", "all")
    difficulty = request.form.get("difficulty", "all")

    questions = _filter_questions(category, difficulty)
    if not questions:
        return redirect(url_for("index"))

    session["quiz"] = _make_quiz_session(questions, category, difficulty)
    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    quiz = session.get("quiz")
    if not quiz:
        return redirect(url_for("index"))

    q_ids = quiz["question_ids"]
    idx   = quiz["current"]
    total = len(q_ids)

    if idx >= total:
        return redirect(url_for("result"))

    q    = _Q_BY_ID[q_ids[idx]]
    lang = quiz["lang"]
    diff = quiz["difficulty"] if quiz["difficulty"] != "all" else q["difficulty"]
    timer_seconds = DIFFICULTY_INFO.get(diff, DIFFICULTY_INFO["medium"])["time"]

    # Build display options — shuffle order but remember original indices
    options_raw = q["options"] if lang == "en" else q.get("options_hi", q["options"])
    opt_indices = list(range(len(options_raw)))
    random.shuffle(opt_indices)
    display_options = [(i, options_raw[i]) for i in opt_indices]

    question_text = q["question"] if lang == "en" else q.get("question_hi", q["question"])
    diff_meta = DIFFICULTY_INFO.get(q["difficulty"], DIFFICULTY_INFO["medium"])

    return render_template(
        "quiz.html",
        q=q,
        question_text=question_text,
        display_options=display_options,
        idx=idx,
        total=total,
        score=quiz["score"],
        timer_seconds=timer_seconds,
        lang=lang,
        diff_meta=diff_meta,
        category_icons=CATEGORY_ICONS,
        answers=quiz["answers"],
    )


@app.route("/answer", methods=["POST"])
def answer():
    quiz = session.get("quiz")
    if not quiz:
        return jsonify({"error": "no session"}), 400

    data         = request.get_json(force=True)
    chosen_index = int(data.get("chosen", -1))
    time_taken   = int(data.get("time_taken", 0))

    idx   = quiz["current"]
    q_ids = quiz["question_ids"]
    q     = _Q_BY_ID[q_ids[idx]]
    correct    = q["correct_index"]
    is_correct = (chosen_index == correct)

    if is_correct:
        quiz["score"] += 1

    # Store a compact answer record (no full option lists — save cookie space)
    quiz["answers"].append({
        "qid":        q["id"],
        "question":   q["question"],
        "question_hi": q.get("question_hi", q["question"]),
        "chosen":     chosen_index,
        "correct":    correct,
        "is_correct": is_correct,
        "time_taken": time_taken,
        "explanation": q.get("explanation", ""),
        "options":    q["options"],
        "options_hi": q.get("options_hi", q["options"]),
    })

    lang = quiz["lang"]
    correct_text = (
        q["options"][correct] if lang == "en"
        else q.get("options_hi", q["options"])[correct]
    )

    quiz["current"] += 1
    session["quiz"] = quiz
    session.modified = True

    total = len(q_ids)
    return jsonify({
        "is_correct":   is_correct,
        "correct_index": correct,
        "correct_text": correct_text,
        "explanation":  q.get("explanation", ""),
        "score":        quiz["score"],
        "next_url":     url_for("quiz") if quiz["current"] < total else url_for("result"),
        "is_last":      quiz["current"] >= total,
    })


@app.route("/result")
def result():
    quiz = session.get("quiz")
    if not quiz:
        return redirect(url_for("index"))

    score   = quiz["score"]
    total   = len(quiz["question_ids"])
    pct     = round((score / total) * 100) if total else 0
    answers = quiz["answers"]
    lang    = quiz["lang"]

    if pct >= 80:
        grade, grade_color = "Excellent! 🌟", "success"
    elif pct >= 60:
        grade, grade_color = "Good Job! 👍", "primary"
    elif pct >= 40:
        grade, grade_color = "Keep Practicing! 💪", "warning"
    else:
        grade, grade_color = "Better Luck Next Time! 🔄", "danger"

    result_data = {
        "category":   quiz["category"],
        "difficulty": quiz["difficulty"],
        "score": score,
        "total": total,
        "pct":   pct,
        "grade": grade,
    }
    _save_result(result_data)

    # clear active quiz
    session.pop("quiz", None)

    return render_template(
        "result.html",
        score=score,
        total=total,
        pct=pct,
        grade=grade,
        grade_color=grade_color,
        answers=answers,
        lang=lang,
        category=result_data["category"],
        difficulty=result_data["difficulty"],
        history=_get_history(),
        difficulty_info=DIFFICULTY_INFO,
        category_icons=CATEGORY_ICONS,
    )


@app.route("/retry")
def retry():
    """Re-start a quiz with the same settings."""
    category   = request.args.get("category", "all")
    difficulty = request.args.get("difficulty", "all")
    questions  = _filter_questions(category, difficulty)
    session["quiz"] = _make_quiz_session(questions, category, difficulty)
    return redirect(url_for("quiz"))


@app.route("/clear_history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    return redirect(url_for("index"))


@app.route("/api/questions")
def api_questions():
    """JSON endpoint — useful for debugging."""
    cat  = request.args.get("category", "all")
    diff = request.args.get("difficulty", "all")
    return jsonify(_filter_questions(cat, diff))


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug, port=int(os.environ.get("PORT", 5000)))
