import cv2
import os
import numpy as np
import traceback
from PIL import Image

from constants import *

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

class TrainPictures:

    def __init__(self):
        self.labels = []
        self.facesData = []        
        #self.peopleList = os.listdir(IMAGES_PATH)

    def training(self):
        faces, ids = self.getImagesAndLabels()
        recognizer.train(faces, np.array(ids))
        # Save the model into trainer/trainer.yml
        recognizer.write(TRAINED_FILE) 
        # Print the numer of faces trained and end program
        print("Modelo almacenado!")
        cv2.destroyAllWindows()

    def getImagesAndLabels(self):
        imagePaths = [os.path.join(IMAGES_PATH,f) for f in os.listdir(IMAGES_PATH)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') # grayscale
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
            
            image = cv2.imread(imagePath,0)
            cv2.imshow('image',image)
            cv2.waitKey(3)

        return faceSamples, ids
