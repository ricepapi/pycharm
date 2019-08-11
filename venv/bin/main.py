import pygame
import pygame.midi
import keyboard
import pynput
import pyautogui
from pynput.mouse import Button, Controller
mouse = Controller()
# import mouse
# import midis2events

pygame.midi.init()
pygame.midi.Input(0)
print("Main input is")
print(pygame.midi.get_default_input_id())
print(pygame.midi.get_device_info(pygame.midi.get_default_input_id()))
print("..........")
print("Main output is")
print(pygame.midi.get_default_output_id())
print(pygame.midi.get_device_info(pygame.midi.get_default_output_id()))
print("Starting Script in 3 seconds...")

pygame.time.wait(3000)

print("Initialize: ")

inp = pygame.midi.Input(1)
# ranges is 21 to 108

# 144 is down, 128 is up

keys_pressed = []
mouse_pressed = []
delay = 0
pressedState = 144
releasedState = 128
width = 1680
length = 1050

bound = [[48, "a"],
         [49, "w"],
         [50, "s"],
         [52, "d"],
         [53, "space"],
         [47, "n"],
         [44, "esc"],
         [51, "e"],
         [46, "q"],
         [54, "r"],
         [71, "u"],
         [69, "k"],
         [77, "o"],
         [79, "8"]]

boundMouse = [[72, "leftClick"], [74, "rightClick"], [73, "scrollUp"], [75, "scrollDown"]]
lookMouse = [[71, "left"], [69, "down"], [77, "right"], [79, "up"]]
# 2880 x 1800


def look(velocity):
    for t in lookMouse:
        if state == pressedState:
            if theKey == t[0]:
                if t[1] == "left":
                    # pyautogui.moveRel(-velocity, 0, delay)
                    mouse.move(-velocity, 0)
                if t[1] == "right":
                    # pyautogui.moveTo(width/2, length/2)
                    pyautogui.moveRel(velocity, 0, delay)
                if t[1] == "down":
                    # pyautogui.moveTo(width/2, length/2)
                    pyautogui.moveRel(0, velocity, delay)
                    # mouse.move(0, velocity)
                if t[1] == "up":
                    # pyautogui.moveTo(width/2, length/2)
                    pyautogui.moveRel(0, -velocity, delay)
                    # mouse.move(0, -velocity)


def add_key():
    for q in bound:
        if state == pressedState:
            if theKey == q[0]:
                # keys_pressed.append(q[1])
                keyboard.press(q[1])
    for e in boundMouse:
        if state == pressedState:
            if theKey == e[0]:
                if e[1] == "leftClick":
                    mouse.click(Button.left)
                if e[1] == "rightClick":
                    mouse.click(Button.right)
                if e[1] == "scrollUp":
                    mouse.scroll(0, 2)
                if e[1] == "scrollDown":
                    mouse.scroll(0, -2)


def remove_key():
    for q in bound:
        if state == releasedState:
            if theKey == q[0]:
                # keys_pressed.remove(q[1])
                keyboard.release(q[1])


on = True

while on:

    # mouse.move(1, 0)

    if inp.poll():
        a = inp.read(1)
        theKey = int(a[0][0][1])
        state = int(a[0][0][0])
        trueVelocity = int(a[0][0][2])
        print(a)
        print("my midi note is " + str(theKey))
        if theKey == 21:
            print("Cancelling...")
            on = False

        add_key()
        remove_key()
        # look(trueVelocity)

        # if int(a[0][0][0]) == 144 and int(a[0][0][1]) == 61:
            # keys_pressed.append("w")

        #if int(a[0][0][0]) == 128 and int(a[0][0][1]) == 61:
            # keys_pressed.remove("w")

        # print(inp.read.status)

        #keys_pressed.clear()
    pygame.time.wait(1)

print("Exit clicked.")
inp.close()
pygame.midi.quit()
pygame.quit()
exit()
