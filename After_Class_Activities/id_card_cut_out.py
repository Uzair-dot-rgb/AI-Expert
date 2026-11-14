# ================================
# ID CARD CUT-OUT
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

photo = np.full((120, 100, 3), 180, np.uint8)                 # a grey classroom wall
cv2.rectangle(photo, (30, 60), (70, 120), (40, 90, 220), -1)  # the student's shirt
cv2.circle(photo, (50, 40), 18, (150, 180, 220), -1)          # the student's face
cv2.rectangle(photo, (80, 10), (95, 30), (60, 60, 60), -1)    # a poster of a person on the wall

person = np.zeros((120, 100), np.float32)                     # what a perfect AI would say
cv2.rectangle(person, (30, 60), (70, 120), 1.0, -1)
cv2.circle(person, (50, 40), 18, 1.0, -1)
matte = cv2.GaussianBlur(person, (7, 7), 0)                   # soft edges, like a real matte
matte[35:45, 42:58] = 0.45                                    # the AI was unsure here (a hand near the face)
matte[10:31, 80:96] = 0.9                                     # the AI thinks the poster is a person too
blue = np.zeros((120, 100, 3), np.uint8)
blue[:] = (200, 120, 40)                                      # the ID card's blue background
print("Photo", photo.shape, "matte", matte.shape)

# ---------- PART 1: read the matte ----------
print("\nPART 1: Read the matte")
# YOUR CODE HERE
# Count the pixels that are sure person (0.8 or more), unsure (0.2 up to 0.8) and room (below 0.2). Print the three numbers.

# ---------- PART 2: keep only the student ----------
print("\nPART 2: Keep only the student")
# YOUR CODE HERE
# Find the separate patches above 0.35, keep only the biggest, fill its outline (exactly as clean() did in class).
# Call the filled picture body. Print how many patches were found and how many pixels body keeps.

# ---------- PART 3: paste onto the ID card ----------
print("\nPART 3: ID card")
# YOUR CODE HERE
# Blend the photo onto blue with body as the matte. Call it card. Print the pixels at (40, 50), (20, 88) and (0, 0).

# ---------- PART 4: the ghost ----------
print("\nPART 4: Raw matte against cleaned")
# YOUR CODE HERE
# Blend again, this time with the raw matte. Print its pixel at (40, 50) next to card's pixel at (40, 50).
