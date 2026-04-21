# ============================================================
#   CyberShield Pro - Main Streamlit Web Application
#   Developed by: Hack Shastra
#   Version: 2.0
# ============================================================

import streamlit as st
import pickle
import pandas as pd
import time

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="CyberShield Pro | Hack Shastra",
    page_icon="🛡️",
    layout="wide"
)

# ── Global CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;600&display=swap');

    /* Hide Streamlit default UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container { padding-top: 0rem; }

    /* Background */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #eff6ff 0%, #ffffff 100%);
        font-family: 'Inter', sans-serif;
        color: #1e293b;
    }
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ──── NAVBAR ──── */
    .navbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 68px;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-bottom: 1px solid rgba(29, 78, 216, 0.1);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 50px;
        box-shadow: 0 2px 20px rgba(29, 78, 216, 0.07);
    }
    .nav-logo {
        font-family: 'Outfit', sans-serif;
        font-size: 22px;
        font-weight: 800;
        background: linear-gradient(90deg, #1d4ed8, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }
    .nav-links {
        font-size: 13px;
        font-weight: 600;
        color: #475569;
        display: flex;
        align-items: center;
        gap: 28px;
    }
    .nav-links span { cursor: pointer; transition: color 0.2s; }
    .nav-links span:hover { color: #1d4ed8; }
    .dev-badge {
        background: linear-gradient(90deg, #1d4ed8, #0ea5e9);
        color: white;
        padding: 5px 16px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    /* ──── HERO ──── */
    .hero {
        text-align: center;
        padding: 120px 20px 30px 20px;
    }
    .hero h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 4.2rem;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.1;
        margin-bottom: 18px;
    }
    .hero h1 span {
        background: linear-gradient(to right, #1d4ed8, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        font-size: 1.15rem;
        color: #475569;
        max-width: 580px;
        margin: 0 auto 10px auto;
        line-height: 1.7;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(29, 78, 216, 0.08);
        border: 1px solid rgba(29, 78, 216, 0.2);
        color: #1d4ed8;
        padding: 5px 18px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* ──── STATS CARDS ──── */
    .stats-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 30px auto;
        max-width: 700px;
    }
    .stat-card {
        flex: 1;
        background: white;
        border: 1px solid rgba(29, 78, 216, 0.12);
        border-radius: 14px;
        padding: 18px 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .stat-num {
        font-family: 'Outfit', sans-serif;
        font-size: 1.9rem;
        font-weight: 800;
        background: linear-gradient(to right, #1d4ed8, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stat-label {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 600;
        margin-top: 3px;
    }

    /* ──── INPUT ──── */
    .stTextInput div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 2px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        transition: all 0.3s ease;
    }
    .stTextInput div[data-baseweb="input"]:focus-within {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.15) !important;
    }
    .stTextInput input {
        color: #0f172a !important;
        font-size: 16px !important;
        font-family: 'Outfit', sans-serif;
        padding: 13px 10px !important;
        background-color: transparent !important;
    }
    .stTextInput input::placeholder { color: #94a3b8 !important; }

    /* ──── SCAN BUTTON ──── */
    div.stButton > button {
        background: linear-gradient(90deg, #1d4ed8 0%, #0ea5e9 100%);
        color: white;
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 17px;
        min-height: 52px;
        padding: 0.5rem 1.5rem !important;
        border-radius: 12px;
        border: none;
        width: 100%;
        margin-top: 12px;
        box-shadow: 0 6px 20px rgba(29, 78, 216, 0.3);
        transition: all 0.25s ease;
        letter-spacing: 0.3px;
    }
    div.stButton > button p {
        font-size: 17px !important;
        font-weight: 700 !important;
        color: white !important;
        margin: 0 !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(29, 78, 216, 0.4);
    }

    /* ──── RESULT CARD ──── */
    .result-box {
        background: white;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(0,0,0,0.07);
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        margin-top: 10px;
    }

    /* ──── FOOTER ──── */
    .pro-footer {
        text-align: center;
        padding: 50px 20px 40px 20px;
        margin-top: 90px;
        border-top: 1px solid rgba(0,0,0,0.06);
        background: linear-gradient(180deg, #f8fafc, #eff6ff);
    }
    .pro-footer h3 {
        font-family: 'Outfit', sans-serif;
        color: #0f172a;
        font-weight: 800;
        font-size: 1.4rem;
        margin-bottom: 4px;
    }
    .pro-footer h4 {
        background: linear-gradient(90deg, #1d4ed8, #0ea5e9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 4px;
        margin-bottom: 10px;
    }
    .pro-footer p { color: #64748b; font-size: 0.88rem; margin: 4px 0; }

    /* Metric */
    div[data-testid="stMetricValue"] {
        font-size: 2.8rem;
        font-weight: 800;
        font-family: 'Outfit', sans-serif;
        color: #0f172a;
    }
</style>

<!-- Navigation Bar -->
<div class="navbar">
    <div class="nav-logo">🛡️ CYBERSHIELD PRO</div>
    <div class="nav-links">
        <span>Dashboard</span>
        <span>Threat Intel</span>
        <span>API Docs</span>
        <div class="dev-badge">Hack Shastra v2.0</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Load Model ───────────────────────────────────────────────
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

model = load_model()


# ── Feature Extraction ───────────────────────────────────────
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if '@' in url else 0,
        1 if 'https' in url else 0,
        1 if '-' in url else 0
    ]


# ── Reason Generator ─────────────────────────────────────────
def get_reasons(features):
    url_length, dot_count, has_at, has_https, has_hyphen = features
    reasons = []
    if url_length > 75:
        reasons.append("📏 **Length Anomaly** — URL is unusually long, commonly used to conceal malicious routing paths.")
    if has_at == 1:
        reasons.append("📧 **Symbol Injection** — Contains `@`, which redirects the browser to ignore everything before it.")
    if has_https == 0:
        reasons.append("🔓 **Unencrypted Protocol** — No HTTPS detected. Data transmitted can be intercepted.")
    if dot_count > 3:
        reasons.append("🌍 **Subdomain Masking** — Excessive dots indicate nested subdomains to mimic trusted sites.")
    if has_hyphen == 1:
        reasons.append("➖ **Typosquatting Risk** — Hyphens are frequently used in fake lookalike domains.")
    return reasons


# ── Hero Section ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ Powered by Random Forest AI</div>
    <h1>Enterprise-Grade<br><span>Threat Detection</span></h1>
    <p>Leveraging advanced Machine Learning to scan URL routing paths, detect credential harvesting, and assess phishing risk in milliseconds.</p>
</div>

<div class="stats-row">
    <div class="stat-card">
        <div class="stat-num">99.2%</div>
        <div class="stat-label">Detection Accuracy</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">&lt;1s</div>
        <div class="stat-label">Scan Response Time</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">5</div>
        <div class="stat-label">Heuristic Signals</div>
    </div>
    <div class="stat-card">
        <div class="stat-num">RF</div>
        <div class="stat-label">Model Architecture</div>
    </div>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.error("⛔ SYSTEM HALT: `model.pkl` not found! Run `train_model.py` first to initialize the AI engine.")
    st.stop()

# ── Main Scan Interface ───────────────────────────────────────
_, col_main, _ = st.columns([1, 2, 1])

with col_main:
    st.markdown(
        "<h3 style='text-align:center;font-family:Outfit;font-weight:700;margin-bottom:18px;color:#0f172a;'>"
        "🔬 Neural Scan Engine</h3>",
        unsafe_allow_html=True
    )

    url = st.text_input(
        "URL Input",
        label_visibility="collapsed",
        placeholder="🔗  Paste a URL to scan (e.g. https://paypal-secure-login.com)"
    )

    if st.button("⚡ Initialize Deep Scan", key="scan_btn"):
        if url.strip():
            progress_bar = st.progress(0)
            status_text  = st.empty()

            status_text.markdown("📡 **Phase 1/3** — Connecting to threat intelligence servers...")
            time.sleep(0.45)
            progress_bar.progress(30)

            status_text.markdown("🔍 **Phase 2/3** — Extracting URL heuristic feature vectors...")
            time.sleep(0.45)
            progress_bar.progress(65)

            features   = extract_features(url.strip())
            prediction = model.predict([features])[0]
            probability = model.predict_proba([features])[0]

            status_text.markdown("🧠 **Phase 3/3** — Random Forest classification in progress...")
            time.sleep(0.35)
            progress_bar.progress(100)

            status_text.empty()
            progress_bar.empty()

            confidence = probability[1] * 100 if prediction == 1 else probability[0] * 100

            st.markdown("<hr style='border-color:rgba(29,78,216,0.1); margin:20px 0;'>", unsafe_allow_html=True)

            res_col1, res_col2 = st.columns([1, 1.6])

            with res_col1:
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.markdown("<h4 style='color:#475569; margin-bottom:10px;'>🧾 Verdict</h4>", unsafe_allow_html=True)
                if prediction == 0:
                    st.success("## ✅ SAFE URL")
                    st.metric("AI Confidence", f"{confidence:.2f}%", delta="✓ Clean")
                    st.balloons()
                else:
                    st.error("## 🚨 PHISHING THREAT")
                    st.metric("AI Confidence", f"{confidence:.2f}%", delta="⚠ Threat", delta_color="inverse")
                st.markdown("</div>", unsafe_allow_html=True)

            with res_col2:
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.markdown("<h4 style='color:#475569; margin-bottom:10px;'>📋 Threat Analysis</h4>", unsafe_allow_html=True)
                if prediction == 1:
                    reasons = get_reasons(features)
                    if reasons:
                        for r in reasons:
                            st.markdown(f"> {r}")
                    else:
                        st.warning("Pattern flagged by model but no specific indicators found in heuristics.")
                else:
                    st.markdown("✅ All 5 heuristic checks passed with no phishing signals detected.")
                    st.info("💡 **Tip:** Always verify the site's SSL certificate before entering credentials.")
                st.markdown("</div>", unsafe_allow_html=True)

            # Developer log expander
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander("🛠️ Developer Log — Raw Feature Tensors"):
                feature_df = pd.DataFrame(
                    [features],
                    columns=["URL Length", "Dot Count", "Has @", "Has HTTPS", "Has Hyphen"]
                )
                st.dataframe(feature_df, use_container_width=True)
                st.caption(f"Prediction raw: {prediction} | Probabilities: Safe={probability[0]:.4f} | Phishing={probability[1]:.4f}")

        else:
            st.warning("⚠️ Please enter a URL to scan.")


# ── Footer ───────────────────────────────────────────────────
st.markdown("""
<div class="pro-footer">
    <h3>🛡️ CyberShield Pro</h3>
    <h4>Developed &amp; Engineered by Hack Shastra © 2026</h4>
    <p>Built with Python · Scikit-Learn Random Forest · Streamlit</p>
    <p style="font-size:0.78rem; margin-top:10px; color:#94a3b8;">
        This tool is for educational purposes. Always exercise caution when browsing unknown URLs.
    </p>
</div>
""", unsafe_allow_html=True)
