# 74751_lab1_task2.py
vo2 = float(input("Enter oxygen consumption (VO2 in ml/kg/min): "))
hr = float(input("Enter heart rate (HR): "))
li = (hr * 0.02) + (vo2 * 0.03)
fs = (li ** 2) / 10
print(f"Lactate Index (LI): {li}")
print(f"Fatigue Score (FS): {fs}")
