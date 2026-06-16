# 74751_lab2_task5.py
intervals = []
for i in range(10):
    val = float(input(f"Enter breathing interval {i+1} (seconds): "))
    intervals.append(val)

total_apnea_events = 0
severe_apnea_count = 0

for i in range(10):
    if intervals[i] > 10:
        total_apnea_events += 1

for i in range(1, 10):
    if intervals[i] > 10 and intervals[i-1] > 10:
        severe_apnea_count += 1

print(f"Total apnea events: {total_apnea_events}")
print(f"Severe apnea count: {severe_apnea_count}")
