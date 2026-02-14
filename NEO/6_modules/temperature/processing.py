
def calculate_statistics(temeratures: list[float]) -> dict:
    if not temeratures:
        return None
    
    min_temp = min(temeratures)
    max_temp = max(temeratures)
    avg_temp = sum(temeratures) / len(temeratures)
    median_temp = calculate_median(temeratures)
    
    return {
        "min": min_temp,
        "max": max_temp,
        "average": avg_temp,
        "median": median_temp,
    }
    
def calculate_median(temperatures: list[float]) -> float:
    temperatures.sort()
    n = len(temperatures)
    mid = n // 2
    if n % 2 == 0:
        return (temperatures[mid - 1]) + temperatures[mid] / 2
    else:
        return temperatures[mid]