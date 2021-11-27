import cv2
import os
import numpy as np
import traceback

from constants import *

class TrainPictures:

    IMAGES_PATH = 'images'

    def __init__(self):
        self.labels = []
        self.facesData = []        
        self.peopleList = os.listdir(IMAGES_PATH)

    def training(self):
        """

        Do training

        def cv_imread(file_path):
            cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
            return cv_img
        file_path = './Test.jpg'
        img = cv_imread(file_path)
        print(img)

        """
        try:
            label = 0
            for nameDir in self.peopleList:
                personPath = '{}/{}'.format(IMAGES_PATH, nameDir)
                print('Leyendo las imágenes...')

                for fileName in os.listdir(personPath):
                    print('Caras: ', nameDir + '/' + fileName)
                    self.labels.append(label)
                    face_image_path = '{}/{}'.format(personPath,fileName)
                    print('Reading')
                    self.facesData.append(cv2.imread(face_image_path,0))
                    print('Showing')
                    image = cv2.imread(face_image_path,0)
                    cv2.imshow('image',image)
                    print('Showed')
                    cv2.waitKey(3)
                
                    label = label + 1

            # Métodos para entrenar el reconocedor
            #1. face_recognizer = cv2.face.EigenFaceRecognizer_create()
            #2. face_recognizer = cv2.face.FisherFaceRecognizer_create()
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()

            # Entrenando el reconocedor de rostros
            print("Entrenando...")
            face_recognizer.train(self.facesData, np.array(self.labels))

            # Almacenando el modelo obtenido
            #face_recognizer.write('modeloEigenFace.xml')
            #face_recognizer.write('modeloFisherFace.xml')
            face_recognizer.write(TRAINED_FILE)
            print("¡Modelo almacenado!")
        except Exception as e:
            print('Error inesperado en el entrenamiento:', e)
            traceback.print_exc()