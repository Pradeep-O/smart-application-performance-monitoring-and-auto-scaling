import random
import time
import csv

def generate_fake_metrics():
    return {
        "timestamp": time.time(),
        "cpu_usage": random.uniform(10, 90),
        "memory_usage": random.uniform(1000, 4000),
        "request_rate": random.uniform(100, 1000)
    }

def write_metrics_to_csv(path="data/metrics.csv", samples=50):
    with open(path, "w", newline='') as csvfile:
        fieldnames = ["timestamp", "cpu_usage", "memory_usage", "request_rate"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(samples):
            metrics = generate_fake_metrics()
            writer.writerow(metrics)
            time.sleep(0.1)  # simulate delay

if __name__ == "__main__":
    write_metrics_to_csv()
