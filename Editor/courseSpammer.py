import pyautogui
import numpy as np
import cv2
import time

print("System check: use Google Chrome")
print("System check: dark mode disabled")
print("System check: correct script version for Windows/Mac")
print("System check: :syntax off in vim")

def click(target_color, duration=30): # seconds

    start_time = time.time()

    while time.time() - start_time < duration:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)

        rgb_image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR) 

        target_r, target_g, target_b = target_color

        threshold = 1

        mask = cv2.inRange(
            rgb_image,
            (target_b - threshold, target_g - threshold, target_r - threshold),
            (target_b + threshold, target_g + threshold, target_r + threshold)
        )

        matching_positions = np.column_stack(np.where(mask > 0))

        if len(matching_positions) == 0:
            print("No matching pixels found.")
            continue

        max_pos = max(matching_positions, key=lambda p: p[0] + p[1])
        max_x, max_y = max_pos[1], max_pos[0] 
        click_x = max_x - 10
        click_y = max_y - 10
        # MAC: screenshot vs. screen coordinate scale is off by factor of 2
        # click_x = (max_x - 10) / 2
        # click_y = (max_y - 10) / 2

        pyautogui.click(click_x, click_y)
        print(click_x, click_y)

        # mac: move cusor away so button does not change color
        # pyautogui.moveTo(1000, 1000, _pause=False)

# Make sure no hover when checking rgb values (changes button color)
target_color = (250, 234, 205) # surface laptop studio

try:
    print("Looking for the target color and spamming clicks for 30 seconds...")
    click(target_color, duration=30)
except KeyboardInterrupt:
    print("Stopped.")
