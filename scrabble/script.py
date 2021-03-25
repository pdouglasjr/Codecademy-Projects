# Name:     scrabble/script.py
# Author:   Phillip Douglas
# Purpose:  Process some data from a group of friends playing scrabble.

# Global variables.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Zip letters and points into letter_to_points.
letter_to_points = {k:v for k,v in zip(letters, points)}

# We need to account for blank tiles. Add a key-value pair to account for blank tiles. 
letter_to_points[" "] = 0

# Dictionary of player_to_words that maps players to a list of words they have played.
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Functions
def score_word(word):
    """This function takes a word and returns how many points that word is worth."""
    point_total = 0

    # Loop through the provided word.
    for letter in word:
        # Add to point_total if letter is in letter_to_points.
        if letter.upper() in letter_to_points:
            point_total += letter_to_points[letter.upper()]

    return point_total

def update_scorecard():
    """This function updates the scorecard for a round of Scrabble"""
    for player in player_to_words:
        player_points = 0
        words = player_to_words.get(player)
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)

    return False

if (__name__=="__main__"):    
    # Empty dictionary player_to_points to calculate points for each player.
    player_to_points = {}

    update_scorecard()
    print(player_to_points)

    play_word('player1', 'bacon')
    update_scorecard()
    print(player_to_points)


