def apply_filter(original_signal, filter_coefficients):
    filtered = []
    for i in range(len(original_signal)):
        val = 0
        for j in range(len(filter_coefficients)):
            if i - j >= 0:
                val += original_signal[i - j] * filter_coefficients[j]
        filtered.append(val)
    return filtered

def process_log(log_ref, target_symptom):
    # Using a list containing a single string to simulate pointer/reference behavior
    log_str = log_ref[0]
    count = log_str.count(target_symptom)
    # Modify log string by replacing the symptom with uppercase
    log_ref[0] = log_str.replace(target_symptom, target_symptom.upper())
    return count

if __name__ == "__main__":
    sig = [1, 2, 3, 4, 5]
    coeffs = [0.2, 0.5, 0.2]
    filtered_sig = apply_filter(sig, coeffs)
    print(f"Filtered signal: {filtered_sig}")
    
    log = ["headache, nausea, headache, fever"]
    count = process_log(log, "headache")
    print(f"Count: {count}, Modified log: {log[0]}")
