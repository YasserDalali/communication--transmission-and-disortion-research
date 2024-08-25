"""

1. Person-to-Person Message Passing (Basic Telephone Game)

- Concept: A message is passed from one person to another, with each person potentially distorting the message slightly before passing it on.

- Implementation: A simple function distorts the message with a small chance of changing a character or adding noise. Each person receives and passes on the distorted message.

- Outcome: The message becomes increasingly distorted as it passes through more people, often resulting in a final message that differs significantly from the original.

"""
import random

def levenshtein_distance(s1, s2):
    """Calculates the Levenshtein distance between two strings."""
    return sum(1 for a, b in zip(s1, s2) if a != b) + abs(len(s1) - len(s2))

def distort_message(message):
    """Randomly distorts the message."""
    characters = list(message)
    if random.random() < 0.3:  # 30% chance to distort the message
        index = random.randint(0, len(characters) - 1)
        if random.random() < 0.5:
            characters[index] = chr(random.randint(97, 122))
        else:
            characters.insert(index, chr(random.randint(97, 122)))
    return ''.join(characters)

def telephone_game_person_to_person(starting_message, num_people):
    current_message = starting_message
    for i in range(1, num_people + 1):
        current_message = distort_message(current_message)
    return current_message


# Parameters
starting_message = """
In the second year of Daryavesh HaMelech, in the sixth month, in yom echad of the month, came the Devar Hashem by Chaggai HaNavi unto Zerubavel ben Sh'altiel, Governor of Yehudah, and to Yehoshua ben Yehotzadak, the Kohen HaGadol, saying:
"""
num_people = 150
num_trials = 10
# Run the experiment
distances = []

for _ in range(num_trials):
    final_message = telephone_game_person_to_person(starting_message, num_people)
    distance = levenshtein_distance(starting_message, final_message)
    distances.append(distance)

average_distance = sum(distances) / num_trials

print(f"NPEOPLE: {num_people} | TRIALS: {num_trials} | DISORT: 30%")
print(f"Original Message: {starting_message}")
print(f"Final Message: {final_message}")
print(f"Average Final Levenshtein Distance: {average_distance} over {num_trials} trials")
print("---------------------------------------------------------")