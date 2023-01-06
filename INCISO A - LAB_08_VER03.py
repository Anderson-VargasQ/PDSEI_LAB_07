import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("images_VER_2.jpeg",0)
img = np.uint8(img > 128)

selem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(30,30))

sold = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, selem)
perf = cv2.bitwise_not(sold)

fig,axes=plt.subplots(2,2)
plt.subplot(121)
plt.imshow(perf, cmap="gray")
plt.title("Perforaciones")

plt.subplot(122)
plt.imshow(sold, cmap="gray")
plt.title("Soldadura")

plt.show()