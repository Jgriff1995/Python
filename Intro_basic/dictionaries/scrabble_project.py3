# =============================================
# Build Your Point Dictionary
# =============================================

# Provided lists of letters and their corresponding points.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary mapping letters to their point values using zip and dictionary comprehension.
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add an entry for blank tiles (spaces) with a point value of 0.
letter_to_points[" "] = 0

print("Letter to Points Mapping:")
print(letter_to_points)

# =============================================
# Score a Word
# =============================================

# Define a function to calculate the score of a word.


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


# Test the function with the word "BROWNIE".
brownie_points = score_word("BROWNIE")
print("\nPoints for 'BROWNIE':", brownie_points)  # Expected output: 15

# =============================================
# Score a Game
# =============================================

# Create a dictionary mapping players to the words they have played.
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Create a dictionary to store each player's total points.
player_to_points = {}

# Calculate points for each player.
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print("\nPlayer Points:")
print(player_to_points)

# =============================================
# (Optional)
# =============================================

# Function to add a word to a player's list of words.


def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

# Function to update point totals after adding a word.


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


# Example usage of the optional functions:
play_word("player1", "CODE")
update_point_totals()

print("\nUpdated Player Points After Adding 'CODE':")
print(player_to_points)
