# ============================================================
#   CyberShield Pro - Terminal Demo Script
#   Developed by: Bhupendra Sinh Rajgopal Kushwaha
#   Version: 2.0
# ============================================================

import pickle
import time

# ── Feature Extractor ────────────────────────────────────────
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if '@' in url else 0,
        1 if 'https' in url else 0,
        1 if '-' in url else 0
    ]

# ── Reason Analyzer ─────────────────────────────────────────
def get_reasons(features):
    url_length, dot_count, has_at, has_https, has_hyphen = features
    reasons = []
    if url_length > 75:   reasons.append("URL is unusually long (hiding malicious path)")
    if has_at == 1:       reasons.append("Contains '@' symbol (browser redirection trick)")
    if has_https == 0:    reasons.append("No HTTPS (unencrypted / insecure connection)")
    if dot_count > 3:     reasons.append("Too many dots (subdomain masking technique)")
    if has_hyphen == 1:   reasons.append("Contains hyphen (typosquatting / fake domain)")
    return reasons

# ── Load Model ───────────────────────────────────────────────
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("❌ ERROR: model.pkl not found! Please run train_model.py first.")
    exit(1)

# ── Test URLs ────────────────────────────────────────────────
test_urls = [
    ("✅ Safe",     "https://google.com/search?q=machine+learning"),
    ("✅ Safe",     "https://github.com/hackshastra/cybershield"),
    ("✅ Safe",     "https://stackoverflow.com/questions/12345"),
    ("🚨 Phishing", "http://login.secure-bank-update.com@192.168.1.1/admin"),
    ("🚨 Phishing", "http://free-iphone-winner-click-here-now.net/claim"),
    ("🚨 Phishing", "http://paypal-secure-login-verify.com/account"),
]

# ── Output Banner ────────────────────────────────────────────
print()
print("=" * 60)
print("   CYBERSHIELD PRO - LIVE TERMINAL DEMO")
print("         Developed by Bhupendra Sinh Rajgopal Kushwaha")
print("=" * 60)
print()

for label, url in test_urls:
    time.sleep(0.3)
    features = extract_features(url)
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0]

    print(f"  Category : {label}")
    print(f"  URL      : {url[:70]}{'...' if len(url) > 70 else ''}")

    if prediction == 0:
        confidence = probability[0] * 100
        print(f"  Result   : ✅ SAFE  ({confidence:.1f}% confidence)")
    else:
        confidence = probability[1] * 100
        print(f"  Result   : 🚨 PHISHING  ({confidence:.1f}% confidence)")
        reasons = get_reasons(features)
        if reasons:
            print("  Flags    :")
            for r in reasons:
                print(f"             ⚠  {r}")

    print("  " + "─" * 60)

print()
print("  Bhupendra Sinh Rajgopal Kushwaha © 2026  |  CyberShield Pro v2.0")
print()
