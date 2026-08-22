import cv2, time, numpy as np
import mediapipe as mp

H = mp.solutions.hands
TIP = H.HandLandmark
ids = {
    "thumb": TIP.THUMB_TIP,
    "index": TIP.INDEX_FINGER_TIP,
    "middle": TIP.MIDDLE_FINGER_TIP,
    "ring": TIP.RING_FINGER_TIP,
    "pinky": TIP.PINKY_TIP
}

hands = H.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
draw = mp.solutions.drawing_utils
pairs = {"middle":("SEPIA", "NEGATIVE"), "ring":("BLUR", "GLITCH"), "pinky":("EDGE", "CARTOON")}
st = {k:0 for k in pairs.keys()}; cur = "SEPIA"
DEB, CAB, TT, TP = 0.6, 1.2, 30, 20
la = lc = 0; pinch_on = False
MAIN, POP = "Gesture-Controlled Photo App", "Captured (ESC / Close to Resume)"
paused = False; freeze = None
SEPIA_M = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])

def apply(img, t):
    if t == "SEPIA": return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8)
    if t == "NEGATIVE": return cv2.bitwise_not(img)
    if t == "BLUR": return cv2.GuassianBlur(img, (15, 15), 0)
    if t == "GLITCH": 
        h, w = img.shape[:2]; r, g, b = img[:,:,2], img[:,:,1], img[:,:,0]