# 🛡️ Phishing Attack Detection System

A Machine Learning powered web application built with Streamlit to detect whether a given URL is safe or a potential phishing attack. 

## 🚀 Features
- **Real-time URL Analysis**: Extracts key features from a URL instantly.
- **Machine Learning**: Uses a Logistic Regression model trained on URL structural patterns.
- **Suspicious Indicators**: Breaks down the result and explains *why* a URL was flagged (too long, missing HTTPS, high subdomain count, etc.).
- **Interactive UI**: Built with Streamlit for a fast and beautiful user experience.

## 🛠️ Technology Stack
- **Python** (Core language)
- **Scikit-Learn** (Machine Learning model - Logistic Regression)
- **Pandas & NumPy** (Data processing)
- **Streamlit** (Web Application UI)

## 📌 How to run locally

1. **Clone the repository** (or download files):
   ```bash
   git clone https://github.com/hackshastra/phishing-detector.git
   cd phishing-detector
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. *(Optional)* **Generate Dataset & Train Model**:
   If you want to train the AI model from scratch on your machine:
   ```bash
   python create_dataset.py
   python train_model.py
   ```
   *(This will generate a fresh `model.pkl` file).*

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   *This will open the app in your default web browser.*

## 📈 Model Features Used
The ML model looks for the following patterns:
1. `url_length`: Unusually long URLs often hide malicious domains.
2. `dot_count`: Many dots (`.`) usually indicate hidden subdomains.
3. `has_at`: The `@` symbol is rarely used legitimately in URLs and often redirects users unassumingly.
4. `has_https`: Lack of `https` indicates insecure, unencrypted traffic.
5. `has_hyphen`: Fraudsters often register domains with hyphens to look like genuine domains (e.g., `secure-login.com`).

## ☁️ Deployment
This application is fully compatible with **Streamlit Community Cloud**. 
1. Push this code to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub account and deploy `app.py`.

---
*Made by Hack Shastra | Developed by Hack Shastra*
