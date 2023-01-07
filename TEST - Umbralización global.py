import cv2

# Imagen
imagen = cv2.imread('nascalines.jpg')

# Conversión a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Umbralización
_, umbral = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite('umbralizada.jpg', umbral) #guardar imagen