import cv2
from WebCam import WebcamVideoStream
import HumanTrackingModule
import HandTrackingModule



print("[INFO] sampling THREADED frames from webcam...")
hd = HandTrackingModule.HandDetector()
vs = WebcamVideoStream(src=0).start()
while True:
    img = vs.read()
    img = cv2.flip(img,1)
    hd.findHand(img)

    # hd.findFace(img)
	# img = imutils.resize(img, width=400)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        vs.stop()
        break

cv2.destroyAllWindows()
