import pickle

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        1 if '@' in url else 0,
        1 if 'https' in url else 0,
        1 if '-' in url else 0
    ]

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    print("Error loading model:", e)
    exit(1)

test_urls = [
    ("Safe Example", "https://google.com/search?q=machine+learning"),
    ("Safe Example", "https://github.com/hackshastra/project"),
    ("Suspicious/Phishing Example", "http://login.secure-bank-update.com@192.168.1.1/admin"),
    ("Phishing Example", "http://free-iphone-winner-click-here.net/win")
]

print("==================================================")
print("CYBERSHIELD AI - LIVE TERMINAL DEMONSTRATION")
print("==================================================\n")

for name, url in test_urls:
    features = extract_features(url)
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0]
    
    print(f"[{name}]")
    print(f"URL: {url}")
    
    if prediction == 0:
        print(f"Result: SAFE ({probability[0]*100:.1f}% AI Confidence)")
    else:
        print(f"Result: PHISHING ({probability[1]*100:.1f}% AI Confidence)")
        
        # Simple extraction of reasons for demo
        reasons = []
        if features[0] > 75: reasons.append("Too long")
        if features[2] == 1: reasons.append("Contains '@'")
        if features[3] == 0: reasons.append("No HTTPS")
        if features[1] > 3:  reasons.append("Too many dots")
        if features[4] == 1: reasons.append("Contains '-'")
        print(f"Reasons flagged: {', '.join(reasons)}")
        
    print("-" * 50)
