import cv2
import time, random 
import numpy

startTime = time.time()
print (startTime)

def take_snapShot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True 
    while(result): 
        ret,frame = videoCaptureObject.read()
        imageName = "snap" + str(number) + ".jpg"
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        result = False 
    videoCaptureObject.release()
    cv2.destroyAllWindows()    

take_snapShot() 