# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/diego/GIT-HUB/aperturas-puertas-deepface/deepface/Faces/selena-gomez-black-and-white-wallpaper-preview.jpg", db_path = "/home/diego/GIT-HUB/aperturas-puertas-deepface/deepface/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])