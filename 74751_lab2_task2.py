# 74751_lab2_task2.py
spo2_values = []
for i in range(8):
    val = float(input(f"Enter SpO2 reading {i+1}: "))
    spo2_values.append(val)

below_90_count = 0
drop_count = 0

if spo2_values[0] < 90:
    below_90_count += 1

for i in range(1, 8):
    if spo2_values[i] < 90:
        below_90_count += 1
    if spo2_values[i] < spo2_values[i-1]:
        drop_count += 1

print(f"Total times SpO2 drops below 90: {below_90_count}")
print(f"Times a drop occurs compared to previous reading: {drop_count}")
