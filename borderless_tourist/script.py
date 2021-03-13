# Name:     borderless_tourist/script.py
# Author:   Phillip Douglas

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

if (__name__ == '__main__'):
    # Tests
    ## Test variables
    test_destinations = ["Los Angeles, USA", "Paris, France", "Hyderabad, India"]
    test_traveler = ["Erin Wilkes","Shanghai, China",["historical site", "art"]]
    test_destination_index = -1
    test_attractions = [
        ["Paris, France", ["the Louvre", ["art", "mus"]]],
        ["Paris, France", ["Arc de Triomphe", ["historical site", "monument"]]],
        ["Shanghai, China", ["Yu Garden", ["garden", "historical site"]]],
        ["Shanghai, China", ["Yuz Museum", ["art", "museum"]]],
        ["Shanghai, China", ["Oriental Peal Tower", ["skyscraper, viewing deck"]]],
        ["Los Angeles, USA", ["LACMA", ["art", "museum"]]],
        ["São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]]],
        ["São Paulo, Brazil", ["Pàtio do Colè", ["historical site"]]],
        ["Cairo, Egypt", ["Egyptian Museum", ["museum"]]]
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

    # Variables
    destinations = ["Paris, France","Shanghai, China","Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt"]
    attractions = [[] for i in destinations]

    # Destinations
    # test_get_destination_index(test_destinations)
    
    # # Traveler
    # test_get_traveler_location(test_traveler)

    # Attractions
    for attraction in test_attractions:
        test_add_attractions(attraction)

    print(attractions)