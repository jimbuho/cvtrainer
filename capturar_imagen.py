import cv2
import os
import imutils

from constants import *

class ImageCapture:

    def __init__(self, person_name):
        self.person_name = person_name
        self.person_path = '{}/{}'.format(IMAGES_PATH, self.person_name)

        self.build_dirs()

        try:
            self.cap = cv2.VideoCapture(NUM_CAMARA, cv2.CAP_DSHOW)  # 0, 1 son los índices de la cámara
        except Exception as error:
            print('Camera Error: {}'.format(error))

        self.faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    def build_dirs(self):
        """
        Directorios
        """
        if not os.path.exists(self.person_path):
            os.makedirs(self.person_path)
            print('Created Folder: ',self.person_path)

    def capture(self):
        try:            
            count = 0

            while True:
                ret, frame = self.cap.read()
                if ret == False: break
                frame =  imutils.resize(frame, width=640)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = frame.copy()

                faces = self.faceClassif.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite('{}/rostro_{}.jpg'.format(self.person_path, count), rostro)
                    count = count + 1
                
                cv2.imshow('frame',frame)

                k =  cv2.waitKey(1)
                if k == 27 or count >= 200:
                    break
            
            self.cap.release()
            cv2.destroyAllWindows()     
        except Exception as e:
            print('Error inesperado en la captura:', e)

