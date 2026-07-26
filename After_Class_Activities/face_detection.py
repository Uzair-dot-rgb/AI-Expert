import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the pre-trained Haar Cascade classifier for smile/happy expression detection
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Start the video capture from default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error, Could not open camera.")
    exit()

while True:
    # Capture frame by frame
    ret, frame = cap.read()
    
    # If frame is read correctly, ret is True
    if not ret:
        print("Error, Could not read frame.")
        break
        
    # Convert frame to grayscale for face detection (works faster)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # Blue rectangle for face
        
        # Isolate the grayscale face region
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect smiles inside the face region
        # Higher minNeighbors
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
        
        # Evaluate expression 
        if len(smiles) > 0:
            emotion_label = "Happy"
            text_color = (0, 255, 0) # Green text for happy
            
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
        else:
            emotion_label = "Neutral / Sad"
            text_color = (0, 0, 255) # Red text for neutral/sad
            
        # Draw the predicted emotion
        cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)

    # Display the resulting frame
    cv2.imshow("Face & Expression Detection (Press 'q' to exit)", frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()
