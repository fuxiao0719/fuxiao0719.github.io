import cv2
import numpy as np
for i in range(22):
    img = cv2.imread(str(i)+'_rgb.jpg')
    blank = np.ones_like(img)*255
    cv2.imwrite(str(i)+'_rgb_blank.jpg', blank)

