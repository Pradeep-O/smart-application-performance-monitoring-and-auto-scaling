def should_scale(predicted_rate, threshold=800):
    if predicted_rate > threshold:
        return "scale_up"
    elif predicted_rate < threshold * 0.5:
        return "scale_down"
    else:
        return "no_action"
