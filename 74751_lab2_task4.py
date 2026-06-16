# 74751_lab2_task4.py
flow_rates = []
for i in range(6):
    val = float(input(f"Enter flow rate {i+1} (ml/hr): "))
    flow_rates.append(val)

risk_counter = 0
critical_event_counter = 0

for i in range(6):
    if flow_rates[i] > 50:
        risk_counter += 1

for i in range(1, 6):
    if flow_rates[i] > 50 and flow_rates[i-1] > 50:
        critical_event_counter += 1

print(f"Risk counter: {risk_counter}")
print(f"Critical event counter: {critical_event_counter}")
