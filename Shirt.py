import subprocess
import sys
import os
import time

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# Set the desired camera resolution
width, height = 1280, 720

# Open the camera with the desired resolution
cap = cv2.VideoCapture(1)
cap.set(3, width)  # 3 is the identifier for width
cap.set(4, height)  # 4 is the identifier for height

detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
print(listShirts)
fixedRatio = 340 / 190  # shirt width/lm12-lm11 distance   shirt eke scale eka wenas karanne
shirtRatioHeighWidtht = 813 / 691  # shirt width/shirt height (in pixels)
ImageNumber = 0
imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
sunglasses = cv2.imread("Resources/Sunglass (1).png", cv2.IMREAD_UNCHANGED)
ShirtButton = cv2.imread("Resources/Shirt.png", cv2.IMREAD_UNCHANGED)
HomeButton = cv2.imread("Resources/Home.png", cv2.IMREAD_UNCHANGED)
counterRight = 0
counterLeft = 0
selectionSpeed = 15


def start_new_process():
    script_path = os.path.join(os.path.dirname(__file__), "filert.py")
    subprocess.run([sys.executable, script_path])


def start_new_process1():
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    subprocess.run([sys.executable, script_path])


while True:
    success, img = cap.read()
    img = cvzone.overlayPNG(img, sunglasses, (128, 128))
    img = cvzone.overlayPNG(img, HomeButton, (128, 512))
    img = cvzone.overlayPNG(img, ShirtButton, (1024, 128))
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        center = bboxInfo["center"]
        lm11 = lmList[11][1:3]  # Left shoulder coordinates (x, y) in pixels
        lm12 = lmList[12][1:3]  # Right shoulder coordinates (x, y) in pixels
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[ImageNumber]), cv2.IMREAD_UNCHANGED)
        widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
        # print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (widthOfShirt,
                                         int(widthOfShirt * shirtRatioHeighWidtht)))  # (0,0) means width and height (0.5, 0.5) means half of the original size
        currentScale = (lm11[0] - lm12[0]) / 180
        # offset = int(44 * currentScale), int(48 * currentScale)
        offset = int(70 * currentScale), int(55 * currentScale)  # shirt eka X,Y axis walata aran yanna puluwan
        try:
            img = cvzone.overlayPNG(img, imgShirt,
                                    (lm12[0] - offset[0], lm12[1] - offset[1]))  # shirt eka uda yata aran yanna puluwan
        except:
            pass

        try:
            if lmList[16][1] > 640:
                counterRight += 1
                # cv2.ellipse(img, (139, 360), (66, 66), 0, 0, counterRight * selectionSpeed, (0, 255, 0), 20)
                # if counterRight*selectionSpeed >= 360:
                #     counterRight = 0

                if ImageNumber < len(listShirts) - 1:
                    ImageNumber += 1
                    time.sleep(1)
            elif lmList[15][1] < 640:
                counterLeft += 1
                # # cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionSpeed, (0, 255, 0), 20)
                # cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionSpeed, (0, 255, 0), 20)
                # if counterLeft * selectionSpeed >= 360:
                #     counterLeft = 0

                if ImageNumber > 0:
                    ImageNumber -= 1
                    time.sleep(1)
            elif 1024 < lmList[19][1] < 1152 and 128 < lmList[19][2] < 256:
                counterLeft += 1
                cv2.rectangle(img, (1086, 190), (67, 67), 0, 0, counterLeft * selectionSpeed, (230, 255, 0), 10)
                time.sleep(2)
                if counterLeft * selectionSpeed >= 360:
                    counterLeft = 0
            elif 256 > lmList[20][1] > 128 and 128 < lmList[20][2] < 256:
                counterRight += 1
                cv2.ellipse(img, (192, 190), (67, 67), 0, 0, counterRight * selectionSpeed, (150, 255, 0), 10)
                if counterRight * selectionSpeed >= 360:
                    cap.release()
                    cv2.destroyAllWindows()
                    start_new_process()
            elif 128 < lmList[20][1] < 256 and 512 < lmList[20][2] < 640:
                counterRight += 1
                cv2.ellipse(img, (192, 575), (67, 67), 0, 0, counterRight * selectionSpeed, (150, 255, 0), 10)
                if counterRight * selectionSpeed >= 360:
                    cap.release()
                    cv2.destroyAllWindows()
                    start_new_process1()

            else:
                counterRight = 0
                counterLeft = 0
        except:
            pass
    # Draw a vertical line

    print(currentScale)

    # img = cv2.line(img, (640, 0), (640, img.shape[1]), (255, 255, 0), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()
