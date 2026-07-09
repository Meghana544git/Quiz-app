/* ╔══════════════════════════════════════════════════════════╗
   ║  QuizMaster Pro — Frontend JS                           ║
   ╚══════════════════════════════════════════════════════════╝ */

// ── Utils ────────────────────────────────────────────────────────────────────
const qs  = (s, ctx = document) => ctx.querySelector(s);
const qsa = (s, ctx = document) => [...ctx.querySelectorAll(s)];

// ── Index page: category & difficulty selection ──────────────────────────────
(function initIndexPage() {
  const catCards  = qsa('.category-card');
  const diffBtns  = qsa('.diff-btn');
  const catInput  = qs('#selected-category');
  const diffInput = qs('#selected-difficulty');
  const startBtn  = qs('#start-btn');
  const catError  = qs('#cat-error');

  if (!catInput) return; // not on index page

  catCards.forEach(card => {
    card.addEventListener('click', () => {
      catCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      catInput.value = card.dataset.category;
      if (catError) catError.style.display = 'none';
      updateStartBtn();
    });
  });

  diffBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      diffBtns.forEach(b => {
        b.classList.remove('selected-easy', 'selected-medium', 'selected-hard');
      });
      const diff = btn.dataset.difficulty;
      btn.classList.add(`selected-${diff}`);
      diffInput.value = diff;
      updateStartBtn();
    });
  });

  function updateStartBtn() {
    if (!startBtn) return;
    const catOk  = catInput.value !== '';
    const diffOk = diffInput.value !== '';
    startBtn.disabled = !(catOk && diffOk);
  }

  if (startBtn) {
    startBtn.closest('form').addEventListener('submit', e => {
      if (!catInput.value) {
        e.preventDefault();
        if (catError) catError.style.display = 'block';
        catError.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  }
})();

// ── Quiz page: timer + answer submission ─────────────────────────────────────
(function initQuizPage() {
  const timerFg    = qs('.timer-ring-fg');
  const timerText  = qs('#timer-text');
  const timerWrap  = qs('.timer-ring-wrap');
  const optBtns    = qsa('.option-btn');
  const feedbackEl = qs('#feedback-banner');
  const nextBtn    = qs('#next-btn');
  const nextBtnTxt = qs('#next-btn-text');

  if (!timerFg) return; // not on quiz page

  const totalSec   = parseInt(timerWrap.dataset.seconds, 10);
  const radius     = 26;
  const circumf    = 2 * Math.PI * radius;
  timerFg.style.strokeDasharray  = circumf;
  timerFg.style.strokeDashoffset = 0;

  let remaining  = totalSec;
  let answered   = false;
  let startedAt  = Date.now();
  let timerInterval;

  function setOffset(secs) {
    const fraction = secs / totalSec;
    timerFg.style.strokeDashoffset = circumf * (1 - fraction);
  }

  function tick() {
    remaining--;
    setOffset(remaining);
    if (timerText) timerText.textContent = remaining;

    if (remaining <= Math.ceil(totalSec * 0.35)) {
      timerWrap.classList.remove('timer-warning');
      timerWrap.classList.add('timer-danger');
    } else if (remaining <= Math.ceil(totalSec * 0.6)) {
      timerWrap.classList.add('timer-warning');
    }

    if (remaining <= 0) {
      clearInterval(timerInterval);
      if (!answered) submitAnswer(-1); // time up → no answer
    }
  }

  timerInterval = setInterval(tick, 1000);

  // ── Option click ──────────────────────────────────────────────────────────
  optBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      submitAnswer(parseInt(btn.dataset.index, 10));
    });
  });

  function submitAnswer(chosenIndex) {
    if (answered) return;
    answered = true;
    clearInterval(timerInterval);

    const timeTaken = Math.round((Date.now() - startedAt) / 1000);

    // Disable all buttons
    optBtns.forEach(b => { b.disabled = true; });

    fetch('/answer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chosen: chosenIndex, time_taken: timeTaken }),
    })
    .then(r => r.json())
    .then(data => {
      showFeedback(data, chosenIndex);
      updateNavDots(data.is_correct);
      if (nextBtn) {
        nextBtn.style.display = 'inline-flex';
        if (nextBtnTxt) {
          nextBtnTxt.textContent = data.is_last ? 'See Results' : 'Next Question';
        }
        nextBtn.href = data.next_url;
      }
    })
    .catch(() => {
      // fallback — just re-enable next
      if (nextBtn) nextBtn.style.display = 'inline-flex';
    });
  }

  function showFeedback(data, chosen) {
    // Colour the buttons
    optBtns.forEach(btn => {
      const idx = parseInt(btn.dataset.index, 10);
      if (idx === data.correct_index) {
        btn.classList.add('correct');
        btn.querySelector('.opt-letter').innerHTML = '✓';
      } else if (idx === chosen && !data.is_correct) {
        btn.classList.add('wrong');
        btn.querySelector('.opt-letter').innerHTML = '✗';
      }
    });

    // Show feedback banner
    if (feedbackEl) {
      feedbackEl.classList.remove('show', 'correct-fb', 'wrong-fb');
      if (data.is_correct) {
        feedbackEl.innerHTML = `<i class="bi bi-check-circle-fill fs-5"></i>
          <div><strong>Correct!</strong> ${escHtml(data.explanation)}</div>`;
        feedbackEl.classList.add('show', 'correct-fb');
      } else {
        const verb = chosen === -1 ? "Time's up!" : "Incorrect!";
        feedbackEl.innerHTML = `<i class="bi bi-x-circle-fill fs-5"></i>
          <div><strong>${verb}</strong> Correct answer: <em>${escHtml(data.correct_text)}</em>.
          ${data.explanation ? ' ' + escHtml(data.explanation) : ''}</div>`;
        feedbackEl.classList.add('show', 'wrong-fb');
      }
    }
  }

  function updateNavDots(isCorrect) {
    const current = qs('.nav-dot.current');
    if (!current) return;
    current.classList.remove('current');
    current.classList.add(isCorrect ? 'answered-correct' : 'answered-wrong');
    // mark next as current
    const next = current.nextElementSibling;
    if (next && next.classList.contains('nav-dot')) next.classList.add('current');
  }
})();

