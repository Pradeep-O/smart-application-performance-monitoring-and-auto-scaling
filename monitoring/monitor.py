import numpy as np
import pandas as pd
import os

def generate_realistic_metrics(path="data/metrics.csv", samples=500):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    timestamps = pd.date_range(start='2025-07-01', periods=samples, freq='min')  # 1-minute intervals
    
    base_traffic = 300 + 200 * np.sin(2 * np.pi * timestamps.hour / 24)  # daily pattern
    weekly_effect = 50 * np.where(timestamps.dayofweek < 5, 1, 0.5)  # weekdays vs weekend
    noise = np.random.normal(0, 20, samples)
    spikes = np.random.choice([0, 400], size=samples, p=[0.98, 0.02])
    
    request_rate = base_traffic + weekly_effect + noise + spikes
    request_rate = np.clip(request_rate, 0, None)
    
    cpu_usage = 20 + (request_rate / 1000) * 70 + np.random.normal(0, 5, samples)
    memory_usage = 1000 + (request_rate / 1000) * 2000 + np.random.normal(0, 100, samples)
    latency = 100 + (request_rate / 1000) * 150 + np.random.normal(0, 20, samples)
    error_rate = np.random.binomial(1, 0.01 + (request_rate / 10000), size=samples)
    
    df = pd.DataFrame({
        "timestamp": timestamps,
        "cpu_usage": np.clip(cpu_usage, 0, 100),
        "memory_usage": np.clip(memory_usage, 0, None),
        "request_rate": request_rate,
        "latency_ms": np.clip(latency, 0, None),
        "error_rate": error_rate
    })
    
    df.to_csv(path, index=False)
    print(f"Generated realistic metrics at {path}")

if __name__ == "__main__":
    generate_realistic_metrics()
