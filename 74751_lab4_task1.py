def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height * height)

def update_heart_rate(hr_history, new_reading, position):
    """Update a patient's heart rate history list by adding a new reading at a specific position."""
    if 0 <= position <= len(hr_history):
        hr_history.insert(position, new_reading)
        return True
    return False

def analyze_vitals(systolic, diastolic, heart_rate):
    """Analyze vital signs and return multiple values."""
    bp_category = ""
    if systolic > 180 or diastolic > 120:
        bp_category = "Hypertensive Crisis"
    elif systolic >= 140 or diastolic >= 90:
        bp_category = "Stage 2 Hypertension"
    elif systolic >= 130 or diastolic >= 80:
        bp_category = "Stage 1 Hypertension"
    elif systolic >= 120 and diastolic < 80:
        bp_category = "Elevated"
    else:
        bp_category = "Normal"

    hr_status = ""
    if heart_rate < 60:
        hr_status = "Bradycardia"
    elif heart_rate > 100:
        hr_status = "Tachycardia"
    else:
        hr_status = "Normal"

    map_val = (systolic + 2 * diastolic) / 3

    return bp_category, hr_status, map_val

if __name__ == "__main__":
    print(f"BMI: {calculate_bmi(70, 1.75):.2f}")
    
    history = [70, 72, 75]
    update_heart_rate(history, 80, 1)
    print(f"Updated History: {history}")
    
    bp, hr, map_val = analyze_vitals(125, 82, 90)
    print(f"BP Category: {bp}, HR Status: {hr}, MAP: {map_val:.2f}")
