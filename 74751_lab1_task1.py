# 74751_lab1_task1.py
distance = float(input("Enter distance between ECG and PPG sensors (meters): "))
time = float(input("Enter time delay (seconds): "))
pwv = distance / time
sbp = 120 + (pwv - 5) * 10
print(f"Pulse Wave Velocity (PWV): {pwv}")
print(f"Systolic Blood Pressure (SBP): {sbp}")
