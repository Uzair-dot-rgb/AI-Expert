import cv2
import numpy as np


def apply_colour_filters(image, filter_type, intensity_value):
    """Apply the specified colour filter with adjustable intensity."""
    filtered_image = image.copy()

    # OpenCV loads images in BGR format: Index 0=Blue, 1=Green, 2=Red

    if filter_type == "red_tint":
        # Keep Red, scale down Blue and Green based on intensity (0 = full tint, 255 = original)
        factor = intensity_value / 255.0
        filtered_image[:, :, 0] = (filtered_image[:, :, 0] * factor).astype(np.uint8)
        filtered_image[:, :, 1] = (filtered_image[:, :, 1] * factor).astype(np.uint8)

    elif filter_type == "blue_tint":
        # Keep Blue, scale down Green and Red
        factor = intensity_value / 255.0
        filtered_image[:, :, 1] = (filtered_image[:, :, 1] * factor).astype(np.uint8)
        filtered_image[:, :, 2] = (filtered_image[:, :, 2] * factor).astype(np.uint8)

    elif filter_type == "green_tint":
        # Keep Green, scale down Blue and Red
        factor = intensity_value / 255.0
        filtered_image[:, :, 0] = (filtered_image[:, :, 0] * factor).astype(np.uint8)
        filtered_image[:, :, 2] = (filtered_image[:, :, 2] * factor).astype(np.uint8)

    elif filter_type == "increased_red":
        # Add adjustable value to the Red channel safely using cv2.add
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity_value)

    elif filter_type == "decreased_blue":
        # Subtract adjustable value from the Blue channel safely using cv2.subtract
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity_value)

    return filtered_image


def on_trackbar_change(val):
    """Callback function required by cv2.createTrackbar."""
    pass


# Load the image
image_path = "camera.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Setup window and trackbar
    window_name = "Filtered Image"
    cv2.namedWindow(window_name)

    # Trackbar controls the parameter value (0 to 255)
    cv2.createTrackbar("Intensity", window_name, 50, 255, on_trackbar_change)

    filter_type = "original"

    print("Press the following keys to change filters:")
    print("R : Red Tint         | B : Blue Tint        | G : Green Tint")
    print("I : Increased Red    | D : Decreased Blue   | O : Original/Reset")
    print("Q : Quit")

    while True:
        # Read current trackbar value dynamically
        intensity = cv2.getTrackbarPos("Intensity", window_name)

        # Apply filter with current intensity
        filtered_image = apply_colour_filters(image, filter_type, intensity)

        # Display image
        cv2.imshow(window_name, filtered_image)

        # Change waitKey delay to 10ms for smooth live updates
        key = cv2.waitKey(10) & 0xFF

        if key == ord("r") or key == ord("R"):
            filter_type = "red_tint"
            print("Switched to Red Tint")
        elif key == ord("b") or key == ord("B"):
            filter_type = "blue_tint"
            print("Switched to Blue Tint")
        elif key == ord("g") or key == ord("G"):
            filter_type = "green_tint"
            print("Switched to Green Tint")
        elif key == ord("i") or key == ord("I"):
            filter_type = "increased_red"
            print("Switched to Increased Red")
        elif key == ord("d") or key == ord("D"):
            filter_type = "decreased_blue"
            print("Switched to Decreased Blue")
        elif key == ord("o") or key == ord("O"):
            filter_type = "original"
            print("Reset to Original")
        elif key == ord("q") or key == ord("Q"):
            print("Exiting.")
            break

    cv2.destroyAllWindows()
