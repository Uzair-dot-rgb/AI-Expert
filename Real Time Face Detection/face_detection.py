import cv2

#Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Start the video capture from default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error, Could not open camera.")
    exit()
    
while True:
    #Capture frame by frame
    ret, frame = cap.read()
    
    #If frame is read correctly, ret is True
    if not ret:
        print("Error, Could not read frame.")
        break
    
    #Conver frame to grayscale for face detection(works faster)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    
    #Draw rectangles around the detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) #Blue rectangle with thickness of 2
        
    #Display the resulting frame
    cv2.imshow("Face Detection (Press 'q' to exit)", frame)
    
    #Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
#Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()