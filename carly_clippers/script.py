# Name:     carly_clippers/script.py
# Author:   Phillip Douglas

# Available hairstyles and prices
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Sales from last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Average price of a haircut
average_price = sum([p for p in prices]) / len(prices)
print(f"Average Haircut Price: ${average_price:.2f}")
print()

# New haircut prices
new_prices = [price - 5 for price in prices]
print("New Haircut Prices:")
for i in range(len(new_prices)):
    print(f"\tHaircut #{i+1}: ${new_prices[i]:.2f}")
print()

# Total revenue from haircuts
total_revenue = sum([prices[i] for i in range(len(hairstyles))])
print(f"Total Revenue: ${total_revenue:.2f}")
print()

# Average daily revenue
average_daily_revenue = total_revenue / 7
print(f"This Week's Daily Revenue Average: ${average_daily_revenue:.2f}")
print()

# Haircuts under $30
cuts_under_30 = [[i+1, new_prices[i]] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts under $30:")
for c in cuts_under_30:
    cid, price = c
    print(f"\tHaircut #{cid}: ${price:.2f}")
