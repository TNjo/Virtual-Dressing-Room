import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
capsPaths = "Resources/Caps"
capList = os.listdir(capsPaths)
print(capList)
ImageNumber = 0
startDist = None
scale = 0
cx, cy = 500, 500

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    overlay = cv2.imread(os.path.join(capsPaths, capList[ImageNumber]))  # Load image with alpha channel

    if len(hands) == 2:
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))

            # print("Zoom Gesture")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            # point 8 is the tip of the index finger
            if startDist is None:
                # length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)
                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)

                startDist = length

            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)

            scale = int((length - startDist) // 2)
            cx, cy = info[4:]
            print(scale)
    else:
        startDist = None

    try:
        h1, w1, _ = overlay.shape
        newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2
        overlay = cv2.resize(overlay, (newW, newH))

        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = overlay

    except:
        pass

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()


