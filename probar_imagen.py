import cv2
import os
import traceback

from constants import *

class TestImage:

    def __init__(self):
        # 1 #face_recognizer = cv2.face.EigenFaceRecognizer_create()
        # 2 #face_recognizer = cv2.face.FisherFaceRecognizer_create()
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Leyendo el modelo
        #face_recognizer.read('modeloEigenFace.xml')
        #face_recognizer.read('modeloFisherFace.xml')
        self.face_recognizer.read(TRAINED_FILE)

        self.cap = cv2.VideoCapture(NUM_CAMARA, cv2.CAP_DSHOW)

        self.faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

        self.imagePaths = os.listdir(IMAGES_PATH)
        print('IMAGES', self.imagePaths)

    def recognize(self):

        try:
            print('Reconociendo...')
            while True:
                ret,frame = self.cap.read()
                if ret == False: break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = gray.copy()

                faces = self.faceClassif.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
                    result = self.face_recognizer.predict(rostro)
                    print('RESULT', result)

                    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                    '''
                    # EigenFaces
                    if result[1] < 5700:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    else:
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                    
                    # FisherFace
                    if result[1] < 500:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    else:
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                    '''
                    # LBPHFace
                    if result[1] < 70:
                        print('Result[0]', result[0])
                        cv2.putText(frame,'{}'.format(self.imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    else:
                        print('Desconocido')
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                    
                cv2.imshow('frame',frame)
                k = cv2.waitKey(1)
                if k == 27:
                    break

            self.cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print('Error de reconocimiento:', e)
            traceback.print_exc()
