# 74751_lab1_task3.py
import math

alpha = float(input("Enter alpha band amplitude: "))
beta = float(input("Enter beta band amplitude: "))
r = (beta ** 2) / (alpha ** 2)
cli = math.log10(r * 100)
print(f"Power Ratio (R): {r}")
print(f"Cognitive Load Index (CLI): {cli}")
