# LIBRARY CAMERA GUESSES
# ---------- SETUP (given to you) ----------
import numpy as np

# The library camera looked at one picture of the reading corner. The model made 6 guesses (one row each).
# Each row has 4 numbers: objectness (is anything here?), then a score for person, chair and book.
# Example numbers made up for this task, in the same layout as the real model's output.
NAMES = ["person", "chair", "book"]
OUTPUT = np.array([
    [0.90, 0.90, 0.05, 0.05],
    [0.80, 0.10, 0.80, 0.10],
    [0.60, 0.20, 0.10, 0.70],
    [0.50, 0.60, 0.30, 0.10],
    [0.10, 0.90, 0.05, 0.05],
    [0.70, 0.30, 0.20, 0.90],
])
MIN_SCORE = 0.5

# ---------- PART 1: score every guess ----------
# YOUR CODE HERE
# scores = objectness x each name score, for every guess. Column 0 of OUTPUT is objectness, columns 1 to 3 are the names.
# Call the result scores. It should have shape (6, 3).
scores = np.zeros((6, 3))   # placeholder: replace this line with your own

print("PART 1: Scores")
print("Shape:", scores.shape)
print("Guess 4, person:", round(float(scores[4, 0]), 2))

# ---------- PART 2: the best name for every guess ----------
# YOUR CODE HERE
# class_ids = the position of the biggest score in each row. confidences = that biggest score.
class_ids = np.zeros(6, dtype=int)   # placeholder: replace this line with your own
confidences = np.zeros(6)            # placeholder: replace this line with your own

print("\nPART 2: Best name")
for i in range(6):
    print("Guess", i, "->", NAMES[class_ids[i]], f"{confidences[i]:.2f}")

# ---------- PART 3: keep the sure guesses ----------
# YOUR CODE HERE
# kept = the numbers of the guesses whose confidence is at least MIN_SCORE.
kept = []   # placeholder: replace this line with your own

print("\nPART 3: Kept")
print("Kept guesses:", [int(i) for i in kept])
print("Kept names:", [NAMES[class_ids[i]] for i in kept])

# ---------- PART 4: change how sure it must be ----------
print("\nPART 4: Three thresholds")
# YOUR CODE HERE
# For each threshold in 0.2, 0.5 and 0.8, count the guesses with confidence at least that big and print one line:
# Threshold <threshold> -> <number> kept
