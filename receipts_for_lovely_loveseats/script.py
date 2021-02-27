# Name:     script.py
# Auhor:    Phillip Douglas

# Lovely Lovseat
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on mood. 32
inches high x 40 inches wide x 30 inches deep. Red or
white.
"""

lovely_loveseat_price = 254.0

# Stylish Settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches
high x 54.75 inches wide x 28 inches deep. Black.
"""

stylish_settee_price = 180.5

# Luxurious Lamp
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tal.l. Brown
with cream shade.
"""

luxurious_lamp_price = 52.15

# Sales Tax
sales_tax = 0.088

# Our First Customer
customer_one_total = 0

customer_one_itemization = ""

# Update Customer One cart with Lovely Loveseat purchase
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Update Customer One cart with Luxurious Lamp purchase
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculate Customer One's sales tax
customer_one_tax = customer_one_total * sales_tax

# Add sales tax to Customer One's total
customer_one_total += customer_one_tax

# Print Customer One's receipt
print("Customer One's Items:")
print(customer_one_itemization)

print(f"Customer One's Total: ${customer_one_total:.2f}")