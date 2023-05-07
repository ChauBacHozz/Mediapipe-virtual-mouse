import cv2
import mediapipe as mp
import time

class HumanDetector:
    def __init__(self, mode=False, modelComp=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComp = modelComp
        self.mpDraw = mp.solutions.drawing_utils
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic(min_detection_confidence=self.detectionCon,
                                                 min_tracking_confidence=self.trackCon)
        self.faceResult = None 
        self.lHandResult = None 
        self.rHandResult = None 
    def findRHand(self, img, draw = True):
        self.rHandResult = self.holistic.process(img)
        if self.rHandResult.left_hand_landmarks:
            if draw:
                print("Right Hand")
                self.mpDraw.draw_landmarks(img, self.rHandResult.left_hand_landmarks, self.mpHolistic.HAND_CONNECTIONS,
                                            self.mpDraw.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                            self.mpDraw.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=1))
    # def findRHand_pos(self, img, lmId_lst = []):
    #     lmList = []

    def findLHand(self, img, draw = True):
        self.lHandResult = self.holistic.process(img)
        if self.lHandResult.right_hand_landmarks:
            if draw:
                print("Left Hand")
                self.mpDraw.draw_landmarks(img, self.lHandResult.right_hand_landmarks, self.mpHolistic.HAND_CONNECTIONS,
                                            self.mpDraw.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                            self.mpDraw.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=1))
    def findFace(self, img, draw = True):
        self.faceResult = self.holistic.process(img)
        if self.faceResult.face_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.faceResult.face_landmarks, self.mpHolistic.FACEMESH_TESSELATION,
                                            self.mpDraw.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                            self.mpDraw.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1))
                
    # def findPos(self, img, handNo = 0, draw = True):
    #     lmList = []

    #     if self.result.multi_hand_landmarks:

    #         myhand = self.result.multi_hand_landmarks[0]
    #         for id, lm in enumerate(myhand.landmark):
    #             h, w, c = img.shape
    #             cx = int(lm.x * w)
    #             cy = int(lm.y * h)
    #             lmList.append([id, cx, cy])
    #             if draw:
    #                 cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
    #     return lmList

# HumanDetector()
# cap = cv2.VideoCapture(0)
# hd = HumanDetector()
# cTime, pTime = 0, 0
# while True:
#     sucsess, img = cap.read()
#     img = cv2.flip(img,1)
#     hd.findLHand(img)
#     # hd.findRHand(img)
#     # hd.findFace(img)
#     cTime = time.time()
#     fps = 1 /(cTime - pTime)
#     pTime = cTime
#     cv2.putText(img, "FPS: " + str(int(fps)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cap.release()
#         break
