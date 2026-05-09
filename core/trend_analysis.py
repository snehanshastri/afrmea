def analyze_trend(values):
    increase = 0
    decrease = 0

    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            increase += 1
        elif values[i] < values[i - 1]:
            decrease += 1

    return {
        "increase_count": increase,
        "decrease_count": decrease
    }