#Importing Required Libraries
#OpenCv: To work on images
import cv2
#Using haarcascade to detect face and eyes
#https://github.com/opencv/opencv/tree/master/data/haarcascades <-- Download links for cascade files
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyeDetect=cv2.CascadeClassifier("haarcascade_eye.xml")
#reading image top be processed
img=cv2.imread('pic2.jpg',cv2.IMREAD_GRAYSCALE)
#Human Face Detection starts
face=faceDetect.detectMultiScale(img,1.3,5)
#Loop to draw Rectangle around detected Faces
for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=img[y:y+h,x:x+w]
        eyes=eyeDetect.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#displaying result image
cv2.imshow('Pic',img)
cv2.waitKey(0)
#closing program on any key pressed
cv2.destroyAllWindows()
