ndPos(img, draw=False)
    # if len(lmList) != 0:
    #     x1_check = lmList[0][1] 
    #     x2_check= lmList[1][1]
    #     x1, y1 = lmList[4][1],lmList[4][2] 
    #     x2, y2 = lmList[8][1],lmList[8][2]
    #     x3, y3 = lmList[12][1],lmList[12][2]

    #     if x2_check - x1_check > 0:
    #         cv2.circle(img, (x1, y1), 15, (255,0,255), cv2.FILLED) 
    #         cv2.circle(img, (x2, y2), 15, (255,0,255), cv2.FILLED)
    #         cv2.line(img, (x1, y1), (x2, y2), (255,0,255), 3) 
    #         line = math.hypot(x2 - x1, y2 - y1)
    #         vol = np.interp(line, (50, 250), (min_vol, max_vol))
    #         volper = np.interp(line, (50, 350), (0, 100))
    #         volume.SetMasterVolumeLevel(vol, None)
    #         cv2.putText(img, "Sound: " + str(int(volper)) + "%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 240, 0), 4)
    #     else:
    #         cv2.circle(img, (x1, y1), 10, (255,0,255), cv2.FILLED) 
    #         cv2.circle(img, (x2, y2), 10, (255,0,100), cv2.FILLED)
    #         pos_x = np.interp(x2, (100, 600), (0, SCREEN_WIDTH))
    #         pos_y = np.interp(y2, (100, 400), (0, SCREEN_HEIGHT))
    #         clocx = plocx + (pos_x - plocx) / 10
    #         clocy = plocy + (pos_y - plocy) / 10
    #         mouse.move(pos_x, pos_y)
    #         plocx, plocy = clocx, clocy
    #         ### FIXXX
    #         if math.hypot(x3 - x1, y3 - y1) < 20:
    #             print("touch")
    #         #     print(math.hypot(x3 - x1, y3 - y1))
    #             mouse.press("left")
    #         else:
    #             mouse.release(