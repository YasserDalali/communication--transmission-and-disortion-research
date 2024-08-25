"""
3. Group-to-Group Message Passing with Group Verification

- Concept: The message is passed between groups, with each group consisting of 10 people. If one person in the group makes a mistake in the message, the other 9 members attempt to correct it before the message is passed to the next group.

- Implementation: Each group distorts the message slightly. Then, a group verification process (where each of the 9 other members in the group checks and corrects the message) attempts to ensure that the message remains accurate before it's passed to the next group.

- Outcome: The final message is much more likely to resemble the original message, as the group verification process allows for more opportunities to catch and correct mistakes. This experiment shows how group dynamics can help preserve the integrity of the message better than individual verification.
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

def group_verify_message(original_message, received_message):
    """Group verifies and corrects the message."""
    for _ in range(9):
        received_message = verify_message(original_message, received_message)
    return received_message

def telephone_game_group_to_group(starting_message, num_groups):
    current_message = starting_message
    for group_num in range(1, num_groups + 1):
        distorted_message = distort_message(current_message)
        current_message = group_verify_message(starting_message, distorted_message)
    return current_message

# Parameters
starting_message = """
In the second year of Daryavesh HaMelech, in the sixth month, in yom echad of the month, came the Devar Hashem by Chaggai HaNavi unto Zerubavel ben Sh'altiel, Governor of Yehudah, and to Yehoshua ben Yehotzadak, the Kohen HaGadol, saying:
"""
num_groups = 150
num_trials = 10
# Run the experiment
distances = []

for _ in range(num_trials):
    final_message = telephone_game_group_to_group(starting_message, num_groups)
    distance = levenshtein_distance(starting_message, final_message)
    distances.append(distance)

average_distance = sum(distances) / num_trials

print(f"NGROUPS: {num_groups} | TRIALS: {num_trials} | DISORT: 30% | CORR: 50% | G-CORR: 90%")
print(f"Original Message: {starting_message}")
print(f"Final Message: {final_message}")
print(f"Average Final Levenshtein Distance: {average_distance} over {num_trials} trials")
print("---------------------------------------------------------")



