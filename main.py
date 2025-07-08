from monitoring.monitor import write_metrics_to_csv
from prediction.forecast import predict_traffic
from decision_engine.decide import should_scale
from scaler.scale import execute_scaling

def run_system():
    print("Generating fake metrics...")
    write_metrics_to_csv()
    
    print("Predicting future traffic...")
    predicted = predict_traffic()
    
    print(f"Predicted rate: {predicted}")
    decision = should_scale(predicted)
    
    print(f"Decision: {decision}")
    execute_scaling(decision)

if __name__ == "__main__":
    run_system()
