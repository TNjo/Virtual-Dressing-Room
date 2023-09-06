import time
import os
import subprocess
import sys

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector


def start_new_process():
    script_path = os.path.join(os.path.dirname(__file__), "Shirt.py")
    subprocess.run([sys.executable, script_path])


def start_new_process1():
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    subprocess.run([sys.executable, script_path])


width, height = 1280, 720

# Open the camera with the desired resolution
cap = cv2.VideoCapture(1)
cap.set(3, width)  # 3 is the identifier for width
cap.set(4, height)  # 4 is the identifier for height
detector = PoseDetector()
sunglassFolderPath = "Resources/Sunglasess"
sunglasses = cv2.imread("Resources/Sunglass (1).png", cv2.IMREAD_UNCHANGED)
ShirtButton = cv2.imread("Resources/Shirt.png", cv2.IMREAD_UNCHANGED)
HomeButton = cv2.imread("Resources/Home.png", cv2.IMREAD_UNCHANGED)
listGlass = os.listdir(sunglassFolderPath)
print(listGlass)
ImageNumber = 0
counterRight = 0
counterLeft = 0
selectionSpeed = 20
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    success, img = cap.read()
    img = cvzone.overlayPNG(img, ShirtButton, (1024, 128))
    img = cvzone.overlayPNG(img, sunglasses, (128, 128))
    img = cvzone.overlayPNG(img, HomeButton, (128, 512))
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        try:
            faces = cascade.detectMultiScale(img)
            overlay = cv2.imread(os.path.join(sunglassFolderPath, listGlass[ImageNumber]), cv2.IMREAD_UNCHANGED)
            for x, y, w, h in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                overlay_resize = cv2.resize(overlay, (int(w * 1.0), int(h * 1.0)))
                img = cvzone.overlayPNG(img, overlay_resize, (x, y - 10))

            if lmList[16][1] > 640:
                counterRight += 1
                if ImageNumber < len(listGlass) - 1:
                    ImageNumber += 1
                    time.sleep(1)
            elif lmList[15][1] < 640:
                counterLeft += 1
                if ImageNumber > 0:
                    ImageNumber -= 1
                    time.sleep(1)
            elif 1024 < lmList[19][1] < 1152 and 128 < lmList[19][2] < 256:
                counterLeft += 1
                cv2.rectangle(img, (1086, 190), (67, 67), 0, 0, counterLeft * selectionSpeed, (230, 255, 0), 10)
                time.sleep(2)
                if counterLeft * selectionSpeed >= 360:
                    cap.release()
                    cv2.destroyAllWindows()
                    start_new_process()
            elif 256 > lmList[20][1] > 128 and 128 < lmList[20][2] < 256:
                counterRight += 1
                cv2.ellipse(img, (192, 190), (67, 67), 0, 0, counterRight * selectionSpeed, (150, 255, 0), 10)
                if counterRight * selectionSpeed >= 360:
                    counterRight = 0
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

    # img = cv2.line(img, (640, 0), (640, img.shape[1]), (255, 255, 0), 3)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == 27:
        break
