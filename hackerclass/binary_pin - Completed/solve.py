# with open('./pin.txt') as f:
#     pins = f.read().splitlines()

# for i in range(0, len(pins)):
#     pins[i] = int(pins[i])

import itertools
from time import sleep
import pyautogui

possible = []

for numbers in itertools.product([0, 1], repeat=10):
    possible.append(numbers)


zero = pyautogui.locateCenterOnScreen('./0.png', grayscale=True, confidence=.8)
one = pyautogui.locateCenterOnScreen('./1.png', grayscale=True, confidence=.8)
reset = pyautogui.locateCenterOnScreen('./reset.png', grayscale=True, confidence=.8)

# PIN = 360 - 365

possible = possible[360:361]

# print(possible.index((0, 1, 0, 1, 1, 0, 1, 0, 1, 0)))

for items in possible:
    print(items)
    for pin in items:
        if pin == 0:
            pyautogui.click(zero)
            # sleep(1)
        elif pin == 1:
            pyautogui.click(one)
            # sleep(1)
    sleep(1)
    # pyautogui.click(reset)