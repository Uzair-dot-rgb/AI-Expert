import cv2 
import numpy as np

def apply_colour_filters(image, filter_type):
    """Apply the specified colour filter to the image."""
    #Create a copy of the image to avoid modifying the original.
    filtered_image = image.copy()
    if filter_type == "red_tint":
        #Remove the blue and green channels for the image.
        filtered_image[:, :, 1] = 0 #Green channels to 0.
        filtered_image[:, :, 0] = 0 #Blue channels to 0.
    elif filter_type == "blue_tint":
        #Remove red and green channels.
        filtered_image[:, :, 2] = 0 #Red channels to 0.
        filtered_image[:, :, 1] = 0 #Green channels to 0.
    elif filter_type == "green_tint":
        #Remove red and blue channels.
        filtered_image[:, :, 2] = 0 #Red channels to 0.
        filtered_image[:, :, 0] = 0 #Blue channels to 0.
    elif filter_type == "increased_red":
        #Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50) #Increase red channel by 50.
    elif filter_type == "increased_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)#Decrease blue channel by 50.
    return filtered_image

#Load the image
image_path = "camera.jpeg" #Provide your image path.
image = cv2.imread(image_path)

if image is None:
    print("Error, Could not load image.")
else: 
    filter_type = "original" #Default filter type.
    
    print("Press the following keys to apply filters.")
    print("R : Red Filter")
    print("B : Blue Filter")
    print("G : Green Filter")
    print("I : Increased Red Filter")
    print("D : Decreased Blue Filter")
    print("Q : Quit")
    
    while True:
        #Apply the selected filter.
        filtered_image = apply_colour_filters(image, filter_type)
        #Display the filtered image.
        cv2.imshow("Filtered Image", filtered_image)
        #Wait for key press.
        key = cv2.waitKey(0) & 0xFF
        
        #Map key press.
        if key == ord("R"):
            filter_type = "red_tint"
        elif key == ord("B"):
            filter_type = "blue_tint"
        elif key == ord("G"):
            filter_type = "green_tint"
        elif key == ord("I"):
            filter_type = "increased_red"
        elif key == ord("D"):
            filter_type = "increased_blue"
        elif key == ord("Q"):
            print("Exiting.")
            break
        else:
            print("Please enter a valid option (R, B, G, I, D, Q).")

cv2.destroyAllwindow()