import keyboard
import pyautogui

moving = 5

while not keyboard.is_pressed('ctrl'):
    if keyboard.is_pressed("up"):
        pyautogui.move(0,-moving)
    if keyboard.is_pressed("down"):
        pyautogui.move(0,moving)
    if keyboard.is_pressed("left"):
        pyautogui.move(-moving,0)
    if keyboard.is_pressed("right"):
        pyautogui.move(moving,0)
    if keyboard.is_pressed("space"):
        pyautogui.mouseDown()
    else:
        pyautogui.mouseUp()

    if keyboard.is_pressed("a"):
        moving -= 1
        print(moving)
    if keyboard.is_pressed("d"):
        moving += 1
        print(moving)

    if keyboard.is_pressed("w"):
        pyautogui.scroll(moving)
    if keyboard.is_pressed("s"):
        pyautogui.scroll(-moving)