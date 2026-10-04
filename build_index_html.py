import json
import os

with open('quiz_complete_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mcq_json = json.dumps(data['mcq'], ensure_ascii=False)
sa_json = json.dumps(data['sa'], ensure_ascii=False)
essay_json = json.dumps(data['essay'], ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Cục Cưng Ôn Thi – Lịch Sử Đảng Cộng Sản Việt Nam</title>
  <meta name="description" content="Ứng dụng ôn tập Quizizz Lịch Sử Đảng Cộng Sản Việt Nam: 81 câu hỏi trắc nghiệm, câu ngắn và tự luận đầy đủ ý chi tiết, mượt mà trên điện thoại.">
  <meta name="theme-color" content="#090d16">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  
  <!-- Favicon SVG -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⭐</text></svg>">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg-base: #080c15;
      --bg-surface: #0f172a;
      --bg-card: rgba(21, 31, 56, 0.72);
      --bg-card-hover: rgba(30, 43, 77, 0.85);
      --bg-glass: rgba(255, 255, 255, 0.05);
      --border-subtle: rgba(148, 163, 184, 0.12);
      --border-glow: rgba(139, 92, 246, 0.35);
      
      --accent-purple: #8b5cf6;
      --accent-pink: #ec4899;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-red: #ef4444;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --gradient-brand: linear-gradient(135deg, #a855f7 0%, #ec4899 50%, #06b6d4 100%);
      --gradient-card: linear-gradient(135deg, rgba(168, 85, 247, 0.12) 0%, rgba(236, 72, 153, 0.06) 100%);
      --gradient-fire: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
      --shadow-glow: 0 0 35px rgba(139, 92, 246, 0.22);
      --shadow-card: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
      
      --radius-sm: 10px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --radius-full: 9999px;
      
      --safe-bottom: env(safe-area-inset-bottom, 16px);
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}

    p, span, h1, h2, h3, h4, h5, div.selectable {{
      user-select: text;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg-base);
      color: var(--text-main);
      min-height: 100vh;
      min-height: -webkit-fill-available;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      touch-action: manipulation;
    }}

    /* Ambient animated orbs */
    .ambient-canvas {{
      position: fixed;
      inset: 0;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
    }}
    .ambient-orb {{
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.28;
      will-change: transform;
      animation: floatOrbit 22s ease-in-out infinite alternate;
    }}
    .orb-1 {{
      width: 380px; height: 380px;
      background: #7c3aed;
      top: -80px; left: -80px;
    }}
    .orb-2 {{
      width: 420px; height: 420px;
      background: #ec4899;
      bottom: -60px; right: -80px;
      animation-delay: -7s;
      animation-duration: 26s;
    }}
    .orb-3 {{
      width: 320px; height: 320px;
      background: #0284c7;
      top: 40%; left: 45%;
      opacity: 0.2;
      animation-delay: -14s;
    }}
    @keyframes floatOrbit {{
      0% {{ transform: translate3d(0, 0, 0) scale(1); }}
      50% {{ transform: translate3d(35px, -45px, 0) scale(1.12); }}
      100% {{ transform: translate3d(-30px, 35px, 0) scale(0.92); }}
    }}

    /* Container */
    .app-viewport {{
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 820px;
      margin: 0 auto;
      padding: 16px 16px calc(24px + var(--safe-bottom));
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Screens */
    .screen {{
      display: none;
      opacity: 0;
      transform: translate3d(0, 14px, 0);
      transition: opacity 0.32s cubic-bezier(0.16, 1, 0.3, 1), transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .screen.active {{
      display: flex;
      flex-direction: column;
      flex: 1;
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }}

    /* ── HEADER ── */
    .header-zone {{
      text-align: center;
      padding: 18px 0 22px;
      position: relative;
    }}
    .brand-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #cbd5e1;
      margin-bottom: 12px;
      backdrop-filter: blur(10px);
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }}
    .brand-pill .sparkle {{
      color: #fbbf24;
      animation: sparkleRotate 2.5s infinite linear;
    }}
    @keyframes sparkleRotate {{
      0% {{ transform: rotate(0deg) scale(1); }}
      50% {{ transform: rotate(180deg) scale(1.2); }}
      100% {{ transform: rotate(360deg) scale(1); }}
    }}
    .header-title {{
      font-size: clamp(24px, 6.5vw, 36px);
      font-weight: 900;
      letter-spacing: -0.5px;
      line-height: 1.18;
      background: var(--gradient-brand);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}
    .header-desc {{
      font-size: clamp(13px, 3.8vw, 15px);
      color: var(--text-muted);
      font-weight: 500;
      line-height: 1.5;
      max-width: 580px;
      margin: 0 auto;
    }}

    /* Quick status stats strip */
    .stats-strip {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin: 18px 0 24px;
    }}
    .strip-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 10px;
      text-align: center;
      backdrop-filter: blur(14px);
    }}
    .strip-num {{
      font-size: clamp(18px, 4.5vw, 24px);
      font-weight: 800;
      color: var(--text-main);
      font-family: 'JetBrains Mono', monospace;
    }}
    .strip-label {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* ── MODE CARDS ── */
    .modes-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .mode-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 18px 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      transition: all 0.24s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(16px);
      position: relative;
      overflow: hidden;
    }}
    .mode-card::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: var(--gradient-card);
      opacity: 0;
      transition: opacity 0.24s ease;
    }}
    .mode-card:active {{
      transform: scale(0.975);
    }}
    @media (hover: hover) {{
      .mode-card:hover {{
        transform: translateY(-3px);
        border-color: var(--border-glow);
        box-shadow: var(--shadow-glow);
      }}
      .mode-card:hover::before {{
        opacity: 1;
      }}
    }}
    .mode-left {{
      display: flex;
      align-items: center;
      gap: 15px;
      position: relative;
      z-index: 1;
    }}
    .mode-icon-box {{
      width: 48px;
      height: 48px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25);
    }}
    .mode-icon-box.purple {{ background: rgba(139, 92, 246, 0.18); border: 1px solid rgba(139, 92, 246, 0.3); }}
    .mode-icon-box.cyan {{ background: rgba(6, 182, 212, 0.18); border: 1px solid rgba(6, 182, 212, 0.3); }}
    .mode-icon-box.pink {{ background: rgba(236, 72, 153, 0.18); border: 1px solid rgba(236, 72, 153, 0.3); }}
    .mode-icon-box.emerald {{ background: rgba(16, 185, 129, 0.18); border: 1px solid rgba(16, 185, 129, 0.3); }}
    .mode-icon-box.amber {{ background: rgba(245, 158, 11, 0.18); border: 1px solid rgba(245, 158, 11, 0.3); }}

    .mode-info h3 {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .mode-info p {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 3px;
      line-height: 1.4;
    }}
    .mode-badge {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      margin-top: 6px;
      letter-spacing: 0.3px;
    }}
    .mode-badge.purple {{ background: rgba(139, 92, 246, 0.2); color: #c4b5fd; }}
    .mode-badge.cyan {{ background: rgba(6, 182, 212, 0.2); color: #67e8f9; }}
    .mode-badge.pink {{ background: rgba(236, 72, 153, 0.2); color: #f472b6; }}
    .mode-badge.emerald {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }}
    .mode-badge.amber {{ background: rgba(245, 158, 11, 0.2); color: #fcd34d; }}

    .mode-arrow {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      color: var(--text-muted);
      flex-shrink: 0;
      position: relative;
      z-index: 1;
      transition: all 0.2s;
    }}
    .mode-card:hover .mode-arrow {{
      background: var(--accent-purple);
      color: #fff;
      transform: translateX(3px);
    }}

    /* ── SETTINGS COLLAPSIBLE ── */
    .settings-accordion {{
      margin-top: 18px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      backdrop-filter: blur(14px);
    }}
    .settings-toggle {{
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .settings-toggle span.arrow {{
      transition: transform 0.24s ease;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .settings-toggle.open span.arrow {{
      transform: rotate(180deg);
    }}
    .settings-content {{
      display: none;
      padding: 0 20px 18px;
      border-top: 1px solid rgba(255,255,255,0.04);
    }}
    .settings-content.open {{
      display: block;
    }}
    .setting-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    }}
    .setting-item:last-child {{
      border-bottom: none;
    }}
    .setting-label {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
    }}
    .setting-select {{
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      padding: 7px 12px;
      font-size: 13px;
      font-family: inherit;
      outline: none;
      cursor: pointer;
    }}
    .setting-select:focus {{
      border-color: var(--accent-purple);
    }}

    /* ── QUIZ RUN SCREEN ── */
    .quiz-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 0 14px;
      gap: 12px;
    }}
    .nav-btn-back {{
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s;
    }}
    .nav-btn-back:active {{
      transform: scale(0.95);
    }}
    .quiz-badges-row {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .pill-stat {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      font-family: 'JetBrains Mono', monospace;
    }}
    .pill-stat.streak {{
      color: #fbbf24;
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.25);
    }}
    .pill-stat.correct {{
      color: #34d399;
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.25);
    }}
    .pill-stat.wrong {{
      color: #f87171;
      background: rgba(239, 68, 68, 0.12);
      border-color: rgba(239, 68, 68, 0.25);
    }}
    .pill-stat.sound-toggle {{
      cursor: pointer;
    }}

    /* Progress bar */
    .progress-track {{
      width: 100%;
      height: 7px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 4px;
      overflow: hidden;
      margin-bottom: 14px;
      position: relative;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--gradient-brand);
      border-radius: 4px;
      width: 0%;
      transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Timer bar */
    .timer-track {{
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 2px;
      overflow: hidden;
      margin-bottom: 14px;
    }}
    .timer-fill {{
      height: 100%;
      width: 100%;
      background: var(--accent-cyan);
      transition: width 0.1s linear, background-color 0.3s;
    }}
    .timer-fill.warn {{ background: var(--accent-amber); }}
    .timer-fill.danger {{ background: var(--accent-red); }}

    /* Question card */
    .q-meta {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }}
    .q-number-pill {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1px;
      color: var(--accent-purple);
      text-transform: uppercase;
      font-family: 'JetBrains Mono', monospace;
    }}
    .q-type-badge {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-muted);
    }}

    .question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 22px 20px;
      box-shadow: var(--shadow-card);
      backdrop-filter: blur(18px);
      margin-bottom: 18px;
      animation: questionPop 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes questionPop {{
      0% {{ opacity: 0; transform: translateY(12px) scale(0.98); }}
      100% {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}
    .question-text {{
      font-size: clamp(16px, 4.4vw, 19px);
      font-weight: 700;
      line-height: 1.55;
      color: var(--text-main);
    }}

    /* MCQ Option buttons */
    .options-stack {{
      display: flex;
      flex-direction: column;
      gap: 11px;
      margin-bottom: 20px;
    }}
    .opt-btn {{
      background: rgba(255, 255, 255, 0.035);
      border: 1.5px solid rgba(255, 255, 255, 0.07);
      border-radius: var(--radius-md);
      padding: 15px 16px;
      display: flex;
      align-items: flex-start;
      gap: 13px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 15px;
      line-height: 1.48;
      text-align: left;
      cursor: pointer;
      width: 100%;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    .opt-btn:active {{
      transform: scale(0.98);
    }}
    @media (hover: hover) {{
      .opt-btn:hover:not(.disabled) {{
        background: rgba(139, 92, 246, 0.09);
        border-color: rgba(139, 92, 246, 0.35);
        transform: translateX(4px);
      }}
    }}
    .opt-letter {{
      width: 30px;
      height: 30px;
      border-radius: 8px;
      background: rgba(139, 92, 246, 0.15);
      color: #c4b5fd;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 13px;
      flex-shrink: 0;
      transition: all 0.2s;
    }}
    .opt-btn.correct {{
      background: rgba(16, 185, 129, 0.16) !important;
      border-color: var(--accent-emerald) !important;
      color: #ecfdf5 !important;
      box-shadow: 0 0 24px rgba(16, 185, 129, 0.25);
      animation: bounceCorrect 0.4s ease;
    }}
    .opt-btn.correct .opt-letter {{
      background: var(--accent-emerald) !important;
      color: #fff !important;
    }}
    .opt-btn.wrong {{
      background: rgba(239, 68, 68, 0.15) !important;
      border-color: var(--accent-red) !important;
      color: #fef2f2 !important;
      animation: shakeWrong 0.45s ease;
    }}
    .opt-btn.wrong .opt-letter {{
      background: var(--accent-red) !important;
      color: #fff !important;
    }}
    .opt-btn.disabled {{
      pointer-events: none;
      opacity: 0.48;
    }}
    .opt-btn.correct.disabled {{
      opacity: 1;
    }}
    @keyframes bounceCorrect {{
      0% {{ transform: scale(1); }}
      40% {{ transform: scale(1.025); }}
      100% {{ transform: scale(1); }}
    }}
    @keyframes shakeWrong {{
      0%, 100% {{ transform: translateX(0); }}
      20% {{ transform: translateX(-6px); }}
      40% {{ transform: translateX(6px); }}
      60% {{ transform: translateX(-4px); }}
      80% {{ transform: translateX(4px); }}
    }}

    /* Short answer input and reveal */
    .sa-box {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .sa-input {{
      width: 100%;
      min-height: 90px;
      background: rgba(255, 255, 255, 0.04);
      border: 1.5px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 15px;
      line-height: 1.5;
      resize: vertical;
      outline: none;
      transition: border-color 0.2s;
    }}
    .sa-input:focus {{
      border-color: var(--accent-cyan);
    }}
    .sa-reveal-card {{
      background: rgba(16, 185, 129, 0.09);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      animation: questionPop 0.3s ease;
    }}
    .sa-reveal-title {{
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: var(--accent-emerald);
      text-transform: uppercase;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .sa-reveal-body {{
      font-size: 14px;
      line-height: 1.6;
      color: #e2e8f0;
      white-space: pre-line;
    }}
    .self-grade-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 14px;
    }}
    .grade-btn {{
      padding: 12px;
      border-radius: var(--radius-md);
      font-size: 14px;
      font-weight: 700;
      font-family: inherit;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      border: 1.5px solid transparent;
      transition: all 0.2s;
    }}
    .grade-btn.pass {{
      background: rgba(16, 185, 129, 0.18);
      border-color: rgba(16, 185, 129, 0.4);
      color: #34d399;
    }}
    .grade-btn.pass:active {{ transform: scale(0.97); }}
    .grade-btn.fail {{
      background: rgba(239, 68, 68, 0.18);
      border-color: rgba(239, 68, 68, 0.4);
      color: #f87171;
    }}
    .grade-btn.fail:active {{ transform: scale(0.97); }}

    /* Next floating button bar */
    .quiz-bottom-bar {{
      position: sticky;
      bottom: var(--safe-bottom);
      z-index: 20;
      margin-top: auto;
      padding-top: 12px;
    }}
    .btn-action-primary {{
      width: 100%;
      background: var(--gradient-brand);
      color: #fff;
      border: none;
      padding: 15px 24px;
      border-radius: var(--radius-md);
      font-family: inherit;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 8px 28px rgba(168, 85, 247, 0.35);
      transition: all 0.24s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-action-primary:active {{
      transform: scale(0.97);
    }}

    /* ── DEDICATED ESSAY SCREEN ── */
    .essay-toolbar {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .search-box {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 14px;
      outline: none;
      backdrop-filter: blur(14px);
    }}
    .search-box:focus {{
      border-color: var(--accent-purple);
    }}
    .essay-tabs-pill {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }}
    .essay-tabs-pill::-webkit-scrollbar {{ display: none; }}
    .pill-tab {{
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .pill-tab.active {{
      background: rgba(139, 92, 246, 0.22);
      border-color: var(--accent-purple);
      color: #fff;
    }}

    .essay-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      margin-bottom: 16px;
      overflow: hidden;
      backdrop-filter: blur(18px);
      box-shadow: var(--shadow-card);
      transition: all 0.24s ease;
    }}
    .essay-card-header {{
      padding: 18px 20px;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
    }}
    .essay-card-header:hover {{
      background: rgba(255, 255, 255, 0.02);
    }}
    .essay-badge-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 800;
      color: var(--accent-pink);
      background: rgba(236, 72, 153, 0.12);
      padding: 4px 8px;
      border-radius: var(--radius-sm);
      display: inline-block;
      margin-bottom: 6px;
    }}
    .essay-q-title {{
      font-size: 15.5px;
      font-weight: 700;
      line-height: 1.5;
      color: var(--text-main);
    }}
    .essay-expand-icon {{
      font-size: 14px;
      color: var(--text-muted);
      transition: transform 0.24s ease;
      margin-top: 4px;
      flex-shrink: 0;
    }}
    .essay-card.expanded .essay-expand-icon {{
      transform: rotate(180deg);
    }}
    .essay-card-body {{
      display: none;
      padding: 0 20px 22px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }}
    .essay-card.expanded .essay-card-body {{
      display: block;
      animation: questionPop 0.3s ease;
    }}
    .essay-actions-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.04);
      margin-bottom: 14px;
    }}
    .btn-copy {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      font-family: inherit;
    }}
    .btn-copy:active {{ transform: scale(0.95); }}
    .essay-text-formatted {{
      font-size: 14px;
      line-height: 1.7;
      color: #e2e8f0;
      white-space: pre-line;
    }}
    .essay-student-highlight {{
      margin-top: 16px;
      padding: 16px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, rgba(236, 72, 153, 0.12) 0%, rgba(139, 92, 246, 0.12) 100%);
      border: 1px solid rgba(236, 72, 153, 0.3);
    }}
    .essay-student-highlight h4 {{
      font-size: 13px;
      font-weight: 800;
      color: #f472b6;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* ── RESULTS SCREEN ── */
    .results-wrap {{
      text-align: center;
      padding: 24px 0 10px;
    }}
    .ring-wrapper {{
      width: 170px;
      height: 170px;
      margin: 0 auto 20px;
      position: relative;
    }}
    .ring-wrapper svg {{
      width: 170px;
      height: 170px;
      transform: rotate(-90deg);
    }}
    .ring-track {{
      fill: none;
      stroke: rgba(255, 255, 255, 0.06);
      stroke-width: 12;
    }}
    .ring-fill {{
      fill: none;
      stroke-width: 12;
      stroke-linecap: round;
      stroke-dasharray: 452;
      stroke-dashoffset: 452;
      transition: stroke-dashoffset 1.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .ring-content {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}
    .ring-pct {{
      font-size: 42px;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
      background: var(--gradient-brand);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .ring-label {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 1px;
      text-transform: uppercase;
    }}
    .result-grade-msg {{
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 6px;
    }}
    .result-grade-sub {{
      font-size: 14px;
      color: var(--text-muted);
    }}

    .results-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin: 22px 0;
    }}
    .res-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 14px 10px;
      backdrop-filter: blur(14px);
    }}
    .res-box-val {{
      font-size: 22px;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
    }}
    .res-box-lbl {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      margin-top: 3px;
    }}

    /* Review section */
    .review-wrap {{
      margin-top: 24px;
      text-align: left;
    }}
    .review-tabs-filter {{
      display: flex;
      gap: 8px;
      margin-bottom: 14px;
    }}
    .btn-filter {{
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s;
    }}
    .btn-filter.active {{
      background: rgba(139, 92, 246, 0.2);
      border-color: var(--accent-purple);
      color: #fff;
    }}
    .review-item-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 15px 16px;
      margin-bottom: 10px;
      backdrop-filter: blur(14px);
    }}
    .review-item-card.is-pass {{
      border-left: 3px solid var(--accent-emerald);
    }}
    .review-item-card.is-fail {{
      border-left: 3px solid var(--accent-red);
    }}
    .review-q-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      line-height: 1.45;
    }}
    .review-ans-row {{
      font-size: 13px;
      line-height: 1.5;
      color: #cbd5e1;
    }}
    .review-ans-row .badge-ans {{
      font-weight: 700;
    }}
    .review-ans-row .ans-correct {{ color: #34d399; }}
    .review-ans-row .ans-wrong {{ color: #f87171; }}

    /* ── POPUPS & MICRO-INTERACTIONS ── */
    .streak-banner {{
      position: fixed;
      top: 40%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.6);
      font-size: clamp(28px, 8vw, 42px);
      font-weight: 900;
      color: #fbbf24;
      text-shadow: 0 0 30px rgba(245, 158, 11, 0.7);
      opacity: 0;
      pointer-events: none;
      z-index: 100;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
    }}
    .streak-banner.active {{
      opacity: 1;
      transform: translate(-50%, -50%) scale(1.1);
    }}

    .toast-pill {{
      position: fixed;
      bottom: calc(24px + var(--safe-bottom));
      left: 50%;
      transform: translate(-50%, 60px);
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      padding: 10px 20px;
      font-size: 13px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      opacity: 0;
      z-index: 90;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      backdrop-filter: blur(12px);
    }}
    .toast-pill.active {{
      opacity: 1;
      transform: translate(-50%, 0);
    }}
    .toast-pill.toast-success {{
      border-color: rgba(16, 185, 129, 0.5);
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(15, 23, 42, 0.95));
    }}
    .toast-pill.toast-error {{
      border-color: rgba(239, 68, 68, 0.5);
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.25), rgba(15, 23, 42, 0.95));
    }}

    /* Confetti canvas */
    #confettiCanvas {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 150;
    }}
  </style>
