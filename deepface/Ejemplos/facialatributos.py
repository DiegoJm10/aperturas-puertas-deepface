from  deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/diego/GIT-HUB/aperturas-puertas-deepface/deepface/Faces/cara.jpg", actions = ['age', 'gender', 'race', 'emotion'])
print ("El resultado del analisis es:")
print (obj)