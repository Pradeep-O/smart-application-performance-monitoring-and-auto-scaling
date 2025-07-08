import time

def execute_scaling_simulated(action, current_instances=3):
    SCALING_LAG_SEC = 10  # Simulate delay
    
    if action == "scale_up":
        print(f"Scaling UP... waiting {SCALING_LAG_SEC} seconds to simulate instance startup")
        time.sleep(SCALING_LAG_SEC)
        current_instances += 1
        print(f"Scaled up to {current_instances} instances")
    elif action == "scale_down":
        print(f"Scaling DOWN... waiting {SCALING_LAG_SEC} seconds to simulate instance shutdown")
        time.sleep(SCALING_LAG_SEC)
        current_instances -= 1
        print(f"Scaled down to {current_instances} instances")
    else:
        print("No scaling needed.")
    return current_instances

if __name__ == "__main__":
    current_instances = 3
    current_instances = execute_scaling_simulated("scale_up", current_instances)
