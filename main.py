import os
import subprocess
import sys
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import time

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
sunglassesT = cv2.imread("Resources/SunglassesT.png", cv2.IMREAD_UNCHANGED)
ShirtButtonT = cv2.imread("Resources/ShirtsT.png", cv2.IMREAD_UNCHANGED)
HomeButtonT = cv2.imread("Resources/HomeT.png", cv2.IMREAD_UNCHANGED)
counterRight = 0
counterLeft = 0
selectionSpeed = 20


def start_new_process():
    script_path = os.path.join(os.path.dirname(__file__), "Shirt.py")
    subprocess.run([sys.executable, script_path])


def start_new_process1():
    script_path = os.path.join(os.path.dirname(__file__), "filert.py")
    subprocess.run([sys.executable, script_path])


while True:
    success, img = cap.read()

    img = cvzone.overlayPNG(img, sunglasses, (128, 128))
    overlay_resize1 = cv2.resize(sunglassesT, (190, 100))
    img = cvzone.overlayPNG(img, overlay_resize1, (100, 80))
    img = cvzone.overlayPNG(img, HomeButton, (128, 512))
    overlay_resize = cv2.resize(HomeButtonT, (170, 60))
    img = cvzone.overlayPNG(img, overlay_resize, (110, 450))
    img = cvzone.overlayPNG(img, ShirtButton, (1024, 128))
    overlay_resize2 = cv2.resize(ShirtButtonT, (170, 60))
    img = cvzone.overlayPNG(img, overlay_resize2, (1000, 70))
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

    try:
        if 1024 < lmList[19][1] < 1152 and 128 < lmList[19][2] < 256:
            counterLeft += 1
            cv2.ellipse(img, (1086, 190), (67, 67), 0, 0, counterLeft * selectionSpeed, (230, 255, 0), 10)
            if counterLeft * selectionSpeed >= 360:
                cap.release()
                cv2.destroyAllWindows()
                start_new_process()
        elif 256 > lmList[20][1] > 128 and 128 < lmList[20][2] < 256:
            counterRight += 1
            cv2.ellipse(img, (192, 190), (67, 67), 0, 0, counterRight * selectionSpeed, (150, 255, 0), 10)
            if counterRight * selectionSpeed >= 360:
                cap.release()
                cv2.destroyAllWindows()
                start_new_process1()
        elif 128 < lmList[20][1] < 256 and 512 < lmList[20][2] < 640:
            counterRight += 1
            cv2.ellipse(img, (192, 575), (67, 67), 0, 0, counterRight * selectionSpeed, (150, 255, 0), 10)
            if counterRight * selectionSpeed >= 360:
                counterRight = 0
        else:
            counterRight = 0
            counterLeft = 0
    except:
        pass

    # Draw a vertical line
    # img = cv2.line(img, (128, 0), (128, img.shape[1]), (255, 0, 0), 3)
    # img = cv2.line(img, (256, 0), (256, img.shape[1]), (0, 255, 0), 3)
    # img = cv2.line(img, (384, 0), (384, img.shape[1]), (0, 0, 255), 3)
    # img = cv2.line(img, (512, 0), (512, img.shape[1]), (0, 255, 255), 3)
    # img = cv2.line(img, (640, 0), (640, img.shape[1]), (255, 255, 0), 3)
    # img = cv2.line(img, (768, 0), (768, img.shape[1]), (255, 0, 255), 3)
    # img = cv2.line(img, (896, 0), (896, img.shape[1]), (255, 255, 255), 3)
    # img = cv2.line(img, (1024, 0), (1024, img.shape[1]), (110, 130, 0), 3)
    # img = cv2.line(img, (1152, 0), (1152, img.shape[1]), (0, 200, 200), 3)
    # img = cv2.line(img, (1280, 0), (1280, img.shape[1]), (255, 0, 0), 3)
    # img = cv2.line(img, (0, 128), (img.shape[1], 128), (255, 0, 0), 3)
    # img = cv2.line(img, (0, 256), (img.shape[1], 256), (0, 255, 0), 3)
    # img = cv2.line(img, (0, 384), (img.shape[1], 384), (0, 0, 255), 3)
    # img = cv2.line(img, (0, 512), (img.shape[1], 512), (0, 255, 255), 3)
    # img = cv2.line(img, (0, 640), (img.shape[1], 640), (255, 255, 0), 3)
    # img = cv2.line(img, (0, 720), (img.shape[1], 768), (255, 0, 255), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit
        break

cap.release()
cv2.destroyAllWindows()
