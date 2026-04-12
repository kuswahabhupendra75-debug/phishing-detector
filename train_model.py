import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

if __name__ == "__main__":
    print("Loading dataset...")
    df = pd.read_csv("phishing_dataset.csv")
    
    # Features: url_length, dot_count, has_at, has_https, has_hyphen
    X = df[["url_length", "dot_count", "has_at", "has_https", "has_hyphen"]]
    y = df["label"]
    
    print("Training Logistic Regression model...")
    model = LogisticRegression()
    model.fit(X, y)
    
    print("Model trained successfully.")
    
    # Get accuracy
    accuracy = model.score(X, y)
    print(f"Model Accuracy on training data: {accuracy * 100:.2f}%")
    
    print("Saving model to model.pkl...")
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    print("Done! You can now run Streamlit app.")
