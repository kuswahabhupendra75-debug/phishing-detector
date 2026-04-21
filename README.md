# 🛡️ CyberShield Pro — AI Phishing Detection System

> **Enterprise-grade URL threat intelligence powered by Machine Learning**  
> *Developed & Engineered by **Hack Shastra** © 2026*

---

## 🔍 What is CyberShield Pro?

CyberShield Pro is an AI-powered phishing URL detection system that analyzes any website link in real-time and determines whether it is **safe** or a **phishing/malicious threat**. It uses a trained **Random Forest ML model** to evaluate structural URL patterns and provide an **AI confidence score** along with detailed threat indicators.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🤖 AI Deep Scan | Random Forest ML model trained on URL heuristics |
| 📊 Confidence Score | Shows % certainty of safe or phishing result |
| 🔎 Threat Breakdown | Explains exactly *why* a URL was flagged |
| ⚡ Real-time Analysis | Instant results with no external API calls |
| 💻 Premium UI | Glassmorphism design, animated scan progress |
| 🖥️ Terminal Demo | CLI demo script for quick offline testing |

---

## 🛠️ Technology Stack

- **Python 3.12** — Core language
- **Scikit-Learn** — Random Forest Classifier (ML model)
- **Pandas & NumPy** — Data processing & feature engineering
- **Streamlit** — Web Application UI framework
- **Pickle** — Model serialization

---

## 📁 Project Structure

```
phishing-detector/
│
├── app.py                 # 🌐 Main Streamlit web application
├── train_model.py         # 🤖 ML model training script
├── create_dataset.py      # 📊 Synthetic dataset generator
├── demo.py                # 💻 Terminal demo / CLI test script
├── phishing_dataset.csv   # 📂 Training dataset
├── model.pkl              # 🧠 Trained ML model (auto-generated)
├── requirements.txt       # 📦 Python dependencies
└── README.md              # 📖 This file
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/hackshastra/phishing-detector.git
cd phishing-detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Retrain the Model
If you want to regenerate the dataset and retrain the AI model from scratch:
```bash
python create_dataset.py
python train_model.py
```
> This will print accuracy metrics and save a fresh `model.pkl`.

### 4. Launch the Web App
```bash
streamlit run app.py
```
> Opens automatically at **http://localhost:8501** in your browser.

### 5. Run Terminal Demo (Optional)
```bash
python demo.py
```
> Tests 6 URLs (safe + phishing) and prints results to the console.

---

## 📈 ML Features Used

The AI model analyzes these 5 URL characteristics:

| Feature | Description |
|---|---|
| `url_length` | Long URLs often hide malicious routing paths |
| `dot_count` | Excessive dots indicate subdomain masking |
| `has_at` | `@` symbol tricks the browser into ignoring prefix |
| `has_https` | Missing HTTPS = unencrypted, unsafe connection |
| `has_hyphen` | Hyphens are used in typosquatting fake domains |

---

## 🌐 Deploy to Streamlit Cloud (Free)

1. Push this repository to **GitHub** (public repo)
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select `app.py` as the entry point
5. Click **Deploy** — it's live instantly! 🚀

---

## 🧪 Example Test URLs

| URL | Expected Result |
|---|---|
| `https://google.com` | ✅ Safe |
| `https://github.com/hackshastra` | ✅ Safe |
| `http://paypal-secure-login.com@evil.net` | 🚨 Phishing |
| `http://free-iphone-winner-click-here.net/win` | 🚨 Phishing |

---

## 👨‍💻 Developer Credits

```
╔══════════════════════════════════════════╗
║     CyberShield Pro — Version 2.0        ║
║     Developed by  :  Hack Shastra        ║
║     Engineered by :  Hack Shastra        ║
║     Designed by   :  Hack Shastra        ║
║     Year          :  2026                ║
╚══════════════════════════════════════════╝
```

---

*CyberShield Pro | Made by Hack Shastra | Powered by Python & Machine Learning*
