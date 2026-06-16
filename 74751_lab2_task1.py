# 74751_lab2_task1.py
rr_intervals = []
for i in range(6):
    val = float(input(f"Enter RR interval {i+1} (seconds): "))
    rr_intervals.append(val)

irregularity_count = 0
for i in range(1, 6):
    if abs(rr_intervals[i] - rr_intervals[i-1]) > 0.2:
        irregularity_count += 1

print(f"Irregularity count: {irregularity_count}")
if irregularity_count > 2:
    print("Potential arrhythmia flagged.")
