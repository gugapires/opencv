import cv2

cam = cv2.imread(0)

#r,f = cam.read()
cv2.imshow('Cam', cam)
cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()
