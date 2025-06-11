# Extract features from alerts
import pandas as pd

def extract_features(log_file):
    df = pd.read_csv(log_file)
    # Simple placeholder feature engineering logic
    features = df.drop(columns=["timestamp", "alert", "source_ip", "dest_ip"], errors='ignore')
    return features
