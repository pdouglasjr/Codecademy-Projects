# Name:     lens_slice/script.py
# Author:   Phillip Douglas

# List to keep track of pizza toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# List to keep track of the costs of pizza slices based on topping
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of pizza types
num_pizzas = len(toppings)

# Print greeting
print(f"We sell {num_pizzas} different kinds of pizza!")

# Combine pizza toppings and their cost
pizzas = list(zip(prices, toppings))

# Sort pizzas by price
pizzas.sort()

# Cheapest pizza on the menu
cheapest_pizza = pizzas[0]

# Most expensive pizza on the menu
priciest_pizza = pizzas[-1]

# Three cheapest pizzas
three_cheapest = pizzas[:3]

# Print the three cheapest pizzas
print()
print("Three cheapest pieces:")
i = 0
for j,k in three_cheapest:
    print(f"\t{i+1}. {k.title()}\t${j:.2f}")
    i+=1

# Number of $2.00 slices
num_two_dollar_slices = prices.count(2)

print()
print(f"We have {num_two_dollar_slices} types of pizza that cost $2.00!")