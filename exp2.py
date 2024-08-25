"""
2.Person-to-Person with Verification

    - Concept: After each person receives a potentially distorted message, they attempt to verify and correct it
before passing it on to the next person.

    - Implementation: After distorting the message, a verification function compares the distorted message with 
the original and attempts to correct any discrepancies before passing it on.
    
    - Outcome: The final message is generally closer to the original compared to the first experiment, as each
person tries to correct any errors introduced before passing it on. However, the correction process isn't perfect, so the message may still change slightly.

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

def verify_message(original_message, received_message):
    """Verifies and attempts to correct the message."""
    if len(received_message) != len(original_message):
        received_message = original_message[:len(received_message)]
    
    corrected_message = list(received_message)
    for i in range(min(len(original_message), len(received_message))):
        if original_message[i] != received_message[i]:
            if random.random() < 0.5:  # 50% chance to correct
                corrected_message[i] = original_message[i]
    
    return ''.join(corrected_message)

def telephone_game_person_to_person_with_verification(starting_message, num_people):
    current_message = starting_message
    for i in range(1, num_people + 1):
        distorted_message = distort_message(current_message)
        current_message = verify_message(starting_message, distorted_message)
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
    final_message = telephone_game_person_to_person_with_verification(starting_message, num_people)
    distance = levenshtein_distance(starting_message, final_message)
    distances.append(distance)

average_distance = sum(distances) / num_trials

print(f"NPEOPLE: {num_people} | TRIALS: {num_trials} | DISORT: 30% | CORR: 50%")
print(f"Original Message: {starting_message}")
print(f"Final Message: {final_message}")
print(f"Average Final Levenshtein Distance: {average_distance} over {num_trials} trials")
print("---------------------------------------------------------")