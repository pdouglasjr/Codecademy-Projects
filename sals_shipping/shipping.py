# Name:     shipping.py
# Author:   Phillip Douglas

import random

weight = float(input("Enter a weight in lbs.: "))
cost = 0.0

# Ground shipping
if weight <= 2.0:
    cost_ground = round(weight * 1.5 + 20.0, 2)
elif weight > 2.0 and weight <= 6.0:
    cost_ground = round(weight * 3.0 + 20.0, 2)
elif weight > 6.0 and weight <= 10.0:
    cost_ground = round(weight * 4.0 + 20.0, 2)
else:
    cost_ground = round(weight * 4.75 + 20.0, 2)

# Ground shipping - Premium
cost_premium = 125.0

# Drone shipping
if weight <= 2.0:
    cost_drone = round(weight * 4.5, 2)
elif weight > 2.0 and weight <= 6.0:
    cost_drone = round(weight * 9.0, 2)
elif weight > 6.0 and weight <= 10.0:
    cost_drone = round(weight * 12.0, 2)
else:
    cost_drone = round(weight * 14.25, 2)

print()
print(f"Shipping weight: {weight} lbs.")
print()

print(f"Cost for Ground Shipping: ${cost_ground:.2f}")
print(f"Cost for Ground Shipping Premium: ${cost_premium:.2f}")
print(f"Cost for Drone Shipping: ${cost_drone:.2f}")