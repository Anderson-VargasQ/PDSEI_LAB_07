import cv2

# Imagen
imagen = cv2.imread('nascalines.jpg')

# Conversión a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Umbralización adaptativa
umbral = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 25)

cv2.imwrite('umbralizada.jpg', umbral) #guardar imagen