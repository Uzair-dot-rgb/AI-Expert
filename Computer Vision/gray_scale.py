import cv2
image = cv2.imread("tree.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayimage = cv2.resize(gray_image, (250, 250))
cv2.imshow("Gray Image", grayimage)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("gray_tree.jpg", grayimage )
cv2.destroyAllWindows()
print(f"Gray Image shape: {grayimage.shape}")   