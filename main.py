from monitoring.monitor import generate_realistic_metrics
from prediction.forecast import predict_traffic_prophet
from anomaly_detection.detect import detect_latency_anomalies
from decision_engine.decide_multitier import decide_multitier
from scaler.scale_multitier import execute_multitier_scaling


def run_auto_scaling_multitier():
    current_instances = {"web": 3, "db": 2, "cache": 2}

    print("\nStep 1: Generate Metrics")
    generate_realistic_metrics()

    print("\nStep 2: Predict Traffic")
    predicted = predict_traffic_prophet()
    print(f"Predicted traffic: {predicted:.2f}")

    print("\nStep 3: Detect Latency Anomalies")
    anomalies_count = detect_latency_anomalies()
    print(f"Latency anomalies detected: {anomalies_count}")

    print("\nStep 4: Decide Multi-Tier Scaling")
    actions = decide_multitier(predicted, anomalies_count, current_instances)
    print(f"Scaling Actions: {actions}")

    print("\nStep 5: Execute Multi-Tier Scaling")
    current_instances = execute_multitier_scaling(actions, current_instances)

    print(f"\nCurrent instance counts: {current_instances}")


if __name__ == "__main__":
    run_auto_scaling_multitier()
