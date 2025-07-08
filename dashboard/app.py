import streamlit as st
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "metrics.csv"

st.set_page_config(page_title="Auto-Scaling Monitoring Dashboard", layout="wide")

st.title("Smart Application Performance Monitoring Dashboard")

@st.cache_data(ttl=60)
def load_metrics():
    df = pd.read_csv(DATA_PATH)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def display_metrics(df):
    st.subheader("Request Rate Over Time")
    st.line_chart(df.set_index('timestamp')['request_rate'])

    st.subheader("Latency Over Time")
    st.line_chart(df.set_index('timestamp')['latency_ms'])

def simulate_latest_stats():
    # Placeholder simulation - replace with actual predicted values or read from a file
    predicted_traffic = 589.71
    latency_anomalies = 3
    scaling_actions = {
        "web": "no_action",
        "db": "scale_up",
        "cache": "scale_down"
    }
    return predicted_traffic, latency_anomalies, scaling_actions

def display_scaling_info(predicted_traffic, latency_anomalies, scaling_actions):
    st.subheader("Predicted Traffic")
    st.metric(label="Predicted Traffic", value=f"{predicted_traffic:.2f}")

    st.subheader("Latency Anomalies Detected")
    st.metric(label="Anomalies", value=latency_anomalies)

    st.subheader("Scaling Actions")
    for tier, action in scaling_actions.items():
        st.write(f"**{tier.capitalize()} Tier:** {action}")

def main():
    df = load_metrics()
    display_metrics(df)

    st.markdown("---")
    st.header("Latest Auto-Scaling Stats (Simulated)")

    predicted_traffic, latency_anomalies, scaling_actions = simulate_latest_stats()
    display_scaling_info(predicted_traffic, latency_anomalies, scaling_actions)

    st.markdown("---")
    st.info("This dashboard auto-refreshes every 60 seconds to simulate real-time monitoring.")

if __name__ == "__main__":
    main()
