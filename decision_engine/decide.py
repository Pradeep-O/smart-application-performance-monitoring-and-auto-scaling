def should_scale_enhanced(predicted_rate, latency_anomalies_count, current_instances=3, max_instances=10, min_instances=1):
    SCALE_UP_THRESHOLD = 800
    SCALE_DOWN_THRESHOLD = 400
    LATENCY_ANOMALY_LIMIT = 5
    
    if latency_anomalies_count > LATENCY_ANOMALY_LIMIT:
        print("High latency anomalies detected → urgent scale up")
        return "scale_up"
    
    if predicted_rate > SCALE_UP_THRESHOLD and current_instances < max_instances:
        print("Traffic high → scale up")
        return "scale_up"
    
    if predicted_rate < SCALE_DOWN_THRESHOLD and current_instances > min_instances:
        print("Traffic low → scale down")
        return "scale_down"
    
    return "no_action"

if __name__ == "__main__":
    decision = should_scale_enhanced(predicted_rate=900, latency_anomalies_count=0)
    print(f"Decision: {decision}")
