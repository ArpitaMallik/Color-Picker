import cv2
import numpy as np


def cross(x):
    pass


img = np.ones((300, 512, 3), np.uint8) * 255
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.namedWindow("Color Picker")

# create switch
s1 = "O:OFF .. 1:ON"
cv2.createTrackbar(s1, "Color Picker", 0, 1, cross)

cv2.createTrackbar("R", "Color Picker", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker", 0, 255, cross)

while True:
    cv2.imshow("Color Picker", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    s = cv2.getTrackbarPos(s1, "Color Picker")
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv2.destroyAllWindows()