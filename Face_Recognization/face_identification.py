import cv2
import os
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def fun():
	dataset_path = "./face_dataset/"
	face_data = []
	labels = []
	class_id = 0
	names = {}


	for fx in os.listdir(dataset_path):
		if fx.endswith('.npy'):
			names[class_id] = fx[:-4]
			data_item = np.load(dataset_path + fx)
			face_data.append(data_item)
			target = class_id * np.ones((data_item.shape[0],))
			class_id += 1
			labels.append(target)

	face_dataset = np.concatenate(face_data, axis=0)
	face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

	#Building model
	model=KNeighborsClassifier(n_neighbors=5)
	model.fit(face_dataset,face_labels.ravel())


	cap = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

	while True:
		ret, frame = cap.read()
		if ret == False:
			continue
		# Convert frame to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect multi faces in the image
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		for face in faces:
			x, y, w, h = face
			face_section = cv2.resize(frame[y:y+h, x:x+w], (100, 100))
			face_section=face_section.reshape((face_section.shape[0]),-1)
			out=model.predict([face_section.flatten()])
			cv2.putText(frame, names[int(out[0])],(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

		cv2.imshow("Faces", frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()