def find_peaks(ecg_values):
    if not ecg_values:
        return None, None
    max_peak = max(ecg_values)
    min_peak = min(ecg_values)
    return max_peak, min_peak

def apply_baseline_correction(ecg_values):
    if not ecg_values:
        return 0
    avg = sum(ecg_values) / len(ecg_values)
    for i in range(len(ecg_values)):
        ecg_values[i] -= avg
    return len(ecg_values)

if __name__ == "__main__":
    ecg = [1.2, 0.5, 2.3, -0.4, 1.1]
    mx, mn = find_peaks(ecg)
    print(f"Max Peak: {mx}, Min Peak: {mn}")
    
    corrected = apply_baseline_correction(ecg)
    print(f"Corrected samples: {corrected}, New values: {ecg}")
