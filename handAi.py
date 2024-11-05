import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import keyboard
import time

webcam = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

time.sleep(1)
showImg = input("Show Webcam?(yes/no):")

while True:
    time.sleep(0.05)
    success, gotImage = webcam.read()
    image = cv2.flip(gotImage,1)
    coordinates, handImage = detector.findHands(image)

    if showImg == "yes":
        cv2.imshow("Your Webcam",image)

    if coordinates:
        Center = coordinates[0]['center']
        PosX = Center[0] * 2
        PosY = Center[1] * 2

        print(PosX,PosY)

        fingersUp = detector.fingersUp(coordinates[0])

        if fingersUp.count(0):
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()
            pyautogui.moveTo(PosX,PosY)

    cv2.waitKey(1)
    if keyboard.is_pressed("ctrl"):
        break

webcam.release()
cv2.destroyAllWindows()