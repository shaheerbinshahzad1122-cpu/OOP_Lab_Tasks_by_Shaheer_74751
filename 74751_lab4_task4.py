def calculate_avg_temperature(voltage_readings):
    if not voltage_readings:
        return 0
    total_temp = sum(v * 10 for v in voltage_readings) # Temp conversion
    return total_temp / len(voltage_readings)

def filter_noisy_readings(readings, valid_min, valid_max):
    valid_count = 0
    for i in range(len(readings)):
        if valid_min <= readings[i] <= valid_max:
            readings[valid_count] = readings[i]
            valid_count += 1
    # Truncate the list to effective size
    del readings[valid_count:]
    return valid_count

if __name__ == "__main__":
    voltages = [3.5, 3.6, 1.2, 3.8, 9.9, 3.7]
    avg_temp = calculate_avg_temperature(voltages)
    print(f"Average Temperature: {avg_temp:.2f}")
    
    valid_cnt = filter_noisy_readings(voltages, 3.0, 4.0)
    print(f"Valid count: {valid_cnt}, Filtered readings: {voltages}")
