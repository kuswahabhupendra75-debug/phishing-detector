# ============================================================
#   CyberShield Pro - Dataset Generation Script
#   Developed by: Bhupendra Sinh Rajgopal Kushwaha
#   Version: 2.0
# ============================================================

import pandas as pd
import numpy as np
import random

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if '@' in url else 0,
        1 if 'https' in url else 0,
        1 if '-' in url else 0
    ]

# We need actual URL strings to be processed by extract_features
# Let's generate dummy URLs

def generate_safe_url():
    domains = ["google.com", "facebook.com", "youtube.com", "amazon.com", "wikipedia.org", "twitter.com", "instagram.com"]
    paths = ["/home", "/about", "/contact", "/index", "/login", ""]
    protocol = "https" if random.random() < 0.9 else "http"
    domain = random.choice(domains)
    path = random.choice(paths)
    prefix = "www." if random.random() < 0.5 else ""
    return f"{protocol}://{prefix}{domain}{path}"

def generate_phishing_url():
    domains = ["update-account.com", "secure-login-paypal.com", "verify-your-apple-id.com", "free-prizes-now.info", "login-bank.net"]
    paths = ["/secure/login.php?id=123", "/verify?token=abc", "/account/update", "/win"]
    protocol = "https" if random.random() < 0.3 else "http"
    domain = random.choice(domains)
    path = random.choice(paths)
    
    # Inject phishing patterns
    prefix = "www." if random.random() < 0.5 else ""
    url = f"{protocol}://{prefix}{domain}{path}"
    
    # Add @ symbol sometimes
    if random.random() < 0.2:
        url = url.replace("://", "://admin@")
    
    # Add extra random subdomains
    if random.random() < 0.5:
        url = url.replace("www.", f"www.login.{random.randint(100,999)}.")
        
    return url

if __name__ == "__main__":
    print("Generating dataset...")
    data = []
    
    # Generate 1000 safe
    for _ in range(1000):
        url = generate_safe_url()
        features = extract_features(url)
        data.append(features + [0]) # 0 = safe
        
    # Generate 1000 phishing
    for _ in range(1000):
        url = generate_phishing_url()
        features = extract_features(url)
        data.append(features + [1]) # 1 = phishing
        
    # Shuffle dataset
    random.shuffle(data)
    
    # Save to CSV
    columns = ["url_length", "dot_count", "has_at", "has_https", "has_hyphen", "label"]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv("phishing_dataset.csv", index=False)
    print("Dataset saved to phishing_dataset.csv with 2000 rows.")
