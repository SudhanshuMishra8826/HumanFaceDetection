#Importing Required Libraries
#OpenCv: To work on images
import cv2
#Using haarcascade to detect face and eyes
#https://github.com/opencv/opencv/tree/master/data/haarcascades <-- Download links for cascade files
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyeDetect=cv2.CascadeClassifier("haarcascade_eye.xml")
#reading frames from primary webcam, Here 0 can be replaced with any video file
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Human Face Detection starts
    face=faceDetect.detectMultiScale(gray,1.3,5)
    #Loop to draw Rectangle around detected Faces
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"HUMAN",(x,y),font,0.5,(0,255,0),1,cv2.LINE_AA)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]\
        #not working accurately 
        '''eyes=eyeDetect.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(roi_color,"Eyes",(ex,ey),font,0.5,(0,255,0),1,cv2.LINE_AA)'''
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)        
    #displaying result image
    cv2.imshow('window',frame)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release()
#closing program on q key pressed
cv2.destroyAllWindows()
