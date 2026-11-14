# ================================
# ROBOT VACUUM DEPTH CHECK
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

raw = np.tile(np.linspace(1.0, 5.0, 60, dtype=np.float32)[:, None], (1, 80))   # the floor: bigger = nearer the robot
raw[:20, :] = 1.0                                              # the far wall of the hallway
cv2.rectangle(raw, (55, 30), (70, 50), 6.0, -1)                # a toy box close to the robot
photo = np.zeros((60, 80, 3), np.uint8)
photo[:, :, 0] = np.arange(80) * 3                             # a test picture: blue = 3 x the column number
WOBBLE = 12
print("Raw depth", raw.shape, "from", raw.min(), "to", raw.max())

# ---------- PART 1: numbers from 0 to 1 ----------
print("\nPART 1: Normalise")
# YOUR CODE HERE
# Turn raw into numbers from 0 (far) to 1 (near), exactly as in TODO 2 of class (with + 1e-6). Call it near.
# Print near at the wall [10, 40], the floor [45, 20] and the box [40, 60], rounded to 2 places.

# ---------- PART 2: where is the obstacle? ----------
print("\nPART 2: Obstacle")
# YOUR CODE HERE
# Mark the pixels with near above 0.85. Call it close. Find the average COLUMN of those pixels, and say "left",
# "middle" or "right" (the picture is 80 columns wide, so each third is about 26.7). Print the count, the side and the column.

# ---------- PART 3: one frame of the wobble ----------
print("\nPART 3: Parallax")
# YOUR CODE HERE
# Make xs and ys (the x and y of every pixel), as wobble() did. Make the slide table for the peak of the swing:
# WOBBLE * (near - 0.5), as float32. Call it shift. Then cv2.remap the photo with xs + shift and ys. Call it moved.
# Print the slide of the box [40, 60] and the wall [10, 40], and which column the box pixel now shows (blue / 3).

# ---------- PART 4: relative, not metres ----------
print("\nPART 4: Relative depth")
raw2 = raw * 3                                                 # the same hallway, another photo: the AI's numbers are 3 times bigger
# YOUR CODE HERE
# raw2 is given: the AI's numbers for another photo of the same hallway, 3 times bigger. Normalise it the same way.
# Call it near2. Print both raw nearest numbers and whether near and near2 are the same map (np.allclose).
