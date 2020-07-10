import cv2
import numpy as np

image0 = cv2.imread('homework2.png')

height, width, trash = image0.shape
for x in range(height):
    for y in range(width):
        blue, green, red = image0[x][y]
        if blue == 0 and green == 0 and red == 255:
            pass
        else:
            image0[x][y] = np.array([127,127,127])

cv2.imshow('Image: test', image0)
cv2.waitKey(0)
cv2.destroyAllWindows()