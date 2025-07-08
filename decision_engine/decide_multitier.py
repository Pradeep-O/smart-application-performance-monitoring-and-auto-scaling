def decide_multitier(predicted_traffic, latency_anomalies, current_instances):
    """
    Decide scaling actions for multi-tier:
    current_instances = {
      "web": int,
      "db": int,
      "cache": int
    }
    Returns dict of actions per tier: scale_up, scale_down, no_action
    """

    actions = {"web": "no_action", "db": "no_action", "cache": "no_action"}

    # Thresholds for scaling decisions per tier
    thresholds = {
        "web": {"up": 800, "down": 400, "min": 2, "max": 10},
        "db": {"up": 700, "down": 350, "min": 1, "max": 5},
        "cache": {"up": 500, "down": 200, "min": 1, "max": 5},
    }

    # Scale Web Tier based on traffic and latency anomalies
    if latency_anomalies > 5:
        actions["web"] = "scale_up"
    elif predicted_traffic > thresholds["web"]["up"] and current_instances["web"] < thresholds["web"]["max"]:
        actions["web"] = "scale_up"
    elif predicted_traffic < thresholds["web"]["down"] and current_instances["web"] > thresholds["web"]["min"]:
        actions["web"] = "scale_down"

    # Scale DB Tier - slower changes, scale up if traffic very high or latency anomalies
    if latency_anomalies > 8 or predicted_traffic > thresholds["db"]["up"]:
        if current_instances["db"] < thresholds["db"]["max"]:
            actions["db"] = "scale_up"
    elif predicted_traffic < thresholds["db"]["down"] and current_instances["db"] > thresholds["db"]["min"]:
        actions["db"] = "scale_down"

    # Scale Cache Tier - aggressive scaling for performance
    if predicted_traffic > thresholds["cache"]["up"]:
        if current_instances["cache"] < thresholds["cache"]["max"]:
            actions["cache"] = "scale_up"
    elif predicted_traffic < thresholds["cache"]["down"] and current_instances["cache"] > thresholds["cache"]["min"]:
        actions["cache"] = "scale_down"

    return actions


if __name__ == "__main__":
    current = {"web": 3, "db": 2, "cache": 2}
    actions = decide_multitier(900, 3, current)
    print("Scaling Actions:", actions)
