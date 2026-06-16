# 74751_lab2_task3.py
amplitudes = []
for i in range(7):
    val = float(input(f"Enter amplitude reading {i+1}: "))
    amplitudes.append(val)

total_decreases = 0
current_consecutive_decreases = 0
max_consecutive_decreases = 0

for i in range(1, 7):
    if amplitudes[i] < amplitudes[i-1]:
        total_decreases += 1
        current_consecutive_decreases += 1
        if current_consecutive_decreases > max_consecutive_decreases:
            max_consecutive_decreases = current_consecutive_decreases
    else:
        current_consecutive_decreases = 0

print(f"Total decrease count: {total_decreases}")
print(f"Max consecutive decrease count: {max_consecutive_decreases}")
