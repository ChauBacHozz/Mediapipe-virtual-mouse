import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, mode=False, maxHands=2, modelComp=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComp = modelComp
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComp, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.drsp = self.mpDraw.DrawingSpec(color = (0, 255, 0), thickness = 8, circle_radius = 5)
        self.mpFaces = mp.solutions.face_detection
        self.faces = self.mpFaces.FaceDetection(self.mode)
        
    def findHand(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                                               self.mpDraw.DrawingSpec(color = (0, 200, 0), thickness = 6, circle_radius = 5),
                                               self.mpDraw.DrawingSpec(color = (0, 0, 240), thickness = 4, circle_radius = 5))
    def findFace(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result2 = self.faces.process(imgRGB)
        if self.result2.detections:
            for detection in self.result2.detections:
                self.mpDraw.draw_detection(img, detection)
                
    def findPos(self, img, handNo = 0, draw = True):
        lmList = []
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[0]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
        return lmList
    
    def findLHand(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        lmList = []
        if self.result.multi_hand_landmarks:
            if (self.result.multi_hand_landmarks[0].landmark[1].x
            > self.result.multi_hand_landmarks[0].landmark[0].x):
                print("Left hand")

    def findRHandPos(self, img, idx_lst, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        lmList = []
        if self.result.multi_hand_landmarks:
            if self.result.multi_handedness[0].classification[0].label == 'Right':
                for idx in idx_lst:
                    cx = int(self.result.multi_hand_landmarks[0].landmark[idx].x * img.shape[1])
                    cy = int(self.result.multi_hand_landmarks[0].landmark[idx].y * img.shape[0])
                    if draw:
                        cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)
                    lmList.append([idx, cx, cy])
        return lmList
            # for handLms in self.result.multi_hand_landmarks:
            #     if draw:
            #         self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
            #                                    self.mpDraw.DrawingSpec(color = (0, 200, 0), thickness = 6, circle_radius = 5),
            #                                    self.mpDraw.DrawingSpec(color = (0, 0, 240), thickness = 4, circle_radius = 5))
