import cv2

cam = cv2.VideoCapture(0)

while(True):

	r,f = cam.read()

	cv2.imshow('Cam', f)

	cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()
