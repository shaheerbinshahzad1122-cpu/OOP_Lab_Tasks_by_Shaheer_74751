# 74751_lab1_task4.py
import math

c0 = float(input("Enter initial drug concentration (C0): "))
k = float(input("Enter elimination rate constant (k): "))
t = float(input("Enter time (t): "))

c = c0 * math.exp(-k * t)
percentage = (c / c0) * 100

print(f"Current concentration (C): {c}")
print(f"Percentage of drug remaining: {percentage}%")
