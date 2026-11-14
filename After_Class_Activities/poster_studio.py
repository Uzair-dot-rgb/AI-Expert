# ================================
# POSTER STUDIO
# ================================

# ---------- SETUP (given to you) ----------
import numpy as np

rng = np.random.default_rng(6)
photo = rng.integers(0, 256, (6, 8, 3)).astype(np.uint8)   # a tiny 6 x 8 camera picture, BGR like OpenCV
matte = np.zeros((6, 8)); matte[1:6, 3:6] = 1.0; matte[1:6, 2] = 0.5   # the cut-out: 1 = the student, 0 = the room, 0.5 = the edge
STYLES = {name: np.random.default_rng(seed).normal(0, 1, (1, 1, 1, 100)).astype(np.float32)
          for name, seed in [("Comic", 1), ("Dream", 2), ("Neon", 3)]}   # 100 style numbers for each poster style
TIMES = {"camera picture": 0.033, "painting": 0.18, "cut-out": 0.1}         # seconds for one of each, on the club laptop


def poster_ai(content_image, style_numbers):   # a stand-in for the any-style network: RGB 0..1 in, RGB 0..1 out
    if content_image.ndim != 4:
        raise ValueError(f"Invalid rank for input: content_image Got: {content_image.ndim} Expected: 4")
    if content_image.max() > 1:
        raise ValueError(f"content_image must be 0 to 1, got numbers up to {content_image.max():.0f}")
    colour = 1 / (1 + np.exp(-style_numbers.reshape(100)[:3]))              # the style's own colour, from its numbers
    return content_image * 0.4 + colour * 0.6


print("Photo:", photo.shape, " styles:", list(STYLES))

# ---------- PART 1: picture in ----------
print("\nPART 1: Ready for the AI")
# YOUR CODE HERE
# Make x: the photo as RGB numbers from 0 to 1, with a "how many pictures" axis first: shape (1, 6, 8, 3).
# Print its shape and its smallest and largest number, rounded to 2 places.

# ---------- PART 2: one network, any style ----------
print("\nPART 2: Three posters, one AI")
# YOUR CODE HERE
# For each style, run poster_ai with x and that style's 100 numbers, and take the one picture it returns.
# Turn it back into a normal picture (0 to 255, uint8, BGR) and keep it in a dict called posters.
# Print the name, the shape and the average B, G, R as whole numbers.

# ---------- PART 3: keep the student real ----------
print("\nPART 3: Dream poster, student kept real")
# YOUR CODE HERE
# Blend: the student (matte 1) from the photo, the room (matte 0) from the Dream poster. Call the result final.
# Print the room pixel (0, 0), the student pixel (2, 4) and the edge pixel (2, 2): final, photo and poster.
# Then count the pixels where final is exactly the photo.

# ---------- PART 4: background threads ----------
print("\nPART 4: Pictures per second")
# YOUR CODE HERE
# If the loop waited for both AIs, one picture would take all three times added up. Print the pictures per second.
# With background threads, each part runs at its own speed. Print the per-second rate of each one, to 1 place.
