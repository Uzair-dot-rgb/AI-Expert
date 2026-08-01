import cv2
import numpy as np

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # 1. ROTATION: Rotate the frame 90 degrees clockwise
    # Options: ROTATE_90_CLOCKWISE, ROTATE_180, ROTATE_90_COUNTERCLOCKWISE
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # 2. BRIGHTNESS: Increase brightness by adding a scalar value
    # cv2.convertScaleAbs ensures pixel values stay safely between 0 and 255
    # alpha = contrast control (1.0 = no change), beta = brightness control (+50 = brighter)
    frame = cv2.convertScaleAbs(frame, alpha=1.0, beta=50)

    # 3. CROPPING: Crop to a specific Region of Interest (ROI)
    # Get current dimensions of the processed frame
    height, width = frame.shape[:2]
    
    # Define bounding box coordinates (e.g., cropping a center square region)
    ymin, ymax = int(height * 0.1), int(height * 0.9)
    xmin, xmax = int(width * 0.1), int(width * 0.9)
    
    # Apply standard NumPy slicing to crop the frame
    frame = frame[ymin:ymax, xmin:xmax]

    # Grayscale the modified frame for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the manipulated frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the count of faces
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"People Count: {len(faces)}", (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the final frame
    cv2.imshow("Face Counting with Manipulated Frame", frame)

    # Exit the loop when "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