</head>
<body>
  <!-- Ambient orbs -->
  <div class="ambient-canvas">
    <div class="ambient-orb orb-1"></div>
    <div class="ambient-orb orb-2"></div>
    <div class="ambient-orb orb-3"></div>
  </div>

  <canvas id="confettiCanvas"></canvas>

  <div class="app-viewport">
    <!-- ════════════ SCREEN 1: HOME ════════════ -->
    <div id="screenHome" class="screen active">
      <header class="header-zone">
        <div class="brand-pill">
          <span class="sparkle">⭐</span>
          <span>CỤC CƯNG ÔN THI 2024–2025</span>
        </div>
        <h1 class="header-title">Lịch Sử Đảng Cộng Sản Việt Nam</h1>
        <p class="header-desc">Hệ thống ôn luyện trắc nghiệm, câu hỏi ngắn và chuyên đề tự luận thi kết thúc học phần.</p>
      </header>

      <div class="stats-strip">
        <div class="strip-item">
          <div class="strip-num" id="statBadgeMcq">45</div>
          <div class="strip-label">Trắc nghiệm</div>
        </div>
        <div class="strip-item">
          <div class="strip-num" id="statBadgeSa">30</div>
          <div class="strip-label">Câu hỏi ngắn</div>
        </div>
        <div class="strip-item">
          <div class="strip-num" id="statBadgeEssay">6</div>
          <div class="strip-label">Tự luận lớn</div>
        </div>
      </div>

      <div class="modes-list">
        <!-- Mode 1: MCQ -->
        <div class="mode-card" onclick="initAndStartQuiz('mcq')">
          <div class="mode-left">
            <div class="mode-icon-box purple">🧠</div>
            <div class="mode-info">
              <h3>Trắc nghiệm chuẩn thi <span class="mode-badge purple">45 Câu</span></h3>
              <p>4 lựa chọn, phản hồi tức thì, tính streak và lưu câu sai</p>
            </div>
          </div>
          <div class="mode-arrow">→</div>
        </div>

        <!-- Mode 2: Short Answer -->
        <div class="mode-card" onclick="initAndStartQuiz('sa')">
          <div class="mode-left">
            <div class="mode-icon-box cyan">✍️</div>
            <div class="mode-info">
              <h3>Câu hỏi ngắn ghi nhớ <span class="mode-badge cyan">30 Câu</span></h3>
              <p>Ôn mốc thời gian, địa điểm, sự kiện cốt lõi & tự đánh giá</p>
            </div>
          </div>
          <div class="mode-arrow">→</div>
        </div>

        <!-- Mode 3: Essay Dedicated -->
        <div class="mode-card" onclick="openEssayScreen()">
          <div class="mode-left">
            <div class="mode-icon-box pink">📜</div>
            <div class="mode-info">
              <h3>Chuyên đề Tự Luận <span class="mode-badge pink">6 Đề Lớn</span></h3>
              <p>Đầy đủ luận điểm, phân tích sâu và liên hệ trách nhiệm sinh viên</p>
            </div>
          </div>
          <div class="mode-arrow">→</div>
        </div>

        <!-- Mode 4: Mixed -->
        <div class="mode-card" onclick="initAndStartQuiz('mix')">
          <div class="mode-left">
            <div class="mode-icon-box emerald">🎯</div>
            <div class="mode-info">
              <h3>Thi thử tổng hợp <span class="mode-badge emerald">Trộn 75 Câu</span></h3>
              <p>Kết hợp ngẫu nhiên trắc nghiệm và câu ngắn theo cấu trúc thi</p>
            </div>
          </div>
          <div class="mode-arrow">→</div>
        </div>

        <!-- Mode 5: Review Wrong -->
        <div class="mode-card" onclick="initAndStartQuiz('wrong')">
          <div class="mode-left">
            <div class="mode-icon-box amber">🔄</div>
            <div class="mode-info">
              <h3>Luyện lại câu sai <span class="mode-badge amber" id="wrongBadgeText">0 Câu</span></h3>
              <p>Chỉ hiển thị các câu bạn từng trả lời sai để ghi nhớ vững vàng</p>
            </div>
          </div>
          <div class="mode-arrow">→</div>
        </div>
      </div>

      <!-- Collapsible Settings -->
      <div class="settings-accordion">
        <div class="settings-toggle" onclick="toggleSettingsAccordion()">
          <span>⚙️ Tùy chỉnh chế độ làm bài</span>
          <span class="arrow" id="settingsArrow">▼</span>
        </div>
        <div class="settings-content" id="settingsContent">
          <div class="setting-item">
            <span class="setting-label">Số lượng câu mỗi lượt</span>
            <select class="setting-select" id="optLimit">
              <option value="10">10 câu nhanh</option>
              <option value="20">20 câu vừa</option>
              <option value="30">30 câu</option>
              <option value="0" selected>Toàn bộ câu hỏi</option>
            </select>
          </div>
          <div class="setting-item">
            <span class="setting-label">Thứ tự câu hỏi</span>
            <select class="setting-select" id="optOrder">
              <option value="random">Trộn ngẫu nhiên</option>
              <option value="sequential" selected>Theo đúng thứ tự</option>
            </select>
          </div>
          <div class="setting-item">
            <span class="setting-label">Đếm ngược mỗi câu</span>
            <select class="setting-select" id="optTimer">
              <option value="0">Không giới hạn</option>
              <option value="15">15 giây</option>
              <option value="30" selected>30 giây</option>
              <option value="60">60 giây</option>
            </select>
          </div>
          <div class="setting-item">
            <span class="setting-label">Âm thanh & Rung điện thoại</span>
            <select class="setting-select" id="optAudio">
              <option value="1" selected>Bật âm thanh & rung</option>
              <option value="0">Tắt âm thanh</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <!-- ════════════ SCREEN 2: QUIZ RUN ════════════ -->
    <div id="screenQuiz" class="screen">
      <div class="quiz-nav-bar">
        <button class="nav-btn-back" onclick="confirmExitQuiz()">
          <span>✕</span> Thoát
        </button>
        <div class="quiz-badges-row">
          <div class="pill-stat streak" id="badgeStreak">🔥 0</div>
          <div class="pill-stat correct" id="badgeCorrect">✓ 0</div>
          <div class="pill-stat wrong" id="badgeWrong">✗ 0</div>
          <div class="pill-stat sound-toggle" id="btnSoundToggle" onclick="toggleMuteSound()">🔊</div>
        </div>
      </div>

      <div class="progress-track">
        <div class="progress-fill" id="quizProgressFill"></div>
      </div>

      <div class="timer-track" id="timerTrackWrap">
        <div class="timer-fill" id="quizTimerFill"></div>
      </div>

      <div class="q-meta">
        <span class="q-number-pill" id="qCurrentNumber">CÂU 1 / 45</span>
        <span class="q-type-badge" id="qTypeBadge">TRẮC NGHIỆM</span>
      </div>

      <div class="question-card">
        <div class="question-text" id="qTitleText">Câu hỏi ở đây</div>
      </div>

      <!-- Options / Inputs Area -->
      <div id="qInteractionArea"></div>

      <!-- Sticky Action Bar for Next -->
      <div class="quiz-bottom-bar" id="quizNextBar" style="display:none;">
        <button class="btn-action-primary" id="btnNextQ" onclick="handleNextQuestion()">
          <span>Câu tiếp theo</span> →
        </button>
      </div>
    </div>

    <!-- ════════════ SCREEN 3: DEDICATED ESSAY ════════════ -->
    <div id="screenEssay" class="screen">
      <div class="quiz-nav-bar">
        <button class="nav-btn-back" onclick="switchScreen('screenHome')">
          <span>←</span> Trang chủ
        </button>
        <div class="pill-stat" style="color:var(--accent-pink); background:rgba(236,72,153,0.15);">
          6 Đề Tự Luận Chuyên Sâu
        </div>
      </div>

      <header style="margin: 6px 0 16px;">
        <h2 style="font-size:22px; font-weight:800; color:var(--text-main);">Dàn Bài Tự Luận Đầy Đủ Ý</h2>
        <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">
          Được biên soạn chuẩn mực: Khái quát bối cảnh, phân tích luận điểm, ý nghĩa lịch sử và <strong>liên hệ trách nhiệm sinh viên</strong> thiết thực.
        </p>
      </header>

      <div class="essay-toolbar">
        <input type="text" class="search-box" id="essaySearchInput" placeholder="🔍 Tìm kiếm từ khóa (Tháng Tám, Kháng chiến, Đại hội VI, CNH-HĐH, Hội nhập...)" oninput="filterEssays()">
        <div class="essay-tabs-pill" id="essayPillTabs">
          <button class="pill-tab active" onclick="filterEssayTab('all')">Tất cả 6 câu</button>
          <button class="pill-tab" onclick="filterEssayTab(76)">Câu 76 (CM Tháng 8)</button>
          <button class="pill-tab" onclick="filterEssayTab(77)">Câu 77 (Kháng chiến Mỹ)</button>
          <button class="pill-tab" onclick="filterEssayTab(78)">Câu 78 (CNH ĐH VIII)</button>
          <button class="pill-tab" onclick="filterEssayTab(79)">Câu 79 (Hội nhập QT)</button>
          <button class="pill-tab" onclick="filterEssayTab(80)">Câu 80 (Đổi mới ĐH VI)</button>
          <button class="pill-tab" onclick="filterEssayTab(81)">Câu 81 (35 năm Đổi mới)</button>
        </div>
      </div>

      <div id="essayListContainer">
        <!-- Rendered via JS -->
      </div>
    </div>

    <!-- ════════════ SCREEN 4: RESULTS ════════════ -->
    <div id="screenResults" class="screen">
      <div class="results-wrap">
        <div class="ring-wrapper">
          <svg viewBox="0 0 160 160">
            <defs>
              <linearGradient id="gradPass" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#10b981" />
                <stop offset="100%" stop-color="#06b6d4" />
              </linearGradient>
              <linearGradient id="gradWarn" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b" />
                <stop offset="100%" stop-color="#ec4899" />
              </linearGradient>
              <linearGradient id="gradFail" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ef4444" />
                <stop offset="100%" stop-color="#f59e0b" />
              </linearGradient>
            </defs>
            <circle class="ring-track" cx="80" cy="80" r="72" />
            <circle class="ring-fill" id="resSvgRing" cx="80" cy="80" r="72" />
          </svg>
          <div class="ring-content">
            <span class="ring-pct" id="resPctText">0%</span>
            <span class="ring-label">Điểm số</span>
          </div>
        </div>

        <h2 class="result-grade-msg" id="resGradeTitle">Xuất sắc!</h2>
        <p class="result-grade-sub" id="resGradeSub">Bạn đã nắm rất vững kiến thức Lịch Sử Đảng.</p>

        <div class="results-grid">
          <div class="res-box">
            <div class="res-box-val" style="color:#34d399;" id="resCountCorrect">0</div>
            <div class="res-box-lbl">Đúng</div>
          </div>
          <div class="res-box">
            <div class="res-box-val" style="color:#f87171;" id="resCountWrong">0</div>
            <div class="res-box-lbl">Sai</div>
          </div>
          <div class="res-box">
            <div class="res-box-val" style="color:#fbbf24;" id="resMaxStreak">0</div>
            <div class="res-box-lbl">Streak kỷ lục</div>
          </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:10px; margin: 18px 0;">
          <button class="btn-action-primary" onclick="restartSameQuiz()">
            <span>🔄 Làm lại lượt này</span>
          </button>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
            <button class="btn-action-primary" style="background:rgba(255,255,255,0.06); border:1px solid var(--border-subtle); color:var(--text-main); box-shadow:none;" onclick="switchScreen('screenHome')">
              🏠 Trang chủ
            </button>
            <button class="btn-action-primary" style="background:rgba(236,72,153,0.18); border:1px solid rgba(236,72,153,0.3); color:#f472b6; box-shadow:none;" onclick="openEssayScreen()">
              📜 Xem tự luận
            </button>
          </div>
        </div>

        <!-- Detailed Review List -->
        <div class="review-wrap">
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
            <h3 style="font-size:16px; font-weight:800;">📋 Chi tiết bài làm</h3>
            <div class="review-tabs-filter">
              <button class="btn-filter active" onclick="filterReviewList('all')">Tất cả</button>
              <button class="btn-filter" onclick="filterReviewList('wrong')">Chỉ câu sai</button>
              <button class="btn-filter" onclick="filterReviewList('correct')">Câu đúng</button>
            </div>
          </div>
          <div id="reviewItemsStack"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Streak celebration popup -->
  <div class="streak-banner" id="streakBanner">🔥 STREAK 5!</div>

  <!-- Toast notification -->
  <div class="toast-pill" id="toastPill">
    <span id="toastIcon">✨</span>
    <span id="toastMessage">Thông báo</span>
  </div>

  <script>
    // ══════════════════════════════════════════════════════════════
    //  DATA SOURCE (81 QUESTIONS FROM DOCX)
    // ══════════════════════════════════════════════════════════════
    const RAW_MCQ = {mcq_json};
    const RAW_SA = {sa_json};
    const RAW_ESSAY = {essay_json};

    const STORAGE_KEY_WRONG = 'cuccung_lsdcs_wrong_v1';
    const STORAGE_KEY_SOUND = 'cuccung_sound_enabled';

    let wrongIds = JSON.parse(localStorage.getItem(STORAGE_KEY_WRONG) || '[]');
    let isSoundOn = localStorage.getItem(STORAGE_KEY_SOUND) !== '0';

    // ══════════════════════════════════════════════════════════════
    //  SYNTHESIZED WEB AUDIO & HAPTIC ENGINE (Zero External Assets)
    // ══════════════════════════════════════════════════════════════
    let audioCtx = null;
    function getAudioContext() {{
      if (!audioCtx) {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) audioCtx = new AudioContext();
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
      return audioCtx;
    }}

    function playSound(type) {{
      if (!isSoundOn) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;

        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'correct') {{
          // Delightful double chime (F5 -> A5)
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(698.46, now); // F5
          osc.frequency.setValueAtTime(880.00, now + 0.08); // A5
          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
          osc.start(now);
          osc.stop(now + 0.35);
          if (navigator.vibrate) navigator.vibrate([15]);
        }} else if (type === 'wrong') {{
          // Soft error buzz
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(180, now);
          osc.frequency.exponentialRampToValueAtTime(110, now + 0.28);
          gain.gain.setValueAtTime(0.25, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.start(now);
          osc.stop(now + 0.3);
          if (navigator.vibrate) navigator.vibrate([35, 30, 35]);
        }} else if (type === 'streak') {{
          // Triple joyful chime
          const osc2 = ctx.createOscillator();
          const gain2 = ctx.createGain();
          osc2.connect(gain2);
          gain2.connect(ctx.destination);

          osc.type = 'sine';
          osc.frequency.setValueAtTime(523.25, now); // C5
          osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
          osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
          osc.frequency.setValueAtTime(1046.50, now + 0.3); // C6

          gain.gain.setValueAtTime(0.25, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.55);
          osc.start(now);
          osc.stop(now + 0.55);
          if (navigator.vibrate) navigator.vibrate([20, 20, 20]);
        }} else if (type === 'tap') {{
          osc.type = 'sine';
          osc.frequency.setValueAtTime(800, now);
          gain.gain.setValueAtTime(0.05, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
          osc.start(now);
          osc.stop(now + 0.05);
        }}
      }} catch (e) {{
        console.warn('Audio play error:', e);
      }}
    }}

    function toggleMuteSound() {{
      isSoundOn = !isSoundOn;
      localStorage.setItem(STORAGE_KEY_SOUND, isSoundOn ? '1' : '0');
      const btn = document.getElementById('btnSoundToggle');
      if (btn) btn.textContent = isSoundOn ? '🔊' : '🔇';
      showToast(isSoundOn ? '🔊 Đã bật âm thanh' : '🔇 Đã tắt âm thanh');
    }}

    // ══════════════════════════════════════════════════════════════
    //  APP STATE & VARIABLES
    // ══════════════════════════════════════════════════════════════
    let currentQuizPool = [];
    let currentIdx = 0;
    let correctScore = 0;
    let wrongScore = 0;
    let currentStreak = 0;
    let maxStreakScore = 0;
    let isCurrentAnswered = false;
    let quizResultsHistory = [];
    let timerId = null;
    let timerTotalMs = 30000;
    let timerRemainingMs = 30000;
    let currentQuizMode = 'mcq';

    // ══════════════════════════════════════════════════════════════
    //  INITIALIZATION
    // ══════════════════════════════════════════════════════════════
    function updateWrongBadgeUI() {{
      const b = document.getElementById('wrongBadgeText');
      if (b) b.textContent = `${{wrongIds.length}} Câu`;
    }}

    function switchScreen(screenId) {{
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      const target = document.getElementById(screenId);
      if (target) {{
        target.classList.add('active');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}

    function toggleSettingsAccordion() {{
      const content = document.getElementById('settingsContent');
      const arrow = document.getElementById('settingsArrow');
      const isOpen = content.classList.contains('open');
      if (isOpen) {{
        content.classList.remove('open');
        arrow.style.transform = 'rotate(0deg)';
      }} else {{
        content.classList.add('open');
        arrow.style.transform = 'rotate(180deg)';
      }}
    }}

    // ══════════════════════════════════════════════════════════════
    //  QUIZ BUILDER & CONTROLLER
    // ══════════════════════════════════════════════════════════════
    function initAndStartQuiz(mode) {{
      currentQuizMode = mode;
      const countSel = parseInt(document.getElementById('optLimit').value);
      const order = document.getElementById('optOrder').value;
      const timerSec = parseInt(document.getElementById('optTimer').value);
      isSoundOn = document.getElementById('optAudio').value === '1';

      let pool = [];
      if (mode === 'mcq') {{
        pool = RAW_MCQ.map(q => ({{ ...q, type: 'mcq' }}));
      }} else if (mode === 'sa') {{
        pool = RAW_SA.map(q => ({{ ...q, type: 'sa', id: `sa_${{q.num}}` }}));
      }} else if (mode === 'mix') {{
        pool = [
          ...RAW_MCQ.map(q => ({{ ...q, type: 'mcq' }})),
          ...RAW_SA.map(q => ({{ ...q, type: 'sa', id: `sa_${{q.num}}` }}))
        ];
      }} else if (mode === 'wrong') {{
        if (wrongIds.length === 0) {{
          showToast('🎉 Bạn chưa có câu sai nào! Hãy làm quiz trước nhé.');
          return;
        }}
        const allQuestionsMap = {{}};
        RAW_MCQ.forEach(q => {{ allQuestionsMap[q.id] = {{ ...q, type: 'mcq' }}; }});
        RAW_SA.forEach(q => {{ allQuestionsMap[`sa_${{q.num}}`] = {{ ...q, type: 'sa', id: `sa_${{q.num}}` }}; }});
        pool = wrongIds.map(id => allQuestionsMap[id]).filter(Boolean);
      }}

      if (order === 'random') {{
        pool = pool.sort(() => Math.random() - 0.5);
      }}

      if (countSel > 0) {{
        pool = pool.slice(0, countSel);
      }}

      currentQuizPool = pool;
      currentIdx = 0;
      correctScore = 0;
      wrongScore = 0;
      currentStreak = 0;
      maxStreakScore = 0;
      quizResultsHistory = [];
      timerTotalMs = timerSec * 1000;

      switchScreen('screenQuiz');
      renderCurrentQuestion();
    }}

    function renderCurrentQuestion() {{
      clearInterval(timerId);
      isCurrentAnswered = false;

      if (currentIdx >= currentQuizPool.length) {{
        showResultsScreen();
        return;
      }}

      const q = currentQuizPool[currentIdx];
      const total = currentQuizPool.length;

      // Update progress
      const pct = (currentIdx / total) * 100;
      document.getElementById('quizProgressFill').style.width = pct + '%';
      document.getElementById('qCurrentNumber').textContent = `CÂU ${{currentIdx + 1}} / ${{total}}`;
      document.getElementById('qTypeBadge').textContent = q.type === 'mcq' ? 'TRẮC NGHIỆM' : 'CÂU HỎI NGẮN';
      document.getElementById('qTitleText').textContent = q.q;

      // Update badges
      document.getElementById('badgeStreak').textContent = `🔥 ${{currentStreak}}`;
      document.getElementById('badgeCorrect').textContent = `✓ ${{correctScore}}`;
      document.getElementById('badgeWrong').textContent = `✗ ${{wrongScore}}`;

      // Hide Next button until answered
      document.getElementById('quizNextBar').style.display = 'none';

      // Build options or input area
      const area = document.getElementById('qInteractionArea');
      area.innerHTML = '';

      if (q.type === 'mcq') {{
        const stack = document.createElement('div');
        stack.className = 'options-stack';
        const letters = ['A', 'B', 'C', 'D'];

        q.opts.forEach((optText, optIdx) => {{
          const btn = document.createElement('button');
          btn.className = 'opt-btn';
          btn.dataset.idx = optIdx;
          btn.innerHTML = `<span class="opt-letter">${{letters[optIdx]}}</span><span>${{optText}}</span>`;
          btn.onclick = () => selectMcqOption(optIdx);
          stack.appendChild(btn);
        }});
        area.appendChild(stack);
      }} else {{
        const box = document.createElement('div');
        box.className = 'sa-box';
        box.innerHTML = `
          <textarea class="sa-input" id="saInputArea" placeholder="Nhập câu trả lời hoặc suy nghĩ câu trả lời trong đầu..."></textarea>
          <button class="btn-action-primary" style="padding:12px 20px; font-size:14px;" onclick="revealSaAnswer()">
            🔍 Xem đáp án mẫu & Tự đánh giá
          </button>
          <div id="saRevealMount"></div>
        `;
        area.appendChild(box);
      }}

      startQuestionTimer();
    }}

    function selectMcqOption(selectedIdx) {{
      if (isCurrentAnswered) return;
      isCurrentAnswered = true;
      clearInterval(timerId);

      const q = currentQuizPool[currentIdx];
      const isCorrect = selectedIdx === q.ans;
      const buttons = document.querySelectorAll('.opt-btn');

      buttons.forEach((btn, idx) => {{
        if (idx === q.ans) btn.classList.add('correct');
        if (idx === selectedIdx && !isCorrect) btn.classList.add('wrong');
        if (idx !== selectedIdx && idx !== q.ans) btn.classList.add('disabled');
      }});

      if (isCorrect) {{
        correctScore++;
        currentStreak++;
        if (currentStreak > maxStreakScore) maxStreakScore = currentStreak;
        playSound('correct');
        // Remove from wrong history if correct
        wrongIds = wrongIds.filter(id => id !== q.id);
        if (currentStreak >= 3 && currentStreak % 3 === 0) {{
          triggerStreakPopup(currentStreak);
        }}
      }} else {{
        wrongScore++;
        currentStreak = 0;
        playSound('wrong');
        if (!wrongIds.includes(q.id)) wrongIds.push(q.id);
      }}

      localStorage.setItem(STORAGE_KEY_WRONG, JSON.stringify(wrongIds));
      updateWrongBadgeUI();

      quizResultsHistory.push({{
        q: q.q,
        type: 'mcq',
        isPass: isCorrect,
        userAns: q.opts[selectedIdx],
        correctAns: q.opts[q.ans]
      }});

      document.getElementById('badgeStreak').textContent = `🔥 ${{currentStreak}}`;
      document.getElementById('badgeCorrect').textContent = `✓ ${{correctScore}}`;
      document.getElementById('badgeWrong').textContent = `✗ ${{wrongScore}}`;

      document.getElementById('quizNextBar').style.display = 'block';
    }}

    function revealSaAnswer() {{
      if (isCurrentAnswered) return;
      isCurrentAnswered = true;
      clearInterval(timerId);

      const q = currentQuizPool[currentIdx];
      const mount = document.getElementById('saRevealMount');
      mount.innerHTML = `
        <div class="sa-reveal-card">
          <div class="sa-reveal-title">
            <span>✅ Đáp án chuẩn</span>
          </div>
          <div class="sa-reveal-body">${{q.a}}</div>
          <div class="self-grade-row">
            <button class="grade-btn pass" onclick="gradeSaAnswer(true)">
              <span>👍 Tôi trả lời đúng</span>
            </button>
            <button class="grade-btn fail" onclick="gradeSaAnswer(false)">
              <span>👎 Cần ôn lại câu này</span>
            </button>
          </div>
        </div>
      `;
    }}

    function gradeSaAnswer(isPass) {{
      const q = currentQuizPool[currentIdx];
      const userInput = document.getElementById('saInputArea')?.value.trim() || '(Xem đáp án)';

      if (isPass) {{
        correctScore++;
        currentStreak++;
        if (currentStreak > maxStreakScore) maxStreakScore = currentStreak;
        playSound('correct');
        wrongIds = wrongIds.filter(id => id !== q.id);
      }} else {{
        wrongScore++;
        currentStreak = 0;
        playSound('wrong');
        if (!wrongIds.includes(q.id)) wrongIds.push(q.id);
      }}

      localStorage.setItem(STORAGE_KEY_WRONG, JSON.stringify(wrongIds));
      updateWrongBadgeUI();

      quizResultsHistory.push({{
        q: q.q,
        type: 'sa',
        isPass: isPass,
        userAns: userInput,
        correctAns: q.a
      }});

      handleNextQuestion();
    }}

    function handleNextQuestion() {{
      playSound('tap');
      currentIdx++;
      renderCurrentQuestion();
    }}

    function startQuestionTimer() {{
      const track = document.getElementById('timerTrackWrap');
      const fill = document.getElementById('quizTimerFill');

      if (timerTotalMs <= 0) {{
        track.style.display = 'none';
        return;
      }}
      track.style.display = 'block';
      timerRemainingMs = timerTotalMs;
      fill.style.width = '100%';
      fill.className = 'timer-fill';

      const intervalMs = 100;
      timerId = setInterval(() => {{
        timerRemainingMs -= intervalMs;
        const pct = Math.max(0, (timerRemainingMs / timerTotalMs) * 100);
        fill.style.width = pct + '%';

        if (pct < 20) fill.className = 'timer-fill danger';
        else if (pct < 50) fill.className = 'timer-fill warn';

        if (timerRemainingMs <= 0) {{
          clearInterval(timerId);
          if (!isCurrentAnswered) {{
            const q = currentQuizPool[currentIdx];
            if (q.type === 'mcq') {{
              selectMcqOption(-1);
            }} else {{
              revealSaAnswer();
            }}
            showToast('⏰ Hết thời gian làm bài câu này!');
          }}
        }}
      }}, intervalMs);
    }}

    function confirmExitQuiz() {{
      if (confirm('Bạn có chắc chắn muốn dừng lượt làm bài này không?')) {{
        clearInterval(timerId);
        switchScreen('screenHome');
      }}
    }}

    function triggerStreakPopup(count) {{
      playSound('streak');
      const banner = document.getElementById('streakBanner');
      banner.textContent = `🔥 STREAK ${{count}}! TUYỆT VỜI!`;
      banner.classList.add('active');
      setTimeout(() => banner.classList.remove('active'), 1100);
    }}

    // ══════════════════════════════════════════════════════════════
    //  RESULTS & REVIEW
    // ══════════════════════════════════════════════════════════════
    function showResultsScreen() {{
      clearInterval(timerId);
      switchScreen('screenResults');

      const total = quizResultsHistory.length;
      const pct = total > 0 ? Math.round((correctScore / total) * 100) : 0;

      document.getElementById('resPctText').textContent = pct + '%';
      document.getElementById('resCountCorrect').textContent = correctScore;
      document.getElementById('resCountWrong').textContent = wrongScore;
      document.getElementById('resMaxStreak').textContent = maxStreakScore;

      // Animate SVG circle
      const circumference = 2 * Math.PI * 72; // ~452.38
      const ring = document.getElementById('resSvgRing');
      ring.style.strokeDasharray = circumference;
      const offset = circumference - (pct / 100) * circumference;
      setTimeout(() => {{ ring.style.strokeDashoffset = offset; }}, 80);

      const title = document.getElementById('resGradeTitle');
      const sub = document.getElementById('resGradeSub');

      if (pct >= 85) {{
        ring.style.stroke = 'url(#gradPass)';
        title.textContent = '🏆 Xuất sắc!';
        sub.textContent = 'Bạn đã nắm trọn vẹn kiến thức và sẵn sàng đạt điểm A!';
        startConfetti();
      }} else if (pct >= 65) {{
        ring.style.stroke = 'url(#gradWarn)';
        title.textContent = '👍 Khá tốt!';
        sub.textContent = 'Kiến thức khá vững, hãy xem lại các câu sai để hoàn thiện hơn.';
      }} else {{
        ring.style.stroke = 'url(#gradFail)';
        title.textContent = '📖 Cần ôn tập thêm!';
        sub.textContent = 'Đừng lo lắng, hãy dùng chế độ "Luyện lại câu sai" và xem Tự luận nhé!';
      }}

      renderReviewList('all');
    }}

    function renderReviewList(filter) {{
      const mount = document.getElementById('reviewItemsStack');
      mount.innerHTML = '';

      let items = quizResultsHistory;
      if (filter === 'wrong') items = items.filter(i => !i.isPass);
      if (filter === 'correct') items = items.filter(i => i.isPass);

      if (items.length === 0) {{
        mount.innerHTML = '<div style="text-align:center; padding:20px; color:var(--text-muted); font-size:13px;">Không có câu hỏi nào.</div>';
        return;
      }}

      items.forEach((item, idx) => {{
        const card = document.createElement('div');
        card.className = `review-item-card ${{item.isPass ? 'is-pass' : 'is-fail'}}`;
        card.innerHTML = `
          <div class="review-q-title">${{item.isPass ? '✅' : '❌'}} ${{item.q}}</div>
          <div class="review-ans-row">
            ${{!item.isPass && item.userAns ? `<div>Bạn chọn: <span class="badge-ans ans-wrong">${{item.userAns}}</span></div>` : ''}}
            <div>Đáp án đúng: <span class="badge-ans ans-correct">${{item.correctAns}}</span></div>
          </div>
        `;
        mount.appendChild(card);
      }});
    }}

    function filterReviewList(filter) {{
      document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
      const activeBtn = Array.from(document.querySelectorAll('.btn-filter')).find(b => b.getAttribute('onclick').includes(filter));
      if (activeBtn) activeBtn.classList.add('active');
      renderReviewList(filter);
    }}

    function restartSameQuiz() {{
      initAndStartQuiz(currentQuizMode);
    }}

    // ══════════════════════════════════════════════════════════════
    //  DEDICATED ESSAY CONTROLLER (6 ESSAYS)
    // ══════════════════════════════════════════════════════════════
    function openEssayScreen() {{
      switchScreen('screenEssay');
      renderEssayCards(RAW_ESSAY);
    }}

    function renderEssayCards(list) {{
      const mount = document.getElementById('essayListContainer');
      mount.innerHTML = '';

      if (list.length === 0) {{
        mount.innerHTML = '<div style="text-align:center; padding:30px; color:var(--text-muted);">Không tìm thấy câu tự luận phù hợp.</div>';
        return;
      }}

      list.forEach((essay, idx) => {{
        const card = document.createElement('div');
        card.className = 'essay-card';
        card.id = `essayCard_${{essay.num}}`;

        card.innerHTML = `
          <div class="essay-card-header" onclick="toggleEssayCard(${{essay.num}})">
            <div>
              <span class="essay-badge-num">CÂU ${{essay.num}} – TỰ LUẬN TRỌNG TÂM</span>
              <div class="essay-q-title">${{essay.q}}</div>
            </div>
            <span class="essay-expand-icon" id="essayArrow_${{essay.num}}">▼</span>
          </div>
          <div class="essay-card-body">
            <div class="essay-actions-bar">
              <span style="font-size:12px; color:var(--text-muted); font-weight:600;">Dàn ý & Phân tích chi tiết</span>
              <button class="btn-copy" onclick="copyEssayContent(${{essay.num}})">
                <span>📋</span> Sao chép dàn ý
              </button>
            </div>
            <div class="essay-text-formatted selectable" id="essayText_${{essay.num}}">${{formatEssayContent(essay.a)}}</div>
          </div>
        `;
        mount.appendChild(card);
      }});
    }}

    function formatEssayContent(text) {{
      // Highlight "LIÊN HỆ TRÁCH NHIỆM CỦA SINH VIÊN" specially
      return text.replace(/II\.\s*LIÊN HỆ TRÁCH NHIỆM[\s\S]*/, match => {{
        return `<div class="essay-student-highlight"><h4>🎓 LIÊN HỆ TRÁCH NHIỆM SINH VIÊN</h4>${{match}}</div>`;
      }});
    }}

    function toggleEssayCard(num) {{
      const card = document.getElementById(`essayCard_${{num}}`);
      if (card) {{
        card.classList.toggle('expanded');
      }}
    }}

    function copyEssayContent(num) {{
      const essay = RAW_ESSAY.find(e => e.num === num);
      if (essay) {{
        const full = `CÂU ${{essay.num}}: ${{essay.q}}\n\n${{essay.a}}`;
        navigator.clipboard.writeText(full).then(() => {{
          showToast('✅ Đã sao chép toàn bộ dàn bài câu ' + num + ' vào clipboard!');
        }});
      }}
    }}

    function filterEssays() {{
      const term = document.getElementById('essaySearchInput').value.toLowerCase().trim();
      const filtered = RAW_ESSAY.filter(e => {{
        return e.q.toLowerCase().includes(term) || e.a.toLowerCase().includes(term);
      }});
      renderEssayCards(filtered);
    }}

    function filterEssayTab(tab) {{
      document.querySelectorAll('.pill-tab').forEach(t => t.classList.remove('active'));
      const clicked = Array.from(document.querySelectorAll('.pill-tab')).find(t => t.getAttribute('onclick').includes(String(tab)));
      if (clicked) clicked.classList.add('active');

      if (tab === 'all') {{
        renderEssayCards(RAW_ESSAY);
      }} else {{
        const item = RAW_ESSAY.filter(e => e.num === parseInt(tab));
        renderEssayCards(item);
        if (item.length > 0) {{
          setTimeout(() => toggleEssayCard(tab), 100);
        }}
      }}
    }}

    // ══════════════════════════════════════════════════════════════
    //  TOAST & CONFETTI
    // ══════════════════════════════════════════════════════════════
    let toastTimeout = null;
    function showToast(msg) {{
      const t = document.getElementById('toastPill');
      const m = document.getElementById('toastMessage');
      m.textContent = msg;
      t.classList.add('active');
      clearTimeout(toastTimeout);
      toastTimeout = setTimeout(() => t.classList.remove('active'), 2200);
    }}

    // Lightweight high-performance canvas confetti
    function startConfetti() {{
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#8b5cf6', '#ec4899', '#06b6d4', '#10b981', '#f59e0b', '#fbbf24', '#ffffff'];

      for (let i = 0; i < 90; i++) {{
        particles.push({{
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height * 0.4,
          r: Math.random() * 5 + 3,
          color: colors[Math.floor(Math.random() * colors.length)],
          vx: (Math.random() - 0.5) * 5,
          vy: Math.random() * 4 + 2,
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 6
        }});
      }}

      let frame = 0;
      function animate() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.rotation += p.rotSpeed;

          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.r, -p.r, p.r * 2, p.r * 1.5);
          ctx.restore();
        }});

        frame++;
        if (frame < 180) {{
          requestAnimationFrame(animate);
        }} else {{
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        }}
      }}
      animate();
    }}

    // Keyboard navigation (Desktop)
    document.addEventListener('keydown', (e) => {{
      if (document.getElementById('screenQuiz').classList.contains('active')) {{
        if (['1', '2', '3', '4'].includes(e.key)) {{
          const idx = parseInt(e.key) - 1;
          const btns = document.querySelectorAll('.opt-btn');
          if (btns[idx] && !isCurrentAnswered) {{
            selectMcqOption(idx);
          }}
        }} else if (e.key === 'Enter' && isCurrentAnswered) {{
          handleNextQuestion();
        }}
      }}
    }});

    // Setup initial state
    updateWrongBadgeUI();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Generated index.html successfully with full 81 questions!")
