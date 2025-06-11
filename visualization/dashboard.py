# Streamlit dashboard for alert visualization
import pandas as pd
import plotly.express as px

def visualize_alerts(csv_file):
    try:
        df = pd.read_csv(csv_file)
        if 'alert_signature' in df.columns:
            fig = px.histogram(df, x='alert_signature', title='Alert Frequency by Signature')
            fig.update_layout(xaxis_title="Signature", yaxis_title="Count")
            fig.show()
        else:
            print("❌ 'alert_signature' column not found in CSV.")
    except Exception as e:
        print(f"🚫 Error during visualization: {e}")
