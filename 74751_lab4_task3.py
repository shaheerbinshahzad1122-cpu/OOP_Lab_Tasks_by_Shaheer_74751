import math

def calculate_stats(hemoglobin_levels):
    if not hemoglobin_levels:
        return 0, 0
    n = len(hemoglobin_levels)
    mean = sum(hemoglobin_levels) / n
    variance = sum((x - mean) ** 2 for x in hemoglobin_levels) / n
    std_dev = math.sqrt(variance)
    return mean, std_dev

def insert_test_result(results, new_result, index):
    if 0 <= index <= len(results):
        results.insert(index, new_result)
        return True
    return False

def assess_risk(patient_id, cholesterol, blood_pressure, fasting_sugar):
    risk = 0
    if cholesterol > 200: risk += 1
    if blood_pressure > 130: risk += 1
    if fasting_sugar > 100: risk += 1
    
    if risk >= 2:
        return f"Patient {patient_id}: High Risk"
    elif risk == 1:
        return f"Patient {patient_id}: Moderate Risk"
    return f"Patient {patient_id}: Low Risk"

if __name__ == "__main__":
    hemo = [13.5, 14.2, 12.8, 15.0]
    avg, std = calculate_stats(hemo)
    print(f"Average: {avg:.2f}, Std Dev: {std:.2f}")
    
    success = insert_test_result(hemo, 14.5, 2)
    print(f"Insert Success: {success}, New list: {hemo}")
    
    risk = assess_risk("P123", 220, 140, 95)
    print(risk)
