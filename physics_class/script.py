# Name:     physics_class/script.py
# Author:   Phillip Douglas

# Global variables
train_mass = 226800
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Functions - "Turn up the Temperature"
# f_to_c:   convert degrees fahrenheit to degrees celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

# c_to_f:   convert degrees celsius to degrees fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Functions - "Use the Force"
# get_force: returns the calculated force given mass and acceleration
def get_force(mass, acceleration):
    return mass * acceleration

# get_energy: returns the calculated energy given mass
def get_enery(mass):
    c = 3 * (10 ** 8)
    return mass * (c ** 2)

# Functions - "Do the Work"
# get_work: returns the calculated work given mass, distance, and acceleration
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

if (__name__ == "__main__"):
    # Test f_to_c functionality
    f100_in_celsius = f_to_c(100)
    print(f100_in_celsius)

    # Test c_to_f functionality
    c100_in_fahrenheit = c_to_f(f100_in_celsius)
    print(c100_in_fahrenheit)

    # Test get_force functionality
    train_force = get_force(train_mass, train_acceleration)
    print(f"The GE train supplies {train_force} Newtons of force.")

    # Test get_energy functionality
    bomb_energy = get_enery(bomb_mass)
    print(f"A {bomb_mass} kg bomb supplies {bomb_energy} Joules.")

    # Test get_work functionality
    train_work = get_work(train_mass, train_acceleration, train_distance)
    print(f"The GE train does {train_work} Joules of work over {train_distance} meters")