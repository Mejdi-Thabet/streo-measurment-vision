import cv2

# initialize the camera
cam = cv2.VideoCapture(0)

# set the format into MJPG in the FourCC format 
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))

cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('J','P','E','G'))

ret, image = cam.read()

if ret:
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/book/output/SnapshotTest.jpg',image)
cam.release()
