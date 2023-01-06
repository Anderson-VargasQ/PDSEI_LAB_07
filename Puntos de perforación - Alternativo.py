import cv2
import numpy as np

class ImageProcessor:
  def __init__(self, image_path):
    # Carga la imagen y la convierte a escala de grises
    self.image = cv2.imread(image_path)
    self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

  def find_shapes(self):
    # Detecta los bordes de los objetos en la imagen
    edges = cv2.Canny(self.gray, 50, 150)

    # Encuentra los contornos de los objetos en la imagen
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Recorre cada contorno
    for c in contours:
      # Aproxima el contorno a una forma simple
      epsilon = 0.01 * cv2.arcLength(c, True)
      approx = cv2.approxPolyDP(c, epsilon, True)

      # Si el contorno tiene tres vértices, se trata de una línea
      if len(approx) <= 6:
        # Obtiene las coordenadas del rectángulo que rodea la línea
        x, y, w, h = cv2.boundingRect(c)
        # Dibuja el rectángulo en la imagen
        cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2) #Verde
        
      # Si el contorno tiene cuatro vértices, se trata de un círculo
      elif len(approx) > 8 and len(approx) <= 20:
        # Obtiene las coordenadas del rectángulo que rodea el círculo
        x, y, w, h = cv2.boundingRect(c)
        # Dibuja el rectángulo en la imagen
        cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 0, 255), 2) #Rojo

  def show_image(self):
    # Muestra la imagen resultante
    cv2.imshow('Image', self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Crea un objeto de la clase ImageProcessor
processor = ImageProcessor('images_VER_2.jpeg')

# Encuentra las formas en la imagen
processor.find_shapes()

# Muestra la imagen con las formas encontradas
processor.show_image()