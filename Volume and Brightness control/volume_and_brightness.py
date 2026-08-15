import cv2, mediapipe as mp, numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
draw = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

try:
    dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities, "GetDefaultOutputDevice") else AudioUtilities.GetSpeakers()
    volctl = dev.EndpointVolume.QueryInterface(IAudioEndpointVolume)
except Exception as e:
    print(f"Pycaw error: {e}"); exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error, could not open webcam"); exit()

WIN = "Hand Gesture Control"

while True:
    ok, img = cap.read()
    if not ok:
        break
    img = cv2.flip(img, 1); h, w = img.shape[:2]
    res = hands.process()

    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            cv2.circle(img, tp, 10, (0, 255, 0), cv2.FILLED)
            cv2.line(img, tp, ip, (0, 255, 0), 3)
            dist = float(np.hypot(tp[0] - ip[0], tp[1] - ip[1]))

            if label == "Left":
                v = np.interp(dist, [30, 300], [minv, maxv])
                try: 
                    volctl.SetMasterVolumeLevelScalar(v, None)
                except Exception as e:
                    print(f"Volume error: {e}")
                bar = int(np.interp(dist, [30, 300], [400, 150])); pct = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3); cv2.rectangle(img, (50, bar), (84, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

            elif label == "Right":
                b = int(np.interp(dist, [30, 300], [0, 100]))
                try:
                    sbc.set_brightness(b)
                except Exception as e:
                    print(f"Brightness error: {e}")
                    bar = int(np.interp(dist, [30, 300], [400, 150])); pct = int(np.interp(dist, [30, 300], [0, 100]))
                    cv2.rectangle(img, (x1, 150), (x2, 400), (255, 0, 0), 3); cv2.rectangle(img, (x1, bar), (x2, 400), (255, 0, 0), cv2.FILLED)
                
