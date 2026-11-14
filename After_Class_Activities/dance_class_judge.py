# ================================
# DANCE CLASS JUDGE
# ================================

# ---------- SETUP (given to you) ----------
import numpy as np

# The pose AI's arm points for one dancer at three moments, as (x, y, sure) in pixels.
# 5 and 6 = shoulders, 7 and 8 = elbows, 9 and 10 = wrists.
moments = {
    "Moment 1": {5: (220, 200, 0.9), 7: (160, 197, 0.8), 9: (100, 195, 0.9),
                 6: (300, 200, 0.9), 8: (360, 198, 0.9), 10: (420, 196, 0.8)},
    "Moment 2": {5: (220, 200, 0.9), 7: (180, 160, 0.9), 9: (150, 110, 0.7),
                 6: (300, 200, 0.9), 8: (350, 170, 0.8), 10: (400, 140, 0.9)},
    "Moment 3": {5: (220, 200, 0.9), 7: (160, 200, 0.6), 9: (100, 200, 0.1),
                 6: (300, 200, 0.9), 8: (360, 200, 0.9), 10: (420, 200, 0.2)},
}
TARGET = [180, 180, 0, 0]        # the teacher's pose, a T-pose: left upper, left lower, right upper, right lower
print("Moments:", len(moments), " target:", TARGET)

# ---------- PART 1: unsure points ----------
print("\nPART 1: Unsure points")
# YOUR CODE HERE
# For each moment, list the point numbers that are less than 0.3 sure, smallest first. Print them.

# ---------- PART 2: arm angles ----------
print("\nPART 2: Arm angles")
# YOUR CODE HERE
# Write arm_angles(points): the 4 arm angles in degrees, exactly as in Strike a Pose.
# Print each moment's 4 angles rounded to whole degrees.

# ---------- PART 3: scores ----------
print("\nPART 3: Scores")
# YOUR CODE HERE
# Write score(points, target): 0 if any arm point is less than 0.3 sure, otherwise 100 minus the mean
# difference the short way round, never below 0. Keep the rounded scores in a dict called scores and print them.

# ---------- PART 4: the judge ----------
print("\nPART 4: The judge")
# YOUR CODE HERE
# Find the moment with the highest score. Print it, its score, and PASS if it is 80 or more, otherwise TRY AGAIN.
