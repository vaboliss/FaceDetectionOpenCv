import cv2

face_cascade = cv2.CascadeClassifier('D:\project\opencv\FaceANDIdent\haarcascades\haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
i = 0
while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)

    
    img_item = "{}.png".format(i)
    cv2.imwrite(img_item, frame)
    i+=1
        

    if cv2.waitKey(20) & 0xFF == ord('q'):
       break; 
