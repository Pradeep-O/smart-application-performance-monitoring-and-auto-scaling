from monitoring.monitor import generate_realistic_metrics
from prediction.forecast import predict_traffic_prophet
from anomaly_detection.detect import detect_latency_anomalies
from decision_engine.decide import should_scale_enhanced
from scaler.scale import execute_scaling_simulated

def run_auto_scaling_system():
    current_instances = 3  # Starting number of instances
    
    print("\nStep 1: Generate Metrics")
    generate_realistic_metrics()
    
    print("\nStep 2: Predict Traffic")
    predicted = predict_traffic_prophet()
    print(f"Predicted traffic: {predicted:.2f}")
    
    print("\nStep 3: Detect Latency Anomalies")
    anomalies_count = detect_latency_anomalies()
    print(f"Latency anomalies detected: {anomalies_count}")
    
    print("\nStep 4: Decide Scaling")
    decision = should_scale_enhanced(predicted, anomalies_count, current_instances)
    print(f"Decision: {decision}")
    
    print("\nStep 5: Execute Scaling")
    current_instances = execute_scaling_simulated(decision, current_instances)
    
    print(f"\nCurrent instance count: {current_instances}")

if __name__ == "__main__":
    run_auto_scaling_system()