// ── Result page: score ring animation ────────────────────────────────────────
(function initResultPage() {
  const ring = qs('.score-ring-fg');
  if (!ring) return;

  const pct      = parseFloat(ring.dataset.pct || 0);
  const radius   = 56;
  const circumf  = 2 * Math.PI * radius;
  ring.style.strokeDasharray  = circumf;
  ring.style.strokeDashoffset = circumf;

  // Determine colour
  if      (pct >= 80) ring.style.stroke = '#19c864';
  else if (pct >= 60) ring.style.stroke = '#6c63ff';
  else if (pct >= 40) ring.style.stroke = '#ffc107';
  else                ring.style.stroke = '#dc3545';

  // Animate after paint
  requestAnimationFrame(() => {
    setTimeout(() => {
      ring.style.strokeDashoffset = circumf * (1 - pct / 100);
    }, 200);
  });

  // Counter animation
  const pctEl = qs('.score-ring-pct');
  if (pctEl) {
    const target = Math.round(pct);
    let cur = 0;
    const step = Math.ceil(target / 60);
    const counter = setInterval(() => {
      cur = Math.min(cur + step, target);
      pctEl.textContent = cur + '%';
      if (cur >= target) clearInterval(counter);
    }, 22);
  }

  // Confetti for high scores
  if (pct >= 80) launchConfetti();
})();

// ── Simple confetti ───────────────────────────────────────────────────────────
function launchConfetti() {
  const canvas = document.createElement('canvas');
  canvas.id = 'confetti-canvas';
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;

  const COLORS = ['#6c63ff','#19c864','#ffc107','#ff6b6b','#4ecdc4','#45b7d1'];
  const pieces = Array.from({ length: 120 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * -canvas.height,
    r: Math.random() * 7 + 3,
    color: COLORS[Math.floor(Math.random() * COLORS.length)],
    vx: (Math.random() - 0.5) * 3,
    vy: Math.random() * 3 + 2,
    spin: Math.random() * 0.2 - 0.1,
    angle: Math.random() * Math.PI * 2,
  }));

  let frame;
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pieces.forEach(p => {
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(p.angle);
      ctx.fillStyle = p.color;
      ctx.fillRect(-p.r, -p.r / 2, p.r * 2, p.r);
      ctx.restore();
      p.x += p.vx; p.y += p.vy; p.angle += p.spin;
    });
    const alive = pieces.filter(p => p.y < canvas.height + 20);
    if (alive.length) {
      frame = requestAnimationFrame(draw);
    } else {
      canvas.remove();
    }
  }
  frame = requestAnimationFrame(draw);
  setTimeout(() => { cancelAnimationFrame(frame); canvas.remove(); }, 5000);
}

// ── Helpers ───────────────────────────────────────────────────────────────────
function escHtml(str) {
  if (!str) return '';
  return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
            .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

// ── Search bar live filter ────────────────────────────────────────────────────
(function initSearch() {
  const input = qs('#category-search');
  if (!input) return;
  input.addEventListener('input', () => {
    const val = input.value.toLowerCase();
    qsa('.category-card').forEach(card => {
      const text = card.dataset.category.toLowerCase();
      card.closest('.col').style.display = text.includes(val) ? '' : 'none';
    });
  });
})();
