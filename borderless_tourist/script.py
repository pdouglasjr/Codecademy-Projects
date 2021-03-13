# Name:     borderless_tourist/script.py
# Author:   Phillip Douglas

# Variables
## Destinations
destinations = ["Paris, France","Shanghai, China","Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt"]

# Functions
## Retrive the index of a destination
def get_destination_index(destination):
    # destination_index = -1
    # for idx in range(len(destinations)):
    #     if destinations[idx] == destination:
    #         destination_index = idx
    # return destination_index
    destination_index = destinations.index(destination)
    return destination_index

## Retrieve the location of a traveler
def get_traveler_location(traveler):
    # Get the location
    traveler_destination = traveler[1]
    
    # Get the index of the location
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

# Tests
## Test variables
test_destinations = ["Los Angeles, USA", "Paris, France", "Hyderabad, India"]
test_traveler = ["Erin Wilkes","Shanghai, China",["historical site", "art"]]
test_destination_index = -1

## Test functions
### test_get_destination_index
def test_get_destination_index(dest):
    for d in dest:
        try:
            print(f"Index of '{d}' is {get_destination_index(d)}.")
        except:
            pass

### test_get_traveler_location
def test_get_traveler_location(trav):
    test_destination_index = get_destination_index(trav[1])
    print(f"Index of '{trav[1]}' is {test_destination_index}.")


if (__name__ == '__main__'):
    test_get_destination_index(test_destinations)
    test_get_traveler_location(test_traveler)
