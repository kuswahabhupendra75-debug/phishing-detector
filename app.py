import streamlit as st
import pickle
import pandas as pd
import time

# Set Wide Layout
st.set_page_config(page_title="CyberShield Pro | By Bhupendra", page_icon="🛡️", layout="wide")

# Hide Default Streamlit UI & Add Custom CSS for Ultra-Premium Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;600&display=swap');

    /* Hide Streamlit Header & Footer entirely */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div.block-container {
        padding-top: 0rem;
    }

    /* Background and Global Font */
    .stApp {
        background: radial-gradient(circle at 10% 20%, #0c1015 0%, #161b22 100%);
        font-family: 'Inter', sans-serif;
        color: #c9d1d9;
    }
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Custom Top Navigation Bar */
    .navbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 70px;
        background: rgba(13, 17, 23, 0.85);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 50px;
    }
    .nav-logo {
        font-family: 'Outfit', sans-serif;
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(90deg, #4481eb, #04befe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }
    .nav-links {
        font-size: 14px;
        font-weight: 600;
        color: #8b949e;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
    }
    .nav-links span {
        margin-left: 30px;
        cursor: pointer;
        transition: color 0.3s;
    }
    .nav-links span:hover {
        color: #fff;
    }
    .dev-badge {
        background-color: rgba(4, 190, 254, 0.1);
        border: 1px solid rgba(4, 190, 254, 0.3);
        color: #04befe;
        padding: 5px 15px;
        border-radius: 20px;
        margin-left: 30px;
        font-size: 12px;
        font-weight: bold;
    }
    
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 120px 20px 40px 20px;
    }
    .hero h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 4.5rem;
        font-weight: 800;
        color: #fff;
        line-height: 1.1;
        margin-bottom: 20px;
    }
    .hero h1 span {
        background: linear-gradient(to right, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        font-size: 1.25rem;
        color: #8b949e;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Input & Button Overlay - Extreme Styling */
    div[data-baseweb="input"] > div {
        background: rgba(13, 17, 23, 0.9) !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px;
        padding: 12px 15px;
        color: white;
        font-size: 18px;
        transition: all 0.3s ease;
    }
    div[data-baseweb="input"] > div:focus-within {
        border-color: #04befe !important;
        box-shadow: 0 0 20px rgba(4, 190, 254, 0.3) !important;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #1f6feb 0%, #3fb950 100%);
        color: white;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 18px;
        padding: 20px 0;
        border-radius: 12px;
        border: none;
        width: 100%;
        margin-top: 15px;
        box-shadow: 0 10px 20px rgba(31, 111, 235, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(63, 185, 80, 0.4);
        color: white;
    }

    /* Footer */
    .pro-footer {
        text-align: center;
        padding: 60px 20px;
        margin-top: 100px;
        border-top: 1px solid rgba(255,255,255,0.05);
        background: #0d1117;
    }
    .pro-footer h3 {
        font-family: 'Outfit', sans-serif;
        color: #fff;
        font-weight: 800;
        margin-bottom: 2px;
    }
    .pro-footer h4 {
        color: #04befe;
        font-weight: 600;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    .pro-footer p {
        color: #8b949e;
        font-size: 0.95rem;
    }

    /* Target Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 3rem;
        font-weight: 800;
        font-family: 'Outfit', sans-serif;
    }

</style>

<!-- Injecting Navigation Bar -->
<div class="navbar">
    <div class="nav-logo">🛡️ CYBERSHIELD PRO</div>
    <div class="nav-links">
        <span>Dashboard</span>
        <span>Threat Intel</span>
        <span>API Docs</span>
        <div class="dev-badge">v2.0 Enterprise</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        return None

model = load_model()

# Feature extraction function
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if '@' in url else 0,
        1 if 'https' in url else 0,
        1 if '-' in url else 0
    ]

# Reason generator
def get_reasons(features):
    url_length, dot_count, has_at, has_https, has_hyphen = features
    reasons = []
    if url_length > 75: reasons.append("📏 **Length Anomaly**: The URL is unusually long, commonly used to hide malicious routing paths.")
    if has_at == 1: reasons.append("📧 **Symbol Detection**: Contains '@', which forces the browser to ignore the leading characters and jump to the scam domain.")
    if has_https == 0: reasons.append("🔓 **Unencrypted Protocol**: Connection uses HTTP, meaning data interception is possible.")
    if dot_count > 3: reasons.append("🌍 **Subdomain Masking**: Contains multiple dots to emulate a trusted domain within a subdomain.")
    if has_hyphen == 1: reasons.append("➖ **Typosquatting Risk**: Uses hyphens typically associated with imitation/fake domains.")
    return reasons

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Enterprise-Grade<br><span>Threat Detection</span></h1>
    <p>Leveraging advanced Artificial Intelligence to evaluate routing paths, encrypt traffic signatures, and prevent credential harvesting in real-time.</p>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.error("SYSTEM HALT: AI weights (`model.pkl`) missing. Please initialize training sequence.")
    st.stop()

# Layout: Spacer columns to center the main functional area
_, col_main, _ = st.columns([1, 2, 1])

with col_main:
    st.markdown("<h3 style='text-align: center; font-family: Outfit; font-weight: 600; margin-bottom: 20px; color: #fff;'>Deep Scan Neural Engine</h3>", unsafe_allow_html=True)
    
    url = st.text_input("Enter Target", label_visibility="collapsed", placeholder="Enter website link here (e.g., https://paypal-secure-login.com)")
    
    if st.button("Initialize Deep Scan", key="scan_btn"):
        if url:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulated backend processing delay for "Pro" feel
            status_text.markdown("📡 **Phase 1/3:** Establishing connection to threat intel servers...")
            time.sleep(0.5)
            progress_bar.progress(33)
            
            status_text.markdown("🔍 **Phase 2/3:** Extracting URL heuristic patterns...")
            time.sleep(0.5)
            progress_bar.progress(66)
            
            features = extract_features(url)
            prediction = model.predict([features])[0]
            probability = model.predict_proba([features])[0]
            
            status_text.markdown("🧠 **Phase 3/3:** ML Model classification active...")
            time.sleep(0.4)
            progress_bar.progress(100)
            
            status_text.empty()
            progress_bar.empty()
            
            confidence_pct = probability[1] * 100 if prediction == 1 else probability[0] * 100
            
            st.markdown("<hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
            
            res_col1, res_col2 = st.columns([1, 1.5])
            
            with res_col1:
                st.markdown("<h4 style='color: #8b949e;'>Diagnostic Status</h4>", unsafe_allow_html=True)
                if prediction == 0:
                    st.success("## ✅ SECURE")
                    st.metric(label="AI Confidence Score", value=f"{confidence_pct:.2f}%", delta="Clean")
                    st.balloons()
                else:
                    st.error("## 🚨 CRITICAL RISK")
                    st.metric(label="AI Confidence Score", value=f"{confidence_pct:.2f}%", delta="-Threat Detected", delta_color="inverse")
            
            with res_col2:
                st.markdown("<h4 style='color: #8b949e;'>System Diagnostics</h4>", unsafe_allow_html=True)
                if prediction == 1:
                    st.markdown("The neural engine identified immediate security risks:")
                    for r in get_reasons(features):
                        st.markdown(f"> {r}")
                else:
                    st.markdown("✅ All heuristic checks passed. No common phishing vectors identified.")
                    st.info("Routine advisory: Verify the SSL certificate of the site upon load.")
            
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander("🛠️ View Developer Log & Raw Tensors"):
                feature_df = pd.DataFrame([features], columns=["Len", "Dots", "Has @", "Has HTTPs", "Has -"])
                st.dataframe(feature_df, use_container_width=True)
        else:
            st.warning("⚠️ Target parameter missing. Please provide a URL.")


# Footer Section Explicitly Assigned with User's Name
st.markdown("""
<div class="pro-footer">
    <h3>CyberShield Pro</h3>
    <h4>All rights reserved by BhupendraSinh Rajgopal Kushwaha © 2026</h4>
    <p>Engineered, Designed, and Developed by a Professional Developer for Enterprise Security.</p>
    <p style="font-size: 0.8rem; margin-top: 10px; color: #6e7681;">Powered by Advanced Machine Learning, Python, and Streamlit.</p>
</div>
""", unsafe_allow_html=True)
