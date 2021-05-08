# Name:     basta_fazoolin/script.py
# Author:   Phillip Douglas
# Purpose:  Practice working with classes, inheritance, polymorphism, dudner methods, etc.
#           by creating various classes and methods for an family-style italian restaurant,
#           Basta Fazoolin'

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        start_time_12hr = f"{self.start_time % 12}am" if self.start_time<12 else f"{self.start_time % 12}pm"
        end_time_12hr = f"{self.end_time % 12}am" if self.end_time<12 else f"{self.end_time % 12}pm"
        
        return f"{self.name} menu available from {start_time_12hr} to {end_time_12hr}"

    def calculate_bill(self, purchased_items):
        total = sum([self.items[item] for item in purchased_items])
        return total

#-- Menus --#
# Brunch
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
brunch = Menu('brunch', brunch_items, 11, 16)

# Early Bird
early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}
early_bird = Menu('early_bird', early_bird_items, 15, 18)

# Dinner
dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}
dinner = Menu('dinner', dinner_items, 17, 23)

# Kids
kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00,
}
kids = Menu('kids', kids_items, 11, 21)

if __name__=='__main__':
    # print(brunch)
    # print(early_bird)
    # print(dinner)
    # print(kids)

    brunch_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
    print(brunch_bill)

    early_bird_bill = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
    print(early_bird_bill)