import cv2
import numpy as np

def fun(file_name):
    c=cv2.VideoCapture(0)

    faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    skip=0
    faceData=[]
    datasetPath="./face_dataset/"


    while(c.isOpened()):
        ret,frame=c.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        if ret==False:
            continue
        faces=faceCascade.detectMultiScale(gray,1.3,5)
        if len(faces)==0:
            continue
        k=1
        faces=sorted(faces,key=lambda x:x[2]*x[3],reverse=True)
        skip+=1
        if skip==1010:
            break

        for face in faces[:1]:
            x,y,w,h=face
            #offset=5
            face_selection=cv2.resize(frame[y:h+y,x:x+w],(100,100))

            if skip%10==0:
                faceData.append(face_selection)
                print(len(faceData))
            
            #cv2.imshow(str(k),face_selection)
            k+=1

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    

        #cv2.imshow('faces',frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    faceData=np.array(faceData)
    faceData=faceData.reshape((faceData.shape[0]),-1)


    np.save(datasetPath+file_name,faceData)
    print("dataset saved at {}".format(datasetPath  +file_name+'.npy'))
    c.release()
    cv2.destroyAllWindows