
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X, y, model_path="model.pkl"):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    return model

def load_model(model_path="model.pkl"):
    return joblib.load(model_path)

