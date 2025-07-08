import pandas as pd

def detect_latency_anomalies(csv_path="data/metrics.csv", threshold=3):
    df = pd.read_csv(csv_path)
    latency = df['latency_ms']
    mean = latency.mean()
    std = latency.std()
    
    df['z_score'] = (latency - mean) / std
    anomalies = df[df['z_score'].abs() > threshold]
    
    print(f"Detected {len(anomalies)} latency anomalies")
    return len(anomalies)

if __name__ == "__main__":
    count = detect_latency_anomalies()
    print(f"Latency anomaly count: {count}")
