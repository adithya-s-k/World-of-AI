import imutils
import cv2
from imutils import face_utils
import dlib
from scipy.spatial import distance
from pygame import mixer

mixer.init()
mixer.music.load(r"C:\Users\vrehm\OneDrive\Desktop\music.wav")

def eye_aspect_ratio(eye):                           #calculate the open eye distance and watch out for the closed eye distance which drops A+B when closed
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A+B)/(2.0*C)
    return ear                                       #differentiate blink
thresh = 0.25                                        #min ear 
flag = 0                                             #frame count
frame_check = 20                                     #min duration for closed eye to avoid warnings on blink
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS['right_eye']


detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor(r"C:\Users\vrehm\OneDrive\Desktop\shape_predictor_68_face_landmarks.dat")    #face landmarks
cap = cv2.VideoCapture(0)       

while True:
    ret, frame = cap.read()                  #read returns boolean value if the frame avails or not-ret, image- frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    for subject in subjects:
        shape = predict(gray, subject)              #predict landmarks on face
        shape = face_utils.shape_to_np(shape)        #converting face to a list of xy coordinates
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEar = eye_aspect_ratio(leftEye)
        rightEar = eye_aspect_ratio(rightEye)
        ear = (leftEar + rightEar) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)         #minimum distance that covers the eye
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)                                              #contours that join the convex hull(outline)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)                                              #contours that join the convex hull(outline)
        if ear<thresh:
            flag+=1
            print(flag)
            if flag>=frame_check:
                cv2.putText(frame, "*****ALERT*****", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "*****ALERT*****", (0,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                mixer.music.play()
        else:
            flag=0        
    cv2.imshow("Frame", frame)               #displays image stored in frame var
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break                                   #waits for a time duration to stop display
cv2.destroyAllWindows()
cap.release()