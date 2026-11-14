# ================================
# STICKER SHOP
# ================================

# ---------- SETUP (given to you) ----------
import cv2
import numpy as np

photo = np.full((256, 512, 3), (200, 210, 220), np.uint8)            # a light table
cv2.circle(photo, (256, 150), 80, (40, 40, 200), -1)                 # a red apple
cv2.ellipse(photo, (300, 58), (30, 14), -30, 0, 360, (60, 170, 60), -1)  # its green leaf
cv2.rectangle(photo, (420, 30), (500, 110), (150, 110, 70), -1)      # a blue mug behind it
clicks = [(256, 150, 1), (460, 60, 0)]                               # click: the apple. Right-click: the mug.

guesses = np.full((3, 256, 256), -4.0, np.float32)                   # SAM's 3 guesses (256 x 256), in no order
cv2.ellipse(guesses[0], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)    # the apple without its leaf
cv2.ellipse(guesses[1], (128, 150), (10, 20), 0, 0, 360, 4.0, -1)    # only a shiny spot on the apple
cv2.ellipse(guesses[2], (128, 150), (40, 80), 0, 0, 360, 4.0, -1)    # the apple with its leaf
cv2.ellipse(guesses[2], (150, 58), (15, 14), -30, 0, 360, 4.0, -1)
print("Photo", photo.shape, "guesses", guesses.shape)

# ---------- PART 1: clicks to prompts ----------
print("\nPART 1: Prompts for SAM")
# YOUR CODE HERE
# Move each click from the photo (512 wide, 256 high) to SAM's 1024 x 1024 square. Call the array points (float32).
# Make labels (int64) from the clicks. Print both as lists, then the shapes SAM wants, using [None, None].

# ---------- PART 2: sort the guesses ----------
print("\nPART 2: Part, bigger, whole")
# YOUR CODE HERE
# Sort the 3 guesses from small to big by how many numbers are above 0. Call the list ordered. Print the 3 sizes.

# ---------- PART 3: the whole apple, photo-sized ----------
print("\nPART 3: Mask")
# YOUR CODE HERE
# Take the biggest guess, resize it to the photo (width first), and make it 1 inside and 0 outside (uint8).
# Call it mask. Print its shape and how many pixels it covers.

# ---------- PART 4: the sticker ----------
print("\nPART 4: Sticker")
# YOUR CODE HERE
# Find the box round the mask, make a soft alpha (0 or 255, blurred 3 x 3), stack it on the photo and crop to the box.
# Call it sticker. Print the box and its shape, the alpha in its middle and in its top-left corner, and save sticker.png.
