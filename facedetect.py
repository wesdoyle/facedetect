import io
import cv2
import numpy as np
import picamera as pic

memStream = io.BytesIO()

fontFace = FONT_HERSHEY_SCRIPT_SIMPLEX;
fontScale =2;
thickness =1;

with pic.PiCamera() as cam:
    cam.resolution = (800, 600)
    cam.caputre(memStream, format='jpeg')

buff = np.fromstring(stream.getvalue(), dtype=np.uint8)

img = cv2.imdecode(buff, 1)

haar_faces = 'faces.xml'
haar_eyes = 'eyes.xml'

faceCascade = cv2.CascadeClassifier(haar_faces)
eyeCascade  = cv2.CascadeClassifier(haar_eyes)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grayImg, 1.05, 5)

print("Detected " + str(len(faces)) + " faces in captured image.")

for (x,y,w,h) in faces:
    caption = str(w + " x " + h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(100,0,255),1)
    cv2.putText(img, caption, (x+w,y+h), font, 1, (255,255,255),2,cv2.LINE_AA)
    r_eyes = img[y:y+h, x:x+w]
    r_eyes_gray = grayImg[y:y+h, x:x+w]
    eyes = eyeCascade.detectMultiscale(r_eyes)
    for (x1,y1,w1,h1) in eyes:
        cv2.rectangle(r_eyes,(x1,y1),(x1+w1,y1+h1),(210,100,0),1)

cv2.imwrite('capture.jpg',img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

