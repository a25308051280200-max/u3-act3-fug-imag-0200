import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

# Alejandra Rivera Valenzuela NC = 0200
print("Alejandra Rivera Valenzuela NC = 0200")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")

# 1. Cargar la imagen en escala de grises
alvarito_foto = cv2.imread('yoko_0200.jfif', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(8, 6))
plt.imshow(alvarito_foto, cmap='gray')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.title('Imagen Normal - Alejandra Rivera 0200')
plt.show()  # Muestra la primera ventana independiente

print("<3<3<3<3 Puntos de la imagen <3<3<3<3")

plt.figure(figsize=(8, 6))
plt.imshow(alvarito_foto, cmap='gray')

x = [100, 100, 300]
y = [100, 400, 500]

plt.scatter(x, y, s=40, c='red', label='Puntos')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.title('Alvarito Diaz y Alejandra Rivera 0200')
plt.show()  