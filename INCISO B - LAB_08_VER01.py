import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('nascalines.jpg',0)
edges = cv.Canny(image,200,500)

gray = cv.imread("nascalines.jpg",0)/255
img = cv.blur(gray, (7,7))

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
scharrx = cv.Scharr(img,cv.CV_64F,1,0)
scharry = cv.Scharr(img,cv.CV_64F,0,1)
sobelx_pos = np.abs(sobelx) 
sobely_pos = np.abs(sobely) 
scharrx_pos = np.abs(scharrx) 
scharry_pos = np.abs(scharry) 
plt.figure(figsize=(12,6))
plt.subplot(221),plt.imshow(sobelx_pos+sobely_pos,cmap = 'gray', vmin=0, vmax=1)
plt.subplot(222),plt.imshow(scharrx_pos+scharry_pos,cmap = 'gray')
plt.subplot(223),plt.imshow(image,cmap = 'gray')
plt.title('Imagen original'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(edges,cmap = 'gray', vmin=0, vmax=256)
plt.show()

