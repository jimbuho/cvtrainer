import cv2
import os
import traceback

from constants import *

font = cv2.FONT_HERSHEY_SIMPLEX

class TestImage:

    def __init__(self, data):
        self.data = data
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read(TRAINED_FILE)
        
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(TRAINED_FILE)
        self.faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
    
    def getImageName(self, code):
        '{}'.format(self.imagePaths[code])
    
    def recognize(self):
        try:
            cap = cv2.VideoCapture(NUM_CAMARA, cv2.CAP_DSHOW)
        except Exception as error:
            print('Error con algo de la cámara ' + str(error))
            return

        while True:
            ret, frame = cap.read()
            if ret == False: break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()

            faces = self.faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                id, confidence = self.face_recognizer.predict(rostro)
                cv2.putText(frame,'{} {}'.format(id, round(100 - confidence)),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                
                if confidence < 70:
                    name = self.data.get_user(id)                    
                    cv2.putText(frame,'{}'.format(name),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                
            cv2.imshow('frame',frame)
            k = cv2.waitKey(1)
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
