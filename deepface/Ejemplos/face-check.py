from deepface import DeepFace
print ("Se han comparado 2 imagenes. Se verificara que la persona sea la misma")
print ("Cargando")
result = DeepFace.verify(img1_path = "/home/diego/GIT-HUB/aperturas-puertas-deepface/deepface/Faces/robert-downey-jr-1.jpg", img2_path = "/home/diego/GIT-HUB/aperturas-puertas-deepface/deepface/Faces/robert-john-downey-jr-posado-1500898215.jpg")
print ("Resultado")
print (result)