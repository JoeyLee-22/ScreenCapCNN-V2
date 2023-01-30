import numpy as np
import time
import cv2
import pyautogui
from PIL import Image

def start_monitor(cnn_instance, seconds=300):    
    while(True):
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshots/screenshot.png') # (2100, 3360, 4);
        
        screenshot = Image.open('screenshots/screenshot.png')
        resized_screenshot = screenshot.resize((1280,720))
        resized_screenshot.save('screenshots/resized_screenshot.png')
        
        screenshot = cv2.cvtColor(np.array(resized_screenshot), cv2.COLOR_RGB2BGR)        
        
        result = cnn_instance.classify(np.asarray(screenshot))
        
        # productive = num close to 0, unproductive = num close to 1
        if (result<=0.5):
            print("\n\n{}: Productive".format(result))
        else:
            print("\n\n{}: Unproductive".format(result))
                 
        for secs in range (seconds):
            time.sleep(0.99)
            print(str(seconds-int(secs)) + "/" + str(seconds), end='\r')