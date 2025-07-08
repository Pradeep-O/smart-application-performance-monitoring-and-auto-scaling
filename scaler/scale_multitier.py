import time

def execute_multitier_scaling(actions, current_instances):
    """
    Simulate scaling per tier with lag and print results.
    actions: dict of tier -> action
    current_instances: dict tier -> int
    Returns updated current_instances dict.
    """

    SCALING_LAG = 5  # seconds per scaling action (simulate delay)

    for tier, action in actions.items():
        if action == "scale_up":
            print(f"Scaling UP {tier} tier...")
            time.sleep(SCALING_LAG)
            current_instances[tier] += 1
            print(f"{tier.capitalize()} instances increased to {current_instances[tier]}")
        elif action == "scale_down":
            print(f"Scaling DOWN {tier} tier...")
            time.sleep(SCALING_LAG)
            current_instances[tier] -= 1
            print(f"{tier.capitalize()} instances decreased to {current_instances[tier]}")
        else:
            print(f"No scaling needed for {tier} tier.")
    return current_instances


if __name__ == "__main__":
    current = {"web": 3, "db": 2, "cache": 2}
    actions = {"web": "scale_up", "db": "no_action", "cache": "scale_down"}
    new_instances = execute_multitier_scaling(actions, current)
    print("New Instances:", new_instances)
