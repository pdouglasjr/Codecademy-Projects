# Name:     borderless_tourist/script.py
# Author:   Phillip Douglas

# Variables
destinations = ["Paris, France","Shanghai, China","Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt", "Seattle, USA"]
attractions = [[] for i in destinations]

# Functions
def get_destination_index(destination):
    """Retrieve the index of a destination"""

    # Get the destination index.
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    """Retrieve the location of a traveler"""

    # Get the traveler's location.
    traveler_destination = traveler[1]
    
    # Get the index of the location.
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

def add_attraction(destination, attraction):
    """Add an attraction to a particular location"""
    try:
        # Get the destination index.
        destination_index = get_destination_index(destination)

        # Add attraction to list of attractions
        attractions[destination_index].append(attraction)
    except ValueError:
        return

def find_attractions(destination, interests):
    """Retrieve places that matches the interests of a traveler in a city new to them"""
    # Get index of destination.
    destination_index = get_destination_index(destination)
    
    # Attractions in the city.
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    try:
        # Get attractions that match the interest of the traveler.
        for possible_attraction in attractions_in_city:
            for interest in interests:
                if interest in possible_attraction[1]:
                    attractions_with_interest.append(possible_attraction[0])
        return attractions_with_interest
    except IndexError:
        return

def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0]
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = ""

    interests_string = f"Hi {traveler_name}, we think you'll like these places around {traveler_destination}: {', '.join(traveler_attractions)}."

    return interests_string

if (__name__ == '__main__'):
    # Tests
    ## Test variables
    test_destinations = ["Los Angeles, USA", "Paris, France", "Hyderabad, India"]
    test_traveler = ["Erin Wilkes","Shanghai, China",["historical site", "art"]]
    test_destination_index = -1
    test_attractions = [
        ["Paris, France", ["the Louvre", ["art", "museum"]]],
        ["Paris, France", ["Arc de Triomphe", ["historical site", "monument"]]],
        ["Shanghai, China", ["Yu Garden", ["garden", "historical site"]]],
        ["Shanghai, China", ["Yuz Museum", ["art", "museum"]]],
        ["Shanghai, China", ["Oriental Peal Tower", ["skyscraper, viewing deck"]]],
        ["Los Angeles, USA", ["LACMA", ["art", "museum"]]],
        ["São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]]],
        ["São Paulo, Brazil", ["Pàtio do Colè", ["historical site"]]],
        ["Cairo, Egypt", ["Egyptian Museum", ["museum"]]],
        ["Seattle, USA", ["the SAM", ["art", "museum"]]],
        ["Seattle, USA", ["the Pike Place Market", ["art", "shopping", "market"]]]
    ]

    ## Test functions
    ### test_get_destination_index
    def test_get_destination_index(dest):
        for d in dest:
            try:
                print(f"Index of '{d}' is {get_destination_index(d)}.")
            except:
                return

    ### test_get_traveler_location
    def test_get_traveler_location(trav):
        test_destination_index = get_destination_index(trav[1])
        print(f"Index of '{trav[1]}' is {test_destination_index}.")

    ### test_add_attractions:
    def test_add_attractions(attraction):
        add_attraction(attraction[0], attraction[1])

    # Destinations
    # test_get_destination_index(test_destinations)
    
    # Traveler
    # test_get_traveler_location(test_traveler)

    # Attractions
    for attraction in test_attractions:
        test_add_attractions(attraction)
    
    # la_arts = find_attractions("Los Angeles, USA", "arts")
    # seattle_shopping = find_attractions("Seattle, USA", "shopping")

    pdouglas_seattle = get_attractions_for_traveler(["Phillip Douglas", "Seattle, USA", ["art"]])
    smills_france = get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]])

    print(pdouglas_seattle)
    print(smills_france)