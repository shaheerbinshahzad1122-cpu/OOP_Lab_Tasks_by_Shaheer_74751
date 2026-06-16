# 74751_lab1_task5.py
import math

r = float(input("Enter body resistance (R): "))
xc = float(input("Enter reactance (Xc): "))
height = float(input("Enter height (in cm): "))

z = math.sqrt(r**2 + xc**2)
tbw = (0.6 * height**2) / z

print(f"Impedance (Z): {z}")
print(f"Total Body Water (TBW): {tbw}")
