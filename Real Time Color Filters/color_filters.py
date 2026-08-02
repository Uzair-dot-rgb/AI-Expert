import numpy as np
import cv2

def apply_filter(image, filter_type):
    img = image.copy()
    if filter_type == "red":
        img[:, :, 1] = 0 
        img[:, :, 2] = 0
    elif filter_type == "blue":
        img[:, :, 0] = 0
        img[:, :, 1] = 0
    elif filter_type == "green":
        img[:, :, 0] = 0
        img[:, :, 2] = 0
    elif filter_type == "sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        sx = cv2.sobel(gray, cv2.CV_64F, 1, 0, ksize = 3)
        sy = cv2.sobel(gray, cv2.CV_64F, 0, 1, ksize = 3)
        sob = cv2.bitwise_or(sx.astype(np.uint8), sy.astype(np.uint8))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    elif filter_type == "cartoon":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        img = cv2.bitwise_and(color, color, mask = edges)
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open camera.")
        return
    filter_type = "original"
    print("Keys: r = Red, b = Blue, g = Green, s + Sobel, c = Canny, t = Cartoon, q = Quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        out = apply_filter(frame, filter_type)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            filter_type = "red"
        elif key == ord("b"):
            filter_type = "blue"
        elif key == ord("g"):
            filter_type = "green"
        elif key == ord("s"):
            filter_type = "sobel"
        elif key == ord("c"):
            filter_type = "canny"
        elif key == ord("t"):
            filter_type = "cartoon"
        elif key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
